# Preventa para alquilar y revender: Mural (Lince), Villa Elenia y dónde está el m² barato (2026-11-19)

El dueño quiere invertir ya en un inmueble. Cotizó dos proyectos:
- **Mural** (Grupo T&C, Av. Arequipa 1936, Lince). Tiene **desembolso postergado**: se da 10% de
  inicial y nada más hasta el desembolso del crédito en sep-2027.
- **Villa Elenia** (Grupo Caral, Av. Angamos Este 1425, Surquillo). El crédito se desembolsa en
  ~2 meses y la entrega llega un año después.

Para Mural, el plan es comprar el 1511 a S/ 258,000 (primera oferta sobre una lista de S/ 277,409),
esperar la independización y vender a ~S/ 300,000 en unos 2.5 años. El dueño señala que los
precios de internet son de lista y que en Perú se negocia 5–7% abajo. Pidió:
- un barrido de los m² más baratos de toda Lima;
- revisar las inmobiliarias por razón social y no solo por marca. Dice haber visto muchas
  denuncias contra Grupo Caral.

## 1. Qué se pudo barrer y qué no

- **Nexo Inmobiliario: descartado.** Su robots.txt no restringe nada, pero sus
  [términos y condiciones](https://nexoinmobiliario.pe/terminos-y-condiciones), cláusula 3.2,
  **prohíben expresamente la extracción automatizada**: "scripts, bots, crawlers, spiders o
  cualquier otro mecanismo automatizado o semiautomatizado".
  - Se revisaron después de un primer barrido de 37 fichas, que Nexo cortó con un 403.
  - El 2026-11-19 se retiraron del repo el barrido y el ranking (commit `e054b6d`) y se borraron
    los datos bajados.
  - Las cifras de Mural de esta nota vienen de su ficha. De aquí en adelante, los datos de
    proyectos entran a mano: cotizaciones, la ficha que lee el dueño o la feria.
- **Urbania:** responde 403 (Cloudflare) y su robots.txt no permite pasar de la página 5. La
  **reventa** se mide entonces con el BCRP, cuyos precios de oferta salen de avisos de portales.
- **INDECOPI, "Mira a quién le compras":** la app usa una API con token OAuth. No se usó por fuera
  de su interfaz web. La consulta por RUC es manual y pública (sección 6).

## 2. Referencia de mercado: BCRP, T1-2026

Precio de oferta de departamentos, todas las antigüedades. En US$/m² convertidos a soles con el
tipo de cambio promedio de T1-2026 (3.387). Fuente:
[BCRPData PD17459PQ–PD37958PQ](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD17459PQ-PD17460PQ-PD17461PQ-PD17462PQ-PD17463PQ-PD17464PQ-PD17465PQ-PD17466PQ-PD17467PQ-PD17468PQ-PD37957PQ-PD37958PQ/json/2024-1/2026-4),
consultado el 2026-11-19.

| Distrito | US$/m² | S/ por m² |
|---|---|---|
| La Molina | 1,510 | 5,115 |
| San Miguel | 1,637 | 5,545 |
| Surco | 1,818 | 6,158 |
| Surquillo | 1,856 | 6,288 |
| Pueblo Libre | 1,875 | 6,351 |
| Lince | 1,894 | 6,415 |
| Magdalena | 1,986 | 6,727 |
| San Borja | 2,099 | 7,109 |
| Jesús María | 2,103 | 7,123 |
| Miraflores | 2,464 | 8,345 |
| Barranco | 2,556 | 8,657 |
| San Isidro | 2,605 | 8,823 |

- Son precios de **lista**: el cierre suele ir 5–7% abajo, igual que en los proyectos.
- Lince en soles quedó plano de 2022 a 2026 (−3.5% acumulado, nota del loft).

## 3. Dónde está el m² más barato en Lima Moderna

Las fuentes son las fichas de Nexo del 12-nov (informe de la feria) y las 37 fichas de hoy. El
precio es "desde", de lista.
- **Entrega inmediata** de unidades nuevas de tamaño normal: ~S/ 6,900–7,500 por m². Ejemplos:
  - Campo Marte (JM): 7,447;
  - Ascenza (PL): 6,933;
  - Millennium (Magdalena): 6,915–7,295;
  - Patriotas (SM): 7,147;
  - Toscana y Lombardía 3D (Lince): ~7,600.
- **Lo más barato en construcción o en planos:**

  | Proyecto (inmobiliaria) | Distrito | S/ por m² de lista | Frente al BCRP | Banco | Ojo |
  |---|---|---|---|---|---|
  | Luma (Grupo MG) | San Miguel | 5,356–5,804 (2D) | −3% | Interbank | entrega jun-2027 |
  | Villa Elenia (Caral) | Surquillo | 5,521–6,900 (2D) | −12% en el piso | Scotiabank | denuncias: ver §6 |
  | Mural, modelo 15 (T&C) | Lince | **6,091 (1D de 45 m²)** | −5% | **financiamiento propio** | T&C en rojo |
  | Loto (Abril) | San Miguel | 5,902–6,273 (2D) | +6% | sin publicar | — |
  | Eucalipto (Abril) | Jesús María | 6,268–6,973 (2D) | **−12%** | BCP | entrega dic-2028 |
  | Allure (Grupo MG) | Jesús María | 6,426–7,234 (2D) | −10% | BCP | en planos |
  | Kaurí (Abril) | Pueblo Libre | 6,332–6,579 (2D) | ≈0% | Scotiabank | entrega dic-2026 |
  | Mural 1511 (T&C) | Lince | 6,774 de lista; 6,300 ofertado | −2% | financiamiento propio | — |

- **Fuera de Lima Moderna** el m² nuevo baja a 4,000–6,200: Santa Beatriz, Breña, Chorrillos,
  Bellavista y SMP (Feliciti, en planos, a 4,070). La renta y la liquidez de reventa también son
  menores.
- **La ganancia de una preventa** es la distancia entre lo que se paga en planos y lo que se paga
  por una unidad terminada en el mismo distrito. Hoy es de ~10–20%. El amigo del dueño compró en
  Barranco ~30% bajo el mercado; el loft, 17% bajo.

## 4. Mural: lo que dice la ficha y el modelo

**Ficha de Nexo**, actualizada el 2026-11-18
([Nexo](https://nexoinmobiliario.pe/departamentos/lince/mural-lince-3469)):
- **Obra:** etapa "En construcción", fase de obra **"En excavación"**, entrega el 31-oct-2027.
  Unidades hasta el piso 23.
- **Banco:** "Financiamiento propio", **sin banco promotor**. ASEI con enlace "novalido".
- **Razón social:** **SARASOTA REAL ESTATE GROUP S.A.C., RUC 20611195843**, GG "W.T.C." (Libro
  de Reclamaciones de [mural.grupotyc.com](https://mural.grupotyc.com/)). Es una empresa reciente,
  creada para el proyecto.
- **Tipologías 1D disponibles:**

  | Modelo | m² | Desde | S/ por m² | Unidades | Pisos |
  |---|---|---|---|---|---|
  | 15 | 45.18 | 275,202 | 6,091 | 13 | 9–23 |
  | 13 | 48.49 | 311,672 | 6,428 | 7 | 1–8 |
  | 14 | 40.61 | 271,861 | 6,694 | 7 | 8–15 |
  | 1, 3–5, 7, 8, 10–12 (micro) | 21.9–23.7 | 201k–225k | 9,100–9,800 | 52 | varios |

  Hay unos 52 micro-departamentos de ~22 m² dirigidos a inversionistas. En la entrega, el
  edificio tendrá mucha oferta de alquiler y de reventa al mismo tiempo.
- **Cotizaciones del dueño (WhatsApp):**
  - 1511: 40.95 m², S/ 277,409, ofrecido a 258,000;
  - 2312: 43.38 m² (44.55 totales), 1D y 2 baños, S/ 280,818;
  - 1706: 2D de 53.68 m², S/ 359,785.

**Modelo** (`tools/flip_preventa.py` y `flip_variantes.py` en el scratchpad).
- **Supuestos:**
  - 10% de inicial ahora. Crédito convencional del 90% al 7.7% TEA a 25 años; cuota de S/ 1,707
    más ~S/ 157 de seguros.
  - Desembolso y entrega en sep-2027; S/ 4,000 de cierre y S/ 12,000 de muebles.
  - Alquiler amoblado de S/ 1,900–1,950, con un mes vacío al año, predial y 5% de IR.
  - Venta en may-2029, con 3.54% de corredor o venta directa, y 5% de IR sobre la ganancia.
  - El precio de venta es el de **cierre**, no el de aviso.
  - La plata propia puesta es ~S/ 49k.
- **TIR anual sobre la plata propia,** con corredor (y en venta directa):

  | Unidad | Compra S/ por m² | Venta a 6,600 | 6,800 | 7,000 | 7,300 | 7,600 | Sin perder |
  |---|---|---|---|---|---|---|---|
  | 1511 (40.95 m², S/ 258k) | 6,300 | −17% | −8% | 0% (+10%) | +11% (+20%) | +21% | 6,996 (S/ 286.5k) |
  | 2312 (43.38 m², lista −7%) | 6,020 | −3% | +5% | +13% (+21%) | +23% | +32% | 6,669 (S/ 289k) |
  | Modelo 15, piso bajo (lista −7%) | 5,900 | +3% | +11% | +18% | +27% | +36% | 6,528 (S/ 283k) |

- **Lectura:**
  - Los S/ 300k que espera el dueño son ~S/ 7,300 por m² de cierre. Hoy la mediana de Lince es
    6,415 y lo terminado nuevo se negocia en ~6,500–7,000. Llegar ahí exige 2–5% anual de
    plusvalía en un distrito que estuvo plano en soles.
  - Con 12 meses de retraso, la TIR baja 2–5 puntos. Como el desembolso es postergado, el
    retraso cuesta tiempo y no intereses.
  - **Por casi la misma plata, el 1D de ~43–45 m² (modelo 15 o el 2312) baja el precio de
    equilibrio de ~7,000 a ~6,500–6,700 por m².** Es la mejora más grande al alcance del dueño.
- **Villa Elenia X08,** de 40.34 m² a lista −6%:
  - El desembolso inmediato obliga a pagar ~14 cuotas sin renta antes de la entrega de mar-2028.
  - La plata propia sube a ~S/ 70k. Con venta a 7,300 la TIR da −0.3% con corredor y +6% en
    venta directa.
  - Para revender, el desembolso postergado de Mural vale más que su precio.

## 5. Riesgos de Mural que no están en el modelo

1. **T&C** ya estaba en rojo en el informe de la feria para compras en planos. Flamingo se entregó
   2–3 años tarde, con 14 denuncias en INDECOPI y 2 paralizaciones municipales.
2. **Sin banco promotor:** ningún banco supervisa la obra ni el destino de la inicial. Si la SPV se
   queda sin caja, la inicial se reclama a una empresa sin otros activos.
3. **"En excavación" con 23 pisos y entrega en oct-2027 no cuadra.** El dueño ve hoy un "buen
   avance": hay que contar los pisos levantados.
4. **Quién desembolsa en sep-2027:** un banco que no financia el proyecto suele prestar con el
   inmueble terminado o independizado. Si no hay crédito a la entrega, la inicial queda expuesta
   a la penalidad del contrato.
5. **Competencia dentro del edificio:** micro-departamentos y una promoción pensada para
   inversionistas.

## 6. Razones sociales, para consultar en INDECOPI

Consulta: [Mira a quién le compras](https://enlinea.indecopi.gob.pe/miraaquienlecompras/), por RUC.
Muestra solo **sanciones**; las denuncias en trámite se ven en la consulta de expedientes.

**Grupo Caral**, según su [Libro de Reclamaciones](https://www.grupocaral.com.pe/libro-de-reclamaciones),
consultado el 2026-11-19:

| Razón social | Proyecto | RUC |
|---|---|---|
| GC Angamos | Villa Elenia | 20612083321 |
| GC Dulanto | Villa Alba | 20612537586 |
| GC La Ribera | Villa Nova | 20613034235 |
| GC Leon Velarde S.A.C. | Villa Velarde | 20606065796 |
| GC Republica Hipolito S.A.C. | Casa Paraud | 20606072971 |
| GCC Viviendas S.A.C. | Nerea | 20603964099 |
| GCK Aviación S.A.C. | Villamar 131 | 20605294627 |
| JC Caral Magdalena | Villa Convivium 1, 2 y 3 | 20602691170 |
| Portal Santa Clara S.R.L. | Uptown 1 y 2, Valente 1 y 2 | 20544155831 |
| Proyectos GCF S.A.C. | Villa Dulanto 1441 | 20603961715 |

- En prensa no aparece ninguna de estas razones sociales con denuncias. Si el dueño las vio en
  INDECOPI, el veredicto "verde provisional" del informe de la feria queda sin sustento.

**Grupo T&C**, según su [Libro de Reclamaciones](https://www.grupotyc.com/libro-de-reclamaciones/)
(33 razones sociales). Las de proyectos vigentes o con historial:

| Razón social | Proyecto | RUC |
|---|---|---|
| Sarasota Real Estate Group S.A.C. | **Mural Lince** | 20611195843 |
| Flamingo Real State S.A.C. | Flamingo (JM), el caso del retraso | 20553452792 |
| Hamptons Real Estate Group S.A.C. | Costanova (SM) | 20613888331 |
| Maitland Real Estate Group S.A.C. | The Summit (SI) | 20613062166 |
| Adam Real Estate S.A.C. | Tree (SI) | 20557800647 |
| Doral Realtors S.A.C. | Skyhouse (JM) | 20602079199 |
| Promotora Vivienda Cinco S.A.C. | Aspiria (Barranco) | 20603435266 |
| Sunrise Investment Reducto S.A.C. | Nossa (JM) | 20546290795 |
| Meridian Real State S.A.C. | IQ Lince | 20553616493 |
| RM Real Vivienda S.A.C. | Slim (Lince) | 20609265575 |
| Inversiones Propco Uno S.A.C. | Vallejo Living (Lince) | 20601142075 |

## 7. Pendiente

- Consultar en MQLC los RUC de las tablas de §6, o pasarle al asistente las capturas.
- ~~Completar el barrido de Nexo~~: descartado por sus términos de uso (§1).
- Llevar a la visita de Mural las preguntas de §5 y las del informe de la feria.

## 8. Respuestas del dueño tras la visita (2026-11-19, tarde)

- **Banco:** BBVA da el hipotecario y lo **desembolsa con el departamento terminado**. Falta saber
  si BBVA también financia la obra (banco promotor); Nexo sigue diciendo "Financiamiento propio".
- **La inicial va a un fideicomiso.** Falta el nombre del fiduciario y en qué condiciones libera
  la plata a la obra.
- **Obra:** van **11 pisos** de 23. La etiqueta "En excavación" de Nexo está desactualizada, y la
  entrega a fines de 2027 se vuelve verosímil.
- **Independización:** 12–18 meses después de la entrega.
- **Si el crédito no sale,** la inmobiliaria se queda con una penalidad. No está claro si es el
  10% de la inicial (~S/ 2.6k) o el 10% del precio (toda la inicial). Hay que leerlo en la minuta.
- **Cesión de posición contractual: no se permite.** La plata queda inmovilizada hasta poder
  vender, ~2.5–3 años.
- **Falta preguntar:** la fecha de entrega del contrato, la penalidad por mes de retraso y desde
  cuántos meses de retraso se puede resolver con devolución.

**De dónde salen los ~S/ 49k propios** del caso base (1511, amoblado), a mayo de 2029:

| Concepto | S/ |
|---|---|
| Inicial (10%) | 25,800 |
| Cierre: notaría, registro, tasación | 4,000 |
| Muebles | 12,000 |
| Primer mes con cuota y sin inquilino | 1,864 |
| 18 meses en que la cuota (S/ 1,864) supera la renta neta (S/ 1,577) | 5,160 |
| **Total** | **~48,800** |

**Variantes** (venta en may-2029; entre paréntesis, sep-2029):

| Caso | Plata propia | TIR si cierra a 6,800 / 7,000 / 7,300 por m² |
|---|---|---|
| Amoblado (S/ 1,900) | 48.8k (50.0k) | −8% / 0% / +11% |
| **Sin amoblar (S/ 1,650)** | **40.7k (42.7k)** | **+1% / +9% / +21%** |
| Sin alquilar | 66.5k (74.2k) | −31% / −21% / −8% |

- **Sin amoblar es mejor:** los muebles cuestan S/ 12k y suben la renta solo ~S/ 250 al mes, menos
  de lo que cuestan en 18 meses.
- **Dejarlo vacío destruye el negocio:** la cuota completa sin renta suma ~S/ 33k.
- **Riesgo nuevo, la tasación:** si en 2027 BBVA tasa por debajo de S/ 258k, presta 90% de la
  tasación y la diferencia sale del bolsillo.

## 9. Con las condiciones del dueño: sin corredor, sin muebles y venta a S/ 300k en feb-2029

Supuestos:
- Renta sin amoblar de S/ 1,650 para el 1511 y de S/ 1,700 para los de ~43 m².
- Independización en ~15 meses, para poder vender en feb-2029.
- 5% de IR sobre la ganancia.
- Modelo: `tools/flip_dueno.py` en el scratchpad.

| Unidad | Compra | Venta | Plata propia | Recibes al vender | Ganancia neta | TIR anual |
|---|---|---|---|---|---|---|
| **1511** (40.95 m²) | 258,000 | 300,000 | 39.2k | 70.2k | **31.0k** | **+36%** |
| 2312 (43.38 m², 2 baños), lista −7% | 261,161 | 300,000 | 39.2k | 67.6k | 28.3k | +33% |
| Modelo 15, piso bajo, lista −7% | 255,938 | 300,000 | 38.1k | 71.9k | 33.8k | +40% |
| 2312 al mismo S/ por m² que la 1511 (7,326) | 261,161 | 317,800 | 39.2k | 84.5k | 45.2k | +50% |
| Modelo 15 a 7,326 por m² | 255,938 | 317,800 | 38.1k | 88.9k | 50.7k | +55% |

- **Sensibilidad de la 1511:**
  - Venta en may-2029 a 300k: +31%.
  - Venta en feb-2029 a 280k: +15.5% (ganancia de 12.0k).
  - **Equilibrio: ~S/ 267k**, unos S/ 6,530 por m², cerca de la mediana actual de Lince.
- **Los de 43 m² ganan solo si se venden por más.** Si un 1D se vende por unidad (~300k sin
  importar los m²), el 1511 queda casi igual que el modelo 15 y mejor que el 2312.
- **Lo exigente es el precio de 300k:** S/ 7,326 por m² de cierre, por encima de lo que hoy se
  negocia en lo terminado nuevo de Lince (~6,500–7,000). Lo que se ahorra en corredor y muebles
  baja mucho el riesgo: el equilibrio pasa de ~286k a ~267k.

**Eucalipto** (Abril, Av. Brasil 1857, JM; 2D de 51.04 m², lista "desde" S/ 326,074; entrega
15-dic-2028):
- Supuestos: renta sin amoblar de S/ 1,950, independización en ~15 meses y venta en may-2030.

| Desembolso | Precio | Venta a 357k / 372.6k / 388k (7,000 / 7,300 / 7,600 por m²) | Plata propia |
|---|---|---|---|
| Postergado | lista | +12% / +20% / +27% | 50.0k |
| Postergado | lista −6% | +24% / +31% / +37% | 45.8k |
| Inmediato | lista | −5% (a 372.6k) | 104.1k |
| Inmediato | lista −6% | +4% (a 372.6k) | 96.6k |

- **Todo depende de que el desembolso sea postergado.** Con desembolso inmediato se pagan ~23
  cuotas sin renta antes de la entrega.
- Hay que confirmar si los S/ 326,074 de Nexo ya incluyen el descuento de feria ("hasta S/ 84k").
- Jesús María fue el distrito que más subió en soles en 2022–2026 (+3.3% al año).
- La plata queda amarrada hasta ~2030.

## 10. Techo de ~S/ 300k para un 1D y la elección de unidad

- **Modelo 15 en Nexo:** 1D y **1 baño**, 45.18 m², pisos 9 al 23, 13 unidades disponibles,
  desde S/ 275,202 (el piso más bajo).
  - [Plano en Nexo](https://e.nexoinmobiliario.pe/customers/grupo-t-c/3469-mural-lince/planos-mural-lince-69433780c11de.png).
  - El 2312 (1D y 2 baños, 43.38/44.55 m²) **no es** el modelo 15, porque Nexo no lista ningún
    1D con 2 baños. El 1511 coincide con el modelo 14 (40.61 m², pisos 8–15).
- **El dueño cree que un 1D no pasa de ~S/ 300k al revender, y es razonable.** A ese precio el
  comprador consigue un 2D nuevo de ~50 m² en Surquillo, San Miguel o Jesús María. Ejemplos de
  lista hoy:
  - Luma, desde 272k;
  - Bugambilias, 327k;
  - Villa Elenia 2D, 329k.
- **Con ese techo gana la unidad más barata que se venda en 300k.** El 1511 (258k) deja S/ 31.0k;
  el 2312 (261k), S/ 28.3k.
  - El segundo baño y los metros extra no suben el techo, pero ayudan a vender rápido en 300k.
  - Pagar ~S/ 3k más por eso es barato. Más de ~S/ 5–8k ya no.

## 11. El 2312 está en el último piso (23)

- **Mural tiene azotea de uso común.** Nexo lista entre sus servicios "Techo Panorámico",
  "Terraza", "Zona de Parrillas" y "Piscina". La web de T&C dice 23 pisos.
- **Si encima del 2312 hay parrillas, terraza o piscina,** es el peor lugar del edificio. Tiene
  ruido de reuniones, tránsito y riesgo de filtraciones. Si encima hay solo losa o zonas sin
  uso, el último piso es una ventaja: más luz, nadie encima y más rapidez para venderse.
- **Alternativa:** la misma tipología de 1D y 2 baños en un piso 19–22, por debajo de la azotea.
