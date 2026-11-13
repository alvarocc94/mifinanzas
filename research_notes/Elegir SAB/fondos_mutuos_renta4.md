# Fondos mutuos en Renta 4 (2026-11-12)

El dueño vio en la plataforma de Renta 4 (pestaña "Fondos") que puede suscribir fondos de cuatro
gestoras: **Sura, Faro, Flip y Blum**. Había escuchado que un fondo de Blum invierte en el S&P 500 y
preguntó si eso evita el problema de liquidez de SPYL en la BVL, y qué rendimientos dan los fondos.

## 1. Blum USA 500 Acciones Fondo de Fondos

Fuente: prospecto simplificado en la SMV, vigente desde el 09-jul-2025
([SMV](https://www.smv.gob.pe/ConsultasP8/temp/USA%20500%20PS090725.pdf); copia leída con
`python -I`). Página del fondo: [miblum.com](https://www.miblum.com/fondo-blum-usa-500).
Lanzamiento anunciado por trii en nov-2024
([trii](https://trii.pe/blog/aprovecha-el-impulso-del-sp-500-invierte-en-el-nuevo-fondo-blum-usa-500-acciones)).

- **Qué compra:** al menos 75% en **CSPX**, el iShares Core S&P 500 UCITS ETF acumulativo
  (Irlanda), hermano de SPYL. Hasta 25% en depósitos o deuda del gobierno o del BCRP. Sin
  derivados. Puede apalancarse hasta 10% para atender rescates.
- **Indicador de comparación:** 95% CSPX + 5% ERNA (bonos ultracortos), menos la comisión de la
  serie B.
- **Series:**

  | Serie | Suscripción mínima | Comisión unificada | Con IGV |
  |---|---|---|---|
  | A | US$ 50,000 | 1.0% + IGV | 1.18% |
  | B | US$ 10 | 1.5% + IGV | **1.77%** |

- **Otros costos:** "comisiones propias de las operaciones de inversión" de hasta 4% + IGV, que
  incluyen el TER del ETF y la intermediación. El prospecto da 0.20% para CSPX.
- **Sin comisión** de suscripción ni de rescate hoy. El prospecto permite cobrar de 0 a 2% por
  suscripción.
- **Sin plazo mínimo de permanencia.** Recomienda no usarlo para rescates antes de 6 años.
- **Liquidez:**
  - La hora de corte es las 14:00, con el valor cuota del día hábil siguiente.
  - El pago llega en T+2 desde ese valor cuota, unos 3 días hábiles en total.
  - Un rescate de más de 3% del patrimonio del fondo puede tardar hasta 10 días hábiles.
- **Distribución:** Renta 4 e Inviu son distribuidores. Kallpa coloca a través de trii.
- **Custodio:** BCP.

## 2. Cuánto cuesta frente a SPYL y SPY

El fondo resuelve la salida: se rescata al valor cuota, sin depender de que haya compradores en
la rueda. El precio es una comisión anual sobre todo el saldo, todos los años.

Supuestos: 9% nominal bruto anual en dólares. Todo lo que va en CSPX o SPYL paga la retención de
15% sobre dividendos dentro del fondo (~0.18% al año).

| Vía | Costo anual aprox. | US$ 1 se vuelve, a 10 años | a 20 años | Frente a SPYL en IBKR, a 20 años |
|---|---|---|---|---|
| SPYL en IBKR | ~0.21% | 2.32 | 5.39 | referencia |
| SPY en la BVL (retención de 30%) | ~0.45% | 2.27 | 5.16 | −4% |
| Blum USA 500, serie B | ~2.05% (1.77% + 0.07% + 0.18%) | 1.96 | 3.83 | **−29%** |

Cálculo propio, al 2026-11-12. No incluye el efecto de tener hasta 25% en caja, que en un mercado
al alza resta un poco más. Tampoco incluye las comisiones de compra y venta en la BVL: ~0.6% por
lado más el spread, que se pagan una vez y no cada año. A los 10 años, el fondo deja ~16% menos
que SPYL.

**El punto de equilibrio está en 1–2 años:** la comisión del fondo supera en un año lo que cuesta
una compra y una venta en la BVL (~1.2% más el spread). Solo convendría para plata que se va a
sacar pronto, y eso no es el núcleo.

## 3. Otros fondos de renta variable vistos

- **Faro Capital Renta Variable Global FMIV** (ficha al 30-jun-2026,
  [Faro](https://farocapital.pe/wp-content/uploads/2026/08/Fact-Sheet-RV-Junio-2026.pdf)):
  - Es gestión activa global. Tiene 46% en IVV, 16% en QQQ, ETFs de memorias y Corea, y 18% en
    Asia.
  - La serie C pide desde US$ 100 y cobra 1.40% + IGV (1.65%). El rescate en el primer año cuesta
    1.5%.
  - Rentabilidad de la serie A, la de menor comisión: 2023 17.24%, 2024 12.76%, 2025 15.61%, 2026
    al 30-jun 21.13%.
  - El S&P 500 con dividendos dio ~26.3% en 2023, ~25.0% en 2024 y ~17.9% en 2025. Son cifras de
    referencia de S&P DJI que no verifiqué en esta sesión.
  - Le ganó a su índice en 2026 hasta junio, pero quedó 9–12 puntos debajo en 2023 y 2024.
- **Flip Cobra Achorada Fondo de Fondos FMIV** (Independiente SAF): acciones de EE.UU., renombrado
  en jun-2025
  ([Gestión](https://gestion.pe/tu-dinero/finanzas-personales/cobra-achorada-el-fondo-mutuo-que-ahora-gana-a-los-de-bancos-en-inversionistas-flip-noticia/)).
  No revisé su comisión. Flip administraba ~S/ 376 millones en abr-2026
  ([AAFM](https://fondosmutuos.pe/wp-content/uploads/2026/05/Informe-Mes-Abril-2026-web.pdf)).
- **Fuera de Renta 4:** BBVA Fondo de Fondos Acciones EE.UU. cobra 1.00% + IGV y 2% + IGV si se
  rescata antes del plazo
  ([prospecto, may-2026](https://fondos.bbva.pe/content/dam/public-web/fondos-peru/documents/personas/avisos-importantes/2-Prospecto-mayo-2026.pdf)).

## 4. Fondos de liquidez, para efectivo que espera

Rentabilidad a 1 año al 10-nov-2026, según la pantalla de Renta 4. Ya viene neta de comisión y
antes de impuestos.

| Fondo | 1 año | Volatilidad 30 d |
|---|---|---|
| Blum Cash Soles, serie O | 4.01% | 0.58% |
| Sura Ultra Cash Soles, serie B | 3.92% | 0.57% |
| Sura Corto Plazo Soles, serie B | 3.61% | 0.56% |
| Blum Cash Soles, serie A | 3.49% | 0.51% |
| Sura Ultra Cash Dólares, serie B | 3.27% | 0.49% |
| Sura Corto Plazo Dólares, serie B | 2.94% | 0.53% |

- Pagan más que Renta 4 Cash (3.04% en soles y 2.32% en dólares) y menos que un DPF a 360 días
  (5.00–5.65%).
- No los cubre el FSD.
- La ganancia paga impuesto (5% efectivo en un fondo peruano, según una guía secundaria:
  [Trámites Perú](https://tramitesperu.com/guias/fondos-mutuos/)). Los intereses de los DPF
  están exonerados hasta el 31-dic-2026.
- Sirven para dólares que esperan semanas una orden, no para el fondo de vivienda.

## 5. Veredicto

- **Núcleo:** no se usa Blum USA 500. A 20 años la comisión se lleva ~29% del patrimonio final
  frente a SPYL. El orden de preferencia no cambia:
  1. SPYL en la BVL, si Renta 4 confirma que puede comprarlo y venderlo;
  2. SPY en la BVL vía Renta 4;
  3. SPYL en IBKR.
- **Salida de SPYL:** si llega el día en que SPYL no tiene compradores en la BVL, la alternativa no
  es el fondo. Es SPY en la BVL, que es líquido, o traspasar los valores.
- **Uso razonable del fondo:** solo para montos chicos y de corto plazo, donde el mínimo de US$ 15
  pesa más que 1.77% al año. Por ejemplo, US$ 300 por menos de 6 meses. No aplica al plan.
- **Fondos de liquidez:** útiles para dólares en espera dentro de Renta 4, en lugar de Renta 4 Cash.

## 6. Pendiente, por escrito

- A Blum: qué impuesto retiene al rescatar a una persona natural domiciliada. El fondo invierte
  en un ETF irlandés y no está claro si la ganancia se atribuye como renta de fuente extranjera
  (tasa progresiva, 14% para el dueño) o como 5%. Tampoco cuánto patrimonio tiene hoy el fondo.
- A Renta 4: si cobra algo por suscribir o rescatar fondos en su plataforma, y si recibe parte de
  la comisión unificada. Lo segundo explicaría el filtro "Renta 4 recomienda".
