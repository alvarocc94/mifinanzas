"""Ranking de precio por m² a partir del barrido de Nexo (salida de nexo_barrido.py).

Uso:
    python -I herramientas/nexo_ranking.py BARRIDO.jsonl SALIDA.csv [--tc 3.39] [--descuento 0.06]

Filtra fichas activas (actualizadas desde mayo de 2026) y tipologías con
unidades disponibles. Compara cada tipología con la mediana de proyectos nuevos de su distrito
y número de dormitorios, y con la mediana del BCRP (precios de oferta, T1-2026).
"""

import argparse
import csv
import json
import statistics
from collections import defaultdict

# BCRP, precios de oferta de departamentos por distrito, US$/m², T1-2026 (PD17459PQ–PD37958PQ)
BCRP_USD = {
    "La Molina": 1510, "Miraflores": 2464, "San Borja": 2099, "San Isidro": 2605,
    "Santiago De Surco": 1818, "Jesus Maria": 2103, "Lince": 1894, "Magdalena Del Mar": 1986,
    "Pueblo Libre": 1875, "San Miguel": 1637, "Barranco": 2556, "Surquillo": 1856,
}
TC_BCRP = 3.387  # tipo de cambio promedio de T1-2026


def norm(d: str) -> str:
    return (d or "").replace("í", "i").replace("á", "a").title().replace("De ", "De ").strip()


def filas(path: str, tc: float, desc: float) -> list[dict]:
    out = []
    for linea in open(path, encoding="utf-8"):
        p = json.loads(linea)
        if p.get("error") or (p.get("provincia") or "") not in ("Lima", "Callao"):
            continue
        if (p.get("actualizado") or "") < "2026-05-01":
            continue
        banco = (p.get("banco") or "").replace("0,", "", 1)
        for t in p.get("tipologias") or []:
            if not t.get("precio") or not t.get("area_m2") or not t.get("unidades"):
                continue
            precio = t["precio"] * (tc if t["moneda"] == "USD" else 1)
            area = t["area_m2"]
            if not 18 <= area <= 250:
                continue
            pm2 = precio / area
            if not 2500 <= pm2 <= 25000:
                continue
            out.append({
                "proyecto": p["nombre"], "inmobiliaria": p["inmobiliaria"], "distrito": norm(p["distrito"]),
                "direccion": p["direccion"], "fase": p["fase"], "fase_obra": p.get("fase_obra") or "",
                "entrega": p["entrega"], "banco": banco or "(sin dato)", "asei": p.get("socio_asei"),
                "modelo": t["modelo"], "dorms": int(t["dorms"] or 0), "area_m2": area, "unidades": int(t["unidades"]),
                "precio_lista": round(precio), "pm2_lista": round(pm2), "pm2_negociado": round(pm2 * (1 - desc)),
                "url": p["url"],
            })
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("barrido")
    ap.add_argument("salida")
    ap.add_argument("--tc", type=float, default=3.39)
    ap.add_argument("--descuento", type=float, default=0.06)
    a = ap.parse_args()
    rows = filas(a.barrido, a.tc, a.descuento)
    grupo = defaultdict(list)
    for r in rows:
        grupo[(r["distrito"], min(r["dorms"], 3))].append(r["pm2_lista"])
    med = {k: statistics.median(v) for k, v in grupo.items() if len(v) >= 5}
    for r in rows:
        m = med.get((r["distrito"], min(r["dorms"], 3)))
        r["mediana_nuevos_distrito"] = round(m) if m else ""
        r["vs_mediana_nuevos"] = round(r["pm2_lista"] / m - 1, 3) if m else ""
        b = BCRP_USD.get(r["distrito"])
        r["bcrp_soles_m2"] = round(b * TC_BCRP) if b else ""
        r["negociado_vs_bcrp"] = round(r["pm2_negociado"] / (b * TC_BCRP) - 1, 3) if b else ""
    rows.sort(key=lambda r: r["pm2_lista"])
    with open(a.salida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} tipologías con unidades disponibles en {len({r['url'] for r in rows})} proyectos")


if __name__ == "__main__":
    main()
