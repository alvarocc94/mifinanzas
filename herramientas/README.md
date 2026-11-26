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

## Préstamo con cuota fija: `prestamo_plantilla.py`

Genera un Excel para llevar un préstamo con cronograma francés, periodo de gracia y anticipos a
capital. Necesita `openpyxl`, que `uv` trae sin instalar nada en el sistema:

```
uv run --no-project --with openpyxl python -I herramientas/prestamo_plantilla.py privado/prestamo/prestamo.xlsx
```

- **Dónde guardarlo:** en `privado/`, que git ignora, porque el archivo lleno tiene datos de una
  persona.
- **Volver a generarlo** sobrescribe el archivo y borra los pagos anotados. Para cambiar monto,
  tasa, fechas o cuotas no hace falta: se editan en la hoja Datos.
- **Hojas:**

  | Hoja | Qué tiene |
  |---|---|
  | Datos | lo pactado: monto, TEA, desembolso, primera cuota, número de cuotas, gracia total o parcial, tasa de IR y qué pasa tras un anticipo (celdas amarillas) |
  | Cronograma | el plan original mes a mes: saldo, interés, amortización y cuota |
  | Pagos | lo que de verdad paga el deudor (fecha, monto, tipo, medio y nota), de donde sale el saldo oficial |
  | Resumen | deuda a hoy, cuotas pagadas y atrasadas, la próxima cuota (recalculada si hubo anticipos) e intereses cobrados por año para la declaración anual |

- **Tipos de pago** (lista desplegable en Pagos):
  - **Cuota:** cubre primero los intereses y luego el capital (Código Civil, art. 1257). Es lo
    único que cuenta como cuota pagada.
  - **Pago parcial:** si una cuota llega en partes, las primeras son parciales y la última es
    Cuota. También sirve para los pagos de interés de una gracia parcial.
  - **Anticipo a capital:** va íntegro a capital. El interés corrido hasta ese día queda
    pendiente y se cobra con la siguiente cuota.
- **Tras un anticipo** (celda de Datos):
  - **Reducir plazo:** la cuota no cambia y el préstamo termina antes; la última cuota sale menor.
  - **Reducir cuota:** la fecha final no cambia y la cuota baja.
  - Resumen muestra las dos opciones y cobra la elegida.
- **Cómo cuenta el interés:**
  - Corre solo sobre el capital; el interés pendiente no genera más interés (art. 1249).
  - Usa meses de 30 días (base 30/360). Si la primera cuota no cae el mismo día que el
    desembolso, el primer periodo es irregular; con desembolso el 20-nov y primera cuota el
    28-feb son 98 días.
  - Cronograma y Pagos cuentan igual, así que si las cuotas se pagan en su fecha coinciden al
    céntimo. Si se pagan tarde o adelantado, el interés se ajusta a los días.
- **No modela** comisiones, seguros ni intereses moratorios.
- **Verificado el 2026-11-20** con el evaluador `formulas` (sin errores) en tres casos, con
  S/ 25,000 al 9% TEA, gracia total y 12 cuotas de S/ 2,218.03 del 28-feb-2027 al 28-ene-2028:
  - pago puntual: el saldo final es S/ 0.00;
  - cuatro cuotas y un anticipo de S/ 5,000 el 10-jun-2027:
    - si reduce la cuota, baja a S/ 1,574.41;
    - si reduce el plazo, quedan 6 cuotas en vez de 8 y termina el 28-nov-2027;
    - todo coincide con un cálculo independiente en Python;
  - gracia parcial: el saldo final es de S/ 0.01.
