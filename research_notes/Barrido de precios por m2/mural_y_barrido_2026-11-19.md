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

- **Nexo Inmobiliario.** Su robots.txt no restringe nada, pero sus
  [términos y condiciones](https://nexoinmobiliario.pe/terminos-y-condiciones), cláusula 3.2,
  **prohíben expresamente la extracción automatizada**: "scripts, bots, crawlers, spiders o
  cualquier otro mecanismo automatizado o semiautomatizado".
  - Se revisaron después de un primer barrido de 37 fichas, que Nexo cortó con un 403.
  - El 2026-11-19 se retiraron del repo el barrido y el ranking y se borraron los datos bajados.
  - El mismo día se restauraron en `herramientas/` a pedido del dueño, que decide si los usa.
  - Las cifras de Mural de esta nota vienen de su ficha. Sin el barrido, los datos de
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

## 12. Lista de precios por piso y promo de inicial (2026-11-20)

Fuente: lista de precios y proforma N° 003950 del 19-nov que T&C le pasó al dueño (capturas,
fuera del repo).
- **El descuento de la proforma es 7.00%,** no 6%: lista 277,408.82, precio 258,000.
- **En Mural los pisos bajos cuestan más,** al revés de lo usual. Cada piso que se sube baja el
  precio:
  - S/ 1,457 en la línea x12 (43.48 m², 1D y 2 baños, el modelo 15 según T&C);
  - S/ 1,386 en la línea x11 (40.95 m²).
- **Lista de la línea x12** (confirmada por el dueño el 20-nov):
  - 2312: 280,818, como ya se usó en §9;
  - 2212: 282,275;
  - de ahí baja hasta el 1112: 298,307;
  - el 1812 ya está separado.
- **El "desde" de Nexo para el modelo 15 (275,202) no aparece en la lista de T&C.** La fila
  "Modelo 15, piso bajo" de §9 no corresponde a ninguna unidad disponible.
- **Línea x11:** 911 y del 1111 al 1511. Además está el 811, de 43.68 m², a S/ 307,354.

Flip con lista −7%, condiciones del dueño (sin corredor ni muebles, venta en feb-2029) e inicial de
10% (modelo: `tools/mural_unidades.py` en el scratchpad). Ganancia neta entre paréntesis:

| Unidad | Precio −7% | S/ por m² | Venta en 300k | Venta en 305k | Venta a 7,326 por m² (318.5k) | Equilibrio |
|---|---|---|---|---|---|---|
| 1511 | 258,000 | 6,300 | +36.3% (31.0k) | — | — | 267.4k |
| 1411 | 259,289 | 6,332 | +34.8% (29.6k) | — | — | 268.8k |
| 2312 (último piso) | 261,171 | 6,007 | +33.4% (28.3k) | +38.1% (33.1k) | +50.2% (45.9k) | 270.2k |
| 2212 | 262,526 | 6,038 | +31.8% (26.9k) | +36.6% (31.6k) | +48.7% (44.5k) | 271.7k |
| 2112 | 263,882 | 6,069 | +30.1% (25.4k) | +35.0% (30.2k) | +47.2% (43.1k) | 273.2k |
| 1912 | 266,593 | 6,131 | +26.9% (22.6k) | +31.8% (27.3k) | +44.1% (40.2k) | 276.2k |
| 1512 | 272,015 | 6,256 | +20.3% (16.9k) | +25.3% (21.6k) | +38.1% (34.5k) | 282.2k |
| 1112 | 277,436 | 6,381 | +13.6% (11.2k) | +18.8% (15.9k) | +32.0% (28.8k) | 288.3k |

- **1511 frente al 2212:**
  - Si los dos se venden en 300k, el 2212 empata solo si se compra en ~258.7k (8.4% de
    descuento).
  - Si el 2212 se vende en 305k, como cree el dueño ("un poquito más y más rápido"), ya empata con
    el 7% (262.5k) y gana con cualquier descuento mayor.
- **Vender más rápido vale poco si el departamento sigue alquilado.** Si el 1511 se vende tres meses
  después (may-2029), pierde solo ~S/ 0.7k de ganancia (la TIR baja de 36% a 31%). Si hay que
  desocuparlo para venderlo, cada mes vacío cuesta ~S/ 1.9k (cuota, seguros y predial).
- **2312:** está debajo de la azotea, donde Nexo lista parrillas, terraza y piscina (§11).
- **Promo de inicial.** Hoy la inicial es de 10%. Desde mañana pasa a 20%: 10% al firmar y otro 10%
  en 6 cuotas (dic-2026 a may-2027). Para el 1511:

  | | 10% hoy | 20% |
  |---|---|---|
  | Plata propia | 39.2k | 61.8k |
  | Ganancia | 31.0k | 33.8k |
  | TIR | +36% | +25% |

  - En valor presente, el 20% sale +S/ 182 descontando al 5.37% (DPF neto) y −S/ 1,196 al 8.55%
    (préstamo familiar neto).
  - La promo vale poco en plata: medio punto más de descuento la compensa. Su valor real está en
    la liquidez y en tener menos plata en riesgo antes de la entrega.
- **Valorización de Lince** (BCRP, oferta de todas las antigüedades, en soles con el tipo de cambio
  bancario promedio de cada trimestre):
  - **En soles:** S/ 5,100 por m² en 2016, 6,913 en 2022 (el pico), 6,643 en 2025 y 6,414 en
    T1-2026. De 2016 a 2025 subió +3.0% al año, igual que San Miguel y Jesús María.
  - **En dólares sigue subiendo:** de US$ 1,803 en 2022 a US$ 1,894 en T1-2026. La caída en soles
    es la apreciación del sol.
  - **Qué exige vender en 300k:** son 7,326 por m², un 14% sobre la mediana de hoy, así que todo
    depende de la prima por ser nuevo. El equilibrio del 1511 (6,530 por m²) está casi en la
    mediana actual.

## 13. Minuta modelo y régimen VIS (revisada el 2026-11-20)

T&C mandó como "modelo" la minuta firmada de otro comprador (departamento 1012, versión del
15-jul-2026, firmada el 30-oct-2026). Trae datos personales de esa persona, así que el PDF no se
guarda en el repo y aquí no se copia ninguno.

- **La venta es VIS.** El título es "Minuta compraventa - VIS". El comprador firma una declaración
  jurada de que cumple los requisitos de acceso a la VIS (Anexo D). La cláusula 12.B deja que la
  vendedora resuelva el contrato si no los cumple.
- **Ley 32379, art. 5** (El Peruano, 11-jun-2025; texto oficial leído el 2026-11-20). Son
  condiciones para acceder a la VIS:
  - a) no ser propietario de vivienda, terreno ni aires;
  - b) "no ser beneficiario de otro apoyo habitacional por parte del Estado";
  - c) valores máximos;
  - d) "La VIS no debe ser objeto de algún acto de transferencia de dominio hasta por el plazo de
    cinco años", contados desde que se inscribe la compraventa. La restricción se inscribe en
    SUNARP y la supervisa el Fondo MIVIVIENDA.
  - El texto no distingue según cómo se financie la compra.
  - [Ley 32379](https://busquedas.elperuano.pe/dispositivo/NL/2408533-1)
- **Proyecto de reglamento (RM 269-2026-VIVIENDA, publicada el 19-jul-2026), art. 21.2:** durante
  esos 5 años no se puede transferir, hay que "habitar exclusivamente la VIS" y no se puede
  arrendar. Al 26-sep-2026 no estaba aprobado
  ([El Peruano, 21-jul-2026](https://elperuano.pe/noticia/300761-no-se-podra-transferir-ni-poner-en-alquiler-viviendas-de-interes-social-durante-cinco-anos);
  [EximiaHaus, 27-sep-2026](https://eximiahaus.pe/blog/ley-32379-vivienda-de-interes-social-que-cambia-2026)).
  - Mientras tanto rige el DS 005-2025-VIVIENDA. Su art. 19.1 repite los requisitos a) y c). Su
    art. 8 trata del alcance de los proyectos, no de requisitos, aunque la minuta lo cita como si
    los tuviera.
- **Consecuencia para el flip:** vender en feb-2029 no es posible. Los 5 años corren desde la
  inscripción, y la independización puede tardar hasta 24 meses tras la entrega (cl. 7). El modelo
  de §9 a §12 solo vale si se compra para vivir 5 años o más.
- **El requisito b) es dudoso para el dueño.** Recibió el BBP en 2022 y lo devolvió al vender, y
  la ley no aclara si eso cuenta. Hay que confirmarlo por escrito antes de firmar la declaración
  jurada.
- **Precio del 1012:** S/ 284,775.72. Sale de la lista del 1112 (298,307) más un piso
  (+1,457 ≈ 299,764) con **5.0% de descuento**.
  - Forma de pago: 10% al firmar (separación de 2,000 y el saldo 6 días después), otro 10% en 10
    cuotas de nov-2026 a ago-2027 y 80% de crédito hipotecario a más tardar el 30-sep-2027.
  - Entrega: 30-oct-2027.
- **Cláusulas en contra del comprador:**
  - **Precio y pagos:**
    - mora automática;
    - los adelantos se devuelven sin intereses si el contrato se resuelve por cualquier causa (cl. 3);
    - si el área real difiere hasta 2.49% no hay compensación, y si es menor, la compensación se paga
      después de la entrega (cl. 9);
    - todos los gastos notariales y registrales los paga el comprador (cl. 14).
  - **Incumplimiento:** si el comprador incumple un pago o la fianza del banco, la vendedora puede
    resolver el contrato sola y quedarse con **10% del precio** (cl. 12). No hay penalidad ni
    derecho a resolver a favor del comprador.
  - **Obra y entrega:**
    - el comprador autoriza de antemano cualquier cambio al proyecto (cl. 6);
    - la entrega se puede prorrogar 6 meses sin causa, y más por fuerza mayor o atrasos de
      proveedores; la única compensación es suspender los pagos (cl. 10);
    - no se puede rechazar la entrega por obras pendientes en áreas comunes (cl. 10).
  - **Inscripción y cesión:**
    - la independización puede tardar hasta 24 meses tras la entrega (cl. 7);
    - el comprador da un poder irrevocable al procurador de la vendedora para firmar minutas
      "modificatorias o aclaratorias" (cl. 7);
    - la vendedora puede ceder su posición a un tercero, pero no hay cesión a favor del comprador
      (cl. 17).
  - **Otros:**
    - la vendedora puede usar gratis las áreas comunes para publicidad y oficina de ventas (cl. 15);
    - el comprador debe reportar sus consumos al FMV durante 24 meses (cl. 16).
- **Datos del proyecto:**
  - **Vendedora:** Sarasota Real Estate Group S.A.C., RUC 20611195843.
  - **Terreno:** partida 40662820. La vendedora puede hipotecarlo a favor de quien financie el
    proyecto (cl. 9).
  - **Licencia:** la minuta solo cita un anteproyecto aprobado por revisor urbano (AE-II-0121,
    ITF E-C-2024-0005856), no la licencia de edificación.
  - **Pagos:** se depositan en una cuenta BBVA de la vendedora.
  - **Acabados:** no incluyen terma ni luminarias.
- **Oferta final de T&C por el 1511 (2026-11-20, según el dueño):** S/ 255,000. Es 8.1% menos que
  la lista de 277,409 y sale a 6,227 por m².
  - Recomendación: como inversión no conviene, por la restricción VIS.
  - Para vivir 5 años o más podría servir, pero solo con confirmación escrita de que el dueño
    califica pese al BBP de 2022.
- **Decisión (2026-11-20):** el dueño separó el 1511 a S/ 255,000 con S/ 3,000 y sigue adelante.
  - Asume como propio el riesgo de no poder transferir durante 5 años.
  - T&C confirmó por correo que devuelve la inicial si el banco deniega el crédito o si el dueño
    no califica como VIS.
  - Plazos: S/ 22,500 de saldo de la inicial al 23-nov; minuta hasta el 30-nov; S/ 229,500 con
    crédito al 30-sep-2027.
  - Los documentos de la compra y las observaciones a la minuta están en Google Drive:
    `G:\Mi unidad\Compra depto Mural 1511\`.
