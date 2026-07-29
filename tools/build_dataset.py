#!/usr/bin/env python3
"""Extrai o catálogo de fontes OSINT do README.md para um dataset JSON estruturado.

Gera (nunca editar à mão):
    data/sources.json   registro canônico por fonte, com links aninhados
    data/index.json     links achatados, prontos para busca

Lê (manuais):
    data/taxonomy.json    vocabulário controlado
    data/overrides.json   curadoria, sobrepõe a heurística

Uso:
    python3 tools/build_dataset.py            regenera os arquivos
    python3 tools/build_dataset.py --check    falha se estiverem desatualizados
    python3 tools/build_dataset.py --report   estatísticas e fontes sem classificação
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
README = RAIZ / "README.md"
DATA = RAIZ / "data"

# Seções que não fazem parte do catálogo de fontes.
CATEGORIAS_IGNORADAS = {
    "avisos-legais-e-eticos",
    "documentacao-complementar",
    "dataset-estruturado",
    "autores",
    "contribuicoes",
    "creditos",
}

# Badges e imagens dinâmicas, que não são fontes de consulta.
DOMINIOS_IGNORADOS = ("img.shields.io", "contributors-img.web.app")

UFS = {
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
    "SP", "SE", "TO",
}

# Alguns agrupamentos usam o nome do estado por extenso: "- São Paulo - <URL>".
NOMES_UF = {
    "acre": "AC", "alagoas": "AL", "amapa": "AP", "amazonas": "AM",
    "bahia": "BA", "ceara": "CE", "distrito federal": "DF",
    "espirito santo": "ES", "goias": "GO", "maranhao": "MA",
    "mato grosso do sul": "MS", "mato grosso": "MT", "minas gerais": "MG",
    "para": "PA", "paraiba": "PB", "parana": "PR", "pernambuco": "PE",
    "piaui": "PI", "rio de janeiro": "RJ", "rio grande do norte": "RN",
    "rio grande do sul": "RS", "rondonia": "RO", "roraima": "RR",
    "santa catarina": "SC", "sao paulo": "SP", "sergipe": "SE",
    "tocantins": "TO",
}

# Plataformas globais. Qualquer outro domínio fora de .br cai em 'privado':
# num catálogo Brasil-only, um .com desconhecido é quase sempre serviço
# brasileiro, não site estrangeiro.
INTERNACIONAIS = {
    "youtube.com", "github.com", "twitter.com", "x.com", "instagram.com",
    "facebook.com", "linkedin.com", "tiktok.com", "reddit.com", "t.me",
    "telegram.org", "whatsapp.com", "snapchat.com", "kwai.com",
    "wikipedia.org", "virustotal.com", "shodan.io", "interpol.int",
    "radarbox.com", "flightradar24.com", "marinetraffic.com", "windy.com",
    "aware-online.com", "radar24.net", "omnisci.com", "onemilliontweetmap.com",
    "google.com", "bing.com", "duckduckgo.com", "steamcommunity.com",
    "trends24.in", "tweetstats.com", "cruisemapper.com", "vesselfinder.com",
}

RE_ANCHOR = re.compile(r"<a\s+name=[\"'][^\"']*[\"']\s*>\s*</a>", re.I)
RE_H1 = re.compile(r"^#\s+(.*)$")
RE_H2 = re.compile(r"^##\s+(?!#)(.*)$")
RE_H3 = re.compile(r"^###\s+(?!#)(.*)$")
RE_H4PLUS = re.compile(r"^#{4,}\s")
RE_FENCE = re.compile(r"^\s*```")
RE_URL = re.compile(r"https?://[^\s<>()\[\]\"`'|,]+")
RE_MDLINK = re.compile(r"\[([^\]]*)\]\((https?://[^)]+)\)")
RE_BULLET = re.compile(r"^(\s*)[-*]\s+(.*)$")
RE_GRUPO_UF = re.compile(r"^\*\*(.+?)\s*\(([A-Z]{2})\)\*\*:?\s*$")
RE_GRUPO_BOLD = re.compile(r"^\*\*(.+?)\*\*:?\s*$")
RE_UF_INLINE = re.compile(r"\(([A-Z]{2})\)")
RE_DETAILS_ABRE = re.compile(r"<details>", re.I)
RE_DETAILS_FECHA = re.compile(r"</details>", re.I)


# --------------------------------------------------------------------------
# Normalização
# --------------------------------------------------------------------------

def eh_decoracao(ch):
    """Emoji, seletor de variação e ZWJ: ruído nos títulos."""
    if ch in "️︎‍":
        return True
    return unicodedata.category(ch) == "So"


def limpa_titulo(texto):
    texto = RE_ANCHOR.sub("", texto)
    texto = "".join(ch for ch in texto if not eh_decoracao(ch))
    return re.sub(r"\s+", " ", texto).strip()


def slug(texto):
    texto = limpa_titulo(texto)
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"[^a-zA-Z0-9]+", "-", texto).lower()
    return texto.strip("-")


def dobra_ascii(texto):
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in texto if not unicodedata.combining(c)).lower().strip()


def uf_do_texto(texto):
    """UF a partir de '(SP)' ou do nome do estado por extenso."""
    if not texto:
        return None
    m = RE_UF_INLINE.search(texto)
    if m and m.group(1) in UFS:
        return m.group(1)
    limpo = re.sub(r"[^a-z ]+", " ", dobra_ascii(texto)).strip()
    limpo = re.sub(r"\s+", " ", limpo)
    if limpo in NOMES_UF:
        return NOMES_UF[limpo]
    for nome in sorted(NOMES_UF, key=len, reverse=True):
        if re.search(rf"\b{re.escape(nome)}\b", limpo):
            return NOMES_UF[nome]
    return None


def uf_do_dominio(url):
    """'<orgao>.sp.gov.br' -> SP. Só vale para domínios de governo estadual."""
    host = re.sub(r"^https?://", "", url).split("/")[0].split(":")[0].lower()
    partes = host.split(".")
    if len(partes) >= 4 and partes[-2:] == ["gov", "br"]:
        sigla = partes[-3].upper()
        if sigla in UFS:
            return sigla
    return None


def normaliza_url(url):
    """Remove pontuação e fragmentos vazios grudados no fim da URL."""
    url = url.strip()
    url = re.sub(r"#+$", "", url)
    url = url.rstrip(".,;:!)")
    return url


# --------------------------------------------------------------------------
# Extração de links
# --------------------------------------------------------------------------

def limpa_rotulo(texto):
    """Tira marcador de bullet, negrito, crases de dork e pontuação de ligação."""
    texto = texto.strip()
    texto = re.sub(r"^[-*+]\s+", "", texto)          # marcador do bullet
    texto = re.sub(r"^\*\*(.*?)\*\*", r"\1", texto)  # **URL Base:**
    texto = texto.strip().strip("`").strip()         # dorks vêm entre crases
    # Os travessões na string abaixo são dados, não prosa: um contribuidor
    # ainda pode separar rótulo e URL com travessão. Não remover.
    texto = texto.rstrip(":-–—").strip()
    return texto.strip("*").strip()


def rotulo_do_prefixo(prefixo):
    """'- **URL Base:**' / '- Portal:' / '- ESAJ (Processos) -' -> rótulo limpo."""
    return limpa_rotulo(prefixo)


def rotulo_do_sufixo(sufixo):
    """'(Transferência de Arquivos)' logo depois da URL."""
    m = re.match(r"^\s*\((.+?)\)\s*$", sufixo.strip())
    return m.group(1).strip() if m else ""


def extrai_links(linha):
    """Retorna [(url, rotulo)] preservando a ordem de aparição na linha."""
    achados = []
    vistos = set()

    # Links markdown primeiro: o texto entre colchetes é o rótulo natural.
    resto = linha
    for m in RE_MDLINK.finditer(linha):
        rotulo, url = m.group(1).strip(), normaliza_url(m.group(2))
        if RE_URL.fullmatch(rotulo or ""):
            rotulo = ""  # [url](url), rótulo redundante
        if url and url not in vistos:
            achados.append((url, rotulo))
            vistos.add(url)
        resto = resto.replace(m.group(0), " ")

    for m in RE_URL.finditer(resto):
        url = normaliza_url(m.group(0))
        if not url or url in vistos:
            continue
        rotulo = rotulo_do_prefixo(resto[: m.start()])
        if not rotulo:
            rotulo = rotulo_do_sufixo(resto[m.end():])
        achados.append((url, rotulo))
        vistos.add(url)

    return achados


def urls_da_linha(linha):
    """Conjunto de URLs distintas na linha, base da reconciliação."""
    return {normaliza_url(u) for u in RE_URL.findall(linha)} - {""}


def eh_ignorada(url):
    return any(d in url for d in DOMINIOS_IGNORADOS)


# --------------------------------------------------------------------------
# Parsing do README
# --------------------------------------------------------------------------

def parse_readme(texto):
    fontes = []
    contadores = {"badge": 0, "code_fence": 0, "secao_ignorada": 0, "extraida": 0}
    orfas = []

    categoria = None
    categoria_ignorada = True
    fonte = None
    em_fence = False
    em_details = False
    uf_grupo = None
    pendente = None  # (indentação, rótulo) de bullet cujo link vem na linha seguinte

    def abre_fonte(nome, linha, implicita=False):
        return {
            "nome": nome,
            "categoria": categoria,
            "readme_linha": linha,
            "links": [],
            "_prosa": [],
            "_implicita": implicita,
        }

    def fecha_fonte():
        """Fontes implícitas (links soltos sob um ##) só valem se tiverem links;
        caso contrário são apenas o texto de abertura da categoria."""
        nonlocal fonte
        if fonte is None:
            return
        if not (fonte.pop("_implicita") and not fonte["links"]):
            fonte["descricao"] = " ".join(fonte["_prosa"]).strip()
            del fonte["_prosa"]
            fontes.append(fonte)
        fonte = None

    def contabiliza_fora(urls):
        """URLs que não pertencem a nenhuma fonte: badge ou seção ignorada."""
        for u in urls:
            contadores["badge" if eh_ignorada(u) else "secao_ignorada"] += 1

    for n, linha in enumerate(texto.splitlines(), start=1):
        crua = linha.rstrip()

        if RE_FENCE.match(crua):
            em_fence = not em_fence
            continue

        if em_fence:
            contadores["code_fence"] += len(urls_da_linha(crua))
            continue

        if RE_DETAILS_ABRE.search(crua):
            em_details = True
        if RE_DETAILS_FECHA.search(crua):
            em_details = False
            uf_grupo = None

        m1 = RE_H1.match(crua)
        m2 = RE_H2.match(crua)
        m3 = RE_H3.match(crua)

        if m1 or m2:
            fecha_fonte()
            uf_grupo = None
            contabiliza_fora(urls_da_linha(crua))
            if m1:
                categoria, categoria_ignorada = None, True
            else:
                titulo = limpa_titulo(m2.group(1))
                categoria = titulo
                categoria_ignorada = slug(titulo) in CATEGORIAS_IGNORADAS
                if not categoria_ignorada:
                    fonte = abre_fonte(titulo, n, implicita=True)
            continue

        if m3:
            fecha_fonte()
            uf_grupo = None
            contabiliza_fora(urls_da_linha(crua))
            if not categoria_ignorada:
                fonte = abre_fonte(limpa_titulo(m3.group(1)), n)
            continue

        if RE_H4PLUS.match(crua):
            contabiliza_fora(urls_da_linha(crua))  # badge de volta ao sumário
            continue

        urls_linha = urls_da_linha(crua)

        if categoria_ignorada or fonte is None:
            contabiliza_fora(urls_linha)
            continue

        # Cabeçalho de agrupamento dentro de <details>: **Bahia (BA)**
        if not urls_linha:
            mg = RE_GRUPO_UF.match(crua.strip())
            m_bullet = RE_BULLET.match(crua)
            if mg and mg.group(2) in UFS:
                uf_grupo = mg.group(2)
                pendente = None
            elif RE_GRUPO_BOLD.match(crua.strip()):
                uf_grupo = None
                pendente = None
            elif m_bullet:
                # "- Painel Estatístico SSP-SP" com a URL na linha seguinte
                pendente = (len(m_bullet.group(1)), limpa_rotulo(m_bullet.group(2)))
            elif crua.strip():
                if not fonte["links"] and not em_details:
                    fonte["_prosa"].append(crua.strip())
            continue

        m_bullet = RE_BULLET.match(crua)
        indent = len(m_bullet.group(1)) if m_bullet else 0

        atribuidas = set()
        for url, rotulo in extrai_links(crua):
            if eh_ignorada(url):
                contadores["badge"] += 1
                atribuidas.add(url)
                continue
            if not rotulo and pendente and indent > pendente[0]:
                rotulo = pendente[1]
            uf = uf_do_texto(rotulo) or uf_grupo or uf_do_dominio(url)
            fonte["links"].append({"url": url, "label": rotulo, "uf": uf})
            contadores["extraida"] += 1
            atribuidas.add(url)
        pendente = None

        for u in urls_linha - atribuidas:
            orfas.append({"linha": n, "url": u, "conteudo": crua.strip()[:120]})

    fecha_fonte()
    return fontes, contadores, orfas


# --------------------------------------------------------------------------
# Classificação heurística
# --------------------------------------------------------------------------

# Regra por categoria: o eixo principal. As 46 categorias já particionam bem
# o domínio, e as grandes (datasets, câmeras, telecom) são homogêneas.
REGRAS_CATEGORIA = {
    "beneficios-sociais-politicas-publicas": (["cpf"], ["beneficio"]),
    "pessoas-desaparecidas": (["nome"], ["dados_cadastrais"]),
    "pessoas-procuradas-pela-justica-no-brasil": (["nome"], ["mandado_prisao"]),
    "consulta-de-processos": (
        ["cpf", "cnpj", "nome", "numero_processo"],
        ["processo", "partes", "movimentacao"],
    ),
    "busca-de-informacoes-via-cpf-cnpj-crm-cna": (
        ["cpf", "cnpj"],
        ["dados_cadastrais", "situacao_cadastral"],
    ),
    "estatisticas-seguranca-publica": (["nenhum"], ["estatistica"]),
    "registros-eleitorais-e-politicos": (
        ["titulo_eleitor", "cpf", "nome"],
        ["dados_cadastrais"],
    ),
    "registros-de-imoveis-e-propriedades": (
        ["matricula_imovel", "endereco"],
        ["imovel"],
    ),
    "registros-ambientais": (["cnpj"], ["licenca_ambiental", "auto_infracao"]),
    "comercio-exterior": (["cnpj"], ["estatistica"]),
    "registros-de-marcas-e-patentes": (["nome", "razao_social"], ["dados_cadastrais"]),
    "transparencia-publica-e-defesa-do-consumidor": (
        ["cnpj", "nome"],
        ["contrato_publico", "licitacao", "sancao"],
    ),
    "diarios-oficiais": (["nome", "cnpj"], ["diario_oficial"]),
    "cultura-e-audiovisual": (["cnpj", "razao_social"], ["dados_cadastrais"]),
    "telecom": (["telefone"], ["operadora"]),
    "estacao-radio-base-erbs": (["coordenadas", "municipio"], ["erb"]),
    "informacoes-academicas": (["nome"], ["curriculo", "publicacao_academica"]),
    "mapas-e-georreferenciamento": (["coordenadas", "municipio"], ["mapa"]),
    "territorio-meio-ambiente-fiscalizacao": (
        ["cnpj", "municipio"],
        ["mapa", "auto_infracao"],
    ),
    "saude": (["cnes", "municipio"], ["dados_cadastrais"]),
    "motores-de-busca-contexto-brasil": (["nome"], ["dork"]),
    "rede-social": (["nome", "email", "telefone"], ["perfil_social"]),
    "indexadores-de-servico-de-mensagens-instantaneas": (["nome"], ["perfil_social"]),
    "datasets-dados-abertos": (["nenhum"], ["dataset"]),
    "dados-de-remuneracao-do-judiciario": (["nome"], ["remuneracao"]),
    "consulta-de-transporte-terrestre": (["placa", "renavam"], ["veiculo"]),
    "tracking-de-viagens-de-onibus": (["nenhum"], ["mapa"]),
    "consulta-de-transporte-aquaviario": (["embarcacao"], ["dados_cadastrais"]),
    "consulta-de-transporte-aereo": (["prefixo_aeronave"], ["dados_cadastrais"]),
    "cameras-online": (["nenhum"], ["video_ao_vivo"]),
    "ministerios-publicos-e-defensorias-publicas": (
        ["nome", "numero_processo"],
        ["processo"],
    ),
    "seguranca-cibernetica": (["dominio", "ip"], ["estatistica"]),
    "apis-publicas-brasileiras": (["cnpj", "cep"], ["api_json"]),
    "blockchain-e-criptomoedas": (["cnpj", "nome"], ["sancao"]),
    "defesa-civil-e-emergencias": (["municipio"], ["mapa"]),
    "energia-e-infraestrutura": (["cnpj", "municipio"], ["dados_cadastrais"]),
    "servicos-publicos-estaduais-e-conselhos-profissionais": (
        ["registro_profissional", "nome"],
        ["dados_cadastrais"],
    ),
    "categorias-de-dominios-br": (["dominio"], ["dados_cadastrais"]),
}

# Refinamento por palavra-chave sobre título + descrição.
REGRAS_PALAVRA = [
    (r"\bCPF\b", ["cpf"], []),
    (r"\bCNPJ\b", ["cnpj"], ["dados_cadastrais"]),
    (r"\bplacas?\b", ["placa"], ["veiculo"]),
    (r"\bchassi\b", ["chassi"], ["veiculo"]),
    (r"\brenavam\b", ["renavam"], ["veiculo"]),
    (r"\bIMEI\b", ["imei"], []),
    (r"\bCEP\b", ["cep"], ["endereco"]),
    (r"\bASN\b|sistema aut[oô]nomo", ["asn"], []),
    (r"\bdom[ií]nios?\b|\bwhois\b|\brdap\b", ["dominio"], []),
    (r"\be-?mails?\b", ["email"], []),
    (r"telefone|celular|portabilidade|orelh[aã]o|\bDDD\b", ["telefone"], ["operadora"]),
    (r"t[ií]tulo de eleitor|elei[çc][aã]o|eleitoral|filia[çc][aã]o partid", ["titulo_eleitor"], []),
    (r"\bOAB\b|advogad", ["oab"], []),
    (r"\bCRM\b|\bCFM\b|\bCFP\b|\bCAU\b|\bCFF\b|\bCFN\b|\bCREA\b|conselho (federal|regional)", ["registro_profissional"], ["dados_cadastrais"]),
    (r"processos?\b|jurisprud|tribunal|judicial", ["numero_processo"], ["processo"]),
    (r"antecedentes? criminal|antecedentes\b", [], ["antecedentes"]),
    (r"certid[aã]o|certid[oõ]es", [], ["certidao"]),
    (r"mandados? de pris[aã]o|procurad", ["nome"], ["mandado_prisao"]),
    (r"multas?\b", ["placa"], ["multa"]),
    (r"d[eé]bitos?\b|restitui[çc][aã]o", [], ["debito"]),
    (r"licita[çc]|preg[aã]o|compras? (governament|p[uú]blic)|contrata[çc][oõ]es", ["cnpj"], ["licitacao", "contrato_publico"]),
    (r"contratos?\b|conv[eê]nio|repasse", ["cnpj"], ["contrato_publico"]),
    (r"san[çc][oõ]es|san[çc][aã]o|inid[oô]ne|empresas punidas|\bCEIS\b|\bCNEP\b|\bCEPIM\b", ["cnpj"], ["sancao"]),
    (r"s[oó]cios?\b|quadro societ[aá]rio", ["cnpj"], ["socios"]),
    (r"\bCNAE\b", [], ["cnae"]),
    (r"sat[eé]lite|sensoriamento|imagens? orbital", [], ["imagem_satelite"]),
    (r"mapas?\b|georref|geogr[aá]fic|geoespacial|cartogr", [], ["mapa"]),
    (r"c[aâ]meras?\b|ao vivo|tempo real|streaming", ["nenhum"], ["video_ao_vivo"]),
    (r"dados abertos|dataset|microdados|reposit[oó]rio de dados", ["nenhum"], ["dataset"]),
    (r"\bAPI\b|\bREST\b|\bJSON\b", [], ["api_json"]),
    (r"benef[ií]cio|aux[ií]lio|previdenci|\bINSS\b|bolsa", ["cpf"], ["beneficio"]),
    (r"remunera[çc]|sal[aá]rio|folha de pagamento|contracheque", ["nome"], ["remuneracao"]),
    (r"estat[ií]stica|indicador|painel|panorama|censo", ["nenhum"], ["estatistica"]),
    (r"curr[ií]culo|lattes", ["nome"], ["curriculo"]),
    (r"teses?\b|disserta[çc]|peri[oó]dico|scielo|acad[eê]mic", [], ["publicacao_academica"]),
    (r"di[aá]rios? oficia", [], ["diario_oficial"]),
    (r"im[oó]vel|im[oó]veis|\bIPTU\b|cart[oó]rio de registro", ["endereco"], ["imovel"]),
    (r"cadastro ambiental rural|\bCAR\b|\bSICAR\b", ["car"], ["area_rural"]),
    (r"licen[çc]a ambiental|licenciamento ambiental", ["cnpj"], ["licenca_ambiental"]),
    (r"auto de infra[çc]|autua[çc]|embargo", ["cnpj"], ["auto_infracao"]),
    (r"radiofrequ[eê]ncia|radioamador|indicativo|\bSTEL\b", [], ["radiofrequencia"]),
    (r"outorga|radiodifus", ["cnpj"], ["outorga"]),
    (r"aeronave|\bRAB\b|v[oô]os?\b|aeroporto", ["prefixo_aeronave"], ["dados_cadastrais"]),
    (r"embarca[çc]|aquavi[aá]rio|mar[ií]tim|navega[çc][aã]o", ["embarcacao"], ["dados_cadastrais"]),
    (r"inscri[çc][aã]o estadual|sintegra|\bNIRE\b|junta comercial", ["inscricao_estadual", "cnpj"], ["dados_cadastrais"]),
    (r"\bCNES\b|estabelecimentos? de sa[uú]de", ["cnes"], ["dados_cadastrais"]),
    (r"\bIBGE\b|munic[ií]pio", ["municipio"], []),
    (r"google hacking|dork|shodan|\bbing\b|duckduckgo", ["nome"], ["dork"]),
    (r"linkedin|instagram|twitter|facebook|tiktok|youtube|telegram|whatsapp|rede social", ["nome"], ["perfil_social"]),
    (r"situa[çc][aã]o cadastral|comprovante de inscri[çc]", [], ["situacao_cadastral"]),
    (r"nome completo|raz[aã]o social", ["nome"], ["dados_cadastrais"]),
    (r"[oó]bitos?\b|falecid|nascimentos?\b|casamentos?\b", ["nome"], ["dados_cadastrais"]),
    (r"cart[oó]rio", ["nome"], ["certidao"]),
    (r"lista telef[oô]nica", ["nome", "telefone"], ["dados_cadastrais"]),
    (r"\bprocon\b|reclama[çc]|consumidor", ["cnpj"], ["sancao"]),
    (r"marcas?\b|patentes?\b|\bINPI\b|desenho industrial", ["razao_social"], ["dados_cadastrais"]),
    (r"seguran[çc]a privada", ["cnpj"], ["dados_cadastrais"]),
    (r"produtos? qu[ií]mic", ["cnpj"], ["licenca_ambiental"]),
    (r"cadastro positivo", ["cpf"], ["dados_cadastrais"]),
    (r"bens a venda|venda ou aluguel|leil[aã]o", ["endereco"], ["imovel"]),
]

REGRAS_PALAVRA = [(re.compile(p, re.I), i, o) for p, i, o in REGRAS_PALAVRA]


def classifica_tipo_fonte(links):
    """Deriva a natureza institucional do domínio da primeira URL."""
    if not links:
        return "indefinido"
    url = links[0]["url"]
    host = re.sub(r"^https?://", "", url).split("/")[0].split(":")[0].lower()
    host = re.sub(r"^www\d?\.", "", host)

    if re.search(r"(google|bing)\.com/search|duckduckgo\.com/\?q=|shodan\.io/search", url):
        return "dork"
    if host.endswith(".jus.br") or host == "jus.br":
        return "judiciario"
    if host.endswith(".mp.br"):
        return "ministerio_publico"
    if host.endswith(".leg.br"):
        return "legislativo"
    if host.endswith(".def.br"):
        return "defensoria"
    if host.endswith(".gov.br") or host == "gov.br":
        partes = host.split(".")
        # <orgao>.<uf>.gov.br  ->  estadual (municipal é indistinguível)
        if len(partes) >= 4 and partes[-3].upper() in UFS:
            return "estadual"
        return "federal"
    if host.endswith(".edu.br") or re.search(r"\b(usp|unb|ufrj|ufrgs|unicamp|fiocruz)\b", host):
        return "academico"
    if host.endswith(".org.br") or host.endswith(".org"):
        return "ong"
    if host.endswith(".rio"):
        return "municipal"  # geo-TLD do município do Rio de Janeiro
    base = ".".join(host.split(".")[-2:])
    if host in INTERNACIONAIS or base in INTERNACIONAIS:
        return "internacional"
    return "privado"


def classifica(fonte, overrides):
    ident = fonte["id"]
    tipo = classifica_tipo_fonte(fonte["links"])
    entradas, saidas = set(), set()

    cat = REGRAS_CATEGORIA.get(fonte["categoria_id"])
    if cat:
        entradas.update(cat[0])
        saidas.update(cat[1])

    alvo = f"{fonte['nome']} {fonte['descricao']}"
    for padrao, ins, outs in REGRAS_PALAVRA:
        if padrao.search(alvo):
            entradas.update(ins)
            saidas.update(outs)

    # 'nenhum' só faz sentido sozinho.
    if len(entradas) > 1:
        entradas.discard("nenhum")

    classificacao = "heuristica" if (entradas or saidas) else "indefinido"

    ov = overrides.get(ident)
    if ov:
        if "input" in ov:
            entradas = set(ov["input"])
        if "output" in ov:
            saidas = set(ov["output"])
        if "tipo_fonte" in ov:
            tipo = ov["tipo_fonte"]
        if "descricao" in ov:
            fonte["descricao"] = ov["descricao"]
        if "observacao" in ov:
            fonte["observacao"] = ov["observacao"]
        classificacao = "override"

    fonte["tipo_fonte"] = tipo
    fonte["input"] = sorted(entradas)
    fonte["output"] = sorted(saidas)
    fonte["classificacao"] = classificacao
    return fonte


# --------------------------------------------------------------------------
# Montagem
# --------------------------------------------------------------------------

def atribui_ids(fontes):
    usados = {}
    for f in fontes:
        cat_id = slug(f["categoria"] or "sem-categoria")
        base = f"{cat_id}/{slug(f['nome'])}"
        n = usados.get(base, 0) + 1
        usados[base] = n
        f["categoria_id"] = cat_id
        f["id"] = base if n == 1 else f"{base}-{n}"
    return fontes


def valida(fontes, taxonomia):
    erros = []
    validos = {
        eixo: set(taxonomia[eixo]["termos"]) for eixo in ("input", "output", "tipo_fonte")
    }
    vistos = set()
    for f in fontes:
        if f["id"] in vistos:
            erros.append(f"id duplicado: {f['id']}")
        vistos.add(f["id"])
        for eixo in ("input", "output"):
            for termo in f[eixo]:
                if termo not in validos[eixo]:
                    erros.append(f"{f['id']}: {eixo} '{termo}' fora da taxonomia")
        if f["tipo_fonte"] not in validos["tipo_fonte"]:
            erros.append(f"{f['id']}: tipo_fonte '{f['tipo_fonte']}' fora da taxonomia")
        for link in f["links"]:
            if link["uf"] and link["uf"] not in UFS:
                erros.append(f"{f['id']}: UF inválida '{link['uf']}'")
    return erros


def monta_index(fontes):
    links = []
    for f in fontes:
        for link in f["links"]:
            links.append({
                "url": link["url"],
                "label": link["label"],
                "uf": link["uf"],
                "fonte_id": f["id"],
                "fonte": f["nome"],
                "categoria": f["categoria"],
                "categoria_id": f["categoria_id"],
                "descricao": f["descricao"],
                "tipo_fonte": f["tipo_fonte"],
                "input": f["input"],
                "output": f["output"],
            })
    return links


def serializa(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def carrega_json(caminho):
    with open(caminho, encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="falha se os arquivos gerados estiverem desatualizados")
    ap.add_argument("--report", action="store_true",
                    help="imprime estatísticas e fontes sem classificação")
    args = ap.parse_args()

    taxonomia = carrega_json(DATA / "taxonomy.json")
    overrides = carrega_json(DATA / "overrides.json").get("overrides", {})
    texto = README.read_text(encoding="utf-8")

    fontes, contadores, orfas = parse_readme(texto)
    fontes = atribui_ids(fontes)
    fontes = [classifica(f, overrides) for f in fontes]

    erros = valida(fontes, taxonomia)
    desconhecidos = sorted(set(overrides) - {f["id"] for f in fontes})
    for ident in desconhecidos:
        erros.append(f"override para id inexistente: {ident}")

    total_urls = sum(len(urls_da_linha(l)) for l in texto.splitlines())
    reconciliadas = sum(contadores.values())
    faltando = total_urls - reconciliadas - len(orfas)

    doc_sources = {
        "_sobre": "GERADO por tools/build_dataset.py a partir de README.md. Não editar à mão: use data/overrides.json.",
        "fonte": "README.md",
        "total": len(fontes),
        "sources": fontes,
    }
    links = monta_index(fontes)
    doc_index = {
        "_sobre": "GERADO por tools/build_dataset.py. Índice achatado de links para busca.",
        "fonte": "README.md",
        "total": len(links),
        "links": links,
    }

    saidas = {
        DATA / "sources.json": serializa(doc_sources),
        DATA / "index.json": serializa(doc_index),
    }

    if args.report or args.check:
        indef = [f for f in fontes if f["classificacao"] == "indefinido"]
        sem_link = [f for f in fontes if not f["links"]]
        print(f"categorias .......... {len({f['categoria_id'] for f in fontes})}")
        print(f"fontes .............. {len(fontes)}")
        print(f"links ............... {len(links)}")
        print()
        print("reconciliação de URLs")
        print(f"  distintas por linha  {total_urls}")
        print(f"  extraídas            {contadores['extraida']}")
        print(f"  badges               {contadores['badge']}")
        print(f"  code fences          {contadores['code_fence']}")
        print(f"  seções ignoradas     {contadores['secao_ignorada']}")
        print(f"  órfãs                {len(orfas)}")
        print(f"  não contabilizadas   {faltando}")
        print()
        print(f"classificação: heurística {sum(1 for f in fontes if f['classificacao'] == 'heuristica')}"
              f" | override {sum(1 for f in fontes if f['classificacao'] == 'override')}"
              f" | indefinido {len(indef)}")
        if sem_link:
            print(f"\nfontes sem nenhum link ({len(sem_link)}):")
            for f in sem_link:
                print(f"  README.md:{f['readme_linha']}  {f['id']}")
        if orfas:
            print(f"\nURLs órfãs ({len(orfas)}):")
            for o in orfas[:20]:
                print(f"  README.md:{o['linha']}  {o['url']}")
        if args.report and indef:
            print(f"\nsem classificação, candidatas a override ({len(indef)}):")
            for f in indef:
                print(f"  README.md:{f['readme_linha']}  {f['id']}")

    if erros:
        print("\nERROS DE VALIDAÇÃO:", file=sys.stderr)
        for e in erros[:40]:
            print(f"  {e}", file=sys.stderr)
        return 1

    if orfas or faltando:
        print("\nERRO: reconciliação de URLs não fechou.", file=sys.stderr)
        return 1

    if args.check:
        for caminho, conteudo in saidas.items():
            atual = caminho.read_text(encoding="utf-8") if caminho.exists() else None
            if atual != conteudo:
                print(f"\nERRO: {caminho.relative_to(RAIZ)} desatualizado. "
                      f"Rode: python3 tools/build_dataset.py", file=sys.stderr)
                return 1
        print("\nOK: arquivos gerados estão atualizados.")
        return 0

    DATA.mkdir(exist_ok=True)
    for caminho, conteudo in saidas.items():
        caminho.write_text(conteudo, encoding="utf-8")
        print(f"escrito {caminho.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
