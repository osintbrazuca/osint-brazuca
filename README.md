<h1 align="center">
  <br>
  <a href="#"><img src="assets/logo_profile.png" width="300px" alt="OSINT Brazuca"></a>
</h1>

<h4 align="center">OSINT (Open-source intelligence)</h4>

<p align="center">
<a href="https://github.com/osintbrazuca/osint-brazuca/blob/main/LICENSE"><img src="https://img.shields.io/github/license/osintbrazuca/osint-brazuca?color=blue"></a>
<a href="https://github.com/osintbrazuca/osint-brazuca/graphs/contributors"><img src="https://img.shields.io/github/contributors-anon/osintbrazuca/osint-brazuca"></a>
<a href="https://github.com/osintbrazuca/osint-brazuca/issues"><img src="https://img.shields.io/github/issues-raw/osintbrazuca/osint-brazuca"></a>
<a href="https://github.com/osintbrazuca/osint-brazuca/discussions"><img src="https://img.shields.io/github/discussions/osintbrazuca/osint-brazuca"></a>
<a href="https://github.com/osintbrazuca/osint-brazuca/network/members"><img src="https://img.shields.io/github/forks/osintbrazuca/osint-brazuca"></a>
<img src="https://img.shields.io/github/stars/osintbrazuca/osint-brazuca.svg?style=social" title="Stars" /> 
</p>

> **Navegação**: [🏠 README Principal](README.md) | [📖 Exemplos Práticos](EXEMPLOS_PRATICOS.md) | [🔀 Fluxogramas](FLUXOGRAMA.md) | [📊 Guia Rápido](GUIA_RAPIDO.md) | [🤝 Contribuir](CONTRIBUICAO.md)

# Introdução

O Projeto **OSINT Brazuca** é um repositório criado com intuito de reunir informações, fontes(websites/portais) e tricks de OSINT dentro do contexto Brasil 🇧🇷.

OSINT (sigla para Open source intelligence ou Inteligência de Fontes Abertas) é um modelo de inteligência que visa encontrar, selecionar e adquirir informações de fontes públicas e analisá-las para que junto com outras fontes possam produzir um conhecimento. As informações coletadas por meio de fontes abertas, possuem baixo custo, se comparado as onerosas operações de campo.

## ⚠️ Avisos Legais e Éticos

> **ATENÇÃO**: Este repositório contém apenas fontes de informação PÚBLICAS e LEGAIS. O uso inadequado das informações aqui contidas é de responsabilidade exclusiva do usuário.

### 🔒 LGPD - Lei Geral de Proteção de Dados
> Todas as consultas devem respeitar a **Lei nº 13.709/2018 (LGPD)**. O tratamento de dados pessoais deve ter base legal e finalidade legítima.


> **⚖️ Base Legal**: Lei nº 13.709/2018 (LGPD) | Lei nº 12.965/2014 (Marco Civil) | Lei nº 12.527/2011 (LAI)

<details>
<summary>✅ Boas Práticas:</summary>

- Utilizar apenas fontes públicas oficiais
- Respeitar a privacidade e dignidade das pessoas
- Documentar fontes e metodologia utilizada
- Ter propósito legítimo (jornalismo, pesquisa, segurança, compliance)
- Não compartilhar dados sensíveis publicamente

</details>

<details>
<summary>❌ Práticas Proibidas:</summary>

- Engenharia social ou invasão de sistemas
- Perseguição (stalking) ou assédio
- Uso para discriminação ou preconceito
- Comercialização não autorizada de dados
- Violação de sigilo profissional

</details>



### ⚠️ Limitações e Avisos Importantes

<details>
<summary>🕒 Atualização de Dados:</summary>

- Dados públicos podem estar **desatualizados**
- Sempre verificar a **data da última atualização** nas fontes
- **Cruzar informações** de múltiplas fontes para validação
- Sistemas governamentais podem estar em **manutenção**
</details>

<details>
<summary>🔒 Acesso e Requisitos:</summary>

- Alguns portais exigem **cadastro prévio via gov.br**
- Serviços pode existir limitação de uso
- **CAPTCHA** pode limitar consultas automatizadas

</details>

<details>
<summary>🤖 Rate Limiting e Automação:</summary>

- APIs públicas possuem **limites de requisições**
- Respeite os **limites técnicos** estabelecidos
- Use **cache** quando possível para reduzir requisições
- Consultas em massa podem ser **bloqueadas**

</details>

<details>
<summary>📱 Responsabilidade e Ética:</summary>

- Informações são **públicas** mas protegidas pela LGPD
- Uso **indevido** pode resultar em **sanções legais** e criminais
- **Não compartilhe** dados sensíveis publicamente
- Documente sempre a **finalidade legítima** da consulta
- Mantenha **registro** de todas as pesquisas realizadas
- Resumindo: Não seja cuzão

</details>

---

## 📚 Documentação Complementar

Para facilitar o uso deste repositório, criamos documentos especializados:

- 📊 **[Guia Rápido de Consultas](GUIA_RAPIDO.md)** - Tabelas comparativas, top 10 consultas e legendas
- 🔍 **[Exemplos Práticos de Investigação](EXEMPLOS_PRATICOS.md)** - 6 casos de uso detalhados com passo a passo
- 🔄 **[Fluxogramas de Investigação](FLUXOGRAMA.md)** - Diagramas visuais de processos investigativos
- 🔄 **[Como Contribuir](CONTRIBUICAO.md)** - Diretrizes para diferentes tipos de contribuições
---

# Sumário

- [Benefícios Sociais](#beneficios-sociais)
- [Pessoas Desaparecidas](#pessoas-desaparecidas)
- [Pessoas Procuradas pela Justiça](#pessoas-procuradas)
- [Consulta de Processos](#consulta-processos)
- [Busca de Informações via CPF/CNPJ/CRM/CNA](#busca-cpf-cnpj-crm-cna)
- [Estatísticas](#estatísticas)
- [Registros Eleitorais e Políticos](#registros-eleitorais-politicos)
- [Registros de Imóveis e Propriedades](#registros-imoveis-propriedades)
- [Registros Ambientais](#registros-ambientais)
- [Comércio Exterior](#comercio-exterior)
- [Registros de Marcas e Patentes](#registros-marcas-patentes)
- [Transparência Pública e Defesa do Consumidor](#transparencia-defesa-consumidor)
- [Diários Oficiais](#diarios-oficiais)
- [Cultura e Audiovisual](#cultura-audiovisual)
- [Telecom](#telecom)
- [Estação Rádio Base - ERBs](#estacoes-radio-erbs)
- [Informações Acadêmicas](#informacoes-academicas)
- [Mapas e Georreferenciamento](#mapas-geo)
- [Território, Meio Ambiente & Fiscalização](#territorio-meio-ambiente-fiscalizacao)
- [Saúde](#saude)
- [Motores de Busca Contexto Brasil](#dorks)
- [Rede Social](#redes-sociais)
- [Indexadores de Serviço de Mensagens Instantâneas](#indexador-mensagens)
- [Segurança Cibernética](#seguranca-cibernetica)
- [Blockchain e Criptomoedas](#blockchain-criptomoedas)
- [Defesa Civil e Emergências](#defesa-civil-emergencias)
- [Energia e Infraestrutura](#energia-infraestrutura)
- [Datasets / Dados Abertos](#datasets)
- [Dados de remuneração do Judiciário](#dados-de-remuneracao-do-judiciario)
- [Consulta de Transporte Terrestre](#consulta-transporte-terrestre)
- [Tracking de Viagens de Ônibus ](#tracking-viagens-onibus)
- [Consulta de Transporte Aquaviário](#consulta-transporte-aquaviario)
- [Consulta de Transporte Aéreo](#consulta-transporte-aereo)
- [Câmeras Online](#cameras-online)
- [Ministérios Públicos e Defensorias Públicas](#ministerios-publicos-defensorias)
- [Serviços Públicos Estaduais e Conselhos Profissionais](#servicos-estaduais)
- [Outras Buscas](#outras-buscas)
- [Categorias de Domínios .br](#dominios-br)
- [Autores](#autores)
- [Contribuições](#contribuicoes)
- [Créditos](#creditos)

---

## Benefícios sociais (Políticas Públicas) 📑 <a name="beneficios-sociais"></a>

### Benefícios sociais existentes

- https://www.caixa.gov.br/programas-sociais/Paginas/default.aspx

### Consulta Benefícios Sociais

As famílias atendidas pelo Programa Bolsa Família devem entregar o extrato bancário de pagamento do benefício, juntamente com a consulta pública do programa “bolsa família”

- https://www.beneficiossociais.caixa.gov.br/consulta/beneficio/04.01.00-00_00.asp

### Consulta ao Auxílio Emergencial

canal para consulta ao resultado da análise do Auxílio Emergencial.
Por aqui você terá condições de saber se atende aos critérios de elegibilidade para recebimento do Auxílio Emergencial.

- https://consultaauxilio.cidadania.gov.br/consulta/#/

### Comprovante Situação Cadastral de Pessoa Jurídica

Comprovante de Inscrição e de Situação Cadastral de Pessoa Jurídica, obtido por meio de consulta no endereço eletrônico:

- http://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/cnpjreva/Cnpjreva_Solicitacao.asp

### Extrato do Benefício de Prestação Continuada (INSS)

- ...

### Meu INSS
Portal oficial para consulta de benefícios previdenciários, extrato de contribuições, agendamentos e outros serviços do INSS.
- https://meu.inss.gov.br/

### Consulta de Valores a Receber do Sistema Financeiro

Consulta para saber se a Pessoa Física ou Jurídica possuem valores a receber no Sistema Financeiro.

- https://valoresareceber.bcb.gov.br/publico/
- Via Requisição GET, substituir os zeros pelo CPF ou CNPJ sem pontos ou traços, e a data de nascimento no formato ANO-MES-DIA:
  https://valoresareceber.bcb.gov.br/publico/rest/valoresAReceber/00000000000/1960-12-01

### Gás do Povo

Portal oficial para consulta de beneficiários do programa gás do povo.
- https://gasdopovo.mds.gov.br/

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Pessoas Desaparecidas 🔍 <a name="pessoas-desaparecidas"></a>

### Portais de Desaparecidos

Uma relação de links com dados sobre desaparecidos, gerida pela estado ou ONGs, tais urls permitem consulta, pela internet, de fotografias e informações de pessoas desaparecidas de diversos estados Brasileiros.

<details>
<summary>Portais de Desaparecidos</summary>

- https://desaparecidos.pcivil.rj.gov.br/pesquisar
- https://www.desaparecidos.pr.gov.br/desaparecidos/
- https://www.pc.rs.gov.br/desaparecidos
- https://desaparecidos.pjc.mt.gov.br/inicio
- https://carapicuiba.sp.gov.br/desaparecido
- https://desaparecidos.policiacivil.mg.gov.br/desaparecido/album
- https://desaparecidosdobrasil.org/pesquisar-desaparecidos/
- https://desaparecidos.policiacivil.mg.gov.br/
- https://www.pcdf.df.gov.br/servicos/desaparecidos
- https://www.disquedenuncia.org.br/desaparecidos-list
- https://www.ssp.ma.gov.br/disque-denuncia/desaparecidos/
- https://desaparecidos.pc.sc.gov.br/#/
- https://www.pm.sc.gov.br/sos-desaparecidos/default/index?sort=-desaparecido_desaparecimento_data
- http://www.policiacivil.pe.gov.br/adultos-desaparecidos
- https://www2.bauru.sp.gov.br/desaparecidos/
- https://desaparecidos.osasco.sp.gov.br/#/portal
- https://www.pm.ce.gov.br/desaparecidos/
- https://desaparecidos.pb.gov.br/desaparecidos/desaparecidos.jsf
- https://desaparecidos.pr.gov.br/desaparecidos/desaparecidos.do?action=iniciarProcesso&m=false
- http://sisgou.seds.al.gov.br/base2/desaparecidos_almanaque/
- http://www.feiradesantana.ba.gov.br/seprev/desaparecidos/desaparecidos.asp
- https://www.policiacivil.se.gov.br/desaparecidos/

</details>

### Busca por Desaparecidos Banco de Dados Geral / São Paulo

É usado CPF da Pessoa Desaparecida como valor de pesquisa

- https://www.ssp.sp.gov.br/servicos/desaparecidos

### Busca por Desaparecidos Banco de Dados Polícia Científica / São Paulo

É usado nome e CPF da Pessoa Desaparecida como valor de pesquisa

- https://www.policiacientifica.sp.gov.br/iml/consultadesaparecidos

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Pessoas Procuradas pela Justiça no Brasil <a name="pessoas-procuradas"></a>

### Brasil — Programa Captura (MJSP)

Lista nacional de criminosos mais procurados, organizada por estado, com mandados de prisão prioritários.  
- https://www.gov.br/mj/pt-br/assuntos/sua-seguranca/seguranca-publica/operacoes-integradas/projeto-captura

### Maranhão (MA) — SSP/MA | Disque-Denúncia – Procurados

Lista pública de pessoas procuradas pela Justiça no Maranhão, com fotos e dados básicos.  
- https://www.ssp.ma.gov.br/disque-denuncia/procurados/

### Ceará (CE) — SSPDS/CE | Procurados

Portal oficial com relação de foragidos e procurados pela Justiça no Estado do Ceará.  
- https://procurados.sspds.ce.gov.br/index

### Bahia (BA) — SSP/BA | Baralho do Crime (Espadas)

Lista oficial dos criminosos mais procurados da Bahia, organizada por categorias.  
- https://disquedenuncia.ssp.ba.gov.br/baralho-do-crime/espadas/

### INTERPOL — Pessoas Procuradas Internacionalmente

Lista pública de fugitivos procurados internacionalmente, incluindo brasileiros com mandados internacionais.  
- https://www.interpol.int/Contacts/Fugitives-wanted-persons

### Brasil — Sinesp Cidadão (Consulta de Procurados)

Consulta oficial de procurados pela Justiça no Brasil via aplicativo do governo federal.  
- https://www.gov.br/pt-br/servicos/consultar-os-criminosos-mais-procurados-do-brasil  
  - Android: https://play.google.com/store/apps/details?id=br.gov.sinesp.cidadao.android  
  - iOS: https://apps.apple.com/br/app/sinesp-cidad%C3%A3o/id768157962


##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Consulta de Processos 🧑‍⚖️ <a name="consulta-processos"></a>

### Portal e-S\*\*

O portal e-S\*\* é uma solução que visa facilitar a troca de informações e agilizar o trâmite processual por meio de diversos serviços WEB voltados para os advogados, cidadãos e serventuários da justiça.

<details>
<summary>Portais TJ</summary>

- https://esaj.tjac.jus.br/esaj/portal.do?servico=190090#
- https://www.tjba.jus.br/portal/busca-resultado/#
- https://esaj.tjce.jus.br/esaj/portal.do?servico=190090#
- https://esaj.tjsc.jus.br/esaj/portal.do?servico=190090#
- https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090#
- http://esaj.tjac.jus.br/esaj/portal.do?servico=190090#
- http://esaj.tjam.jus.br/esaj/portal.do?servico=190090#
- http://esaj.tjce.jus.br/esaj/portal.do?servico=190090#

</details>

### PJe - Processo Judicial Eletrônico por Tribunal

Sistema de consulta processual unificado utilizado por diversos tribunais brasileiros.

<details>
<summary>Consultas PJe - Justiça Federal</summary>

**Tribunais Regionais Federais:**
- TRF1 (1ª Região - DF, GO, TO, MT, BA, PI, MA, PA, AM, AC, RR, RO, AP): https://pje1g.trf1.jus.br/consultapublica/ConsultaPublica/listView.seam
- TRF2 (2ª Região - RJ, ES): https://pje.trf2.jus.br/pje/ConsultaPublica/listView.seam
- TRF3 (3ª Região - SP, MS): https://pje1g.trf3.jus.br/consultapublica/ConsultaPublica/listView.seam
- TRF4 (4ª Região - RS, SC, PR): https://pje2g.trf4.jus.br/pje/ConsultaPublica/listView.seam
- TRF5 (5ª Região - CE, RN, PB, PE, AL, SE): https://pje.trf5.jus.br/pje/ConsultaPublica/listView.seam
- TRF6 (6ª Região - MG): https://pje.trf6.jus.br/pje/ConsultaPublica/listView.seam

</details>

<details>
<summary>Consultas PJe - Justiça do Trabalho</summary>

**Tribunais Regionais do Trabalho (principais):**
- TST (Tribunal Superior do Trabalho): https://pje.tst.jus.br/consultaprocessual/
- TRT1 (Rio de Janeiro): https://pje.trt1.jus.br/consultaprocessual/
- TRT2 (São Paulo): https://pje.trt2.jus.br/consultaprocessual/
- TRT3 (Minas Gerais): https://pje.trt3.jus.br/consultaprocessual/
- TRT4 (Rio Grande do Sul): https://pje.trt4.jus.br/consultaprocessual/
- TRT15 (Campinas/SP): https://pje.trt15.jus.br/consultaprocessual/

</details>

<details>
<summary>Consultas PJe - Justiça Eleitoral</summary>

**Tribunal Superior Eleitoral:**
- TSE: https://pje.tse.jus.br/pje/ConsultaPublica/listView.seam

</details>

### Portal de Jurisprudência Unificada
Busca unificada de jurisprudência e acórdãos dos tribunais superiores (STF, STJ, TST, TSE, STM).
- https://jurisprudencia.stf.jus.br/

### Consulta Processual Unificada - CNJ
Sistema em desenvolvimento para consulta unificada de processos em todos os tribunais do Brasil.
- https://www.cnj.jus.br/consulta-processual-publica/

### Banco Nacional de Mandados de Prisão

O Sistema BNMP – Banco Nacional de Mandados de Prisão tem a finalidade de facilitar o conhecimento por qualquer pessoa e o cumprimento de diligências por parte das autoridades policiais, assim como auxiliar os juízes no exercício de sua jurisdição. Este será alimentado através de um WebService e tem a finalidade de disponibilizar a consulta e a recepção dos mandados de prisão.

- https://portalbnmp.cnj.jus.br/#/pesquisa-peca#

### Portais de Tribunais Regionais Federal (TRF)

**TRF1**: O Tribunal Regional Federal da 1ª Região, com sede em Brasília, tem sob sua jurisdição o Distrito Federal e os estados do Acre, Amapá, Amazonas, Bahia, Goiás, Maranhão, Mato Grosso, Minas Gerais, Pará, Piauí, Rondônia, Roraima e Tocantins.
- https://portal.trf1.jus.br

**TRF2**: 2a instância da Justiça Federal da 2a Região, com jurisdição no Rio de Janeiro e no Espírito Santo.
- https://portal.trf2.jus.br

**TRF5**: Portal com informações e serviços providos pelo TRF5, tem sob sua jurisdição jfal ,jfce ,jfpb ,jfpe ,jfrn ,jfse.
- https://portal.trf5.jus.br

### JusBrasil

Startup que une Direito e Tecnologia para fazer com que a justiça ultrapasse as fronteiras dos tribunais e chegue às casas de qualquer cidadão ou cidadã, empoderando suas decisões por meio da informação.

- https://www.jusbrasil.com.br/

### Escavador

Encontre e acompanhe informações relevantes para você sua empresa seu cliente. Pesquise por pessoas, instituições, processos judiciais ou qualquer termo do seu interesse.

- https://www.escavador.com/

### ABRAJI - Publique-se

Descubra os processos judiciais no Brasil que citam políticos como partes em ações judiciais de interesse público. O banco de dados do projeto permite atualmente a consulta de processos do STF, STJ, tribunais federais e tribunais de Justiça, que citam 3445 políticos. Mais processos e tribunais serão adicionados ao longo de 2025.

- https://www.publique-se.org.br/

### STJ - Superior Tribunal de Justiça
Sistema de consultas processuais do Superior Tribunal de Justiça com múltiplas funcionalidades.
<details>
<summary>Consultas STJ</summary>

- Portal de Processos - https://processo.stj.jus.br/processo/
- Diário da Justiça - https://processo.stj.jus.br/processo/dj/init
- Pesquisa de Processos - https://processo.stj.jus.br/processo/pesquisa/
- Preferências de Pesquisa - https://processo.stj.jus.br/processo/pesquisa/preferencias/
- Informações Técnico-Administrativas - https://processo.stj.jus.br/processo/ita/
- Emissão de Certidão - https://processo.stj.jus.br/processo/certidao/emissao
- Validação de Certidão - https://processo.stj.jus.br/processo/certidao/validacao
- Editais do Diário da Justiça - https://processo.stj.jus.br/processo/dj/edital/?aplicacao=dj.editais&ind_vigentes=true

</details>

### CNJ - Consulta de Processos de Improbidade Administrativa
Consulta pública de processos de improbidade administrativa por número do processo.
- https://www.cnj.jus.br/improbidade_adm/consultar_processo.php

### CNJ - Consulta de Requeridos por Improbidade
Consulta de pessoas e entidades requeridas em ações de improbidade administrativa.
- https://www.cnj.jus.br/improbidade_adm/consultar_requerido.php

### CNJ - Consulta de Classes Processuais SGT
Sistema de Gestão de Tabelas Processuais Unificadas - consulta de classes processuais.
- https://www.cnj.jus.br/sgt/consulta_publica_classes.php

### PJe - Comunicação Processual
Sistema de intimações e comunicações processuais eletrônicas do Processo Judicial Eletrônico.
- https://comunica.pje.jus.br/

### Consultas Processuais por Estado
Consultas de processos judiciais em Tribunais de Justiça Estaduais e outras instâncias.

<details>
<summary>Consultas por Estado</summary>

**Acre (AC)**
- ESAJ (Processos) - https://esaj.tjac.jus.br/esaj/portal.do?servico=190090

**Alagoas (AL)**
- TJ-AL Processos - https://www2.tjal.jus.br/cpopg/open.do

**Amapá (AP)**
- TJ-AP PJe 1º Grau - https://pje.tjap.jus.br/1g/ConsultaPublica/listView.seam
- TJ-AP PJe 2º Grau - https://pje.tjap.jus.br/2g/ConsultaPublica/listView.seam
- TJ-AP Tucujuris (Processos Físicos) - https://tucujuris.tjap.jus.br/pages/consultar-processo/consultar-processo.html
- SEEU-AP Sistema Eletrônico de Execução Unificado - https://seeu-consulta-pub.pje.jus.br/seeu/processo/consultaPublica.do?actionType=iniciar

**Amazonas (AM)**
- TJ-AM Processos - https://consultasaj.tjam.jus.br/cpopg/open.do

**Bahia (BA)**
- TJ-BA Processos 1º Grau - https://esaj.tjba.jus.br/cpopg/open.do
- TJ-BA Processos 2º Grau - https://esaj.tjba.jus.br/cposg5/open.do

**Ceará (CE)**
- TJ-CE Processos - https://esaj.tjce.jus.br/cpopg/open.do

**Distrito Federal (DF)**
- TJ-DFT Processos - https://pje2i.tjdft.jus.br/consultapublica

**Goiás (GO)**
- Processos físicos 1º grau - https://www.tjgo.jus.br/index.php/processo-fisico/primeiro-grau
- Processos físicos 2º grau - https://www.tjgo.jus.br/index.php/processo-fisico/segundo-grau
- Processo judicial digital - https://projudi.tjgo.jus.br/BuscaProcessoPublica?PaginaAtual=4
- TJ-GO Acordo Aqui - https://acordoaqui.tjgo.jus.br/acordo-aqui/pesquisa

**Rio de Janeiro (RJ)**
- Justiça Militar - https://www.stm.jus.br/servicos-stm/certidao-negativa/emitir-certidao-negativa
- Justiça Federal - https://procweb.jfrj.jus.br/certidao/emissao_cert.asp
- Crimes Eleitorais - https://www.tse.jus.br/eleitor/certidoes/certidao-de-crimes-eleitorais

**São Paulo (SP)**
- Consulta de Processos WEB | Limeira - https://serv42.limeira.sp.gov.br/procweb/cnsProcesso/

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Busca de Informações via CPF/CNPJ/CRM/CNA 🔭 <a name="busca-cpf-cnpj-crm-cna"></a>
### Consulta Situação Cadastral CPF
Consulta pública da situação cadastral do CPF na Receita Federal.
- https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp 

### Busca Dados Usando CNPJ

<details>
<summary>Links de Consulta</summary>

- http://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp 
- https://brasilcnpj.net/ 
- https://cnpj.biz/ 
- https://cadastroempresa.com.br/ 
- https://casadosdados.com.br/ 
- https://www.informecadastral.com.br/ 
- https://www.situacaocadastral.info/ 
- http://www8.receita.fazenda.gov.br/simplesnacional/aplicacoes.aspx?id=21 
- https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/ 
- https://dados-abertos-rf-cnpj.casadosdados.com.br/arquivos/ 
- https://cnpja.com/ 
- https://cnpjgo.com.br/
- https://iefacil.com.br/ 

</details>

### Automação de força Bruta para encontrar CPF e Nome completo

Este repositório contém duas ferramentas úteis para a manipulação e consulta de CPFs. A primeira ferramenta gera uma lista de CPFs válidos com base em dígitos centrais fornecidos pelo usuário (dígitos que são retornados do pix por exemplo: `***123456**`), enquanto a segunda realiza consultas automáticas de situação cadastral desses CPFs, utilizando um bot automatizado via Selenium para interagir com um site de consulta.

- https://github.com/fernandobortotti/CPF-Tools

### Busca Nome Usando CPF/CNPJ

A intenção deste serviço é ajudar você descobrir e confirmar qual a situação cadastral do documento de CPF (Cadastro de Pessoa Física) e/ou CNPJ (Cadastro Nacional da Pessoa Jurídica).

- https://www.situacao-cadastral.com/

### Retornando Nome Completo CPF/CNPJ

Neste serviço é possível descobrir o nome completo utilizando CPF (Cadastro de Pessoa Física) e/ou CNPJ (Cadastro Nacional da Pessoa Jurídica). Bem como, consultar Certidão Eletrônica de Ações Trabalhistas - CEAT. Em escolha ao CPNJ poder ser que retorne o CPF como complemento ao nome.

- https://sistemas.trt3.jus.br/certidao/feitosTrabalhistas/aba1.emissao.htm

### Visualização de dados públicos de CNPJ

Ferramenta para observar o relacionamento entre empresas e sócios, a partir dos dados públicos disponibilizados pela Receita Federal. Pode ser executado localmente, baixando o código do Github ou executado online diretamente no site do projeto.

- https://www.redecnpj.com.br/rede/
- https://github.com/rictom/rede-cnpj/

### Consulta de Antecedente Criminal

Nesta consulta é gerado um documento válido até a data que será exibida ao final do processo. Apesar de ser do Estado do Paraná, é possível selecionar outros estados.

- https://antecedentes.policiacivil.pa.gov.br/consulta

### Antecedentes Criminais por Estado
Consultas de antecedentes criminais em Polícias Civis estaduais.

<details>
<summary>Consultas por Estado</summary>

**Acre (AC)**
- Antecedente criminal - https://pc.ac.gov.br/certidao-de-antecedentes-criminais/

**Pará (PA)**
- Consulta de Antecedente Criminal - https://antecedentes.pc.pa.gov.br/consulta

**Rio de Janeiro (RJ)**
- Antecedentes Criminais - http://atestadodic.detran.rj.gov.br/
- B.O - https://dedic.pcivil.rj.gov.br/Consulta.aspx

**Rio Grande do Sul (RS)**
- Emitir certidão de antecedentes criminais - https://www.pc.rs.gov.br/emitir-certidao-de-antecedentes-policiais

**Santa Catarina (SC)**
- Antecedentes Criminais - https://sistemas.pc.sc.gov.br/formulario-antecedentes-cidadao/#/

</details>

### Consulta Cadastro Nacional dos Advogados (CNA)

Pesquisar no Repositório do cadastro de todos os advogados do Brasil.
Mantido pelo Conselho Federal da OAB, que exerce a função de repositório do cadastro de todos os advogados do Brasil. Para realizar a consulta, basta preencher o formulário e pesquisar. (Nome; Nº da inscrição; Seccional; Tipo de inscrição)

- https://cna.oab.org.br

### Consulta Conselho Federal de Medicina (CFM)

Pesquisar no Repositório do cadastro de médicos do Brasil.
Mantido pelo Conselho Federal de Medicina, órgão que fiscaliza e normatiza a prática médica no Brasil. Para realizar a consulta, basta preencher o formulário e pesquisar.

- https://portal.cfm.org.br/busca-medicos/

### Consulta Conselho Federal de Psicologia (CFP)

Pesquisar no Repositório do cadastro de psicólogos do Brasil.
Mantido pelo Conselho Federal de Psicologia, órgão com a finalidade fiscalizar o exercício da profissão de Psicólogo no Brasil. Para realizar a consulta, basta preencher o formulário e pesquisar.

- https://cadastro.cfp.org.br

### Conselho de Arquitetura e Urbanismo (CAU)
Consulta de profissionais registrados no CAU.
- https://www.caubr.gov.br/

### Conselho Federal de Farmácia (CFF)
Consulta de profissionais de farmácia registrados.
- https://www.cff.org.br/

### COFFITO - Conselho Federal de Fisioterapia e Terapia Ocupacional
Consulta de fisioterapeutas e terapeutas ocupacionais.
- https://www.coffito.gov.br/

### Conselho Federal de Nutricionistas (CFN)
Consulta de nutricionistas registrados.
- https://www.cfn.org.br/

### Conselho Federal de Engenharia e Agronomia (Confea)

Pesquisar no Repositório do cadastro das profissões inseridas no Sistema Confea/Crea.
Mantido pelo Conselho Federal de Engenharia e Agronomia – Confea, instituído juntamente com os Conselhos Regionais de Engenharia e Agronomia pelo Decreto nº 23.569, de 11 de dezembro de 1933, é a instância superior da fiscalização do exercício das profissões inseridas no Sistema Confea/Crea.
Para realizar a consulta, basta preencher o formulário e pesquisar.

- https://consultaprofissional.confea.org.br

### Consulta MEI

Nesta consulta será exibido informações do cadastro MEI. Para consulta é necessário apenas o CPF e data de nacimento. Vale para todo território nacional.

- http://www22.receita.fazenda.gov.br/inscricaomei/private/pages/certificado_acesso.jsf

### Declaração do Simples Nacional

Para obter informações de declaração do simples nacional, basta informar o CNPJ nessa pesquisa. Vale para todo o território nacional

- http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/dasnsimei.app/Default.aspx
- https://www8.receita.fazenda.gov.br/SimplesNacional/controleAcesso/Autentica.aspx?id=16
- https://www8.receita.fazenda.gov.br/SimplesNacional/aplicacoes.aspx?id=21

### Consulta de Inscrição Estadual (SINTEGRA)
Consulta ao cadastro de contribuintes de ICMS (Inscrição Estadual) nos sistemas SINTEGRA estaduais. Permite verificar a situação cadastral de empresas junto às Secretarias de Fazenda dos estados.
<details>
<summary>Consultas por Estado</summary>

- Paraná (PR) - http://www.sintegra.fazenda.pr.gov.br/sintegra/
- Rio Grande do Sul (RS) - https://www.sefaz.rs.gov.br/consultas/contribuinte
- Santa Catarina (SC) - https://sat.sef.sc.gov.br/tax.NET/Sat.Cadastro.Web/ComprovanteIE/Consulta.aspx
- Rio de Janeiro (RJ) - https://sucief-sincad-web.fazenda.rj.gov.br/sincad-web/index.jsf
- São Paulo (SP) - https://www.cadesp.fazenda.sp.gov.br/(S(o4dmnsp1bcc2na341cmodgoq))/Pages/Cadastro/Consultas/ConsultaPublica/ConsultaPublica.aspx
- Distrito Federal (DF) - https://agnet.fazenda.df.gov.br/area.cfm?id_area=1140
- Goiás (GO) - https://appasp.sefaz.go.gov.br/Sintegra/Consulta/default.html
- Mato Grosso do Sul (MS) - https://servicos.efazenda.ms.gov.br/consultapublica
- Alagoas (AL) - https://sintegra.sefaz.al.gov.br/#/
- Bahia (BA) - https://portal.sefaz.ba.gov.br/scripts/cadastro/cadastroBa/consultaBa.asp
- Ceará (CE) - https://consultapublica.sefaz.ce.gov.br/sintegra/preparar-consultar
- Maranhão (MA) - https://sistemas1.sefaz.ma.gov.br/sintegra/jsp/consultaSintegra/consultaSintegraFiltro.jsf
- Paraíba (PB) - https://www4.sefaz.pb.gov.br/sintegra/SINf_ConsultaSintegra.jsp
- Rio Grande do Norte (RN) - https://uvt.sefaz.rn.gov.br/#/services/consultaContribuinte
- Sergipe (SE) - https://security.sefaz.se.gov.br/SIC/sintegra/index.jsp
- Acre (AC) - https://sefazonline.ac.gov.br/sefazonline/app.wmsintegralista
- Amazonas (AM) - https://online.sefaz.am.gov.br/sintegra/index.asp
- Pará (PA) - https://app.sefa.pa.gov.br/sintegra/
- Rondônia (RO) - https://portalcontribuinte.sefin.ro.gov.br/Publico/parametropublica.jsp
- Roraima (RR) - https://portalweb.sefaz.rr.gov.br/sintegra/servlet/wp_siate_consultasintegra
- Tocantins (TO) - https://sintegra.sefaz.to.gov.br/sintegra/servlet/wpsico01

</details>


### Consulta de Inutilização / CNPJ
Consulta de inutilização de numeração de documentos fiscais eletrônicos e verificação de CNPJ no sistema de CT-e.
- https://www.cte.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=inutilizacao&tipoConteudo=MZ1N+CQHCgA=

### Consulta Comunicação de Decisão do Requerimento/Benefício

Consulta o status de requisição de aposentádoria de INSS. Vale para todo o território nacional.

- https://www2.dataprev.gov.br/sabiweb/relatorio/imprimirCRER.view?acao=imprimir_CRER

### Consulta Restituição do Imposto de Renda

Nesta consulta serão exibidas informações (banco, agência e data de restituição) da Restituição do Imposto de Renda. Para consulta é necessário apenas o CPF e data de nascimento.

### Portal e-CAC Receita Federal
Centro de Atendimento Virtual (e-CAC) da Receita Federal permite acesso a serviços digitais.
- https://cav.receita.fazenda.gov.br/

### CEIS - Cadastro de Empresas Inidôneas e Suspensas
Consulta de empresas impedidas de participar de licitações e celebrar contratos com a Administração Pública.
- http://www.portaltransparencia.gov.br/sancoes/ceis

### CNEP - Cadastro Nacional de Empresas Punidas
Consulta de empresas punidas com base na Lei Anticorrupção.
- http://www.portaltransparencia.gov.br/sancoes/cnep

### CEPIM - Cadastro de Entidades Privadas Sem Fins Lucrativos Impedidas
Consulta de entidades privadas sem fins lucrativos impedidas de celebrar convênios com a Administração Pública Federal.
- http://www.portaltransparencia.gov.br/sancoes/cepim

### InfoConv - Sistema de Gestão de Convênios e Contratos de Repasse
Consulta de convênios e contratos de repasse firmados com órgãos e entidades da Administração Pública Federal.
- https://www.convenios.gov.br/

### Consulta Junta Comercial do Estado de São Paulo (Jucesp)

Pesquisa no banco de dados da Junta Comercial do Estado de São Paulo.
Para consulta é necessário apenas o Nome da empresa, CNPJ, Razão social ou NIRE.
<details>
<summary>Consultas JUCESP</summary>

- Pesquisa Geral - https://www.jucesponline.sp.gov.br/pesquisa.aspx
- Validação de Ficha - https://www.jucesponline.sp.gov.br/Valida_Ficha.aspx
- Consulta Produto 7 - https://www.jucesponline.sp.gov.br/pesquisa.aspx?IDProduto=7
- Consulta Produto 4 - https://www.jucesponline.sp.gov.br/Pesquisa.aspx?IDProduto=4
- Pré-visualização por NIRE - https://www.jucesponline.sp.gov.br/Pre_Visualiza.aspx?nire={VALOR}&idproduto=

</details>

### Simples Nacional - Consulta de Optantes
Verificação se empresa é optante do regime Simples Nacional, incluindo histórico de opção.
- https://www8.receita.fazenda.gov.br/SimplesNacional/

### REDESIM - Rede Nacional para Simplificação
Plataforma para consulta de viabilidade e registro de empresas em todo Brasil.
- https://www.redesim.gov.br/

### Cadastro de Beneficiários Efetivos (CadBE)
Consulta pública de beneficiários finais de pessoas jurídicas (transparência corporativa).
- https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/cadastro-de-beneficiarios-efetivos-cadbe

### CNPJ.rocks - Consulta Rápida
Interface moderna e rápida para consulta de dados de CNPJ.
- https://cnpjs.rocks/

### Nire.im - Busca de Empresas
Busca simplificada de informações empresariais por CNPJ ou razão social.
- https://nire.im/

### Consulta Etrevistador do IBGE

Pesquisa informações sobre entrevistador do IBGE. Para consulta é necessário: número matrícula, CPF ou RG.

- https://respondendo.ibge.gov.br/verifique-a-identidade-do-entrevistador.html
- https://www.ibge.gov.br/acesso-informacao/institucional/documentos-ibge/1861-novo-portal/institucional/17422-servidores.html

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Estatísticas Segurança Pública <a name="estatísticas"></a> 🔐

Fontes oficiais de estatísticas criminais (OSINT)
Painéis governamentais, dados abertos e relatórios públicos por UF.

### Painéis Nacionais


Ministério da Justiça e Segurança Pública (MJSP)

- SINESP – Estatísticas de Segurança Pública (VDE)
  - https://www.gov.br/mj/pt-br/assuntos/sua-seguranca/seguranca-publica/estatistica

- Dados abertos – Segurança Pública (Gov.br)
  - https://dados.gov.br/dados/conjuntos-dados/seguranca-publica


### Painéis Estaduais

<details> 
<summary>Secretarias de Segurança Pública</summary>

- Estatísticas da Grande São Luís
 - https://www.ssp.ma.gov.br/estatisticas-da-grande-sao-luis/

- Portal institucional da SSP-MA
 - https://www.ssp.ma.gov.br/

- Painel Estatístico SSP-SP
  - https://www.ssp.sp.gov.br/estatistica/painel-estatistico

- Dados mensais por tipo de crime (SSP-SP)
  - https://www.ssp.sp.gov.br/estatistica

- ISP Dados – Painel interativo
 - https://www.ispdados.rj.gov.br/

- Séries históricas e dados abertos
 - https://www.isp.rj.gov.br/

- Dados abertos de segurança pública (MG)
 - https://www.seguranca.mg.gov.br/index.php/transparencia/dados-abertos

- Portal institucional
 - https://www.seguranca.mg.gov.br/

- Estatísticas criminais oficiais
 - https://www.ba.gov.br/ssp/estatistica

- Portal da SSP-BA
 - https://www.ssp.ba.gov.br/

- Indicadores criminais do Ceará
 - https://www.sspds.ce.gov.br/estatisticas/

- Portal institucional
 - https://www.sspds.ce.gov.br/

- Estatísticas criminais
 - https://www.ssp.rs.gov.br/estatisticas

- Portal institucional
 - https://www.ssp.rs.gov.br/

- Estatísticas de criminalidade (PR)
 - https://www.seguranca.pr.gov.br/Estatisticas

- Portal institucional
 - https://www.seguranca.pr.gov.br/

- Estatísticas criminais – SDS PE
 - https://www.sds.pe.gov.br/estatisticas

- Portal institucional
 - https://www.sds.pe.gov.br/

</details>

### Fórum Brasileiro de Segurança Pública (FBSP)
Anuário Brasileiro de Segurança Pública com dados consolidados sobre violência, criminalidade e sistema de justiça criminal.
- https://forumseguranca.org.br/
- https://forumseguranca.org.br/anuario-brasileiro-seguranca-publica/

### Monitor da Violência - G1/NEV-USP/FBSP
Painel colaborativo com dados consolidados de homicídios no Brasil.
- https://g1.globo.com/monitor-da-violencia/

### Instituto Sou da Paz
Dados, análises e pesquisas sobre violência urbana e políticas públicas de segurança.
- https://www.soudapaz.org/

### Onde Fui Roubado
Mapa colaborativo de ocorrências policiais reportadas por usuários em diversas cidades brasileiras.
- https://www.ondefuiroubado.com.br/

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Registros Eleitorais e Políticos 🗳️ <a name="registros-eleitorais-politicos"></a>

### TSE - Divulgação de Candidaturas e Contas Eleitorais
Sistema de divulgação de candidaturas, contas eleitorais e de prestação de contas.
- https://divulgacandcontas.tse.jus.br/divulga/

### TSE - Consulta de Contas Eleitorais
Consulta de prestação de contas de campanhas eleitorais.
- https://www.tse.jus.br/eleicoes/contas-eleitorais

### Consulta de Filiação Partidária
Consulta pública de filiação partidária de eleitores.
- https://filiaweb.tse.jus.br/filiaweb/

### Câmara dos Deputados - Votações
Consulta de votações realizadas na Câmara dos Deputados.
- https://www.camara.leg.br/busca-portal/proposicoes/votacoes

### Senado Federal - Votações
Consulta de votações realizadas no Senado Federal.
- https://www25.senado.leg.br/web/atividade/votacoes

### TSE - Portal de Dados Abertos
Dados abertos sobre eleições, votação, eleitorado, partidos, candidatos, prestação de contas, pesquisas eleitorais e urnas eletrônicas.
- https://dadosabertos.tse.jus.br/

### Repositório de Dados Eleitorais - TSE
Base completa de dados eleitorais desde 1945, incluindo resultados, candidaturas e perfil do eleitorado.
- https://dadosabertos.tse.jus.br/dataset/

### DivulgaCand - API do TSE
Acesso programático aos dados de candidaturas e prestação de contas eleitorais.
- https://divulgacandcontas.tse.jus.br/divulga/rest/v1/docs/

### Meu TSE
Portal com dados personalizados do eleitor, incluindo local de votação e histórico eleitoral.
- https://www.tse.jus.br/eleitor/titulo-e-local-de-votacao/consulta-por-nome

### Certidão de Quitação Eleitoral
Emissão de certidão que comprova a regularidade da situação eleitoral do cidadão.
- https://www.tse.jus.br/eleitor/certidoes/certidao-de-quitacao-eleitoral

### Base dos Dados - Eleições
Dados eleitorais tratados, padronizados e prontos para análise estatística.
- https://basedosdados.org/dataset/br-tse-eleicoes

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Registros de Imóveis e Propriedades 🏠 <a name="registros-imoveis-propriedades"></a>

### SREI - Sistema de Registro Eletrônico de Imóveis
Sistema que integra informações de registros de imóveis.
- https://www.registradores.org.br/

### Consulta IPTU São Paulo
Consulta de IPTU da cidade de São Paulo.
- https://www.prefeitura.sp.gov.br/cidade/secretarias/fazenda/servicos/iptu/

### Consulta IPTU Rio de Janeiro
Consulta de IPTU da cidade do Rio de Janeiro.
- https://carioca.rio/servicos/consulta-iptu/

### SPU - Secretaria do Patrimônio da União
Consulta de imóveis da União.
- https://www.gov.br/economia/pt-br/assuntos/patrimonio-da-uniao

### INCRA - Sistema Nacional de Cadastro Rural
Consulta e certificação de imóveis rurais.
- https://sncr.serpro.gov.br/sncr-web/

### Cartórios de Registro de Imóveis
Diretório de cartórios de registro de imóveis no Brasil.
- https://www.registrodeimoveis.org.br/cartorios

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Registros Ambientais 🌳 <a name="registros-ambientais"></a>

### IBAMA - Consulta de Autuações Ambientais
Consulta pública de áreas embargadas e autuações ambientais.
- https://servicos.ibama.gov.br/ctf/publico/areasembargadas/ConsultaPublicaAreasEmbargadas.php

### CTF/APP - Cadastro Técnico Federal de Atividades Potencialmente Poluidoras
Cadastro obrigatório de pessoas físicas e jurídicas que realizam atividades potencialmente poluidoras.
- https://servicos.ibama.gov.br/ctf/

### SINAFLOR - Sistema Nacional de Controle da Origem dos Produtos Florestais
Sistema de controle do transporte e armazenamento de produtos e subprodutos florestais.
- https://sinaflor2.ibama.gov.br/

### CETESB - Licenciamento Ambiental São Paulo
Consulta de licenças ambientais do Estado de São Paulo.
- https://cetesb.sp.gov.br/licenciamentoambiental/

### MapBiomas - Plataforma de Consulta
Plataforma interativa para consulta de dados de cobertura e uso do solo no Brasil com visualização de mapas e análises temporais.
- https://plataforma.brasil.mapbiomas.org/

### MapBiomas - Estatísticas
Estatísticas detalhadas sobre mudanças no uso da terra e cobertura vegetal no Brasil.
- https://brasil.mapbiomas.org/estatisticas/

### MapBiomas - Cobertura 10m
Mapas de alta resolução (10 metros) de cobertura e uso da terra.
- https://brasil.mapbiomas.org/mapbiomas-cobertura-10m/

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Comércio Exterior 📦 <a name="comercio-exterior"></a>

### Comexstat - Estatísticas de Comércio Exterior
Estatísticas de comércio exterior brasileiro.
- http://comexstat.mdic.gov.br/pt/home

### Siscomex - Sistema Integrado de Comércio Exterior
Consulta pública do Sistema Integrado de Comércio Exterior.
- https://portalunico.siscomex.gov.br/

### AliceWeb - Análise das Informações de Comércio Exterior
Sistema de análise das informações de comércio exterior brasileiro.
- http://aliceweb.desenvolvimento.gov.br/

### Radar Siscomex
Consulta de habilitação de empresas no Siscomex.
- https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/radar

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Registros de Marcas e Patentes ™️ <a name="registros-marcas-patentes"></a>

### INPI - Busca de Marcas
Consulta de marcas registradas no Brasil.
- https://busca.inpi.gov.br/pePI/jsp/marcas/Pesquisa_classe_basica.jsp

### INPI - Busca de Patentes
Consulta de patentes registradas no Brasil.
- https://busca.inpi.gov.br/pePI/jsp/patentes/PatenteSearchBasico.jsp

### INPI - Desenhos Industriais
Consulta de desenhos industriais registrados.
- https://busca.inpi.gov.br/pePI/jsp/desenhos/DesenhoSearchBasico.jsp

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Transparência Pública e Defesa do Consumidor 🧾 <a name="transparencia-defesa-consumidor"></a>

### Portal da Transparência - Governo Federal
Consultas a favorecidos, convênios, servidores, CEIS/CNEP, despesas, viagens oficiais e outros dados financeiros da União.
- https://portaldatransparencia.gov.br/

### Portal da Transparência - Consulta de Sanções
Consulta pública de sanções aplicadas a pessoas físicas e jurídicas.
- https://portaldatransparencia.gov.br/sancoes/consulta?cadastro=1&ordenarPor=nomeSancionado&direcao=asc

### Portal da Transparência - API de Dados
Interface REST oficial permitindo consultas automatizadas a despesas, convênios, favorecidos e dados de pessoal.
- https://portaldatransparencia.gov.br/api-de-dados

### Dados.gov.br - Portal Brasileiro de Dados Abertos
Catálogo central de dados abertos do governo federal com mais de 10 mil conjuntos de dados.
- https://dados.gov.br/

### Painel de Compras Governamentais
Centralização de informações sobre licitações, contratos e compras do governo federal.
- https://paineldecompras.economia.gov.br/

### ComprasNet - Portal de Compras do Governo Federal
Sistema oficial de compras e licitações públicas do governo federal.
- https://www.gov.br/compras/pt-br

### PNCP - Portal Nacional de Contratações Públicas
Plataforma unificada de licitações conforme nova Lei de Licitações (Lei 14.133/2021).
- https://www.gov.br/pncp/

### TCU - Tribunal de Contas da União
Fiscalização de gastos públicos federais, relatórios de auditoria e decisões.
- https://portal.tcu.gov.br/

### TCU - Consulta de Acórdãos
Busca de decisões do TCU sobre prestação de contas e irregularidades.
- https://pesquisa.apps.tcu.gov.br/

**📖 Documentação da API:**
<details>
<summary>Exemplos de Uso da API</summary>

**Endpoints Principais:**
- `/api-de-dados/despesas/` - Consulta de despesas públicas
- `/api-de-dados/servidores/` - Dados de servidores públicos
- `/api-de-dados/convenios/` - Convênios federais
- `/api-de-dados/favorecidos/` - Pessoas/empresas favorecidas

**Exemplo de Requisição (Python):**
```python
import requests

url = "https://api.portaldatransparencia.gov.br/api-de-dados/despesas"
headers = {"chave-api-dados": "SUA_CHAVE_AQUI"}
params = {
    "mesAno": "01/2024",
    "orgaoSuperior": "20000"
}
response = requests.get(url, headers=headers, params=params)
print(response.json())
```

**Como obter chave API:**
1. Acesse https://portaldatransparencia.gov.br/api-de-dados
2. Clique em "Solicitar Chave"
3. Preencha o formulário com seus dados
4. Aguarde aprovação por e-mail

**Limitações:**
- Máximo de 60 requisições por minuto
- Período máximo de consulta: 12 meses
- Formato de resposta: JSON

</details>

### CGU - Controladoria-Geral da União
Órgão responsável pela defesa do patrimônio público, combate à corrupção, transparência e controle interno do Governo Federal.
- https://www.gov.br/cgu/pt-br

### CGU - Notícias e Informações
Portal de notícias da CGU com informações sobre ações de controle, transparência e combate à corrupção.
- https://www.gov.br/cgu/pt-br/assuntos/noticias

### Portal de Acesso à Informação - Governo Federal
Portal oficial para solicitações de acesso à informação baseado na Lei de Acesso à Informação (LAI).
- https://www.gov.br/acessoainformacao/pt-br

### Fala.BR - Plataforma Integrada de Ouvidoria e Acesso à Informação
Sistema oficial para LAI (Lei de Acesso à Informação), denúncias, reclamações, sugestões e elogios aos órgãos públicos federais.
- https://falabr.cgu.gov.br/web/home

### Consumidor.gov.br
Plataforma pública para registro de reclamações contra empresas, acompanhamento de respostas e avaliação do atendimento.
- https://www.consumidor.gov.br/

### Senacon - Secretaria Nacional do Consumidor
Portal oficial da Secretaria Nacional do Consumidor com informações sobre direitos do consumidor, recalls e regulamentações.
- https://www.gov.br/mj/pt-br/assuntos/seus-direitos/consumidor

### INMETRO - Produtos Certificados
Consulta de produtos certificados pelo Instituto Nacional de Metrologia, Qualidade e Tecnologia.
- http://www.inmetro.gov.br/prodcert/produtos/busca.asp

### Dados Abertos - Consumidor.gov.br
Dataset oficial com histórico de reclamações registradas no Consumidor.gov.br (Ministério da Justiça).
- https://dados.mj.gov.br/dataset/reclamacoes-do-consumidor-gov-br

### PROCON-SP - Espaço do Consumidor
Portal do PROCON-SP com orientações, consultas e canais de reclamação.
- https://www.procon.sp.gov.br/espaco-consumidor/

### Portal da Transparência - Estado de São Paulo
Portal estadual de transparência com dados de remuneração, contratos, convênios e despesas do governo paulista.
- https://www.transparencia.sp.gov.br/

### E-Agendas CGU
Consulta de agendas públicas de autoridades do Governo Federal.
- https://eagendas.cgu.gov.br/

### Tribunais de Contas Estaduais
Portais dos Tribunais de Contas responsáveis pela fiscalização das contas públicas estaduais e municipais.

<details>
<summary>Portais por Estado</summary>

**Acre (AC)**
- Informações disponíveis em processo de atualização

**Amapá (AP)**
- Portal: https://www.tce.ap.gov.br/

**Alagoas (AL)**
- Portal em manutenção

**Bahia (BA)**
- Portal: https://www.tce.ba.gov.br/

**Ceará (CE)**
- Portal: https://www.tce.ce.gov.br/

**Minas Gerais (MG)**
- Portal: https://www.tce.mg.gov.br/

**Mato Grosso do Sul (MS)**
- Portal: https://www.tce.ms.gov.br/

**Mato Grosso (MT)**
- Portal: https://www.tce.mt.gov.br/

**Paraíba (PB)**
- Portal: https://tce.pb.gov.br/

**Paraná (PR)**
- Portal: https://www1.tce.pr.gov.br/

**Rio Grande do Norte (RN)**
- Portal: http://www.tce.rn.gov.br/

**São Paulo (SP)**
- Portal: https://www.tce.sp.gov.br/

</details>

### Portal da Transparência - Consulta de Notas Fiscais
Consulta detalhada de notas fiscais emitidas para órgãos públicos federais, com filtros por UF, fornecedor, período e órgão.
- https://portaldatransparencia.gov.br/notas-fiscais/consulta

### Nota Fiscal Eletrônica e Transparência por Estado
Consultas de Notas Fiscais Eletrônicas e Portais de Transparência estaduais e municipais.

<details>
<summary>Consultas por Estado</summary>

**Acre (AC)**
- Nota Fiscal - http://sefaznet.ac.gov.br/nfe/consulta.xhtml

**Alagoas (AL)**
- Nota Fiscal Eletrônica - https://nfce.sefaz.al.gov.br/consultaNFCe.aspx
- Portal da Transparência AL - https://transparencia.al.gov.br/

**Amazonas (AM)**
- Nota Fiscal Eletrônica - https://sistemas.sefaz.am.gov.br/nfce/qrcode
- Portal da Transparência AM - https://www.transparencia.am.gov.br/

**Bahia (BA)**
- Nota Fiscal Eletrônica - http://nfe.sefaz.ba.gov.br/
- Portal da Transparência BA - http://www.transparencia.ba.gov.br/

**Ceará (CE)**
- Nota Fiscal Eletrônica - https://nfce.sefaz.ce.gov.br/pages/consultarNFCe.jsf
- Portal da Transparência CE - https://cearatransparente.ce.gov.br/

**Distrito Federal (DF)**
- Nota Fiscal Eletrônica - https://dec.fazenda.df.gov.br/ConsultarNFe.aspx
- Portal da Transparência DF - https://www.transparencia.df.gov.br/

**Goiás (GO)**
- Consulta Nota Fiscal - https://www.goiania.go.gov.br/sing_servicos/nota-fiscal-eletronica/
- Consulta DUAM-IPTU-ITU-ISSQN - https://www.goiania.go.gov.br/sing_servicos/emissao-duam-itu-iptu-issqn/
- Consulta matrículas - https://www.goiania.go.gov.br/sing_servicos/matriculas-web/
- Consulta processos - https://www.goiania.go.gov.br/sing_servicos/consulta-processos/

**Minas Gerais (MG)**
- Consulta de Certidão Negativa de Débito | Belo Horizonte - http://cndonline.siatu.pbh.gov.br/CNDOnline/?null

**Piauí (PI)**
- Sefaz Piauí - https://webas.sefaz.pi.gov.br/
- Inadimplentes - https://webas.sefaz.pi.gov.br/caginweb/
- Certidões - https://webas.sefaz.pi.gov.br/certidaonft-web/index.xhtml
- MEI - https://webas.sefaz.pi.gov.br/MEI-WEB/
- Impedidos de contratar com o poder público - https://sistemas.tce.pi.gov.br/ImpedimentoAS/impedimentos/listapessoas.xhtml

**Rondônia (RO) - Porto Velho**
- Certidão Negativa de Débitos de Tributos Fiscais - https://semfazonline.portovelho.ro.gov.br/portal/certidao_negativa.action
- Consulta de Débitos Imobiliários - IPTU - https://semfazonline.portovelho.ro.gov.br/portal/iptu_consulta_debito_input.action
- Consulta Empresas Cadastradas - https://semfazonline.portovelho.ro.gov.br/portal/consulta_empresa_input.action

**São Paulo (SP)**
- Consulta de nome e salários de servidores do Estado - https://www.transparencia.sp.gov.br/home/servidor

**Maranhão (MA) - São Luís**
- Portal da Transparência Prefeitura | São Luís - https://transparencia.saoluis.ma.gov.br/
- Diário Eletrônico Prefeitura | São Luís - https://diariooficial.saoluis.ma.gov.br/

**Maranhão (MA) - São José de Ribamar**
- Portal da Transparência Prefeitura | São José de Ribamar - https://transparencia.saojosederibamar.ma.gov.br/
- Diário Eletrônico Prefeitura | São José de Ribamar - https://www.saojosederibamar.ma.gov.br/detalhe-da-materia/info/diario-eletronico/148327

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Diários Oficiais 📰 <a name="diarios-oficiais"></a>

### Diário Oficial da União (DOU)
Publicações oficiais do Governo Federal.
- https://www.in.gov.br/

### Imprensa Nacional - Consulta de Matérias
Busca avançada de matérias publicadas no Diário Oficial da União com filtros por período, seção, órgão e palavras-chave.
- https://www.in.gov.br/materia

### Querido Diário
Projeto da Open Knowledge Brasil que reúne e disponibiliza em formato aberto os diários oficiais de centenas de prefeituras brasileiras.
- https://queridodiario.ok.org.br/

### Diários Oficiais Estaduais

<details>
<summary>Região Norte</summary>

- Acre (AC) - https://diario.ac.gov.br/
- Amazonas (AM) - https://doe.am.gov.br/
- Amapá (AP) - https://www.diariooficial.ap.gov.br/
- Pará (PA) - https://www.ioepa.com.br/
- Rondônia (RO) - https://diariooficial.ro.gov.br/
- Roraima (RR) - https://imprensaoficial.rr.gov.br/
- Tocantins (TO) - https://diariooficial.to.gov.br/

</details>

<details>
<summary>Região Nordeste</summary>

- Alagoas (AL) - https://www.imprensaoficialal.com.br/
- Bahia (BA) - https://dool.egba.ba.gov.br/
- Ceará (CE) - https://www.diariooficial.ce.gov.br/
- Maranhão (MA) - https://diariooficial.ma.gov.br/
- Paraíba (PB) - https://auniao.pb.gov.br/servicos/diario-oficial
- Pernambuco (PE) - https://www.cepe.com.br/diario-oficial
- Piauí (PI) - https://www.diariooficial.pi.gov.br/
- Rio Grande do Norte (RN) - https://www.diariooficial.rn.gov.br/
- Sergipe (SE) - https://doe.se.gov.br/

</details>

<details>
<summary>Região Centro-Oeste</summary>

- Distrito Federal (DF) - https://dodf.df.gov.br/
- Goiás (GO) - https://diariooficial.go.gov.br/
- Mato Grosso (MT) - https://www.iomat.mt.gov.br/
- Mato Grosso do Sul (MS) - https://www.imprensaoficial.ms.gov.br/

</details>

<details>
<summary>Região Sudeste</summary>

- Espírito Santo (ES) - https://ioes.dio.es.gov.br/
- Minas Gerais (MG) - https://www.jornalminasgerais.mg.gov.br/
- Rio de Janeiro (RJ) - https://portal.ioerj.com.br/diario-oficial/
- São Paulo (SP) - https://doe.sp.gov.br/

</details>

<details>
<summary>Região Sul</summary>

- Paraná (PR) - https://www.documentos.dioe.pr.gov.br/
- Rio Grande do Sul (RS) - https://diariooficial.rs.gov.br/
- Santa Catarina (SC) - https://doe.sc.gov.br/

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Cultura e Audiovisual 🎬 <a name="cultura-audiovisual"></a>

### ANCINE - Consulta de Processos SEI
Sistema de consulta pública de processos administrativos da ANCINE.
- https://sei.ancine.gov.br/sei/modulos/pesquisa/md_pesq_processo_pesquisar.php?acao_externa=protocolo_pesquisar&acao_origem_externa=protocolo_pesquisar&id_orgao_acesso_externo=0

### ANCINE - Consulta de Unidades de Exibição
Consulta pública de salas de cinema e espaços de exibição cadastrados.
- https://sad.ancine.gov.br/consultapublica/telaPrincipalUE.do?method=initListar

### ANCINE - Consulta de Projetos Audiovisuais
Consulta de projetos audiovisuais registrados na ANCINE.
- https://sad.ancine.gov.br/projetosaudiovisuais/ConsultaProjetosAudiovisuais.do?method=init

### ANCINE - Consulta de Empresas Cadastradas
Consulta de agentes econômicos (empresas) do setor audiovisual cadastrados.
- https://sad2.ancine.gov.br/agenteeconomico/consultaViaPortal/consultaExternaEmpresasCadastradas.seam

### ANCINE - Consulta de Agentes Econômicos
Consulta detalhada de agentes econômicos do setor audiovisual por tipo.
- https://sad2.ancine.gov.br/agenteeconomico/consultaViaPortal/consultaExternaAE.seam

### ANCINE - Consulta de Obras Publicitárias
Consulta de obras publicitárias registradas na ANCINE.
- https://sad2.ancine.gov.br/obraspublicitarias/consultaGeralViaPortal/consultaGeralViaPortal.seam

### ANCINE - Certificado de Registro de Título (CRT)
Consulta de CRT de obras audiovisuais.
- https://sad2.ancine.gov.br/obrasnaopublicitarias/consultarCrtViaPortal/consultarCrtViaPortal.seam

### ANCINE - Certificado de Produto Brasileiro (CPB)
Consulta de CPB de obras audiovisuais brasileiras.
- https://sad2.ancine.gov.br/obrasnaopublicitarias/pesquisarCpbViaPortal/pesquisarCpbViaPortal.seam

### ANCINE - Registro de Obra Estrangeira (ROE)
Consulta de obras estrangeiras registradas no Brasil.
- https://sad2.ancine.gov.br/obrasnaopublicitarias/consultarRoeViaPortal/consultarRoeViaPortal.seam

### ANCINE - Consulta de Obras
Consulta geral de obras audiovisuais cadastradas.
- https://sad2.ancine.gov.br/obrasnaopublicitarias/consultarObraViaPortal/consultarObraViaPortal.seam

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---
## Telecom 📡 <a name="telecom"></a>

### Busca Através do IMEI/Legalidade do Aparelho

O serviço prestado por este site informa somente a situação do aparelho celular que foi informado pelo usuário à operadora de telefonia móvel como roubado, furtado, perdido ou extraviado.

<details>
<summary>Links para pesquisa</summary>

- https://www.consultaaparelhoimpedido.com.br/public-web/welcome
- https://www.consultaserialaparelho.com.br/public-web/homeSiga
- https://www.imei.info/pt/

</details>

### Busca de Situação Cadastro / Portabilidade de Números Celulares e Fixos

- https://consultanumero.abrtelecom.com.br/consultanumero/consulta/consultaSituacaoAtualCtg
- https://consultanumero.abrtelecom.com.br/consultanumero/consulta/consultaHistoricoRecenteCtg

### Busca Operadora por Número Celular

<details>
<summary>Links para pesquisa</summary>

- https://consultanumero.info/
- https://www.qualoperadora.net/
- http://consultaoperadora.com.br/site2015/
- https://www.qualoperadora.org/

</details>

### Busca Operadora / Linha Pré ativa por CPF

Consultar se possui linha pré-paga ativa nas Prestadoras participantes (Algar, Claro, Oi, Sercomtel, TIM e Vivo).

- https://cadastropre.com.br/#/consulta

### Mapas de Cobertura das Operadoras

Consulte a cobertura de rede 2G, 3G, 4G e 5G em qualquer região do Brasil, verificando a disponibilidade e intensidade do sinal das operadoras

<details>
<summary>Links para pesquisa</summary>

- (Visão geral) - https://conexis.org.br/numeros/mapa-de-antenas-completo/
- https://mapadecobertura.vivo.com.br/
- https://www.claro.com.br/mapa-de-cobertura
- https://www.tim.com.br/para-voce/cobertura-e-roaming/mapa-de-cobertura
- https://www.oi.com.br/portal-oi-cobertura/
- https://www2.sercomtel.com.br/mapa-cobertura
- https://algartelecom.com.br/para-voce/celular/cobertura-celular
- https://www.brisanet.com.br/mapa-de-area-de-cobertura
- https://www.gigamaisfibra.com.br/onde-estamos/
</details>

### ANATEL - Consulta de Outorgas de Radiodifusão
Consulta de outorgas de serviços de radiodifusão.
- https://sistemas.anatel.gov.br/easp/Novo/ConsultaIndicativo/Tela.asp

### ANATEL - Radiodifusão
Informações e regulamentação sobre serviços de radiodifusão no Brasil.
- https://www.gov.br/anatel/pt-br/regulado/radiodifusao

### ANATEL - Sistema de Serviços de Telecomunicações (STEL)
Sistema para consulta de frequências, entidades e serviços de telecomunicações autorizados.
- https://sistemas.anatel.gov.br/stel/

### ANATEL - Infraestrutura de Telecomunicações
Painéis de dados sobre infraestrutura de telecomunicações no Brasil.
- https://www.anatel.gov.br/paineis/infraestrutura

### ANATEL - Consulta de Provedores Regionais
Consulta de prestadoras de serviços de telecomunicações por localidade.
- https://informacoes.anatel.gov.br/paineis/infraestrutura/consulta-de-provedores-regionais

### Teleco - Inteligência em Telecomunicações
Portal com informações, estatísticas, análises e consultas sobre o setor de telecomunicações brasileiro.
- https://teleco.com.br
- https://sistemas.anatel.gov.br/sis/cadastrosimplificado/ConsultaPrestadoraLocalidade/tela.asp

### ANATEL - Consulta de Radiofrequências por Sistema
Consulta de sistemas de radiofrequência autorizados pela ANATEL.
- https://sistemas.anatel.gov.br/srd/TelaListagem.asp?PagSRD=DescSistema&NumServico=231&op=5&SISQSmodulo=9830

### ANATEL - Sistema de Radiocomunicação Digital
Portal de consulta de serviços de radiocomunicação digital.
- https://sistemas.anatel.gov.br/srd/Default.asp?SISQSmodulo=208&SISQSsistema=16

### Base De Orelhão X Mapa

Por meio da busca é possível encontrar orelhões pelo número, localizar ruas, municípios, estados ou cidades

- http://sistemas.anatel.gov.br/sgmu/fiqueligado/tups.asp

### Painéis de Telecomunicações (ANATEL)

### Painel Geral — Indicadores de Telecomunicações

Dados gerais de telecomunicações no Brasil, com acesso a todos os painéis setoriais da Anatel, incluindo infraestrutura, acessos, cobertura, espectro, outorgas e conectividade.

- https://informacoes.anatel.gov.br/paineis/

### Meu Município — Panorama Municipal de Telecom

Panorama completo das telecomunicações de um município específico, com possibilidade de comparação com outros municípios da mesma UF, da região e com o Brasil.

- https://informacoes.anatel.gov.br/paineis/meu-municipio

### Índice Brasileiro de Conectividade (IBC)

Ranking e indicadores de conectividade de municípios e estados, considerando acesso à internet, cobertura móvel, banda larga fixa e outros fatores de conectividade.

- https://informacoes.anatel.gov.br/paineis/meu-municipio/indice-brasileiro-de-conectividade

### Infraestrutura e Cobertura de Redes Móveis

O que contém:
Cobertura de telefonia móvel (3G, 4G e 5G), mapas de infraestrutura, presença de sinal por município, UF e rodovias.

- https://informacoes.anatel.gov.br/paineis/infraestrutura/panorama

### Cobertura Móvel em Rodovias

O que contém:
Informações sobre presença de sinal móvel ao longo das rodovias federais e estaduais, integradas ao painel de infraestrutura.

- https://informacoes.anatel.gov.br/paineis/infraestrutura/panorama

### Acessos aos Serviços de Telecomunicações

O que contém:
Dados de acessos à banda larga fixa, telefonia móvel, telefonia fixa e TV por assinatura, com rankings e evolução histórica.

- https://informacoes.anatel.gov.br/paineis/acessos

### Outorga e Licenciamento — Serviço Móvel Pessoal (SMP)

O que contém:
Autorizações de operadoras, licenciamento de estações rádio base, tecnologias autorizadas e faixas de radiofrequência por município.

- https://informacoes.anatel.gov.br/paineis/outorga-e-licenciamento/autorizacoes-e-licenciamentos-do-smp

### Espectro e Órbita / Lei das Antenas

O que contém:
Informações sobre uso do espectro de radiofrequência, implantação do 5G e adequação dos municípios à Lei Geral de Antenas.

- https://informacoes.anatel.gov.br/paineis/espectro-e-orbita/lei-das-antenas

### Certificação de Produtos — Celulares 5G

O que contém:
Lista de aparelhos celulares certificados pela Anatel para operação em redes 5G no Brasil.

- https://informacoes.anatel.gov.br/paineis/certificacao-de-produtos/celulares-em-5g

### Áreas Tarifárias e Numeração

O que contém:
Divisão das áreas tarifárias da telefonia fixa, códigos DDD e áreas locais por município e UF.

- https://informacoes.anatel.gov.br/paineis/areas-tarifarias

### Consultar e identificar Frequências de Rádios / SISTEMA DE SERVIÇOS DE TELECOMUNICAÇÕES (STEL)

Abrirá uma página para preenchimento, preencha da seguinte forma:

1.  Em recuperação de dados: marque UF;
2.  Em apresentar dados por: marque a letra J (frequência e entidade) em faixa de frequência: coloque a frequência que deseja scanear, ex.: inicial: 450,000 final: 460,000 (NÃO ESQUEÇA DA VÍRGULA) OBS: não de um espaço de frequencia muito largo,as vezes dá erro na pesquisa;
3.  Em unidade coloque MHZ nos dois;
4.  Em sigla da UF: coloque a sigla do seu estado
5.  m serviço inicial e serviço final nao coloque nada, deixe do jeito que está em grupo de estações: marque todos (consolidado);
6.  Agora clique abaixo em exportar excel e salve o arquivo em seu micro;

- https://sistemas.anatel.gov.br/stel/Consultas/RecuperacaoFrequencias/tela.asp?SISQSmodulo=9896

### Consultar responsável por um indicativo

Digite o Indicativo da Estação sem pontos e sem traços.

- https://sistemas.anatel.gov.br/easp/Novo/ConsultaIndicativo/Tela.asp

### Mais informações sobre Radio amador

Alguns dos sistemas dependem de cadastro de usuário (CPF + Senha). Abaixo dos links da ANATEL, links por tipo de serviços (Radioamador e Rádio do Cidadão)

- https://araf.org.br/anatel-links-rapidos

### Lista de frequências e repetidoras

<details>
<summary>Links para pesquisa</summary>

- https://www.radioamador.com/vhf/repetidorasold.htm
- https://www.radiohaus.com.br/pagina.php?cod=22&nomodal
- https://pt.wikipedia.org/wiki/Lista_de_faixas_e_subfaixas_do_servi%C3%A7o_radioamador_no_Brasil

</details>

### Números Discagem direta a distância ( DDD )

- https://pt.wikipedia.org/wiki/Discagem_direta_a_dist%C3%A2ncia
- https://www.mbi.com.br/mbi/biblioteca/utilidades/estado-onde-fica-ddd/

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Estação Rádio Base / ERBs 📻 <a name="estacoes-radio-erbs"></a>

Estações Radio Base ou ERBs são equipamentos que fazem a conexão entre os telefones celulares e a companhia telefônica, ou mais precisamente a Central de Comutação e Controle (CCC).

<details>
<summary>Links de Consulta</summary>

- https://www.teleco.com.br/erb.asp
- https://sistemas.anatel.gov.br/stel/consultas/ListaEstacoesLocalidade/tela.asp?pNumServico=010
- http://www.telecocare.com.br/telebrasil/mapa_erb.php
- https://conexis.org.br/numeros/mapa-de-antenas-2/
- http://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php
- http://sistemas.anatel.gov.br/siec-servico-movel-web/
- https://dados.gov.br/dataset?tags=ERB
- https://www.google.com/maps/d/u/0/viewer?msa=0&mid=1Xh8EWBDY97vtLnEYuAVLvRGvu2o&ll=-16.816639560865948%2C-51.73607799999998&z=5
- http://www.coberturacelular.com.br/
- https://servicos.pc.sc.gov.br/antena/

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Informações Acadêmicas 📄 <a name="informacoes-academicas"></a>

### Buscar Currículo Lattes

Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) é uma entidade ligada ao Ministério da Ciência, Tecnologia, Inovações e Comunicações para incentivo à pesquisa no Brasil.

- https://buscatextual.cnpq.br/buscatextual/busca.do?metodo=apresentar

### Buscar Informações de Instituições de Ensino Superior

Sistema do Ministerio da Educacao (MEC) responsavel pela tramitacao dos processos de ato regulatorio das instituicoes de educacao superior do Brasil. É possível buscar cursos e outras informações das instituições direto no MEC.

- https://emec.mec.gov.br/

### Biblioteca Digital de Teses e Dissertações (BDTD)
Repositório nacional que integra teses e dissertações defendidas em todo o Brasil.
- https://bdtd.ibict.br/

### Biblioteca Digital de Teses e Dissertações da USP
Repositório oficial com teses e dissertações da Universidade de São Paulo.
- https://www.teses.usp.br/

### Repositório Institucional da UnB
Acervo digital de produção científica da Universidade de Brasília.
- https://repositorio.unb.br/

### Pantheon - UFRJ
Repositório institucional da Universidade Federal do Rio de Janeiro.
- https://pantheon.ufrj.br/

### Lume - UFRGS
Repositório digital da Universidade Federal do Rio Grande do Sul.
- https://lume.ufrgs.br/

### ENADE - Resultados por Instituição
Consulta de resultados do Exame Nacional de Desempenho dos Estudantes.
- https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enade

### SciELO Brasil - Scientific Electronic Library Online
Biblioteca científica eletrônica com periódicos brasileiros de acesso aberto.
- https://www.scielo.br/

### Portal CAPES de Periódicos
Acesso a publicações científicas nacionais e internacionais (requer acesso institucional).
- https://www.periodicos.capes.gov.br/

### Observatório do PNE - Plano Nacional de Educação
Acompanhamento e monitoramento das metas do Plano Nacional de Educação.
- https://www.observatoriodopne.org.br/

### Censo da Educação Superior - INEP
Dados estatísticos completos sobre educação superior no Brasil.
- https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-da-educacao-superior

### INEP Data - Dados Abertos
Dados abertos sobre educação, incluindo censo escolar, ENEM, ENADE e outros indicadores educacionais.
- https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data

### Microdados INEP
Microdados detalhados de pesquisas, exames e avaliações educacionais.
- https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados

### MEC - Consulta de Diplomas Digitais
Validação de diplomas digitais emitidos por instituições de ensino.
- https://diplomadigital.mec.gov.br/

### Plataforma Sucupira
Sistema de informações sobre os programas de pós-graduação stricto sensu.
- https://sucupira.capes.gov.br/

### ENADE - Resultados por Instituição
Consulta de resultados do Exame Nacional de Desempenho dos Estudantes.
- https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enade

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)  
---

## Mapas e Georreferenciamento 🗺️ <a name="mapas-geo"></a>

### Imagens de Satélite via inpe.br

Instituto Nacional de Pesquisas Espaciais é um instituto federal brasileiro dedicado à pesquisa e exploração espacial, criado em 1961.

<details>
<summary>Mapas Inep</summary>

- http://www.dgi.inpe.br/catalogo/
- http://sigma.cptec.inpe.br/
- http://sigma2.cptec.inpe.br/
- http://sigma.cptec.inpe.br/radar/
- http://sigma.cptec.inpe.br/prec_sat/
- http://sigma.cptec.inpe.br/fortracc/
- http://satelite.cptec.inpe.br/vento/
- http://satelite.cptec.inpe.br/radiacao/
- http://terrabrasilis.dpi.inpe.br/app/map/alerts?hl=pt-br
- http://terrabrasilis.dpi.inpe.br/app/map/deforestation?hl=pt-br
- http://www2.dgi.inpe.br/catalogo/explore
- http://satelite.cptec.inpe.br/mapsat/
- http://sigma-soschuva.cptec.inpe.br/#
- https://queimadas.dgi.inpe.br/queimadas/bdqueimadas
- https://queimadas.dgi.inpe.br/queimadas/portal-static/situacao-atual/
- https://queimadas.dgi.inpe.br/queimadas/portal/videoaulas
- https://queimadas.dgi.inpe.br/queimadas/mapas-mensais/
- http://www.dgi.inpe.br/CDSR/
- https://www.arcgis.com/home/webmap/viewer.html?url=https%3A%2F%2Farcgis.sema.df.gov.br%2Fserver%2Frest%2Fservices%2FAreas_Queimadas%2FMapServer&source=sd
- https://arcgis.sema.df.gov.br/server/rest/services/Areas_Queimadas/MapServer
- https://www.cptec.inpe.br/dsat/
- http://mapas.sosma.org.br/
- http://www.inpe.br/webelat/homepage/
- https://sigef.incra.gov.br/

</details>

### Sistema Nacional de Cadastro Ambiental Rural ( SICAR-CAR )

O SICAR é um sistema público de geoprocessamento que mapeia todas as propriedades rurais registradas com o CAR (Cadastro Ambiental Rural). Sendo o CAR um registro público, nacional e obrigatório à todas as propriedades rurais do Brasil, com a finalidade de formar uma base de dados e integrar informações.

- https://www.car.gov.br/publico/imoveis/index
- https://www.car.gov.br/#/consultar

### Instituto do Patrimônio Histórico e Artístico Nacional ( IPHAN ) 🗿

O SICG (Sistema Integrado de Conhecimento e Gestão) é o desenvolvimento de Inventários de Conhecimento, para formar uma base de informações sobre os patrimônio cultural de todo o Brasil.

- https://sicg.iphan.gov.br/sicg/pesquisarBem

### Rede de Meteorologia do Comando da Aeronáutica ( REDEMET )

A Rede de Meteorologia do Comando da Aeronáutica tem como objetivo integrar os produtos meteorológicos voltados à aviação civil e militar, visando tornar o acesso a estas informações mais rápido, eficiente e seguro.

- https://redemet.decea.gov.br/#
- https://redemet.decea.gov.br/novo/

### Banco de Dados Geográficos do Exército ( BDGEx )

- https://bdgex.eb.mil.br/bdgexapp/mobile/

### Radar de Aeronaves

<details>
<summary>Links de pesquisa</summary>

- https://www.radarbox.com/@-19.21547,-46.45469,z5
- https://www.flightradar24.com/-18.82,-52.19/5
- https://www.edestinos.com.br/radar
- https://planefinder.net/airport/BSB

</details>

### Consulta de Licença Aeronáutica ( CHT )

Todos os tripulantes civis brasileiros devem ser registrados na ANAC. Sendo validado o registro pelo seu Código Anac (CANAC).

- https://sistemas.anac.gov.br/consultadelicencas/
- https://ais.cavok.in/lichab/

### Cidades e Estados - IBGE - Instituto Brasileiro de Geografia e Estatística

Consulta de dados por Cidades e Estados

- https://www.ibge.gov.br/cidades-e-estados/

### Portal de Mapas do IBGE
Portal com mapas interativos e bases cartográficas do IBGE.
- https://portaldemapas.ibge.gov.br/

### ANA - Agência Nacional de Águas - Mapas Interativos
Mapas e visualizações de dados sobre recursos hídricos no Brasil.
<details>
<summary>Mapas ANA</summary>

- Sistema Nacional de Informações sobre Recursos Hídricos - https://portal1.snirh.gov.br/ana/apps/webappviewer/index.html?id=ef7d29c2ac754e9890d7cdbb78cbaf2c
- Atlas de Abastecimento Urbano - https://portal1.snirh.gov.br/ana/apps/webappviewer/index.html?id=6d866c5d54c64b17bd53af4bdcfb4b91
- Conjuntura dos Recursos Hídricos - https://portal1.snirh.gov.br/ana/apps/webappviewer/index.html?id=76eaa4f324f2404a86784e21d882b6ec
- Sistema de Acompanhamento de Reservatórios - https://portal1.snirh.gov.br/ana/apps/webappviewer/index.html?id=0d9d29ec24cc49df89965f05fc5b96b9

</details>

### SIGMINE - Sistema de Informações Geográficas da Mineração
Sistema com informações georreferenciadas sobre mineração no Brasil.
- https://geo.anm.gov.br/portal/

### INDE - Infraestrutura Nacional de Dados Espaciais
Portal da Infraestrutura Nacional de Dados Espaciais.
- https://www.inde.gov.br/

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Território, Meio Ambiente & Fiscalização 🏞️ <a name="territorio-meio-ambiente-fiscalizacao"></a>

### UNAI — Terras Indígenas

Informações oficiais sobre povos indígenas, terras indígenas, demarcação e proteção territorial.  
- https://www.gov.br/funai/pt-br

---

### FUNAI — Mapas e Dados Geoespaciais

Mapas e bases georreferenciadas de terras indígenas (shapefiles, KML, situação territorial).  
- https://www.gov.br/funai/pt-br/atuacao/terras-indigenas/geoprocessamento-e-mapas

---

### INCRA — Reforma Agrária e Conflitos Fundiários

Dados sobre assentamentos, imóveis rurais, regularização fundiária e disputas por terra.  
- https://www.gov.br/incra/pt-br

---

### INCRA — Dados Abertos Fundiários

Bases estatísticas sobre assentamentos, imóveis rurais e políticas fundiárias.  
- https://www.gov.br/incra/pt-br/acesso-a-informacao/dados-abertos

---

### IBAMA — Fiscalização Ambiental

Fiscalização ambiental, crimes ambientais, desmatamento, garimpo ilegal e sanções administrativas.  
- https://www.ibama.gov.br

---

### IBAMA — Autos de Infração e Embargos

Consulta pública de autos de infração ambiental, embargos, apreensões e penalidades.  
- https://www.gov.br/ibama/pt-br/servicos/consultas/autuacoes-e-embargos

---

### INPE — Monitoramento Ambiental

Estatísticas oficiais de desmatamento e degradação ambiental com base em imagens de satélite.  
- https://www.gov.br/inpe/pt-br

---

### INPE — Programa Queimadas

Dados e estatísticas de focos de incêndio em tempo quase real.  
- https://queimadas.dgi.inpe.br/queimadas/portal

---

### ICMBio — Unidades de Conservação

Informações sobre parques nacionais, reservas ambientais e áreas protegidas federais.  
- https://www.gov.br/icmbio/pt-br

---

### ICMBio — Dados Abertos Ambientais

Estatísticas e bases públicas sobre unidades de conservação federais.  
- https://www.gov.br/icmbio/pt-br/acesso-a-informacao/dados-abertos

---

### MMA — Ministério do Meio Ambiente

Políticas ambientais, programas nacionais e dados institucionais do setor ambiental.  
https://www.gov.br/mma/pt-br

---

### MA — Indicadores Ambientais

Indicadores ambientais oficiais e dados estatísticos nacionais.  
- https://www.gov.br/mma/pt-br/assuntos/indicadores

---

### IBGE — Território e Meio Ambiente

Estatísticas territoriais, ambientais, uso do solo e dados geográficos oficiais.  
- https://www.ibge.gov.br

---

### IBGE — Geociências e Mapas

Mapas oficiais, limites territoriais, biomas e dados geoespaciais.  
- https://www.ibge.gov.br/geociencias

---

### ANM — Agência Nacional de Mineração

Dados sobre mineração, processos minerários, áreas concedidas e fiscalização.  
- https://www.gov.br/anm/pt-br

---

### ANM — Dados Abertos de Mineração

Bases estatísticas e dados públicos sobre atividades minerárias no Brasil.  
- https://www.gov.br/anm/pt-br/acesso-a-informacao/dados-abertos

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Saúde 🏥 <a name="saude"></a>

### Cadastro Nacional de Estabelecimentos de Saúde

Informações acerca de estabelecimentos e profissionais de saúde.

- https://cnes.datasus.gov.br/

### Fundo Nacional de Saúde (FNS)

- https://consultafns.saude.gov.br/#/consolidada

### ANS - Consulta de Operadoras de Planos de Saúde
Dados e indicadores sobre operadoras de planos de saúde.
- https://www.ans.gov.br/perfil-do-setor/dados-e-indicadores-do-setor

### ANVISA - Consulta de Medicamentos Registrados
Consulta de medicamentos e produtos registrados na ANVISA.
- https://consultas.anvisa.gov.br/#/medicamentos/

### SINAN - Sistema de Informação de Agravos de Notificação
Informações sobre agravos de notificação compulsória.
- http://www.portalsinan.saude.gov.br/

### Farmácia Popular - Estabelecimentos Credenciados
Lista de estabelecimentos credenciados no programa Farmácia Popular.
- https://www.gov.br/saude/pt-br/assuntos/assistencia-farmaceutica-no-sus/farmacia-popular

### DataSUS - Transferência de Arquivos
Portal para download de bases de dados de saúde pública, incluindo SIM, SINASC, SIH, SIA e outros sistemas.
- https://datasus.saude.gov.br/transferencia-de-arquivos/
  - https://datasus.saude.gov.br/wp-content/zipupload/ (Transferência de Arquivos / DataSUS)

### RIPSA - Rede Interagencial de Informações para a Saúde
Portal com indicadores de saúde, dados demográficos e socioeconômicos relacionados à saúde no Brasil.
- https://www.ripsa.org.br/

### Fiocruz - Mapas de Clima e Saúde
Plataforma de monitoramento e análise da relação entre clima e saúde no Brasil.
- https://mapas.climaesaude.icict.fiocruz.br/

### Fiocruz - Monitoramento de Seca
Sistema de monitoramento de eventos de seca e seus impactos na saúde.
- https://shiny.icict.fiocruz.br/sentseca2/

### Monitoramento dos Gastos no Combate à COVID-19

<details>
<summary>Links de pesquisa</summary>

- https://www.tesourotransparente.gov.br/visualizacao/painel-de-monitoramentos-dos-gastos-com-covid-19
- https://www.gov.br/compras/pt-br/painel-covid
- https://portaldatransparencia.gov.br/coronavirus

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Motores de Busca Contexto Brasil 🤖 <a name="dorks"></a>

### Google Hacking: DataLeak/SQL

- `site:com.br ext:sql "CREATE TABLE"`
  - https://www.google.com/search?q=site%3Acom.br+ext%3Asql+%22CREATE+TABLE%22###
- `site:com.br intext:"phpMyAdmin" ext:txt`
  - https://www.google.com/search?q=site%3Acom.br+intext%3A%22phpMyAdmin%22+ext%3Atxt

- ```site:br ext:sql | ext:db "senha" | "password"```
    - https://www.google.com/search?q=site%3Abr+ext%3Asql+%7C+ext%3Adb+%22senha%22+%7C+%22password%22

- ```site:com.br inurl:"backup" ext:sql | ext:bak```
    - https://www.google.com/search?q=site%3Acom.br+inurl%3A%22backup%22+ext%3Asql+%7C+ext%3Abak

### Google Hacking: Documento em Arquivos

- `cpf "SEU_ALVO" ext:txt`
  - https://www.google.com/search?q=cpf+%22SE_ALVO%22+%22123456789%22+ext
- `"cpf|cnpj|email|rg|contato" ext:xls "SEU_ALVO"`
  - https://www.google.com/search?q=%22cpf%7Ccnpj%7Cemail%7Crg%7Ccontato%22+ext%3Axls+%22SE_ALVO%22

### Google Hacking: Sites do Governo

Adicione sua string alvo para direcionar a busca

- `site:mil.br`
  - https://www.google.com/search?q=site%3Amil.br
- `site:gov.br`
  - https://www.google.com/search?q=site%3Agov.br

### Google Hacking: Documentos em Sites do Governo

Adicione sua string alvo para direcionar a busca

- `site:mil.br ext:pdf`
  - https://www.google.com/search?q=site%3Amil.br
- `site:gov.br  ext:xls`
  - https://www.google.com/search?q=site%3Agov.br
- `inurl:"mil.br" ext:php`
  - https://www.google.com/search?q=inurl:%22mil.br%22+ext:php

### Google Hacking: Informações Expostas

Adicione sua string alvo para direcionar a busca

- `site:anonfiles.com "SE_ALVO"`
  - https://www.google.com/search?q=site%3Aanonfiles.com+%22SE_ALVO%22
- `site:docs.google.com "SEU_ALVO"`
  - https://www.google.com/search?q=site%3Adocs.google.com+%22SEU_ALVO%E2%80%9D
- `site:facebook.com "SEU_ALVO"`
  - https://www.google.com/search?q=site%3Afacebook.com+%22SEU_ALVO%22
- `site:pastebin.com "SEU_ALVO" `
  - https://www.google.com/search?q=site%3Apastebin.com+%22nubank%22

### Google Hacking: Filtrar Empresa via Linkedin

Adicione sua string alvo para direcionar a busca

- `site:linkedin.com "at EMPRESA_ALVO"`
  - https://www.google.com/search?q=site%3Alinkedin.com+%22at+EMPRESA_ALVO%22

- ```site:linkedin.com/in intitle:"EMPRESA_ALVO" location:"Brazil"```
    - https://www.google.com/search?q=site%3Alinkedin.com%2Fin+intitle%3A%22EMPRESA_ALVO%22+location%3A%22Brazil%22

- ```site:linkedin.com "CARGO" "EMPRESA_ALVO" "São Paulo" | "Brasil"```
    - https://www.google.com/search?q=site%3Alinkedin.com+%22CARGO%22+%22EMPRESA_ALVO%22+%22S%C3%A3o+Paulo%22+%7C+%22Brasil%22

- ```site:linkedin.com/company "EMPRESA_ALVO"```
    - https://www.google.com/search?q=site%3Alinkedin.com%2Fcompany+%22EMPRESA_ALVO%22

### Google Hacking: Filtrar Grupos WhatsApp em Sites .br
Busca por links de grupos do WhatsApp compartilhados publicamente.

- ```"https://chat.whatsapp.com/" & site:br```
    - https://www.google.com/search?q=%22https%3A%2F%2Fchat.whatsapp.com%2F%22+%26+site%3Abr

- ```"chat.whatsapp.com" intext:"grupo" | "canal" brasil```
    - https://www.google.com/search?q=%22chat.whatsapp.com%22+intext%3A%22grupo%22+%7C+%22canal%22+brasil

- ```site:com.br "invite" "whatsapp"```
    - https://www.google.com/search?q=site%3Acom.br+%22invite%22+%22whatsapp%22

### Google Hacking: Filtrar Grupos Telegram + Contexto da String

- `inurl:"https://t.me" site:me "SEU_ALVO"`
  - https://www.google.com/search?q=inurl%3A%22https%3A%2F%2Ft.me%22+site%3Ame+%22SEU_ALVO%22
- `site:me "joinchat" "SEU_ALVO"`
  - https://www.google.com/search?q=site%3Ame+%22joinchat%22+%22Bolsonaro%22

### Google Hacking: Identificar Powerbi Exposto

- `site:app.powerbi.com/view?r intext:"br"`
  - https://www.google.com/search?q=site%3Aapp.powerbi.com%2Fview%3Fr+intext%3A%22br%22
- `site:app.powerbi.com/view?r intext:"brasil"`
  - https://www.google.com/search?q=site%3Aapp.powerbi.com%2Fview%3Fr+intext%3A%22brasil%22

### Shodan: Busca de Servidores Brasileiro

Shodan é um mecanismo de pesquisa que permite ao usuário encontrar tipos específicos de computadores conectados à Internet usando uma variedade de filtros.

- `country:"BR"`
  - https://www.shodan.io/search?query=country%3A%22BR%22
Busca por grupos e canais do Telegram relacionados ao Brasil.

- ```inurl:"https://t.me" site:me "SEU_ALVO"```
    - https://www.google.com/search?q=inurl%3A%22https%3A%2F%2Ft.me%22+site%3Ame+%22SEU_ALVO%22

- ```site:me "joinchat" "SEU_ALVO"```
    - https://www.google.com/search?q=site%3Ame+%22joinchat%22+%22SEU_ALVO%22

- ```site:t.me brasil | brasileiro | br```
    - https://www.google.com/search?q=site%3At.me+brasil+%7C+brasileiro+%7C+br

- ```inurl:"t.me/" "canal" | "grupo" português```
    - https://www.google.com/search?q=inurl%3A%22t.me%2F%22+%22canal%22+%7C+%22grupo%22+portugu%C3%AAs

### Google Hacking: Identificar PowerBI Exposto
Busca por dashboards do PowerBI com dados brasileiros.

- ```site:app.powerbi.com/view?r intext:"br"```
    - https://www.google.com/search?q=site%3Aapp.powerbi.com%2Fview%3Fr+intext%3A%22br%22

- ```site:app.powerbi.com/view?r intext:"brasil"```
    - https://www.google.com/search?q=site%3Aapp.powerbi.com%2Fview%3Fr+intext%3A%22brasil%22

- ```site:app.powerbi.com intext:"governo" | "prefeitura" | "estado"```
    - https://www.google.com/search?q=site%3Aapp.powerbi.com+intext%3A%22governo%22+%7C+%22prefeitura%22+%7C+%22estado%22

- ```site:powerbi.com "dashboard" | "relatório" brasil```
    - https://www.google.com/search?q=site%3Apowerbi.com+%22dashboard%22+%7C+%22relat%C3%B3rio%22+brasil

### Google Hacking: Servidores e Câmeras Expostas
Busca por servidores, webcams e sistemas expostos.

- ```inurl:"/view/index.shtml" site:br```
    - https://www.google.com/search?q=inurl%3A%22%2Fview%2Findex.shtml%22+site%3Abr

- ```intitle:"webcamXP 5" site:br```
    - https://www.google.com/search?q=intitle%3A%22webcamXP+5%22+site%3Abr

- ```inurl:"ViewerFrame?Mode=" site:com.br```
    - https://www.google.com/search?q=inurl%3A%22ViewerFrame%3FMode%3D%22+site%3Acom.br

- ```intitle:"Network Camera" site:br```
    - https://www.google.com/search?q=intitle%3A%22Network+Camera%22+site%3Abr

### Google Hacking: Informações de Contato
Busca por e-mails, telefones e contatos corporativos.

- ```site:com.br "@gmail.com" | "@hotmail.com" | "@yahoo.com"```
    - https://www.google.com/search?q=site%3Acom.br+%22%40gmail.com%22+%7C+%22%40hotmail.com%22+%7C+%22%40yahoo.com%22

- ```site:br "contato" | "fale conosco" ext:html```
    - https://www.google.com/search?q=site%3Abr+%22contato%22+%7C+%22fale+conosco%22+ext%3Ahtml

- ```site:com.br intext:"telefone:" | "celular:" | "whatsapp:"```
    - https://www.google.com/search?q=site%3Acom.br+intext%3A%22telefone%3A%22+%7C+%22celular%3A%22+%7C+%22whatsapp%3A%22

- ```site:br "@empresa.com.br" -site:linkedin.com```
    - https://www.google.com/search?q=site%3Abr+%22%40empresa.com.br%22+-site%3Alinkedin.com

### Google Hacking: Dados Acadêmicos
Busca por trabalhos acadêmicos, teses e dissertações.

- ```site:edu.br ext:pdf "tcc" | "dissertação" | "tese"```
    - https://www.google.com/search?q=site%3Aedu.br+ext%3Apdf+%22tcc%22+%7C+%22disserta%C3%A7%C3%A3o%22+%7C+%22tese%22

- ```site:br filetype:pdf "universidade" "trabalho de conclusão"```
    - https://www.google.com/search?q=site%3Abr+filetype%3Apdf+%22universidade%22+%22trabalho+de+conclus%C3%A3o%22

- ```site:edu.br inurl:"biblioteca" | inurl:"repositorio"```
    - https://www.google.com/search?q=site%3Aedu.br+inurl%3A%22biblioteca%22+%7C+inurl%3A%22repositorio%22

### Bing: Buscas Alternativas
Exemplos de dorks usando Bing para contexto brasileiro.

- ```site:com.br ext:xlsx```
    - https://www.bing.com/search?q=site%3Acom.br+ext%3Axlsx

- ```site:gov.br filetype:pdf licitação```
    - https://www.bing.com/search?q=site%3Agov.br+filetype%3Apdf+licita%C3%A7%C3%A3o

- ```ip:200.* country:BR```
    - https://www.bing.com/search?q=ip%3A200.*+country%3ABR

### DuckDuckGo: Buscas com Privacidade
Exemplos usando DuckDuckGo para pesquisas no Brasil.

- ```site:br filetype:csv```
    - https://duckduckgo.com/?q=site%3Abr+filetype%3Acsv

- ```site:com.br "email" OR "e-mail"```
    - https://duckduckgo.com/?q=site%3Acom.br+%22email%22+OR+%22e-mail%22


### Consulta de Domínios Maliciosos
Verificação de reputação e histórico de domínios brasileiros.

- **VirusTotal** - Análise de URLs, arquivos e domínios
    - https://www.virustotal.com/
    - Filtro para domínios .br: `entity:domain AND tld:br`
    - Busca por idioma: `content:"pt-br" OR content:"português"`
    
- **URLScan.io** - Scanner de URLs com análise visual
    - https://urlscan.io/
    - Busca avançada: `domain:.br AND (lang:pt OR lang:pt-br)`

### Shodan: Busca de Servidores Brasileiro
Shodan é um mecanismo de pesquisa que permite encontrar dispositivos conectados à Internet no Brasil.

- ```country:"BR"```
    - https://www.shodan.io/search?query=country%3A%22BR%22

- ```country:"BR" port:80,443 "Apache"```
    - https://www.shodan.io/search?query=country%3A%22BR%22+port%3A80%2C443+%22Apache%22

- ```country:"BR" port:3389```
    - https://www.shodan.io/search?query=country%3A%22BR%22+port%3A3389

- ```country:"BR" "webcam" has_screenshot:true```
    - https://www.shodan.io/search?query=country%3A%22BR%22+%22webcam%22+has_screenshot%3Atrue

- ```country:"BR" org:"Governo" | org:"Prefeitura"```
    - https://www.shodan.io/search?query=country%3A%22BR%22+org%3A%22Governo%22+%7C+org%3A%22Prefeitura%22  

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Rede Social 👥 <a name="redes-sociais"></a>

### LinkedIn

É uma rede social de negócios fundada com mais de 750 milhões de usuários.

- https://www.linkedin.com/jobs/search/?keywords=SEU_ALVO&location=Brasil

### Instagram

Rede mais utilizada atualmente, ótimo para a busca de imagens por localidade

- https://www.instagram.com/explore/

Ferramenta para busca de dados no Instagram

- https://www.aware-online.com/en/osint-tools/instagram-search-tool/
- https://www.aware-online.com/en/osint-tools/instagram-tools/

### Twitter

É uma rede social e um servidor para microblogging e é possível uma busca mais efetiva usando sua busca avançada.

- `seu_alvo lang:pt`
  - https://twitter.com/search?q=seu_alvo+lang%3Apt&src=typed_query
  - https://twitter.com/search-advanced

### OmniSci Tweetmap Demo

OmniSci é um banco de dados alimentado por GPU (Unidade de Processador Gráfico) e plataforma de visualização projetada para exploração de dados imersiva e ultrarrápida que elimina a desconexão entre o analista e os dados.

- https://www.omnisci.com/demos/tweetmap

### Maptimize Demo Sentiment Analysis on Tweets

Esta página exibe os tweets e geolocalização das últimas 24 horas entregues pela API de fluxo público do Twitter.

- https://onemilliontweetmap.com/?center=-18.79191774423444,-39.33105468750001&zoom=5&search=SEU_ALVO

### TweetStats Graficamente

Represente graficamente suas estatísticas do Twitter, incluindo Tweets por hora, Tweets por mês, cronograma do Tweet, estatísticas de resposta.

- https://www.tweetstats.com/graphs/PERFIL_ALVO

### Trend24 Trends e buscas locais e global

Uma ferramenta para capturando pensamentos e emoções da população do Twitter em qualquer ponto do tempo.

- https://trends24.in/SEU_ALVO/

### Snap Map

- https://map.snapchat.com/@-15.127315,-51.412151,4.51z

### YouTube

- https://www.aware-online.com/en/osint-tools/youtube-search-tool/

### Reedit

- https://www.aware-online.com/en/osint-tools/reddit-search-tool/

### Tiktok

- https://www.tiktok.com/explore

### Kwai

- https://www.kwai.com/discover/

### Facebook Biblioteca de Anúncios

A Biblioteca de Anúncios garante a transparência publicitária oferecendo uma coleção abrangente e pesquisável de todos os anúncios em veiculação nos aplicativos e serviços do Facebook, incluindo o Instagram

- https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=BR&media_type=all

### Procurador de redes sociais

Uma ferramenta que busca redes sociais como Linkedin, instagram e facebook somente adicionando o nome no final do link.

- https://www.social-searcher.com/search-users/?q6=NOME+SOBRENOME

### UVRX buscador de redes sociais

Um site onde utiliza a busca do google para fazer uma pesquisa mais avançada em redes sociais.

- http://www.uvrx.com/social.html
- https://www.aware-online.com/osint-tools/

### OSINT Steam

Uma ferramenta [open-source](https://github.com/Berchez/OSINT-steam) que retorna informações públicas, como lista de amigos e possíveis localizações, de perfís do Steam.

- https://osint-steam.vercel.app/pt

### Scan User

Ferramenta desenvolvida em linguagem shellscript em português para buscas de perfis online com e-mail e nickname, incluindo fotos, onde é possível enviar os resultados para o Telegram via API.

- https://github.com/faciltech/scan-user
- Autor: Eduardo Amaral

### Caipora Pro

Repositório de ferramentas para Inteligência de Fontes Abertas (OSINT) e Investigação Digital com enfoque no Brasil.

- https://caipora.pro

### OSINTkit-Brasil

Curadoria nacional de ferramentas de OSINT (Open Source Intelligence), cuidadosamente organizadas para facilitar investigações, pesquisas e atividades de segurança da informação.
O projeto reúne mais de 1600 links úteis categorizados em formato de bookmarks HTML compatíveis com qualquer navegador.

- https://github.com/felipeluan20/OSINTKit-Brasil

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Indexadores de Serviço de Mensagens Instantâneas 💬 <a name="indexador-mensagens"></a>

### Grupos de WhatsApp

WhatsApp é um aplicativo multiplataforma de mensagens instantâneas e chamadas de voz para smartphones.

<details>
<summary>Indexadores WhatsApp</summary>

Lista de recursos para encontrar grupos públicos de WhatsApp.

- https://gruposwhats.app/
- https://whatsapp.statusestories.com/
- https://grupos-online.com/
- https://grupowhats.online/
- https://buscagrupos.com.br/
- https://www.gruposwats.com/
- https://gruposputaria.com/
- https://www.gruposexozap.com.br/
- https://www.grupopaquera.com.br/
- https://gruposdezap.com/
- https://grupodewhatsapp.com/
- https://gruposdewhatss.com.br/

</details>

### Grupos de Telegram

O Telegram é um serviço de mensagens instantâneas baseado na nuvem.

<details>
<summary>Indexadores Telegram</summary>

Lista de recursos para encontrar grupos públicos de Telegram.

- https://tgstat.com/search
- https://cse.google.com/cse?cx=008239573640124656331:o29gdxc2osj
- https://www.telegram-group.com/en/#
- https://tgstat.com/
- https://xtea.io/ts_en.html#gsc.tab=0&gsc.q=SEU_ALVO
- https://telemetr.io/en/channels?language=pt&channel=SEU_ALVO&period=30
- https://combot.org/telegram/top/groups?lng=pt&page=1&q=SEU_ALVO
- https://lyzem.com/search?f=all&l=pt&p=1&per-page=100&q=SEU_ALVO
- https://gruposdetelegram.com.br/

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Datasets / Dados Abertos 🗂️ <a name="datasets"></a>

### Dados Abertos / Gov BR

Conjuntos de datasets disponibilizados pelo Governo Federal

- https://dados.gov.br/home

### Brasil.io

Repositório de dados públicos disponibilizados em formato acessível

- https://brasil.io/datasets/

### Dados MMA - Ministério do Meio Ambiente e Mudança do Clima

Datasets em formato aberto, o conteúdo sobre a área ambiental disponibilizado pelo Ministério do Meio Ambiente

- https://dados.mma.gov.br/

### Dados Ibict - Instituto Brasileiro de Informação em Ciência e Tecnologia

O Dados Ibict é um repositório de dados abertos para promover, ampliar e aprimorar a abertura de dados do IBICT

- https://dados.ibict.br/dataset

### Dados BCB - Banco Central Do Brasil

O Portal Brasileiro de Dados Abertos do Banco Central é o meio utilizado pelo BC para disponibilizar dados e informações públicas

- https://dadosabertos.bcb.gov.br/dataset

### Dados MTur - Ministério do Meio Ambiente e Mudança do Clima

O Plano de Dados Abertos do MTur abrange os setores do turismo e da cultura, e é o documento orientador para as ações de implementação e promoção de abertura de dados produzidos ou que estão sob a responsabilidade do Ministério do Turismo (MTur)

- https://dados.turismo.gov.br/dataset/

### Dados IBAMA - Instituto Brasileiro do Meio Ambiente e dos Recursos Naturais Renováveis

O IBAMA utilizado o portal abaixo para disponibilizar dados e informações públicas, relacionados a operação e fiscalização.

- https://dadosabertos.ibama.gov.br/en/dataset/

### Sistema Nacional de Dados Migratórios
Sistema de dados e estatísticas sobre migração no Brasil, gerido pelo Ministério da Justiça e Segurança Pública.
- https://datamigra.mj.gov.br

### Dados PF - Polícia Federal

Em síntese, o trabalho de produção do PDA/PF consistiu na elaboração do inventário de bases de dados da Polícia Federal, no saneamento do inventário pelas Diretorias e unidades responsáveis, e, por fim, na priorização dos bancos a serem abertos com base em critérios sugeridos pelo Comitê Gestor da Infraestrutura Nacional de Dados Abertos-CGINDA.

- https://dados.gov.br/dados/organizacoes/visualizar/policia-federal
- (BETA) https://www.gov.br/pf/pt-br/acesso-a-informacao/dados-abertos/plano-de-dados-abertos-2024-2026

### Superintendências e Delegacias da Polícia Federal
Diretório com informações sobre as superintendências regionais e delegacias da Polícia Federal em todo o Brasil.
- https://www.gov.br/pf/pt-br/acesso-a-informacao/institucional/quem-e-quem/superintendencias-e-delegacias

### Dados CAPES - Coordenação de Aperfeiçoamento de Pessoal de Nível Superior

A primeira iniciativa da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES) para a publicação de dados abertos foi a elaboração do Plano de Dados Abertos (PDA). O propósito deste documento é o de publicitar as ações e estratégias organizacionais que nortearão as atividades de implementação e promoção da abertura de dados, no âmbito da CAPES de forma institucionalizada e sistematizada.

- https://dadosabertos.capes.gov.br/dataset/

### Dados IBGE - Instituto Brasileiro de Geografia e Estatística

Acesso a conteúdos das pesquisas estruturais, censos, entre outras, na área de estatísticas.

- https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html

### Dados Prefeitura de Mogi das Cruzes

O Portal da Prefeitura de Mogi das Cruzes com Dados Abertos da Administração Pública Municipal.

- https://dados.mogidascruzes.sp.gov.br/dataset/

### Dados Alagoas SEPLAG - Secretaria de Estado do Planejamento, Gestão e Patrimônio

O Portal Alagoas em Dados é uma plataforma desenvolvida pela Secretaria de Estado do Planejamento, Gestão e Patrimônio (SEPLAG) de Alagoas, que oferece acesso a uma ampla gama de informações e estatísticas sobre o estado. Por meio desse portal, os usuários podem obter dados atualizados em áreas cruciais como educação, saúde, economia.

- https://dados.al.gov.br/catalogo/dataset

### Dados MAPA - Ministério da Agricultura e Pecuária

O Ministério da Agricultura e Pecuária (Mapa) é responsável pela gestão das políticas públicas de estímulo à agropecuária, pelo fomento do agronegócio e pela regulação e normatização de serviços vinculados ao setor. No Brasil.

- https://dados.agricultura.gov.br/dataset

### Dados MJ - Ministério da Justiça

O Portal da Dados MJ disponibiliza Dados Abertos da Administração Pública, dentro do contexto de Justiça Brasileira.

- https://dados.mj.gov.br/dataset

### Dados Santa Catarina

O Portal de Dados Abertos do Estado de Santa Catarina é a plataforma oficial de publicação de dados governamentais em formato aberto.

- https://dados.sc.gov.br/

### Dados DNIT - Departamento Nacional de Infraestrutura de Transportes

O Plano de Dados Abertos – PDA é o documento orientador para as ações de implementação e promoção de abertura de dados, inclusive georreferenciados, no Departamento Nacional de Infraestrutura de Transportes

- https://servicos.dnit.gov.br/dadosabertos/

### Dados Prefeitura de São Paulo

O Portal de Dados Abertos da Prefeitura de São Paulo tem sua origem no Catálogo Municipal de Bases de Dados (CMBD). Organizado pela Coordenadoria de Promoção da Integridade (COPI) da Controladoria Geral do Município (CGM-SP) em conjunto com os órgãos e entidades da Prefeitura, o Catálogo apresenta aos munícipes uma relação com todos os dados disponíveis produzidos pela Prefeitura.

- http://dados.prefeitura.sp.gov.br/dataset

### Dados Abertos do Estado de Pernambuco

O Portal de Dados Abertos do Estado de Pernambuco (dados.pe.gov.br) reúne, em um só lugar, os conjuntos de dados dos órgãos pertencentes ao Poder Executivo Estadual.

- https://dados.pe.gov.br/dataset

### Dados BNDES - Banco Nacional de Desenvolvimento Econômico e Social

O Banco Nacional de Desenvolvimento Econômico e Social (BNDES) é uma empresa pública federal cujo principal objetivo é o financiamento de longo prazo e investimento em todos os segmentos da economia brasileira.

- https://dadosabertos.bndes.gov.br/dataset

### Dados Abertos do Estado de Minas Gerais

Os conjuntos de dados (datasets) deste Portal Estado de Minas Gerais estão documentados conforme as especificações Frictionless Data (dados sem fricção), que atendem à caracterização descrita nos normativos citados acima e possibilitam a validação automática dos dados.

- https://dados.mg.gov.br/dataset/

### Dados Abertos do Estado do Maranhão

- https://dados.ma.gov.br/

### Dados Abertos da Prefeitura de Belo Horizonte

O Portal de Dados Abertos da Prefeitura de Belo Horizonte é a ferramenta disponibilizada pelo governo municipal para que todos possam encontrar e utilizar dados e informações públicas.

- https://dados.pbh.gov.br/dataset/

### Dados ANTT - Agência Nacional de Transportes Terrestres

O Portal de Dados Abertos da ANTT é a ferramenta disponibilizada pela ANTT para facilitar a localização e utilização dos dados públicos, com previsão de abertura nos Plano de Dados Abertos.

- https://dados.antt.gov.br/dataset

### Dados SESGO - Secretaria Estadual de Saúde de Goiás

Página dedicada aos dados da Secretaria Estadual de Saúde de Goiás. Aqui, é disponibilizado uma vasta coleção de informações detalhadas e atualizadas sobre diversos aspectos da saúde pública no estado de Goiás.

- https://dados.saude.go.gov.br/dataset/

### Dados SiBBr - Sistema de Informação sobre a Biodiversidade Brasileira

Infraestrutura nacional de dados e informações em biodiversidade, é responsável pela organização, indexação, armazenamento e disponibilização de dados e informações sobre a biodiversidade e os ecossistemas brasileiros

- https://collectory.sibbr.gov.br/collectory/datasets

### Dados CVM - Portal de Dados Abertos da Comissão de Valores Mobiliários

A CVM é a Autarquia do governo federal que atua para garantir a integridade, estimular a eficiência e promover o desenvolvimento do mercado de capitais brasileiro, promovendo o equilíbrio entre a iniciativa dos agentes e a efetiva proteção dos investidores.

- https://dados.cvm.gov.br/dataset/
- https://dados.cvm.gov.br/dados/

### Dados TCMGO - Portal oficial do Tribunal de Contas dos Municípios do Estado de Goiás

- https://www.tcm.go.gov.br/Reports/browse/

### Serviço Geológico do Brasil

- https://www.sgb.gov.br/

### Querido Diário - Diários oficiais

Projeto da Open Knowledge Brasil que reúne e disponibiliza em formato aberto os diários oficiais de centenas de prefeituras brasileiras.

- https://queridodiario.ok.org.br

### Fogocruzado
O maior banco de dados sobre violência armada da América Latina. Pesquisar ocorrências. É possivel pesquisar dados por estado, cidades, datas e tipo de ocorrência.
- https://api.fogocruzado.org.br/search

### Portal Brasileiro de Dados Abertos - Governo Federal
Portal central de dados abertos do governo federal brasileiro. Hub principal para descoberta de datasets de diversos órgãos.
- https://dados.gov.br/

### Página Dados Abertos - Governo Digital
Contexto, normas e orientações sobre a política de dados abertos do Governo Federal.
- https://www.gov.br/governodigital/pt-br/dados-abertos

### Portal Brasileiro de Dados Científicos
Repositório de dados científicos brasileiros.
- https://dadoscientificos.ufsc.br/

### Dados Abertos da Câmara dos Deputados
Conjuntos de dados abertos da Câmara dos Deputados.
- https://dadosabertos.camara.leg.br/

### Dados Abertos do Senado Federal
Conjuntos de dados abertos do Senado Federal.
- https://www12.senado.leg.br/dados-abertos

### Dados Abertos do TCU
Dados abertos do Tribunal de Contas da União.
- https://portal.tcu.gov.br/dados-abertos/

### IPEA Data
Base de dados macroeconômicos, sociais e regionais do Brasil.
- http://www.ipeadata.gov.br/

### Consulta de CEP - Correios
Consulta de CEP e endereçamento postal.
- https://www.correios.com.br/enviar-e-receber/ferramentas/consulta-cep

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Dados de remuneração do Judiciário 📊 <a name="dados-de-remuneracao-do-judiciario"></a>

### DadosJusBr

Base estruturada (2018–2025) com salários, benefícios e índices de transparência de mais de 120 órgãos do sistema de Justiça Brasileira.

- https://dadosjusbr.org/

## Consulta de Transporte Terrestre 🚗 <a name="consulta-transporte-terrestre"></a>

### Consulta de Licenciamento Veicular

- http://licenciamento.detran.ma.gov.br/Licenciamento/consulta/Home.xhtml

### Consulta de Bicicletas / São Paulo

Serviço online que permite a qualquer pessoa verificar se uma bicicleta tem histórico de roubo ou furto. É usado Número ou Serial para consulta.

- https://www.ssp.sp.gov.br/consultabicicleta

### Consulta de Dados via Placa

<details>
<summary>Links de Consulta</summary>

- https://carfacts.com.br/ConsultaGratis
- https://www.qualveiculo.net/
- https://www.olhonocarro.com.br/
- https://www.consultarplaca.com.br/
- http://infocarrosp.com.br/
- https://www.iq.com.br/veiculos/consulta-placa/
- https://www.carcheck.com.br/
- https://www.consultapelaplaca.com.br/
- https://site.bibipecas.com.br/home
- https://www.historicar.com.br/
- https://www.keplaca.com
- https://www.fipeplaca.com.br/
- https://placafipe.com
- https://placaipva.com.br
- https://www.tabelafipebrasil.com/placa
- https://www.ipvabr.com.br/placa
</details>

### Consulta de Dados FIPE

<details>
<summary>Links de Consulta</summary>

- https://veiculos.fipe.org.br
- https://www.tabelafipebrasil.com
- https://www.tabelafipe.website
- https://www.tabelafipemotos.com.br
- https://www.fipeveiculos.com.br
- https://www.valortabelafipe.com.br
- https://veiculosfipe.org/
- https://fipevalor.com.br/
</details>

### Consulta Terminais Ônibus São Paulo

Secretaria Municipal de Transporte e Mobilidade Urbana ( SPTRANS )

- https://www.sptrans.com.br/terminais
- https://sistemas.sptrans.com.br/PlanOperWeb/

### Consulta Históricos de Ônibus

As buscas do Ônibus Brasil são um serviço de utilidade pública que permite rastrear registros históricos de ônibus que circulam ou circularam pelas ruas do Brasil e diversos outros países.

- https://onibusbrasil.com/placas

### Consulta Veículos Habilitados pela ANTT

Permite visualizar os veículos, nacionais e estrangeiros, habilitados pela ANTT ao transporte rodoviário internacional de cargas.

- https://appweb1.antt.gov.br/scff/conPlaca.asp

### Consulta Linhas de Ônibus

Consulta Linhas que Fazem Ligação entre Duas Localidades

- https://portal.antt.gov.br/linhas-de-onibus

### Consulta de Linhas de Ônibus Ao vivo para São Paulo

- https://radar24.net/train-radar/

### Consulta de Linhas de Trem

- https://radar24.net/train-radar/

### SERPRO - Consulta de Multas Federais
Consulta de multas aplicadas em rodovias federais.
- https://servicos.serpro.gov.br/multas/

### INFRAERO - Informações de Aeroportos
Portal de transparência da INFRAERO com informações sobre aeroportos.
- https://transparencia.infraero.gov.br/

### DNIT - Sistema de Gerenciamento de Pontes
Informações sobre pontes e viadutos sob responsabilidade do DNIT.
- https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/sgp

### Consulta Horários e Passagens Ônibus

Somos o portal de pesquisa de horários e passagens de ônibus mais completo e mais acessado do Brasil, chegando a 4,1 milhões de visitas mensais.

- https://www.buscaonibus.com.br/

### Empresas Habilitadas

Empresas habilitadas para a prestação do serviço de transporte rodoviário coletivo interestadual e internacional de passageiros, sob regime de autorização e fretamento.

- https://dados.antt.gov.br/dataset/empresas-habilitadas

### Consulta Pública de Transportadores

RNTRC - Registro Nacional de Transportadores Rodoviários de Cargas

- https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/consultapublica

### Pesquisar no Portal de Dados Abertos da ANTT

A Política de Dados Abertos do Poder Executivo Federal, instituída pelo Decreto n° 8.777, de 11 de maio de 2016, tem o objetivo de aprimorar a cultura de transparência pública ao estabelecer regras para publicação, em formato aberto.

- https://dados.antt.gov.br/

### Urbanização de Curitiba S/A (URBS) / Informações dos Táxis de Curitiba

Localização dos Pontos de Táxi em Curitiba

- https://www.urbs.curitiba.pr.gov.br/mobile/taxiLegal
- https://urbs.curitiba.pr.gov.br/transporte/pontos-de-taxi

### Urbanização de Curitiba S/A (URBS) / Embarques e Desembarques da Rodoviária

Informações sobre Linhas Rodoviárias em Curitiba

- https://www.urbs.curitiba.pr.gov.br/mobile/monitorRod
- https://urbs.curitiba.pr.gov.br/horario-de-onibus/rodoviaria

### Consultas DETRAN por Estado
Consultas veiculares, CNH, pontuação e outros serviços dos DETRANs estaduais.

<details>
<summary>Consultas por Estado</summary>

**Acre (AC)**
- Consulta estampagem - https://www.detran.ac.gov.br/consultar-autorizacao-de-estampagem/
- Consulta SNG - https://www.ac.getran.com.br/site/apps/veiculo/consulta/filtro-chassi-sng.jsp
- Consulta de pontuação CNH - https://www.detran.ac.gov.br/portal-de-servicos/consulta-pontuacao-de-cnh/

**Alagoas (AL)**
- DETRAN-AL Consulta Veículos - http://www.detran.al.gov.br/consulta-veiculo/

**Amazonas (AM)**
- DETRAN-AM Consultas - https://www.detran.am.gov.br/servicos/

**Bahia (BA)**
- DETRAN-BA Consultas - https://www.detran.ba.gov.br/

**Ceará (CE)**
- DETRAN-CE Consultas - https://www.detran.ce.gov.br/

**Distrito Federal (DF)**
- DETRAN-DF Consultas - https://www.detran.df.gov.br/

**Goiás (GO)**
- Consulta veículos/infrações - https://www.detran.go.gov.br/psw/#/pages/conteudo/consulta-multas-renainf
- Consulta processos - https://www.detran.go.gov.br/psw/#/pages/conteudo/consulta-processo/1
- Consulta CNH Social - https://www.detran.go.gov.br/psw/#/pages/conteudo/acompanhar-cnh-social
- Consulta Prontuário CNH - https://www.detran.go.gov.br/psw/#/pages/conteudo/prontuario-cnh
- Primeira CNH - https://www.detran.go.gov.br/psw/#/pages/conteudo/primeira-cnh

**Maranhão (MA)**
- Consulta de Licenciamento Veicular - http://licenciamento.detran.ma.gov.br/Licenciamento/consulta/Home.xhtml

**Pará (PA)**
- Consulta de Veículo Detalhada - https://www.detran.pa.gov.br/sistransito/detran-web/servicos/veiculos/indexRenavam.jsf
- Consultar Pontuação CNH - https://www.detran.pa.gov.br/servicos/pontuacao/index.php

**Piauí (PI)**
- Licenciamento DETRAN-PI - http://taxas.detran.pi.gov.br/licenciamento/index.jsf

**Rio de Janeiro (RJ)**
- Atestado DIC - http://atestadodic.detran.rj.gov.br/
- Certidão de Inteiro TEOR (CIT) - http://certidaoiifppcerj.detran.rj.gov.br/
- CONSULTA DÉBITO DE VEÍCULO - RJ - https://www.ib7.bradesco.com.br/ibpfdetranrj/debitoVeiculoRJLoader.do
- Documento Único do DETRAN de Arrecadação - RJ - https://www.ib7.bradesco.com.br/ibpfdetranrj/debitoVeiculoRJDudaSelecionarProduto.do?cdProdutoInicial=INI
- Guia de Recolhimento de Multas - RJ - https://www.ib7.bradesco.com.br/ibpfdetranrj/debitoVeiculoRJGrmConsultar.do
- Guia de Regularização de Taxas - RJ - https://www.ib7.bradesco.com.br/ibpfdetranrj/DebitoVeiculoRJGRTLoaderAction.do
- Informações de Pagamentos Efetuados - RJ - https://www.ib7.bradesco.com.br/ibpfdetranrj/debitoVeiculoRJConsultaLoader.do

**Rondônia (RO)**
- Consultar Veículos por placa + renavam e/ou CPF/CNPJ - https://consulta.detran.ro.gov.br/CentralDeConsultasInternet/Software/ViewConsultaVeiculos.aspx
- Descobrir Número da CNH com CPF e Data de Nascimento - https://consulta.detran.ro.gov.br/CentralDeConsultasInternet/Internet/Habilitacao/ConsultaProcesso.asp
- Consulta Pública do Veículo - https://centralservicos.detran.ro.gov.br/consulta/veiculo
- Consultar Resultado da Prova do DETRAN - https://consulta.detran.ro.gov.br/ResultadoProva

**Roraima (RR)**
- DETRAN-RR Consulta de Veículos - https://www.rr.getran.com.br/site/apps/veiculo/filtroplacarenavam-consultaveiculo.jsp
- DETRAN-RR Nada Consta - https://www.rr.getran.com.br/site/apps/nada-consta/filtroPessoaNadaConsta.jsp

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Tracking de Viagens de Ônibus 🚌 <a name="tracking-viagens-onibus"></a>

### Onibus.info

Acompanhe ônibus de Joinville em tempo real

- https://onibus.info

### SPTrans Olho Vivo

Localização dos ônibus, ao longo do trajeto, em quanto tempo e quais linhas de ônibus se aproximam, corredores, velocidade média e tempo de percurso.

- https://olhovivo.sptrans.com.br

### Urbanização de Curitiba S/A (URBS) / Monitoramento de Ônibus

Rastreamento de informações sobre transporte na cidade de Curitiba. É possivel filtrar por linhas, rotas de ônibus, posição de pontos, veículos.

<details>
<summary>Links de pesquisa</summary>

- Linhas, rotas de ônibus, posição de pontos e veículos
  - https://www.urbs.curitiba.pr.gov.br/mobile/itibus
  - https://www.urbs.curitiba.pr.gov.br/mobile/itibus6
  - https://urbs.curitiba.pr.gov.br/horario-de-onibus

- Boletim informacional relacionado ao transporte coletivo de Curitiba
  - https://www.urbs.curitiba.pr.gov.br/mobile/boletim

- Extrato do cartão transporte Avulso
  - https://www.urbs.curitiba.pr.gov.br/mobile/cartao

</details>

### Viação Ouro e Prata S/A, UneSul e TTL

É possivel acompanhar uma viagem de ônibus usando parâmetros como Empresa, Data, número de reserva ou número de serviço.

- https://rastreamento.viacaoouroeprata.com.br/

### Viação Águia Branca S.A.

É possivel acompanhar uma viagem de ônibus usando parâmetro o número de serviço.

- https://acompanheaviagem.aguiabranca.com.br

### FlixBus Transporte e Tecnologia do Brasil Ltda.

É possivel acompanhar uma viagem de ônibus da empresa FlixBus usando parâmetros como saída, chegada e número de reserva.

- https://www.flixbus.com.br/track/

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Consulta de Transporte Aquaviário 🛫 <a name="consulta-transporte-aquaviario"></a>

### Consulta dados públicos de fiscalização e processos sancionadores da ANTAQ

- https://aquarela.antaq.gov.br/single/?appid=62518b21-6421-4eab-9c35-bcfac6d57ffd&sheet=70ada7af-9026-4f15-a862-8a40becb7e7d&theme=horizon&opt=currsel,ctxmenu

### Dados Públicos - Gestão de multas e indicadores | ANTAQ

- https://app.powerbi.com/view?r=eyJrIjoiYTI4MDc3OWEtMmY5Yi00OTU4LTk3OWYtZjExODY0NTExMTQ0IiwidCI6IjhlNTdmNzI3LTBlNWUtNDEzMC04ZTI0LTJkNWY3YzhjMzhmNiJ9

### Navegação Interior - Pesquisa de Empresas Autorizadas

- https://web3.antaq.gov.br/Portal/Frota/ConsultarEmpresaInteriorAutorizada.aspx

### Pesquisa de Linhas e Horários Navegação Interior

- https://web3.antaq.gov.br/ea/sense/index.html#pt

### Atlas Aquaviários

- https://www.gov.br/dnit/pt-br/assuntos/aquaviario/atlas-aquaviario/

### Patrimônio Imobiliário do DNIT no Âmbito da Infraestrutura Aquaviária

- https://www.gov.br/dnit/pt-br/assuntos/aquaviario/patrimonio

### Radar de Tráfego Marítimo

- https://www.marinetraffic.com/en/ais/home/centerx:-40.1/centery:-3.4/zoom:7
- https://radar24.net/ship-radar/

### Rotas de Tráfego Marítimo

- https://marineradar.de/en/

### Pesquisa de Ferrys

- https://www.ferryscanner.com/pt/navios-de-ferry

### Pesquisa de Cruzeiros

- https://centraldecruzeiros.com.br/

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Consulta de Transporte Aéreo 🛫 <a name="consulta-transporte-aereo"></a>

### Consulta de Vôos via Infraero

As informações aqui fornecidas são obtidas diretamente das companhias aéreas. Não nos responsabilizamos por consequências resultantes de possíveis erros ou omissões.

- http://voos.infraero.gov.br/voos/index.aspx

### Consulta de Vôos de autoridades Brasileiras

Os dados incluem a autoridade solicitante, trajeto, data, horário de decolagem e de pouso, o motivo da solicitação, além da previsão do número de passageiros;

- https://www.fab.mil.br/voos

### Consulta de Empresas e de Aeronaves de Táxi-Aéreo

A ANAC disponibiliza uma consulta de empresas ou aeronaves de táxi-aéreo a todos os cidadãos interessados.

- https://sistemas.anac.gov.br/voeseguro/

### Consulta de Nada Consta de Multas do CBAER

- https://sistemas.anac.gov.br/nadaconsta/

### Consultas ao Registro Aeronáutico Brasileiro (RAB)

Todas as aeronaves civis brasileiras devem ser registradas na ANAC. O Registro Aeronáutico Brasileiro (RAB) – regulamentado por meio da Resolução ANAC nº 293/2013

- https://sistemas.anac.gov.br/aeronaves/cons_rab.asp
- https://ais.cavok.in/rab/
<details>
<summary>Consultas RAB/ANAC</summary>

- Portal Principal de Aeronaves - https://aeronaves.anac.gov.br/aeronaves/
- Consulta por Matrícula - https://aeronaves.anac.gov.br/aeronaves/#matricula
- Consulta por Habilitação - https://aeronaves.anac.gov.br/aeronaves/#habilitacao
- Consulta por Código ICAO - https://aeronaves.anac.gov.br/aeronaves/#icao
- Consulta por Modelo - https://aeronaves.anac.gov.br/aeronaves/#modelo
- Consulta por Fabricante - https://aeronaves.anac.gov.br/aeronaves/#fabricante
- Consulta por Número de Série - https://aeronaves.anac.gov.br/aeronaves/#nserie
- Consulta RAB - Resposta - https://aeronaves.anac.gov.br/aeronaves/cons_rab_resposta2.asp?
- Sistema Antigo - https://sistemas.anac.gov.br/aeronaves/cons_rab.asp
- Cavok RAB - https://ais.cavok.in/rab/

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Câmeras Online 🎥 <a name="cameras-online"></a>

### Projeto City Câmeras

O Projeto City Câmeras é um programa público, de iniciativa exclusiva da Prefeitura Municipal de São Paulo, que visa constituir uma ampla rede de videomonitoramento por meio de câmeras públicas e privadas instaladas pela cidade.

- https://www.citycameras.prefeitura.sp.gov.br/home

### Câmeras Cia. de Engenharia de Tráfego (CET)

- http://cameras.cetsp.com.br/

### Câmeras DER - Departamento de Estradas de Rodagem (DER)

- http://www.der.sp.gov.br/WebSite/Servicos/ServicosOnline/CamerasOnlineMapa.aspx

### Windy - Serviço de Cãmeras e Radar meteorológico

- https://www.windy.com/pt/-Webcams/webcams?-16.994,-54.316,5

### Câmeras Rodovias Online

O site Rodovias Online é um serviço de Utilidade Pública, onde procuramos reunir de forma fácil e eficaz visualizações de câmeras on-line.

<details>
<summary>rodoviasonline.com.br</summary>

- http://www.rodoviasonline.com.br/rodovias-der-sp/
  - http://www.rodoviasonline.com.br/cameras-ao-vivo-das-rodovias-do-estado-do-parana/
  - https://www.rodoviasonline.com.br/cameras-ao-vivo-nas-rodovias-do-rio-grande-de-sul-daer-rs/
  - https://www.rodoviasonline.com.br/rodovia-governador-ney-braga-br-277/
  - https://www.rodoviasonline.com.br/cameras-ao-vivo-viapar-parana/

</details>

### Câmeras Concessionária Tamoios

<details>
<summary>concessionariatamoios.com.br</summary>

- https://concessionariatamoios.com.br/cameras/ver/12
- https://concessionariatamoios.com.br/cameras/ver/14
- https://concessionariatamoios.com.br/cameras/ver/10
- https://concessionariatamoios.com.br/cameras/ver/9
- https://concessionariatamoios.com.br/cameras/ver/8
- https://concessionariatamoios.com.br/cameras/ver/13

</details>

### Câmeras Concessionária EcoRodovias

<details>
<summary>ecovias.com.br</summary>

- https://www.ecovias.com.br/condicoes-da-via#condition-camera
  - BALANCA IMIGRANTES PLANALTO
    - https://www.ecovias.com.br/boletim/camera/2
  - ENTRADA IMIGRANTES PLANALTO
    - http://site.ecovias.com.br/cameras/vpon/0kamera1.jpg
  - PEDAGIO IMIGRANTES
    - https://www.ecovias.com.br/boletim/camera/4
  - PLANALTO IMIGRANTES
    - http://site.ecovias.com.br/cameras/vpon/0kamera6.jpg
  - TRECHO SERRA IMIGRANTES
    - https://www.ecovias.com.br/boletim/camera/6
  - BALANCA IMIGRANTES BAIXADA
    - https://www.ecovias.com.br/boletim/camera/7
  - ACESSO IMIGRANTES BAIXADA
    - https://www.ecovias.com.br/boletim/camera/8
  - INTERLIGACAO PLANALTO
    - https://www.ecovias.com.br/boletim/camera/15
  - TREVO CUBATAO
    - https://www.ecovias.com.br/boletim/camera/1
  - ANCHIETA RIBEIRAO DOS COUROS
    - https://www.ecovias.com.br/boletim/camera/11
  - SERRA ANCHIETA
    - https://www.ecovias.com.br/boletim/camera/12
  - ANCHIETA TREVO DA VOLKSWAGEM
    - https://www.ecovias.com.br/boletim/camera/13
  - PEDAGIO ANCHIETA
    - https://www.ecovias.com.br/boletim/camera/14
  - ENTRADA SANTOS
    - https://www.ecovias.com.br/boletim/camera/16
  - PEDAGIO GUARUJA
    - https://www.ecovias.com.br/boletim/camera/9
  - PEDAGIO SAO VICENTE
    - https://www.ecovias.com.br/boletim/camera/10

</details>

### Câmeras DAER - Rio Grande do Sul

- https://daer.kopp.com.br/ftp/imagem.php?id=Santa_Maria

### Câmeras Governo de Santa Catarina

<details>
<summary>ssp.sc.gov.br</summary>

- https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online
- https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-florianopolis
- https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-florianopolis-trindade
- https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-florianopolis-2
- https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-sao-jose
- https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-biguacu

</details>

### Câmeras por Estado
Câmeras de monitoramento de rodovias, segurança pública e clima por estado.

<details>
<summary>Câmeras por Estado</summary>

**Maranhão (MA)**
- São Luis - https://www.climaaovivo.com.br/ma/sao-luis-hotel-abbeville
- Açailândia - https://www.climaaovivo.com.br/ma/acailandia/acailandia
- Imperatriz - https://www.climaaovivo.com.br/ma/imperatriz/centro-empresarial-oeste
- Imperatriz - https://www.climaaovivo.com.br/ma/imperatriz/centro-empresarial-leste

**Rio Grande do Sul (RS)**
- Localizar pessoas desaparecidas nas enchentes do RS - https://www.achados-e-perdidos-rs.com.br/
- Osório: RS-389 KM 14 - https://camerasdaer.perkons.com:60000/DAER-6716
- Osório: ERS-030 KM 89,9 - https://camerasdaer.perkons.com:60000/DAER-6714
- Osório: ERS-030, 1916 KM 85,3 - https://camerasdaer.perkons.com:60000/DAER-6713
- Restinga Seca: ERS-149 KM 100 - https://daer.kopp.com.br/ftp/imagem.php?id=Restinga_Seca
- Ijuí: ERS-155 KM 2,3 - https://daer.kopp.com.br/ftp/imagem.php?id=Ijui
- Santa Maria: ERS-509 KM 4,1 - https://daer.kopp.com.br/ftp/imagem.php?id=Santa_Maria
- Venâncio Aires: RSC-453 KM 4,1 - https://daer.kopp.com.br/ftp/imagem.php?id=Venancio_Aires
- Montenegro: ERS-124 KM 29,6 - https://daer.kopp.com.br/ftp/imagem.php?id=Montenegro01
- Montenegro: RSC-287 KM 3,4 - https://daer.kopp.com.br/ftp/imagem.php?id=Montenegro02
- Montenegro: RSC-287 KM 8 - https://daer2.fiscaltech.com.br:8843/panoramicas/6208.jpg
- Portão: ERS-240 KM 9,9 - https://daer.kopp.com.br/ftp/imagem.php?id=Portao
- São Jerônimo: ERS-401 KM 10,3 - https://daer.kopp.com.br/ftp/imagem.php?id=Sao_Jeronimo
- Farroupilha: RSC-453 KM 121,3 - https://daer.kopp.com.br/ftp/imagem.php?id=Farroupilha
- Farroupilha: RSC-453 KM 109 - https://daer2.fiscaltech.com.br:8843/panoramicas/6212.jpg
- Farroupilha: ERS-122 KM 47 - https://daer2.fiscaltech.com.br:8843/panoramicas/6213.jpg
- Caxias do Sul: RSC-453 KM 143 - https://daer.kopp.com.br/ftp/imagem.php?id=Caxias_do_Sul
- Caxias do Sul: ERS-122 KM 66,56 - https://camerasdaer.perkons.com:60000/DAER-6743
- Caxias do Sul: RSC-453 KM 168,36 - https://camerasdaer.perkons.com:60000/DAER-6744
- Glorinha: ERS-030 KM 24,2 - https://daer.kopp.com.br/ftp/imagem.php?id=Glorinha
- Igrejinha: ERS-115 KM 115 - https://daer.kopp.com.br/ftp/imagem.php?id=Igrejinha
- Gramado: ERS-235 KM 36,6 - https://daer.kopp.com.br/ftp/imagem.php?id=Gramado01
- Gramado: ERS-235 KM 36,6 - https://daer.kopp.com.br/ftp/imagem.php?id=Gramado02
- Itati: ERS-486 KM 29,7 - https://daer.kopp.com.br/ftp/imagem.php?id=Itati
- Candelária: RSC-287 KM 135 - https://daer2.fiscaltech.com.br:8843/panoramicas/6210.jpg
- Boa Vista do Cadeado: ERS-342 KM 137 - https://daer2.fiscaltech.com.br:8843/panoramicas/6214.jpg
- Vera Cruz: RSC-287 KM 113 - https://daer2.fiscaltech.com.br:8843/panoramicas/6215.jpg
- Passo Fundo: ERS-324 KM 195 - https://daer2.fiscaltech.com.br:8843/panoramicas/6216.jpg
- Passo Fundo: ERS-324 KM 182,4 - http://186.227.239.150:2150/ftp/imagem.php?id=Passo_Fundo
- Novos Cabrais: RSC-287 KM 166 - https://daer2.fiscaltech.com.br:8843/panoramicas/6211.jpg
- Capão da Canoa: ERS-389 KM 36,9 - https://camerasdaer.perkons.com:60000/DAER-6718
- Torres: ERS-389 KM 86,1 - https://camerasdaer.perkons.com:60000/live/media/PK5916/DeviceIpint.6/SourceEndpoint.video:0:0
- Parobé: ERS-239 KM 42,3 - https://191.253.194.194:60000/live/media/PK5916/DeviceIpint.7/SourceEndpoint.video:0:0
- Sapiranga: ERS-239 KM 32 - https://191.253.194.194:60000/live/media/PK5916/DeviceIpint.8/SourceEndpoint.video:0:0
- São Leopoldo: ERS-240 KM 2 - https://191.253.194.194:60000/live/media/PK5916/DeviceIpint.9/SourceEndpoint.video:0:0
- Capela de Santana: ERS-240 KM 22,1 - https://191.253.194.194:60000/live/media/PK5916/DeviceIpint.10/SourceEndpoint.video:0:0
- São Sebastião do Caí: ERS-122 KM 6,5 - https://camerasdaer.perkons.com:60000/DAER-6734
- São Sebastião do Caí: ERS-122 KM 15,9 - https://camerasdaer.perkons.com:60000/DAER-6737
- Bom Princípio: ERS-122 KM 29,45 - https://camerasdaer.perkons.com:60000/DAER-6739
- Teutônia: RSC-453 KM 55,8 - https://camerasdaer.perkons.com:60000/DAER-6748
- Serafina Côrrea: ERS-129 KM 147,2 - https://daer.kopp.com.br/ftp/imagem.php?id=Serafina_Correa
- Nova Bassano: ERS- 324 KM 282,7 - https://daer.kopp.com.br/ftp/imagem.php?id=Nova_Bassano
- Sananduva: ERS-126 KM 110 - https://daer.kopp.com.br/ftp/imagem.php?id=Sananduva
- Estação: ERS-135 KM 48,4 - https://daer2.fiscaltech.com.br:8843/panoramicas/6204.jpg
- Viamão: ERS-040 KM 14 - https://camerasdaer.perkons.com:60000/DAER-6712

**Santa Catarina (SC)**
- Ponte Hercílio Luz 01: Santa Catarina - https://bemtevi.segurancapublica.sc.gov.br:10346/Interface/Cameras/GetJPEGStream?Camera=FNS_CEN_159&width=1920&height=1080
- Ponte Hercílio Luz 02: Santa Catarina - https://bemtevi.segurancapublica.sc.gov.br:10346/Interface/Cameras/GetJPEGStream?Camera=FNS_CEN_160&width=1920&height=1080
- Ponte Hercílio Luz 03: Santa Catarina - https://bemtevi.segurancapublica.sc.gov.br:10346/Interface/Cameras/GetJPEGStream?Camera=FNS_CEN_162&width=1920&height=1080
- Ponte Hercílio Luz 04: Santa Catarina - https://bemtevi.segurancapublica.sc.gov.br:10346/Interface/Cameras/GetJPEGStream?Camera=FNS_CEN_162&width=1920&height=1080
- Lauro Linhares/Álvaro Ramos: Trindade - http://bemtevi.segurancapublica.sc.gov.br:10351/Interface/Cameras/GetJPEGStream?Camera=FNS_STM_051&width=1920&height=1080
- Lauro Linhares/Álvaro Ramos 02: Trindade - http://bemtevi.segurancapublica.sc.gov.br:10351/Interface/Cameras/GetJPEGStream?Camera=FNS_STM_052&width=1920&height=1080
- Lauro Linhares/Travessa São Lourenço 01: Trindade - http://bemtevi.segurancapublica.sc.gov.br:10351/Interface/Cameras/GetJPEGStream?Camera=FNS_STM_061&width=1920&height=1080
- Lauro Linhares/Travessa São Lourenço 02: Trindade - http://bemtevi.segurancapublica.sc.gov.br:10351/Interface/Cameras/GetJPEGStream?Camera=FNS_STM_062&width=1920&height=1080
- Rua 13 de Maio/Sebastião Lara: Biguaçú - https://bemtevi.segurancapublica.sc.gov.br:10311/Interface/Cameras/GetJPEGStream?Camera=BGC_CEN_012&width=1920&height=1080
- Rua Júlio T. Martins/Homero de Miranda Gome: Biguaçú - https://bemtevi.segurancapublica.sc.gov.br:10311/Interface/Cameras/GetJPEGStream?Camera=BGC_CEN_020&width=1920&height=1080
- Marginal BR101/Rua Acácio Reitz: Biguaçú - https://bemtevi.segurancapublica.sc.gov.br:10311/Interface/Cameras/GetJPEGStream?Camera=BGC_CEN_032&width=1920&height=1080
- Major Livramento/Rua João José Rodrigues: Biguaçú - https://bemtevi.segurancapublica.sc.gov.br:10311/Interface/Cameras/GetJPEGStream?Camera=BGC_VDV_040&width=1920&height=1080

</details>

### Câmeras da Prefeitura de João Pessoa - PB (SEMOB)

- http://transito.gtrans.com.br/semobjp/index.php

### Câmeras da Prefeitura de Recife - PE (CTTU)

- http://transito.gtrans.com.br/cttupe/index.php/mapa

### Câmeras do Centro Integrado de Operações de Belém do Pará (Segup no Trânsito)

- [https://www.ciop.pa.gov.br/aovivo/index.html](https://www.ciop.pa.gov.br/aovivo/index.html)

### Câmeras da BHTRANS (Em beta ainda)

- http://infotrafego.pbh.gov.br/info_trafego_cameras.html

### Câmeras do Aeroporto Internacional de São Paulo/Guarulhos - SGBR

- https://www.youtube.com/@SBGRLIVE
- https://www.youtube.com/@GolfOscarRomeo

### Câmera do Aeroporto de Congonhas São Paulo - SBSP FULL ATC

- https://www.youtube.com/@GolfOscarRomeo

### Câmera do Aeroporto Santos Dumont - Rio de Janeiro - SBRJ FULL ATC

- https://www.youtube.com/@avtv

### Câmera do Aeroporto Galeão - Rio de Janeiro - SBGL

- https://www.youtube.com/@avtv

### Câmera do Aeroporto Pinto Martins - Fortaleza - SBFZ

- https://www.youtube.com/@mundo_aviao

### Câmera do Aeroporto Internacional de Florianópolis - SBFL Com Fonia

- https://www.youtube.com/@maaxcamaovivo

### Câmera do Aeroporto da Pampulha - Belo Horizonte 24 horas (BHZ)(SBBH)

- ...

### Câmera do Aeroporto Guararapes - Recife - SBRF

- https://www.youtube.com/@papacharliegolfTV

### Câmera do Aeroporto Viracopos - Campinas - VCP

- https://www.youtube.com/@ViracoposFullHD

### Câmeras de Obras em Andamento de Mato Grosso (SINFRA)

- https://mapas.sinfra.mt.gov.br/portal/apps/sites/#/central-infra-20-2-1/pages/monitoramento-de-obras

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Ministérios Públicos e Defensorias Públicas ⚖️ <a name="ministerios-publicos-defensorias"></a>

### Ministérios Públicos Estaduais
Instituições responsáveis pela defesa da ordem jurídica, do regime democrático e dos interesses sociais.

<details>
<summary>Ministérios Públicos por Estado</summary>

**Acre (AC)**
- Portal: https://www.mpac.mp.br/

**Amazonas (AM)**
- Portal: https://www.mpam.mp.br/

**Maranhão (MA)**
- Portal: https://www.mpma.mp.br/

**Mato Grosso do Sul (MS)**
- Portal: https://www.mpms.mp.br/

**Pará (PA)**
- Portal: https://www2.mppa.mp.br/

**Paraná (PR)**
- Portal: https://www.mppr.mp.br/

**Rio de Janeiro (RJ)**
- Portal: https://www.mprj.mp.br/

**Rio Grande do Norte (RN)**
- Portal: https://www.mprn.mp.br/

**Rio Grande do Sul (RS)**
- Portal: https://www.mprs.mp.br/

**Santa Catarina (SC)**
- Portal: https://www.mpsc.mp.br/

**Sergipe (SE)**
- Portal: https://www.mpse.mp.br/

</details>

### Defensorias Públicas
Instituições que prestam assistência jurídica gratuita aos cidadãos que não podem pagar por advogado.

<details>
<summary>Defensorias por Estado e União</summary>

**Defensoria Pública da União (DPU)**
- Portal: https://www.dpu.def.br/

**Bahia (BA)**
- Portal: https://www.defensoria.ba.def.br/

**Ceará (CE)**
- Portal: https://www.defensoria.ce.def.br/

**Espírito Santo (ES)**
- Portal: https://www.defensoria.es.def.br/

**Pará (PA)**
- Portal: https://www.defensoria.pa.def.br/

**Paraná (PR)**
- Portal: https://www.defensoriapublica.pr.def.br/

**Rio de Janeiro (RJ)**
- Portal: https://www.defensoria.rj.def.br/

**São Paulo (SP)**
- Portal: https://www.defensoria.sp.def.br/

</details>

### Disque Denúncia e Segurança Pública
Canais para denúncias anônimas e informações sobre segurança pública.

<details>
<summary>Portais por Estado</summary>

**Disque Denúncia Rio de Janeiro**
- Portal: https://www.disquedenuncia.org.br/

**SSP-SP - Disque Denúncia São Paulo**
- Portal: https://www.ssp.sp.gov.br/disque-denuncia

**Espírito Santo - Disque Denúncia**
- Portal: https://www.es.gov.br/disquedenuncia

</details>

### Polícias Estaduais
Órgãos de segurança pública responsáveis pela investigação e prevenção de crimes.

<details>
<summary>Polícias por Estado</summary>

**Minas Gerais**
- Polícia Civil MG: https://www.policiacivil.mg.gov.br/

**São Paulo**
- Polícia Científica SP: https://www.policiacientifica.sp.gov.br/

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Segurança Cibernética 🛡️ <a name="seguranca-cibernetica"></a>

### CERT.br - Centro de Estudos, Resposta e Tratamento de Incidentes
Notificações de incidentes, estatísticas de segurança e alertas de vulnerabilidades.
- https://www.cert.br/
- https://www.cert.br/stats/ (Estatísticas)

### Delegacias de Crimes Cibernéticos
<details>
<summary>Delegacias Especializadas por Estado</summary>

- São Paulo - https://www.policiacivil.sp.gov.br/portal/faces/pages_home/cidadao/delegacias_especializadas
- Rio de Janeiro - http://www.policiacivil.rj.gov.br/
- Minas Gerais - https://www.policiacivil.mg.gov.br/
- Paraná - https://www.policiacivil.pr.gov.br/
- Rio Grande do Sul - https://www.pc.rs.gov.br/
- Santa Catarina - https://www.pc.sc.gov.br/

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Outras Buscas 🔎 <a name="outras-buscas"></a>

### MCTI - Ministério da Ciência, Tecnologia e Inovação
Portal oficial do Ministério com informações sobre políticas de ciência, tecnologia e inovação.
- https://www.gov.br/mcti/pt-br

### Embrapii - Unidades de Pesquisa e Inovação
Consulta de unidades credenciadas da Empresa Brasileira de Pesquisa e Inovação Industrial.
- https://embrapii.org.br/unidades/

### Finep - Financiadora de Estudos e Projetos
Portal da agência de fomento à inovação com informações sobre editais, financiamentos e projetos.
- http://www.finep.gov.br/

### IBRE - Instituto Brasileiro de Economia (FGV)
Portal com indicadores econômicos, pesquisas e análises do Instituto Brasileiro de Economia da FGV.
- https://portalibre.fgv.br/

### SUFRAMA - Superintendência da Zona Franca de Manaus
Portal oficial da Suframa com informações sobre a Zona Franca de Manaus, incentivos fiscais e projetos aprovados.
- https://www.gov.br/suframa/pt-br

### Banco Central - Cadastro Positivo
Informações sobre o Cadastro Positivo e consulta de bureaus de crédito autorizados.
- https://www.bcb.gov.br/estabilidadefinanceira/cadastropositivo

### Antecedentes Criminais

- https://servicos.dpf.gov.br/antecedentes-criminais/certidao

### Sinesp Cidadão (Site a APP)

- Consultar informações sobre: Veículos, Mandados de prisão, Pessoas desaparecidas, Criminosos procurados
- https://seguranca.sinesp.gov.br/sinesp-seguranca/login.jsf

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

### Consulta Informações Sobre Domínios
Informações sobre proprietários de domínios brasileiros.

<details>
<summary>Links para Pesquisa</summary>

- https://registro.br/dominio/lista-processo-liberacao.txt
- https://rdap.registro.br/domain/seu_dominio_exemplo.com.br
- https://registro.br/tecnologia/ferramentas/whois/
- https://registro.br/tecnologia/ferramentas/pesquisa-de-usuario/
- https://kaponline.com.br/whois/
</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## APIs Públicas Brasileiras 🔌 <a name="apis-publicas"></a>

### BrasilAPI - APIs de Utilidades
Conjunto de APIs públicas e gratuitas com informações sobre CEP, CNPJ, bancos, feriados, ISBN, e outros dados brasileiros.
- https://brasilapi.com.br/
- Documentação: https://brasilapi.com.br/docs

**Recursos disponíveis:**
- Consulta de CEP
- Informações de bancos
- Códigos de cidades (IBGE)
- Feriados nacionais
- Tabela FIPE
- ISBN
- Taxas de câmbio

### ReceitaWS - API CNPJ
API gratuita para consulta de informações cadastrais de empresas brasileiras.

<details>
<summary>Informações da API</summary>

- **URL Base:** https://receitaws.com.br/v1/cnpj/
- **Autenticação:** Não requer
- **Rate Limit:** 3 requisições por minuto
- **Formato:** JSON

**Exemplo de uso:**
```bash
curl https://receitaws.com.br/v1/cnpj/00000000000191
```

**Retorna:**
- Razão social
- Nome fantasia
- CNAE
- Endereço completo
- Situação cadastral
- Lista de sócios
- Capital social

</details>

### ViaCEP - API de Consulta de CEP
API gratuita para consulta de endereços por CEP.

<details>
<summary>Informações da API</summary>

- **URL Base:** https://viacep.com.br/ws/
- **Autenticação:** Não requer
- **Formatos:** JSON, XML, JSONP
- **Limite:** Sem limite oficial

**Exemplo de uso:**
```bash
curl https://viacep.com.br/ws/01310100/json/
```

**Recursos:**
- Consulta por CEP
- Busca por endereço (UF, cidade, logradouro)

</details>

### Registro.br - API RDAP
Protocolo RDAP para consulta de informações sobre domínios .br.

<details>
<summary>Informações da API</summary>

- **URL Base:** https://rdap.registro.br/
- **Documentação:** https://registro.br/tecnologia/ferramentas/rdap/
- **Formato:** JSON

**Exemplo de uso:**
```bash
curl https://rdap.registro.br/domain/registro.br
```

**Retorna:**
- Titular do domínio
- Data de criação
- Data de expiração
- Nameservers
- Status do domínio

</details>

### IBGE - API de Serviços
APIs do IBGE para consulta de informações geográficas, estatísticas e de localidades.

<details>
<summary>Informações da API</summary>

- **Documentação:** https://servicodados.ibge.gov.br/api/docs
- **Autenticação:** Não requer
- **Formato:** JSON, XML

**Recursos principais:**
- Localidades (estados, municípios, distritos)
- Malhas geográficas
- Agregados do SIDRA
- Notícias e releases

**Exemplo - Listar estados:**
```bash
curl https://servicodados.ibge.gov.br/api/v1/localidades/estados
```

</details>

### Painel de Compras - API
Dados sobre licitações e compras governamentais do governo federal.
- https://paineldecompras.economia.gov.br/

### Querido Diário - API
API para busca em diários oficiais municipais.

<details>
<summary>Informações da API</summary>

- **Documentação:** https://queridodiario.ok.org.br/api/docs
- **URL Base:** https://queridodiario.ok.org.br/api/
- **Formato:** JSON

**Exemplo de uso:**
```bash
curl 'https://queridodiario.ok.org.br/api/gazettes?territory_id=3550308&since=2024-01-01'
```

</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Blockchain e Criptomoedas 💰 <a name="blockchain-criptomoedas"></a>

### CVM - Consulta de Processos Envolvendo Criptomoedas
Processos administrativos e sanções relacionadas a criptoativos.
- https://www.gov.br/cvm/pt-br

### CVM - Alertas sobre Fraudes com Criptomoedas
Comunicados oficiais sobre esquemas fraudulentos.
- https://www.gov.br/cvm/pt-br/assuntos/noticias

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Defesa Civil e Emergências 🚨 <a name="defesa-civil-emergencias"></a>

### Defesa Civil Nacional - Sistema de Alertas
Sistema nacional de alertas de desastres naturais.
- https://www.gov.br/mdr/pt-br/assuntos/protecao-e-defesa-civil

### S2iD - Sistema Integrado de Informações sobre Desastres
Registro e consulta de desastres e emergências no Brasil.
- https://s2id.mi.gov.br/

### CEMADEN - Centro Nacional de Monitoramento e Alertas
Monitoramento de risco de desastres naturais em tempo real.
- https://www.cemaden.gov.br/
- https://www.cemaden.gov.br/mapainterativo/ (Mapa interativo)

### ANA - Monitoramento de Secas e Inundações
Sistema de acompanhamento de eventos hidrológicos críticos.
- https://www.snirh.gov.br/
- https://portal1.snirh.gov.br/ana/apps/webappviewer/index.html?id=0d9d29ec24cc49df89965f05fc5b96b9

### Defesa Civil - Consulta de Abrigos Públicos
Localização de abrigos emergenciais por município.
- https://www.gov.br/mdr/pt-br/assuntos/protecao-e-defesa-civil/abrigos-temporarios

### Mapa de Áreas de Risco
Identificação de áreas suscetíveis a deslizamentos e inundações.
- https://www.cprm.gov.br/publique/Gestao-Territorial/Cartas-de-Suscetibilidade-a-Movimentos-Gravitacionais-de-Massa-e-Inundacoes-5511.html

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Energia e Infraestrutura ⚡ <a name="energia-infraestrutura"></a>

### ANEEL - Agência Nacional de Energia Elétrica
Consulta de usinas, distribuidoras e empreendimentos de geração de energia.
- https://www.aneel.gov.br/
- https://www.aneel.gov.br/siga (Sistema de Informações de Geração)

### ANEEL - Consulta de Distribuidoras
Informações sobre concessionárias de distribuição de energia.
- https://www.aneel.gov.br/area.cfm?idArea=550

### ANEEL - Consulta de Usinas e Geradoras
Banco de dados de empreendimentos de geração de energia elétrica.
- https://www2.aneel.gov.br/aplicacoes/capacidadebrasil/capacidadebrasil.cfm

### ONS - Operador Nacional do Sistema Elétrico
Dados operacionais do sistema elétrico brasileiro em tempo real.
- http://www.ons.org.br/
- http://www.ons.org.br/paginas/resultados-da-operacao/historico-da-operacao

### EPE - Empresa de Pesquisa Energética
Dados e estatísticas do setor energético brasileiro.
- https://www.epe.gov.br/pt
- https://www.epe.gov.br/pt/publicacoes-dados-abertos

### Mapa de Linhas de Transmissão
Visualização de linhas de transmissão e subestações do Brasil.
- http://sigel.aneel.gov.br/portal/home/

### Consulta de Interrupções de Energia
Sistema de registro e acompanhamento de apagões e interrupções.
- https://www.aneel.gov.br/ranking-da-continuidade

### Tarifa de Energia - Simulador
Comparação de tarifas de energia elétrica por região.
- https://www.aneel.gov.br/ranking-das-tarifas

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Serviços Públicos Estaduais e Conselhos Profissionais 🏛️ <a name="servicos-estaduais"></a>

### Conselhos Profissionais Nacionais
Consultas de registro profissional e certidões em conselhos federais e regionais.

<details>
<summary>Conselhos de Medicina (CRM)</summary>

**CREMESP - Conselho Regional de Medicina do Estado de São Paulo**
- Portal: https://www.cremesp.org.br/

**CRM-PR - Conselho Regional de Medicina do Paraná**
- Portal: https://www.crmpr.org.br/

**CREMEB - Conselho Regional de Medicina da Bahia**
- Portal: https://www.cremeb.org.br/

</details>

<details>
<summary>Conselhos de Enfermagem (COREN)</summary>

**COFEN - Conselho Federal de Enfermagem**
- Portal: https://www.cofen.gov.br/

**COREN-RJ - Conselho Regional de Enfermagem do Rio de Janeiro**
- Portal: https://www.coren-rj.org.br/

</details>

<details>
<summary>Outros Conselhos Profissionais</summary>

**CFP - Conselho Federal de Psicologia**
- Portal: https://site.cfp.org.br/

**COFFITO - Conselho Federal de Fisioterapia e Terapia Ocupacional**
- Portal: https://www.coffito.gov.br/nsite/

</details>

### Serviços Públicos por Estado
Portais de serviços públicos, conselhos profissionais e outras instituições estaduais.

<details>
<summary>Consultas por Estado</summary>

**Espírito Santo (ES)**
- Acesso Cidadão - Portal de serviços digitais estaduais (processos, notas fiscais, agendamentos) - https://acessocidadao.es.gov.br/
- IDE Geobases - Infraestrutura de Dados Espaciais - https://ide.geobases.es.gov.br/?limit=5&offset=0

**Maranhão (MA)**
- Serviços disponíveis TRE | Maranhão - https://www.tre-ma.jus.br/institucional/servicos-disponiveis
- Serviços disponíveis TRT | Maranhão - https://www.trt16.jus.br/servicos/para-o-cidadao-e-advogado
- Serviços disponíveis MP | Maranhão - https://www.mpma.mp.br/servicos/
- Serviços disponíveis TJ | Maranhão - https://www.tjma.jus.br/portal
- Serviços disponíveis DETRAN | Maranhão - https://www.detran.ma.gov.br/inicio/paginas/Home.xhtml
- Serviços disponíveis Assembleia legislativa | Maranhão - https://www.al.ma.leg.br/sitealema/
- Sistema S | Maranhão - https://www.fiema.org.br/home
- OAB | Maranhão - https://www.oabma.org.br/
- FAM | Maranhão - https://famem.org.br/
- Serviços disponíveis GOV | Maranhão - https://www.ma.gov.br/servicos/
- Contatos do GOV | Maranhão - https://www.ma.gov.br/contatos
- Diário Oficial GOV | Maranhão - https://www.diariooficial.ma.gov.br/

**Maranhão (MA) - São Luís**
- Serviços disponíveis Prefeitura | São Luís - https://saoluis.ma.gov.br/servicos
- Informações de Secretarias e Órgãos da prefeitura | São Luís - https://saoluis.ma.gov.br/secretarias

**Maranhão (MA) - São José de Ribamar**
- Serviços disponíveis Prefeitura | São José de Ribamar - https://www.saojosederibamar.ma.gov.br/servicos
- Informações de Secretarias e Órgãos da prefeitura | São José de Ribamar - https://www.saojosederibamar.ma.gov.br/detalhe-da-materia/info/secretarias/16510

**Piauí (PI)**
- Sistema Intranet Corpo de Bombeiros Militar do Piauí - http://www.bombeiros.pi.gov.br/distec/index2.php

**São Paulo (SP)**
- Consulta Situação RG - https://www.policiacivil.sp.gov.br/portal/faces/pages_home/servicos/consultaSituacaoRG
- Consulta de concluintes em unidades escolares do Estado - https://concluintes.educacao.sp.gov.br/publica/consultapublica/Search

</details>

### Conselhos Profissionais do Maranhão
Consultas de registro e certidões em conselhos profissionais do Maranhão.

<details>
<summary>Conselhos Maranhão</summary>

- CRMMA (Medicina) - https://crmma.org.br/servicos-para-medicos/certidoes-declaracoes/certidao-negativa-nada-consta
- CRFMA (Farmácia) - https://crfma.org.br/
- CREAMA (Engenharia e Agronomia) - https://www.creama.org.br/
- CRPMA (Psicologia) - https://crpma.org.br/
- CREFMA (Educação Física) - https://cref21.org.br/
- CRAMA (Administração) - https://cra-ma.org.br/
- COREMA (Representantes Comerciais) - https://www.coremaranhao.org.br/
- CORENMA (Enfermagem) - https://corenma.gov.br/site2/
- CEEM (Educação) - https://conselhodeeducacao.ma.gov.br/
- CRCMA (Contabilidade) - https://crcma.org.br/
- CRTMA (Técnicos Industriais) - https://www.crt02.gov.br/maranhao/
- CRQMA (Química) - https://crq11.org.br/
- CRESSMA (Serviço Social) - https://www.cressma.org.br/
- CROMA (Museologia) - https://www.croma.org.br/
- CFCMA (Contabilidade) - https://cfc.org.br/conselhos/conselho-regional-de-contabilidade-do-maranhao/
- CRMVMA (Medicina Veterinária) - https://www.crmvma.org.br/
- CRTRMA (Técnicos em Radiologia) - https://crtr17.gov.br/
- CORECON (Economia) - https://corecon-ma.org.br/
- CRBMMA (Biomedicina) - https://crbm2.gov.br/
- CRNMA (Nutrição) - https://crbm2.gov.br/

</details>

### Empresas de Serviços Públicos do Maranhão
Consultas de serviços essenciais do Maranhão.

<details>
<summary>Serviços Maranhão</summary>

- CAEMA (Água) - https://www.caema.ma.gov.br/
- EQUATORIAL (Energia) - https://ma.equatorialenergia.com.br/
- BRK (Saneamento) - https://minhabrk.com.br/home

</details>

### Consulta de Empresa - Junta Comercial Pará (JUCEPA)
Consulta pública de empresas registradas na JUCEPA.
- https://integrador.jucepa.pa.gov.br/projetos/usuario/consulta_empresa_site

### Consulta de Processo Administrativo Eletrônico - Pará
Sistema de consulta pública de processos administrativos eletrônicos do estado do Pará.
- https://pae-consulta-publica.sistemas.pa.gov.br/

### Boletim Geral de Bombeiros - Pará
Consulta pública de boletins do Corpo de Bombeiros do Pará.
- https://siga.bombeiros.pa.gov.br/boletins.php

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Outras Buscas 🔎 <a name="outras-buscas"></a>

### Busca de Falecidos/Óbitos

- https://www.falecidosnobrasil.org.br/

### Consulta de Embarcações Navais 🛥️

- https://www.mercante.transportes.gov.br/g36127/html/Manife/EmbarcConsul.html?noCampo=cdIrin

### Estatísticas de Nascimentos, Óbitos, Registros e Casamentos

- https://transparencia.registrocivil.org.br/registros

### Empresas de Segurança Privada

- https://www.gov.br/pf/pt-br/assuntos/seguranca-privada

### Consulta de Registro, Licença e Controle de Produtos Quimicos

- https://www.gov.br/pf/pt-br/assuntos/produtos-quimicos

### Informações sobre um endereço de e-mail

Permite recuperar, sem notificar o usuário, vários elementos relacionados a um endereço de e-mail, Nome, GoogleID, se há Mapas criados ou Agendas Públicas do Google Calendar, Validar se o e-mail está sendo utilizado em contas em outros sites.

<details>
<summary>Links de pesquisa</summary>

- https://www.predictasearch.com
- https://tools.epieos.com/email.php

</details>

### Busca de Bens a venda ou aluguel

<details>
<summary>Links de pesquisa</summary>

- https://www.olx.com.br/
- https://www.estantevirtual.com.br/
- https://www.enjoei.com.br/
- https://www.repassa.com.br/
- https://www.pegueibode.com.br/
- https://www.ficoupequeno.com/
- https://www.facebook.com/marketplace/?locale=pt_BR
- https://www.mercadolivre.com.br/
- https://www.elo7.com.br/
- https://shopee.com.br/
- https://napista.com.br/
- https://autoline.com.br/
- https://www.kavak.com/br
- https://www.webmotors.com.br/

</details>

### Conhecimento de empreendimentos por dentro

<details>
<summary>Links de pesquisa</summary>

- https://www.vrbo.com/pt-br/
- https://www.airbnb.com.br/
- https://www.quintoandar.com.br/
- https://www.trivago.com.br/
- https://www.tripadvisor.com.br/
- https://www.booking.com/index.pt-br.html
</details>
        
### Sites Notificados pelo Procon-SP

Lista de sites que devem ser evitados, pois tiveram reclamações de consumidores registrada no Procon-SP, foram notificados, não responderam ou não foram encontrados.

- https://sistemas.procon.sp.gov.br/evitesite/list/evitesites.php

### Consulta em cartórios

<details>
<summary>Links de pesquisa</summary>

  - https://www.pesquisaprotesto.com.br/
  - https://protestosp.com.br/consulta-de-protesto?hc=1
  - https://e-cartoriodobrasil.com/pedido/imoveis/pesquisa-qualificada-de-bens
</details>


### Lista Telefônica

- https://www.telenumeros.com/

### Consulta no Instituto Nacional da Propriedade Industrial (INPI)

No link abaixo é possível consultar informações referentes a: Marcas, Patentes, Desenhos Industriais, Patentes Tecnológicas, dentre outras áreas.

- https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login

### Consulta de Licitações, Contratos e Compras Públicas

<details>
<summary>Links de pesquisa</summary>
- https://alertalicitacao.com.br/
- https://www.portaldecompraspublicas.com.br/18/Processos/
- http://www.portaltransparencia.gov.br/

</details>

### Consulta os Processos Licitatórios da SPTrans

Acompanhe os processos licitatórios instaurados pela São Paulo Transporte S/A
Acompanhe os processos licitatórios instaurados pela São Paulo Transporte S/A. Sistema permite consultar editais, resultados, atas e processos administrativos relacionados a licitações e contratos.

<details>
<summary>Links para Pesquisa</summary>

- Portal de Licitações SPTrans
  - https://sptrans.com.br/licitacoes/

- Consulta de Resultados de Licitações por Ano
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrt2rc_Ano.aspx

- Consulta de Atas de Registro de Preços
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrtarp.aspx

- Consulta de Avisos de Prorrogação
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrtap.aspx

- Consulta de Contratos Administrativos
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrt2ca.aspx

- Consulta de Convênios e Termos de Cooperação
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrtcp_tc.aspx

- Consulta de Contratos de Parceria
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrtcp.aspx

- Consulta de Contratos Rescindidos
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrt2cr.aspx

- Consulta de Editais
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrted.aspx

- Consulta de Extrato de Contratos
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrt2ec.aspx

- Consulta de Avisos de Prorrogação (Novo)
  - https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrt2apn.aspx

- Editais da Secretaria de Mobilidade
  - https://www.prefeitura.sp.gov.br/cidade/secretarias/mobilidade/edital/index.php?p=247319

- Demonstrativo de Pagamentos
  - https://sistemas.sptrans.com.br/DemPag/hdempag.aspx

</details>

### Acesso à Informação - SPTrans
Portal de acesso à informação da São Paulo Transporte S/A com dados sobre contratos, despesas, licitações e transparência.
- https://www.prefeitura.sp.gov.br/cidade/secretarias/mobilidade/institucional/sptrans/acesso_a_informacao/index.php

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)

---

## Categorias de Domínios .br 📰 <a name="dominios-br"></a>

Abaixo estão listadas todas as categorias de domínio .br oferecidas pelo Registro.br. Os domínios de pessoa física e profissionais liberais só podem ser registrados por um titular com CPF. Os domínios de pessoa jurídica devem ser associados a um CNPJ. Já os domínios genéricos e de cidades podem ser registrados por CPF ou CNPJ.

<details>
<summary>Lista de Domínios</summary>

  | TLD              | Destinado a            | Descrição                                                              |
  | ---------------- | ---------------------- | ---------------------------------------------------------------------- | 
  | APP.BR           | Genéricos              | Aplicativos                                                            |
  | ART.BR           | Genéricos              | Artes: música, pintura, folclore                                       |
  | COM.BR           | Genéricos              | Atividades comerciais                                                  |
  | DEV.BR           | Genéricos              | Desenvolvedores e Plataformas de Desenvolvimento                       |
  | ECO.BR           | Genéricos              | Atividades com foco eco-ambiental                                      |
  | EMP.BR           | Genéricos              | Pequenas e micro-empresas                                              |
  | LOG.BR           | Genéricos              | Transportes e Logistica                                                |
  | NET.BR           | Genéricos              | Atividades comerciais                                                  |
  | ONG.BR           | Genéricos              | Atividades não governamentais individuais ou associativas              |
  | SEG.BR           | Genéricos              | Segurança                                                              |
  | TEC.BR           | Genéricos              | Tecnologia                                                             |
  | EDU.BR           | Universidades          | Instituições de ensino superior                                        |
  | BLOG.BR          | Pessoas Físicas        | Web logs                                                               |
  | FLOG.BR          | Pessoas Físicas        | Foto logs                                                              |
  | NOM.BR           | Pessoas Físicas        | Pessoas Físicas                                                        |
  | VLOG.BR          | Pessoas Físicas        | Vídeo logs                                                             |
  | WIKI.BR          | Pessoas Físicas        | Páginas do tipo 'wiki'                                                 |
  | ADM.BR           | Profissionais Liberais | Administradores                                                        |
  | ADV.BR           | Profissionais Liberais | Advogados                                                              |
  | ARQ.BR           | Profissionais Liberais | Arquitetos                                                             |
  | ATO.BR           | Profissionais Liberais | Atores                                                                 |
  | BIB.BR           | Profissionais Liberais | Bibliotecários / Biblioteconomistas                                    |
  | BIO.BR           | Profissionais Liberais | Biólogos                                                               |
  | BMD.BR           | Profissionais Liberais | Biomédicos                                                             |
  | CIM.BR           | Profissionais Liberais | Corretores                                                             |
  | CNG.BR           | Profissionais Liberais | Cenógrafos                                                             |
  | CNT.BR           | Profissionais Liberais | Contadores                                                             |
  | COZ.BR           | Profissionais Liberais | Profissionais de Gastronomia                                           |
  | DES.BR           | Profissionais Liberais | "Designers" e Desenhistas                                              |
  | DET.BR           | Profissionais Liberais | Detetives / Investigadores Particulares                                |
  | ECN.BR           | Profissionais Liberais | Economistas                                                            |
  | ENF.BR           | Profissionais Liberais | Profissionais de Enfermagem                                            |
  | ENG.BR           | Profissionais Liberais | Engenheiros                                                            |
  | ETI.BR           | Profissionais Liberais | Especialista em Tecnologia da Informação                               |
  | FND.BR           | Profissionais Liberais | Fonoaudiólogos                                                         |
  | FOT.BR           | Profissionais Liberais | Fotógrafos                                                             |
  | FST.BR           | Profissionais Liberais | Fisioterapeutas                                                        |
  | GEO.BR           | Profissionais Liberais | Geólogos                                                               |
  | GGF.BR           | Profissionais Liberais | Geógrafos                                                              |
  | JOR.BR           | Profissionais Liberais | Jornalistas                                                            |
  | LEL.BR           | Profissionais Liberais | Leiloeiros                                                             |
  | MAT.BR           | Profissionais Liberais | Matemáticos e Estatísticos                                             |
  | MED.BR           | Profissionais Liberais | Médicos                                                                |
  | MUS.BR           | Profissionais Liberais | Músicos                                                                |
  | NOT.BR           | Profissionais Liberais | Notários                                                               |
  | NTR.BR           | Profissionais Liberais | Nutricionistas                                                         |
  | ODO.BR           | Profissionais Liberais | Dentistas                                                              |
  | PPG.BR           | Profissionais Liberais | Publicitários e profissionais da área de propaganda e marketing        |
  | PRO.BR           | Profissionais Liberais | Professores                                                            |
  | PSC.BR           | Profissionais Liberais | Psicólogos                                                             |
  | QSL.BR           | Profissionais Liberais | Rádio amadores                                                         |
  | REP.BR           | Profissionais Liberais | Representantes Comerciais                                              |
  | SLG.BR           | Profissionais Liberais | Sociólogos                                                             |
  | TAXI.BR          | Profissionais Liberais | Taxistas                                                               |
  | TEO.BR           | Profissionais Liberais | Teólogos                                                               |
  | TRD.BR           | Profissionais Liberais | Tradutores                                                             |
  | VET.BR           | Profissionais Liberais | Veterinários                                                           |
  | ZLG.BR           | Profissionais Liberais | Zoólogos                                                               |
  | 9GUACU.BR        | Cidades                | Nova Iguaçu                                                            |
  | ABC.BR           | Cidades                | Região ABC Paulista                                                    |
  | AJU.BR           | Cidades                | Aracaju                                                                |
  | ANANI.BR         | Cidades                | Ananindeua                                                             |
  | APARECIDA.BR     | Cidades                | Aparecida                                                              |
  | BARUERI.BR       | Cidades                | Barueri                                                                |
  | BELEM.BR         | Cidades                | Belém                                                                  |
  | BHZ.BR           | Cidades                | Belo Horizonte                                                         |
  | BOAVISTA.BR      | Cidades                | Boa Vista                                                              |
  | BSB.BR           | Cidades                | Brasília                                                               |
  | CAMPINAGRANDE.BR | Cidades                | Campina Grande                                                         |
  | CAMPINAS.BR      | Cidades                | Campinas                                                               |
  | CAXIAS.BR        | Cidades                | Caxias                                                                 |
  | CONTAGEM.BR      | Cidades                | Contagem                                                               |
  | CUIABA.BR        | Cidades                | Cuiabá                                                                 |
  | CURITIBA.BR      | Cidades                | Curitiba                                                               |
  | FEIRA.BR         | Cidades                | Feira de Santana                                                       |
  | FLORIPA.BR       | Cidades                | Florianópolis                                                          |
  | FORTAL.BR        | Cidades                | Fortaleza                                                              |
  | FOZ.BR           | Cidades                | Foz do Iguaçu                                                          |
  | GOIANIA.BR       | Cidades                | Goiânia                                                                |
  | GRU.BR           | Cidades                | Guarulhos                                                              |
  | JAB.BR           | Cidades                | Jaboatão dos Guararapes                                                |
  | JAMPA.BR         | Cidades                | João Pessoa                                                            |
  | JDF.BR           | Cidades                | Juiz de Fora                                                           |
  | JOINVILLE.BR     | Cidades                | Joinville                                                              |
  | LONDRINA.BR      | Cidades                | Londrina                                                               |
  | MACAPA.BR        | Cidades                | Macapá                                                                 |
  | MACEIO.BR        | Cidades                | Maceió                                                                 |
  | MANAUS.BR        | Cidades                | Manaus                                                                 |
  | MARINGA.BR       | Cidades                | Maringá                                                                |
  | MORENA.BR        | Cidades                | Campo Grande                                                           |
  | NATAL.BR         | Cidades                | Natal                                                                  |
  | NITEROI.BR       | Cidades                | Niterói                                                                |
  | OSASCO.BR        | Cidades                | Osasco                                                                 |
  | PALMAS.BR        | Cidades                | Palmas                                                                 |
  | POA.BR           | Cidades                | Porto Alegre                                                           |
  | PVH.BR           | Cidades                | Porto Velho                                                            |
  | RECIFE.BR        | Cidades                | Recife                                                                 |
  | RIBEIRAO.BR      | Cidades                | Ribeirão                                                               |
  | RIO.BR           | Cidades                | Rio de Janeiro                                                         |
  | RIOBRANCO.BR     | Cidades                | Rio Branco                                                             |
  | RIOPRETO.BR      | Cidades                | São José do Rio Preto                                                  |
  | SALVADOR.BR      | Cidades                | Salvador                                                               |
  | SAMPA.BR         | Cidades                | São Paulo                                                              |
  | SANTAMARIA.BR    | Cidades                | Santa Maria                                                            |
  | SANTOANDRE.BR    | Cidades                | Santo André                                                            |
  | SAOBERNARDO.BR   | Cidades                | São Bernardo do Campo                                                  |
  | SAOGONCA.BR      | Cidades                | São Gonçalo                                                            |
  | SJC.BR           | Cidades                | São José dos Campos                                                    |
  | SLZ.BR           | Cidades                | São Luis                                                               |
  | SOROCABA.BR      | Cidades                | Sorocaba                                                               |
  | THE.BR           | Cidades                | Teresina                                                               |
  | UDI.BR           | Cidades                | Uberlândia                                                             |
  | VIX.BR           | Cidades                | Vitória                                                                |
  | **##########**   | **Pessoas Jurídicas**  | **SEM RESTRIÇÃO**                                                      |
  | AGR.BR           | Pessoas Jurídicas      | Empresas agrícolas, fazendas                                           |
  | ESP.BR           | Pessoas Jurídicas      | Esporte em geral                                                       |
  | ETC.BR           | Pessoas Jurídicas      | Empresas que não se enquadram nas outras categorias                    |
  | FAR.BR           | Pessoas Jurídicas      | Farmácias e drogarias                                                  |
  | IMB.BR           | Pessoas Jurídicas      | Imobiliárias                                                           |
  | IND.BR           | Pessoas Jurídicas      | Indústrias                                                             |
  | INF.BR           | Pessoas Jurídicas      | Meios de informação (rádios, jornais, bibliotecas, etc..)              |
  | RADIO.BR         | Pessoas Jurídicas      | Empresas que queiram enviar áudio pela rede                            |
  | REC.BR           | Pessoas Jurídicas      | Atividades de entretenimento, diversão, jogos, etc...                  |
  | SRV.BR           | Pessoas Jurídicas      | Empresas prestadoras de serviços                                       |
  | TMP.BR           | Pessoas Jurídicas      | Eventos temporários, como feiras e exposições                          |
  | TUR.BR           | Pessoas Jurídicas      | Empresas da área de turismo                                            |
  | TV.BR            | Pessoas Jurídicas      | Empresas de radiodifusão ou transmissão via Internet de sons e imagens |
  | **##########**   | **Pessoas Jurídicas**  | **COM RESTRIÇÃO**                                                      |
  | AM.BR            | Pessoas Jurídicas      | Empresas de radiodifusão sonora                                        |
  | COOP.BR          | Pessoas Jurídicas      | Cooperativas                                                           |
  | FM.BR            | Pessoas Jurídicas      | Empresas de radiodifusão sonora                                        |
  | G12.BR           | Pessoas Jurídicas      | Instituições de ensino de primeiro e segundo grau                      |
  | GOV.BR           | Pessoas Jurídicas      | Instituições do governo federal                                        |
  | MIL.BR           | Pessoas Jurídicas      | Forças Armadas Brasileiras                                             |
  | ORG.BR           | Pessoas Jurídicas      | Instituições não governamentais sem fins lucrativos                    |
  | PSI.BR           | Pessoas Jurídicas      | Provedores de serviço Internet                                         |
  | **##########**   | **Pessoas Jurídicas**  | **DNSSEC OBRIGATÓRIO**                                                 |
  | B.BR             | Pessoas Jurídicas      | Bancos                                                                 |
  | DEF.BR           | Pessoas Jurídicas      | Defensorias Públicas                                                   |
  | JUS.BR           | Pessoas Jurídicas      | Instituições do Poder Judiciário                                       |
  | LEG.BR           | Pessoas Jurídicas      | Instituições do Poder Legislativo                                      |
  | MP.BR            | Pessoas Jurídicas      | Instituições do Ministério Público                                     |
  | TC.BR            | Pessoas Jurídicas      | Tribunais de Contas                                                    |

</details>

### ASN disponíveis do Whois público do registro NIR Nic.br

Compilação de informações de origem do prefixo ASN disponíveis do Whois público do registro NIR Nic.br. Campos separados por pipe.da
ASN|OrgName|OrgID|prefixos... (Tradução da própria descrição fornecida pelo RegistroBR - https://ftp.registro.br/pub/numeracao/origin/00README)

- Diretório com histórico de arquivos - https://ftp.registro.br/pub/numeracao/origin/
- Lista atualizada - https://ftp.registro.br/pub/numeracao/origin/nicbr-asn-blk-latest.txt

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-blue?style=plastic&logo=Acclaim)](#sumário)



---

## Autores 👔 <a name="autores"></a>

<p >
<img src="assets/logo_profile.png" width="20%" /><br>
<p>

- **Cleiton P. (MrCl0wnLab)** - [Twitter](https://twitter.com/MrCl0wnLab), [Git](https://github.com/MrCl0wnLab)

- **Diego (c4nh0t0)** - [Twitter](https://twitter.com/C4nh0t0GH), [Git](https://github.com/c4nh0t0)

---

## Contribuições ✨ <a name="contribuicoes"></a>

Contribuições de qualquer tipo são bem-vindas!

<a href="https://github.com/osintbrazuca/osint-brazuca/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=osintbrazuca/osint-brazuca&max=500" alt="Lista de contribuidores" width="100%"/>
</a>
    
---
    
## Créditos 👏 <a name="creditos"></a>
À todas as instituições públicas governamentais e inciativas privadas que disponibilizaram os links para consulta.
<br>
À todos que de alguma forma contribuíram para o compartilhamento de links e tricks de consulta nos websites.
