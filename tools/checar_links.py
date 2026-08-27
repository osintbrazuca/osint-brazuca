#!/usr/bin/env python3
"""Verifica quais URLs do catálogo respondem, para curadoria local.

Lê data/index.json (rode tools/build_dataset.py antes) e faz uma requisição
em cada URL distinta. Não integra o CI: muitos sites .gov.br bloqueiam
robôs ou oscilam, então o resultado precisa de revisão humana antes de
virar issue ou correção no README.

Uso:
    python3 tools/checar_links.py                     todas as URLs
    python3 tools/checar_links.py --filtro detran     só URLs que contêm o texto
    python3 tools/checar_links.py --csv links.csv     grava o resultado completo

Sem dependências além do Python 3.
"""

import argparse
import csv
import json
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlsplit

RAIZ = Path(__file__).resolve().parent.parent
INDEX = RAIZ / "data" / "index.json"

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OSINT-Brazuca/checar_links (+https://github.com/osintbrazuca/osint-brazuca)"
TIMEOUT = 20

# Rótulo por situação, para o resumo final.
OK, REDIRECT, BLOQUEIO, OFFLINE, ERRO = "ok", "redirect", "bloqueio", "offline", "erro"


def classifica(status, destino, url):
    if status is None:
        return ERRO
    if status in (401, 403, 405, 429, 503):
        return BLOQUEIO  # provável anti-robô ou exige sessão; conferir no navegador
    if status >= 400:
        return OFFLINE
    if destino and urlsplit(destino).netloc != urlsplit(url).netloc:
        return REDIRECT
    return OK


def requisita(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    inicio = time.monotonic()
    for metodo in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=metodo, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
                return resp.status, resp.geturl(), round(time.monotonic() - inicio, 1), ""
        except urllib.error.HTTPError as e:
            if metodo == "HEAD" and e.code in (400, 403, 404, 405, 501):
                continue  # muitos servidores rejeitam HEAD; tenta GET
            return e.code, e.geturl() if hasattr(e, "geturl") else "", round(time.monotonic() - inicio, 1), ""
        except (urllib.error.URLError, socket.timeout, ssl.SSLError, ConnectionError, OSError) as e:
            if metodo == "HEAD":
                continue
            return None, "", round(time.monotonic() - inicio, 1), type(e).__name__ + ": " + str(getattr(e, "reason", e))[:80]
    return None, "", round(time.monotonic() - inicio, 1), "sem resposta"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--filtro", help="só URLs que contenham este texto")
    parser.add_argument("--csv", help="grava o resultado completo neste arquivo")
    parser.add_argument("--paralelo", type=int, default=12, help="requisições simultâneas (padrão 12)")
    args = parser.parse_args()

    if not INDEX.exists():
        print("data/index.json não existe; rode: python3 tools/build_dataset.py", file=sys.stderr)
        return 2
    links = json.loads(INDEX.read_text(encoding="utf-8"))["links"]
    fontes = {}
    for l in links:
        fontes.setdefault(l["url"], []).append(l["fonte_id"])
    urls = sorted(fontes)
    if args.filtro:
        urls = [u for u in urls if args.filtro.lower() in u.lower()]
    print(f"verificando {len(urls)} URLs distintas com {args.paralelo} conexões...\n")

    resultados = []
    with ThreadPoolExecutor(max_workers=args.paralelo) as pool:
        futuros = {pool.submit(requisita, u): u for u in urls}
        for i, fut in enumerate(as_completed(futuros), start=1):
            url = futuros[fut]
            status, destino, segundos, detalhe = fut.result()
            situacao = classifica(status, destino, url)
            resultados.append((situacao, status, url, destino, segundos, detalhe, ";".join(fontes[url])))
            if situacao != OK:
                print(f"[{i:4}/{len(urls)}] {situacao:8} {status or '-':>4} {url}"
                      + (f"  -> {destino}" if situacao == REDIRECT else "")
                      + (f"  ({detalhe})" if detalhe else ""))

    resumo = Counter(r[0] for r in resultados)
    print("\nresumo")
    for chave in (OK, REDIRECT, BLOQUEIO, OFFLINE, ERRO):
        print(f"  {chave:9} {resumo.get(chave, 0)}")
    print("\nbloqueio = 401/403/405/429/503, provável anti-robô: confira no navegador antes de reportar.")

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["situacao", "status", "url", "destino", "segundos", "detalhe", "fontes"])
            w.writerows(sorted(resultados))
        print(f"resultado gravado em {args.csv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
