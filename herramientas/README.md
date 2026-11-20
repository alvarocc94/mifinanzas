# Herramientas

Scripts de apoyo al plan. Solo usan la biblioteca estándar de Python, salvo que se indique otra
cosa. Se corren con `python -I` desde la raíz del repo.

## Barrido de Nexo Inmobiliario

> **Antes de usarlo:** la cláusula 3.2 de los
> [términos y condiciones de Nexo](https://nexoinmobiliario.pe/terminos-y-condiciones),
> consultados el 2026-11-19, prohíbe la extracción automatizada (scripts, bots, crawlers).
> El 19-nov Nexo bloqueó la IP tras 37 fichas a una por segundo. Usarlo es decisión del dueño;
> la vía sin ese conflicto es pedir permiso por escrito a Nexo (CODIP).

### `nexo_barrido.py`: bajar las fichas

```
python -I herramientas/nexo_barrido.py "research_notes/Barrido de precios por m2/raw/nexo_AAAA-MM-DD.jsonl"
```

- **Qué hace:** lee el sitemap de proyectos de Nexo, se queda con los departamentos de Lima y
  Callao (~775 fichas) y baja cada ficha. De cada proyecto guarda:
  - nombre, inmobiliaria, distrito, dirección y coordenadas;
  - fecha de entrega, etapa (planos, construcción, entrega inmediata) y fase de obra;
  - banco, si es socio de ASEI, fecha de actualización e historial del precio "desde";
  - por tipología: modelo, unidades disponibles, moneda, precio "desde", área, dormitorios,
    baños y pisos.
- **Salida:** una línea JSON por proyecto. Si se corta, se vuelve a correr con el mismo archivo
  y sigue desde donde quedó.
- **Ritmo:** 12 s entre fichas por defecto (`--pausa`); el barrido completo toma ~2.5 horas.
  `--limite N` baja solo N fichas, útil para probar.
- **Bloqueo:** ante el primer HTTP 403 o 429 se detiene y no reintenta. No lo fuerces con otro
  User-Agent, una VPN o un proxy: espera a que se levante.
- **Dónde guardar:** en `research_notes/**/raw/`, que git ignora.

### `nexo_ranking.py`: precio por m² y comparación

```
python -I herramientas/nexo_ranking.py "research_notes/Barrido de precios por m2/raw/nexo_AAAA-MM-DD.jsonl" "research_notes/Barrido de precios por m2/raw/ranking.csv" [--tc 3.39] [--descuento 0.06]
```

- **Filtros:** fichas actualizadas desde mayo de 2026 y tipologías con unidades disponibles,
  de 18 a 250 m² y de S/ 2,500 a 25,000 por m².
- **Moneda:** convierte los precios en US$ con `--tc`.
- **Columnas del CSV,** ordenado de menor a mayor S/ por m²:

  | Columna | Qué es |
  |---|---|
  | `pm2_lista` | precio "desde" ÷ área |
  | `pm2_negociado` | `pm2_lista` menos el `--descuento` (6% por defecto: lo que suele ceder una inmobiliaria) |
  | `mediana_nuevos_distrito` | mediana de `pm2_lista` de los proyectos del mismo distrito y número de dormitorios (con 5 o más tipologías; 3D o más van juntos) |
  | `vs_mediana_nuevos` | cuánto más barato (negativo) o caro está frente a esa mediana |
  | `bcrp_soles_m2` | mediana del BCRP del distrito, T1-2026, en soles (precio de oferta, todas las antigüedades) |
  | `negociado_vs_bcrp` | `pm2_negociado` frente a la mediana del BCRP |

- **Cómo leerlo:** lo interesante es lo que está **12–15% o más por debajo** de la mediana de
  nuevos de su distrito. Ese es el descuento que hizo rentable el loft de 2022.
- **Antes de entusiasmarse, revisar:**
  - etapa y fecha de entrega;
  - banco (alerta si dice "Financiamiento propio");
  - la inmobiliaria por razón social en INDECOPI;
  - si hay desembolso postergado, que Nexo no publica.
- **Actualizar el BCRP:** la tabla `BCRP_USD` del script se actualiza a mano cada trimestre con la
  [API del BCRP](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD17459PQ-PD17460PQ-PD17461PQ-PD17462PQ-PD17463PQ-PD17464PQ-PD17465PQ-PD17466PQ-PD17467PQ-PD17468PQ-PD37957PQ-PD37958PQ/json/2024-1/2026-4).
