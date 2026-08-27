#!/usr/bin/env python3
"""Valida as regras de formatação dos documentos do OSINT Brazuca.

Erros (saída 1), conforme CONTRIBUICAO.md:
    travessão (—) fora de crases em qualquer .md
    menu de navegação (bloco de badges) diferente entre os documentos
    link interno (#ancora) sem âncora correspondente no README.md

Avisos (não falham; só com --avisos):
    URL repetida em mais de uma fonte do catálogo
    URL em http:// em vez de https://

Uso:
    python3 tools/validar_docs.py            só erros
    python3 tools/validar_docs.py --avisos   erros e avisos
"""

import argparse
import json
import re
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = ["README.md", "CONTRIBUICAO.md", "EXEMPLOS_PRATICOS.md", "FLUXOGRAMA.md", "GUIA_RAPIDO.md"]

RE_TRAVESSAO = re.compile(r"(?<!`)—(?!`)")
RE_MENU = re.compile(r'^<p align="center">\n((?:  <a href=.*\n)+)</p>$', re.M)
RE_ANCORA = re.compile(r'<a name="([^"]+)"')
RE_LINK_INTERNO = re.compile(r"\]\(#([^)]+)\)")


def le(nome):
    return (RAIZ / nome).read_text(encoding="utf-8")


def checa_travessao():
    erros = []
    for nome in DOCS:
        for n, linha in enumerate(le(nome).splitlines(), start=1):
            if RE_TRAVESSAO.search(linha):
                erros.append(f"{nome}:{n}: travessão (—); use vírgula, dois-pontos, ponto final ou parênteses")
    return erros


def checa_menu():
    menus = {}
    for nome in DOCS:
        m = RE_MENU.search(le(nome))
        if not m:
            return [f"{nome}: menu de navegação (bloco de badges) não encontrado"]
        menus[nome] = m.group(1)
    referencia = menus["README.md"]
    return [
        f"{nome}: menu de navegação diferente do README.md; replique a mudança em todos os documentos"
        for nome, menu in menus.items()
        if menu != referencia
    ]


def checa_ancoras():
    texto = le("README.md")
    ancoras = set(RE_ANCORA.findall(texto))
    # Títulos também geram âncoras no GitHub; aceita o slug simples deles.
    for titulo in re.findall(r"^#{1,6}\s+(.*)$", texto, re.M):
        ancoras.add(slug_github(titulo))
    erros = []
    for n, linha in enumerate(texto.splitlines(), start=1):
        for alvo in RE_LINK_INTERNO.findall(linha):
            alvo = urllib.parse.unquote(alvo)
            if alvo not in ancoras and alvo.lower() not in ancoras:
                erros.append(f"README.md:{n}: link interno #{alvo} sem âncora correspondente")
    return erros


def slug_github(titulo):
    titulo = re.sub(r"<[^>]+>", "", titulo)
    titulo = re.sub(r"[^\w\s-]", "", titulo.strip().lower(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", titulo).strip("-")


def avisos_catalogo():
    caminho = RAIZ / "data" / "index.json"
    if not caminho.exists():
        return ["data/index.json não existe; rode tools/build_dataset.py"]
    links = json.loads(caminho.read_text(encoding="utf-8"))["links"]
    avisos = []
    por_url = defaultdict(set)
    for link in links:
        por_url[link["url"]].add(link["fonte_id"])
    for url, fontes in sorted(por_url.items()):
        if len(fontes) > 1:
            avisos.append(f"URL repetida em {len(fontes)} fontes: {url}\n    " + "\n    ".join(sorted(fontes)))
    inseguras = sorted({l["url"] for l in links if l["url"].startswith("http://")})
    if inseguras:
        avisos.append(f"{len(inseguras)} URLs em http://; confira se há versão https:")
        avisos.extend(f"    {u}" for u in inseguras)
    return avisos


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--avisos", action="store_true", help="mostra também URLs repetidas e http://")
    args = parser.parse_args()

    erros = checa_travessao() + checa_menu() + checa_ancoras()

    if args.avisos:
        avisos = avisos_catalogo()
        if avisos:
            print(f"AVISOS ({len(avisos)}):")
            for a in avisos:
                print(f"  {a}")
            print()

    if erros:
        print(f"ERROS ({len(erros)}):", file=sys.stderr)
        for e in erros:
            print(f"  {e}", file=sys.stderr)
        return 1
    print("OK: documentos seguem as regras de formatação.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
