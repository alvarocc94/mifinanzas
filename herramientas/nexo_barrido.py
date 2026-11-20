"""Barrido de proyectos de vivienda en Nexo Inmobiliario: precio por m² de cada tipología.

Lee el sitemap público de proyectos (robots.txt de Nexo no restringe nada), descarga cada ficha
con una pausa larga entre pedidos y extrae los datos del proyecto y de sus tipologías disponibles.
Guarda una línea JSON por proyecto, así que se puede cortar y reanudar. Ante el primer 403 o 429
se detiene: el 19-nov-2026 Nexo bloqueó la IP tras 37 fichas a una por segundo.

Uso:
    python -I herramientas/nexo_barrido.py SALIDA.jsonl [--pausa 12] [--limite N]

Solo usa la biblioteca estándar.
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

SITEMAP = "https://nexoinmobiliario.pe/sitemap-proyectos.xml"
UA = "Mozilla/5.0 (barrido personal de precios, pausado)"
FASES = {"1": "En planos", "2": "En construcción", "3": "Entrega inmediata"}


def bajar(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        crudo = r.read()
    try:
        return crudo.decode("utf-8")
    except UnicodeDecodeError:
        return crudo.decode("cp1252", errors="replace")


def numero(texto: str) -> float | None:
    m = re.search(r"[\d.,]+", texto)
    if not m:
        return None
    s = m.group(0)
    if "," in s and "." in s:
        s = s.replace(",", "")
    elif "," in s:
        # "201,994" es separador de miles; "40,5" sería decimal
        s = s.replace(",", "") if re.search(r",\d{3}$", s) else s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def tipologias(html: str) -> list[dict]:
    salida = []
    trozos = html.split('class="fp-modelo-disponible-content"')[1:]
    for t in trozos:
        t = t.split('class="Project-available-model', 1)[0]
        disp = re.search(r'fp-modelo-disponible-availability"[^>]*>\s*([^<]+)<', t)
        precio = re.search(r'fp-modelo-disponible-price">\s*([^<]+?)\s*<', t)
        modelo = re.search(r'fp-modelo-disponible-model">\s*([^<]+?)\s*<', t)
        tid = re.search(r'class="typology_id"[^>]*>(\d+)<', t)
        rasgos = [re.sub(r"\s+", " ", x).strip() for x in re.findall(r'fp-modelo-disponible-feature-text">\s*([^<]+?)\s*</h4>', t)]
        area = next((numero(x) for x in rasgos if "m²" in x or "m2" in x), None)
        dorms = next((numero(x) for x in rasgos if "dorm" in x.lower()), None)
        banos = next((numero(x) for x in rasgos if "baño" in x.lower()), None)
        pisos = next((x for x in rasgos if x.lower().startswith("piso")), None)
        p_txt = precio.group(1) if precio else ""
        salida.append({
            "typology_id": tid.group(1) if tid else None,
            "modelo": modelo.group(1) if modelo else None,
            "unidades": numero(disp.group(1)) if disp else None,
            "moneda": "USD" if ("US$" in p_txt or "$" in p_txt.replace("S/", "")) else "PEN",
            "precio": numero(p_txt),
            "area_m2": area,
            "dorms": dorms,
            "banos": banos,
            "pisos": pisos,
        })
    return salida


def ficha(url: str) -> dict:
    html = bajar(url)
    m = re.search(r"var obj_project_completo = (\{.*?\});\s*\n", html, re.S)
    if not m:
        return {"url": url, "error": "sin obj_project_completo"}
    o = json.loads(m.group(1))
    hist = [
        {"fecha": h.get("created_at"), "desde": h.get("precio_desde"), "moneda": h.get("type_currency")}
        for h in o.get("historial_precios_tabla") or []
    ]
    return {
        "url": url,
        "project_id": o.get("project_id"),
        "nombre": o.get("name"),
        "inmobiliaria": o.get("tradename"),
        "inmobiliaria_slug": o.get("builder_slug"),
        "distrito": o.get("distrito_project"),
        "provincia": o.get("provincia_project"),
        "direccion": o.get("direccion"),
        "lat": o.get("coord_lat"),
        "lng": o.get("coord_lng"),
        "entrega": o.get("date_delivery"),
        "fase": FASES.get(str(o.get("project_phase")), o.get("project_phase")),
        "fase_obra": o.get("proyecto_fase_construccion"),
        "banco": o.get("finance_bank"),
        "socio_asei": o.get("socio_asei"),
        "actualizado": o.get("update_creation"),
        "tipo": o.get("type_project"),
        "historial_desde": hist,
        "tipologias": tipologias(html),
    }


def urls_lima() -> list[str]:
    xml = bajar(SITEMAP)
    locs = re.findall(r"<loc>([^<]+)</loc>", xml)
    no_lima = ("arequipa", "piura", "tumbes", "pasco", "san-martin", "cusco", "trujillo", "chiclayo", "ica")
    return [u for u in locs if "/departamentos/" in u and u.split("/")[4] not in no_lima]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("salida")
    ap.add_argument("--pausa", type=float, default=12.0)
    ap.add_argument("--limite", type=int, default=0)
    a = ap.parse_args()
    out = Path(a.salida)
    hechos = set()
    if out.exists():
        for linea in out.read_text(encoding="utf-8").splitlines():
            if linea.strip():
                hechos.add(json.loads(linea)["url"])
    urls = [u for u in urls_lima() if u not in hechos]
    if a.limite:
        urls = urls[: a.limite]
    print(f"{len(hechos)} ya hechos, {len(urls)} por bajar", flush=True)
    with out.open("a", encoding="utf-8") as f:
        for i, u in enumerate(urls, 1):
            try:
                rec = ficha(u)
            except urllib.error.HTTPError as e:
                if e.code in (403, 429):
                    # El sitio nos está frenando: se para y se reintenta otro día, sin forzar
                    print(f"HTTP {e.code} en {u}: me detengo ({i - 1} fichas nuevas)", flush=True)
                    return
                rec = {"url": u, "error": repr(e)[:200]}
            except Exception as e:  # una ficha caída no detiene el barrido
                rec = {"url": u, "error": repr(e)[:200]}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            if i % 50 == 0:
                print(f"{i}/{len(urls)}", flush=True)
            time.sleep(a.pausa)
    print("listo", flush=True)


if __name__ == "__main__":
    sys.exit(main())
