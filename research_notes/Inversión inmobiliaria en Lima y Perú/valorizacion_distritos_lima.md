# Valorización histórica y rentabilidad por alquiler de departamentos por distrito — Lima Metropolitana y Callao (datos a octubre 2026)

> **Cómo leer estas notas.** Casi todas las cifras cuantitativas salen de las series trimestrales del BCRP (BCRPData), que descargué por API el 29-oct-2026. El último dato publicado es **T1-2026**, actualizado el 31-07-2026; el T2-2026 aún no estaba publicado. Las tasas compuestas (CAGR), las conversiones a soles y la deflactación son **cálculo propio** sobre esas series:
> - **Soles nominales** = US$/m² × tipo de cambio interbancario promedio del trimestre (BCRP).
> - **Soles reales** = soles nominales ÷ IPC Lima Metropolitana (índice dic-2021=100, promedio trimestral), expresados en soles de T1-2026.
> - Comprobación del método: la serie agregada del BCRP en S/ corrientes (7,217 S/ por m², T1-26) ÷ su serie en US$ (2,130.9) = 3.387, que coincide con mi tipo de cambio de T1-26.
>
> **Tipo de precio.** Tanto el BCRP como Urbania usan **precios de oferta (avisos publicados en Urbania)**, no precios de transacción. No encontré una serie pública de precios de transacción por distrito.
>
> **CAGR "suavizado".** Las medianas trimestrales por distrito son ruidosas: por ejemplo, Pueblo Libre saltó +9% en un solo trimestre (T4-25→T1-26). Por eso reporto dos versiones de la CAGR:
> - **Punto a punto:** T1 contra T1.
> - **Suavizada:** promedio de los 4 trimestres que terminan en T1-26, contra el promedio equivalente 5 o 10 años antes. Es la que uso para conclusiones.

## 1. Series de precio/m² por distrito y CAGR a 5 y 10 años (nominal y real, en S/ y US$)

### Takeaway
En la última década (T1-2016 → T1-2026), **ningún distrito de la muestra del BCRP le ganó al IPC solo con precio**. El "sector medio" (Lince, Jesús María, San Miguel, Magdalena, Pueblo Libre) apenas empató con la inflación: CAGR real de 0.0% a −0.4%/año. Surquillo, también del sector medio, se quedó atrás (−1.1%). El "sector alto" perdió entre −1.4% y −2.5% real por año: San Isidro, Miraflores, San Borja, La Molina y Surco. Barranco quedó en un punto intermedio (−0.6%). A 5 años (2021→2026) todos los distritos pierden en términos reales (−1.3% a −4.8%/año), por la inflación de 2021-22 y la apreciación del sol frente a precios que se cotizan en dólares.

### Cited Findings
- **Fuente base y cobertura.** El BCRP publica la serie trimestral "Venta de departamentos por distrito (dólares corrientes por m²)" para 12 distritos:
  - Desde T4-2007: La Molina, Miraflores, San Borja, San Isidro, Surco, Jesús María, Lince, Magdalena, Pueblo Libre y San Miguel.
  - Desde T1-2013: Barranco.
  - Desde T3-2000: Surquillo (el dato útil empieza en 2013).
  - Último dato: T1-2026, actualizado el 31-07-2026 — [BCRPData, Indicadores del mercado inmobiliario](https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/indicadores-del-mercado-inmobiliario); [API BCRP, series PD17459PQ…PD17468PQ, PD37957PQ, PD37958PQ](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD17459PQ-PD17460PQ-PD17461PQ-PD17462PQ-PD17463PQ-PD17464PQ-PD17465PQ-PD17466PQ-PD17467PQ-PD17468PQ-PD37957PQ-PD37958PQ/json/2007-4/2026-4)
- **Series por distrito solo en dólares.** El BCRP no publica series por distrito en soles. Sí publica agregados en US$, S/ corrientes y S/ constantes de 2009 para tres grupos: "12 distritos", "Sector Alto" (Barranco, La Molina, Miraflores, San Borja, San Isidro, Surco) y "Sector Medio" (Jesús María, Lince, Magdalena, Pueblo Libre, San Miguel, Surquillo) — [BCRPData, mismo grupo](https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/indicadores-del-mercado-inmobiliario)
- **Metodología del BCRP.** Según la descripción de la Nota de Estudios N.º 16-2026 (indicadores del IV-2025):
  - Los datos provienen de Urbania y son **precios listados (ofertados)**.
  - Se usa el promedio de medianas trimestrales.
  - Por tanto, no necesariamente reflejan precios de transacción.
  - [BCRP, Nota de Estudios 16-2026](https://www.bcrp.gob.pe/docs/Publicaciones/Notas-Estudios/2026/nota-de-estudios-16-2026.pdf). Ojo: el PDF devolvió una página anti-bot y no pude abrirlo; tomo la descripción del índice del buscador.
- **Deflactor y tipo de cambio** — [API BCRP: IPC Lima PN38705PM y var. 12m PN01273PM](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN38705PM-PN01273PM/json/2007-1/2026-10); [API BCRP: tipo de cambio PN01205PM-PN01207PM](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01205PM-PN01206PM-PN01207PM-PN01210PM/json/2007-1/2026-10)
  - IPC Lima (promedios trimestrales): 85.14 en T1-16, 94.84 en T1-21 y 117.47 en T1-26.
    - Inflación acumulada a 5 años: **+23.9%** (4.4%/año).
    - Inflación acumulada a 10 años: **+38.0%** (3.3%/año).
  - Tipo de cambio interbancario promedio: S/ 3.451 en T1-16, 3.660 en T1-21 y 3.387 en T1-26.
    - El sol se apreció **7.5% en 5 años**.
    - Entre T4-24 (3.756) y T4-25 (3.384) se apreció ~10%.
  - Inflación de Lima a 12 meses en sep-2026: **4.55%**.

**Tabla 1 — Precio de oferta por m² en T1-2026 y CAGR (%/año)**
(cálculo propio sobre las series BCRP citadas arriba; versión suavizada con promedios de 4 trimestres; la punto a punto va en la tabla 1b)

| Distrito | US$/m² T1-26 | S/ /m² T1-26 | US$ nom. 5a | US$ nom. 10a | S/ nom. 5a | S/ nom. 10a | **S/ real 5a** | **S/ real 10a** |
|---|---|---|---|---|---|---|---|---|
| San Isidro | 2,605 | 8,822 | 1.5 | 1.2 | 1.1 | 1.8 | −3.2 | −1.4 |
| Barranco | 2,556 | 8,656 | 0.2 | 2.1 | −0.1 | 2.7 | −4.3 | −0.6 |
| Miraflores | 2,464 | 8,345 | 0.9 | 1.1 | 0.5 | 1.7 | −3.7 | −1.5 |
| Jesús María | 2,103 | 7,123 | **3.5** | 2.6 | **3.0** | 3.2 | **−1.3** | −0.1 |
| San Borja | 2,099 | 7,108 | 0.8 | 0.9 | 0.4 | 1.5 | −3.8 | −1.8 |
| Magdalena | 1,986 | 6,728 | 1.6 | 2.3 | 1.1 | 2.9 | −3.1 | −0.3 |
| Lince | 1,894 | 6,415 | 1.8 | **2.7** | 1.3 | **3.3** | −2.9 | **0.0** |
| Pueblo Libre | 1,875 | 6,351 | 2.3 | 2.2 | 1.8 | 2.9 | −2.4 | −0.4 |
| Surquillo | 1,856 | 6,287 | 0.8 | 1.6 | 0.4 | 2.2 | −3.8 | −1.1 |
| Surco | 1,818 | 6,158 | 0.1 | 0.1 | −0.3 | 0.7 | −4.5 | −2.5 |
| San Miguel | 1,637 | 5,546 | 2.9 | 2.6 | 2.5 | 3.2 | −1.8 | −0.1 |
| La Molina | 1,510 | 5,116 | −0.3 | 0.3 | −0.7 | 0.9 | −4.8 | −2.3 |

**Tabla 1b — CAGR punto a punto (T1 vs T1), %/año**
(mismo cálculo propio sobre BCRP)

| Distrito | US$ 5a | US$ 10a | S/ nom 5a | S/ nom 10a | S/ real 5a | S/ real 10a |
|---|---|---|---|---|---|---|
| La Molina | −0.2 | 0.8 | −1.7 | 0.6 | −5.8 | −2.6 |
| Miraflores | 2.3 | 1.4 | 0.7 | 1.2 | −3.5 | −2.0 |
| San Borja | 1.2 | 1.5 | −0.4 | 1.3 | −4.6 | −1.9 |
| San Isidro | 3.7 | 1.6 | 2.1 | 1.4 | −2.2 | −1.8 |
| Surco | 0.6 | 0.7 | −0.9 | 0.5 | −5.1 | −2.7 |
| Jesús María | 4.2 | 3.1 | 2.6 | 2.9 | −1.7 | −0.4 |
| Lince | 2.0 | 2.8 | 0.4 | 2.6 | −3.8 | −0.7 |
| Magdalena | 1.5 | 2.9 | −0.1 | 2.7 | −4.3 | −0.5 |
| Pueblo Libre | 3.6 | 2.5 | 2.0 | 2.3 | −2.3 | −0.9 |
| San Miguel | 3.4 | 3.5 | 1.8 | 3.3 | −2.5 | 0.0 |
| Barranco | 2.7 | 3.2 | 1.1 | 3.0 | −3.1 | −0.3 |
| Surquillo | 1.3 | 2.1 | −0.2 | 1.9 | −4.4 | −1.3 |

- **Agregados del propio BCRP en S/ constantes de 2009 (deflactados por el BCRP)** — [API BCRP, PD37941PQ…PD38030PQ](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD37944PQ-PD37945PQ-PD37946PQ-PD37941PQ-PD37942PQ-PD37943PQ-PD38028PQ-PD38029PQ-PD38030PQ-PD37940PQ/json/2007-4/2026-4)

  | Agregado | T1-16 | T1-21 | T1-26 | Variación 10 años | Variación 5 años |
  |---|---|---|---|---|---|
  | 12 distritos | 4,995.6 | 5,048.7 | 4,088.3 | **−18.2%** | — |
  | Sector Alto | 5,302.9 | 5,241.9 | 4,266.0 | **−19.6%** | — |
  | Sector Medio | 3,986.6 | 4,399.4 | 3,780.0 | **−5.2%** | −14.1% |

  - En dólares nominales, los mismos agregados en esas tres fechas:

    | Agregado (US$) | T1-16 | T1-21 | T1-26 | Variación 10 años |
    |---|---|---|---|---|
    | Sector Medio | 1,416.8 | 1,642.2 | 1,888.2 | **+33%** (2.9%/año) |
    | Sector Alto | 1,884.6 | 1,956.6 | 2,130.9 | **+13%** (1.2%/año) |

  - Estos agregados confirman la tabla distrital de forma independiente al cálculo propio.
- **Índice de precios hedónicos de inmuebles del BCRP (PD37940PQ)** — [API BCRP, misma consulta](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD37944PQ-PD37945PQ-PD37946PQ-PD37941PQ-PD37942PQ-PD37943PQ-PD38028PQ-PD38029PQ-PD38030PQ-PD37940PQ/json/2007-4/2026-4)

  | Fecha | Valor |
  |---|---|
  | T4-07 | 37.4 |
  | T2-14 (máximo previo a 2017) | 111.4 |
  | T1-16 | 100.4 |
  | T1-21 | 109.4 |
  | T1-26 | 119.0 (+18.5% en 10 años, ~1.7%/año nominal) |

- **Índice Urbania (en soles, avisos del portal), promedio Lima** — [Urbania, Informe de mercado julio 2025 (PDF)](https://urbania.pe/blog/wp-content/uploads/2025/08/INDEX_LIMA_REPORTE_2025-07.pdf); [Urbania, Informe noviembre 2025 (PDF)](https://urbania.pe/blog/wp-content/uploads/2025/12/INDEX_LIMA_REPORTE_2025-11.pdf); [El Comercio, 06-may-2026](https://elcomercio.pe/economia/peru/urbania-precios-de-viviendas-en-lima-muestran-una-ligera-alza-del-1-en-lo-que-va-del-2026-l-ultimas-noticia/); [Infobae, 09-may-2026](https://www.infobae.com/peru/2026/05/09/este-es-el-nuevo-distrito-mas-caro-para-comprar-un-departamento-supero-a-barranco-con-un-precio-promedio-de-s-9268/)

  | Mes | Precio medio (S/ por m²) | Comentario del informe |
  |---|---|---|
  | jul-2025 | 6,821 | +1.1% acumulado en 2025, "caída real de 0.2%" |
  | nov-2025 | 6,806 | +0.9% en 2025, por debajo de la inflación |
  | abr-2026 | 6,886 | +1.0% acumulado en 2026 |

  - La fuente de datos declarada es "Todos los anuncios de Urbania".
  - Es decir, en soles el precio medio de Lima está **prácticamente plano en nominal** desde 2025.
- **Precio por m² de distritos fuera de la muestra BCRP (Urbania, julio 2025, S/ por m², precio de oferta)** — [Urbania, julio 2025](https://urbania.pe/blog/wp-content/uploads/2025/08/INDEX_LIMA_REPORTE_2025-07.pdf)
  - Distritos medios y de Lima Top:

    | Distrito | S/ por m² | Var. 12m |
    |---|---|---|
    | La Victoria | 6,752 | +13.5% |
    | Cercado de Lima | 6,120 | +8.9% |
    | Chorrillos | 5,637 | −2.5% |
    | La Molina | 5,466 | −2.1% |
    | Breña | 5,309 | +8.7% |

  - Distritos más baratos:

    | Distrito | S/ por m² | Var. 12m |
    |---|---|---|
    | Ate | 4,517 | −1.7% |
    | La Perla | 4,279 | +7.7% |
    | Bellavista | 4,138 | +0.1% |
    | San Juan de Miraflores | 3,692 | +2.7% |
    | Los Olivos | 3,643 | −2.8% |
    | Callao | 3,374 | −5.8% |
    | San Martín de Porres | 2,934 | −6.0% |

  - Mismo informe, para comparar con los distritos BCRP:

    | Distrito | S/ por m² | Var. 12m |
    |---|---|---|
    | Barranco | 9,395 | +0.2% |
    | San Isidro | 9,285 | +1.2% |
    | Miraflores | 8,768 | +0.7% |
    | Jesús María | 7,384 | +6.4% |
    | San Borja | 7,221 | −0.9% |
    | Lince | 7,173 | −0.2% |
    | Magdalena | 6,985 | +3.9% |
    | Surquillo | 6,845 | +5.0% |
    | Surco | 6,780 | +0.5% |
    | Pueblo Libre | 6,323 | +2.3% |
    | San Miguel | 6,084 | +4.2% |
    | Promedio Lima | 6,821 | +2.0% |

  - Asigné cada nombre a su cifra porque el PDF tiene el texto desalineado. La asignación se validó contra el ranking de variaciones y el texto: "La Victoria es el de mayor incremento: +13.5%".
- **Precios por distrito de abril 2026 (Urbania/QuintoAndar, según prensa)** — [Infobae, 09-may-2026](https://www.infobae.com/peru/2026/05/09/este-es-el-nuevo-distrito-mas-caro-para-comprar-un-departamento-supero-a-barranco-con-un-precio-promedio-de-s-9268/); [El Comercio, 06-may-2026](https://elcomercio.pe/economia/peru/urbania-precios-de-viviendas-en-lima-muestran-una-ligera-alza-del-1-en-lo-que-va-del-2026-l-ultimas-noticia/)

  | Distrito o zona | S/ por m² |
  |---|---|
  | San Isidro | 9,268 |
  | Barranco | 9,169 |
  | Miraflores | 8,831 |
  | Jesús María | 7,711 |
  | Lince | 7,703 |
  | Los Olivos | 3,488 |
  | San Martín de Porres | 3,163 |
  | Callao | 2,956 |
  | San Isidro Sur (zona) | 11,947 |

  - El Comercio sitúa a "Lima Moderna" (Jesús María, Lince, Magdalena, Pueblo Libre, San Miguel, Surquillo, Cercado) "entre S/ 6,000 y S/ 7,000 por m²".
  - **Conflicto entre las dos fuentes:**
    - El Comercio atribuye 9,169 a San Isidro; Infobae, a Barranco.
    - El Comercio publica para Barranco "S/ 2,068", evidente error tipográfico.
    - Las variaciones interanuales no coinciden. Infobae: Jesús María +6.3%, Lince +6.3%, La Molina +5.8%, Los Olivos +5.6%, Magdalena −4.2%, Breña −3.3%, San Juan de Miraflores −8.9%. El Comercio: Lince +6.3%, Magdalena +6.3%, Breña +5.8%, San Juan de Miraflores +5.6%.

### Inferences
- **La moneda de cotización domina el resultado.** Los precios de Lima se cotizan en US$, mientras que la inflación y el ingreso del inversor están en soles.
  - En 10 años (suavizado), el US$/m² del sector medio subió ~1.6–2.7%/año (Surquillo 1.6%, el resto 2.2–2.7%). El del sector alto subió ~0.1–1.2%/año, salvo Barranco (2.1%).
  - La depreciación neta del sol fue mínima (−1.8% en 10 años): 3.451 → 3.387.
  - La inflación acumulada fue de 38%. Resultado: real ≈ 0 en el sector medio y negativo en el sector alto.
- **Ranking a 10 años, real suavizado.** El patrón "Lima Moderna > Lima Top" es robusto a la forma de medir (punto a punto o suavizado) y también se ve en los agregados oficiales del BCRP (Sector Medio −5% vs Sector Alto −20% real).
  - Lince 0.0%, Jesús María −0.1%, San Miguel −0.1%, Magdalena −0.3%, Pueblo Libre −0.4%, Barranco −0.6%.
  - Surquillo −1.1%, San Isidro −1.4%, Miraflores −1.5%, San Borja −1.8%, La Molina −2.3%, Surco −2.5%.
- **A 5 años, los únicos que "resisten" son Jesús María (−1.3%) y San Miguel (−1.8%).** Pueblo Libre (−2.4%) va tercero. La Molina y Surco son los peores (−4.5% a −4.8%).
- **No hay evidencia de que Miraflores o Barranco hayan sido la mejor compra en precio.** Barranco solo destaca en punto a punto a 10 años (3.2% US$) por un T1-16 bajo; suavizado está en la media.

### Gaps
- **CAGR real en dólares (deflactado por el IPC de EE.UU.).** No pude descargar el CPI-U (FRED/BLS no accesibles desde el entorno) y no lo invento. Para el redactor: el CAGR real en US$ = (1+CAGR nominal US$)/(1+inflación de EE.UU.) − 1. Con la inflación de EE.UU. de 2021-2026, el real en US$ sería claramente negativo a 5 años en casi todos los distritos.
- No existe serie BCRP por distrito para Breña, Cercado, Chorrillos, Los Olivos, Callao/Bellavista, San Juan de Miraflores, SMP ni La Victoria. Para ellos solo tengo cortes puntuales de Urbania (julio 2025) y prensa de 2026, sin series de 5 o 10 años.
- No encontré serie histórica de precios de transacción (registral, SUNARP o tasaciones) por distrito. Tinsa y Nexo no publican series largas por distrito de acceso abierto.
- Los informes mensuales de Urbania de 2026 en PDF no aparecieron con el patrón de URL habitual. Probé ene–sep 2026 sin éxito; las cifras de 2026 vienen de prensa.

## 2. Rentabilidad bruta por alquiler y PER (precio / alquiler anual) por distrito

### Takeaway
La rentabilidad bruta de Lima ronda **5.3–6.0%** según la fuente: Urbania 5.25–5.53%, BCRP PER 16.7 ≈ 6.0%. Las fuentes coinciden en que **Surquillo, Lince, Magdalena y Cercado de Lima** rinden más (6–6.7%) y que **Surco, Miraflores, San Borja y San Isidro** rinden menos (4.8–5.6%). Pueblo Libre está en la media (~5.2–5.9%).

### Cited Findings
- **PER del BCRP por distrito**, serie "Indicador Precio de Venta/Alquiler Anual – PER", 12 distritos + promedio, desde T3/T4-2013, último dato T1-2026. La rentabilidad bruta implícita es 1/PER — [API BCRP, PD41940PQ…PD41952PQ](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD41940PQ-PD41941PQ-PD41942PQ-PD41943PQ-PD41944PQ-PD41945PQ-PD41946PQ-PD41947PQ-PD41948PQ-PD41949PQ-PD41950PQ-PD41951PQ-PD41952PQ/json/2013-1/2026-4)

| Distrito | PER T1-26 | Rent. bruta T1-26 | PER prom. 4T | Rent. prom. 4T | PER medio 10a (T2-16→T1-26) | Rent. media 10a |
|---|---|---|---|---|---|---|
| Surquillo | 15.0 | **6.7%** | 15.0 | 6.7% | 16.6 | 6.0% |
| Lince | 15.1 | **6.6%** | 14.6 | **6.9%** | 16.1 | **6.2%** |
| Magdalena | 15.4 | 6.5% | 15.6 | 6.4% | 17.0 | 5.9% |
| La Molina | 15.5 | 6.4% | 16.3 | 6.1% | 19.5 | 5.1% |
| San Isidro | 16.7 | 6.0% | 16.3 | 6.1% | 18.4 | 5.4% |
| Pueblo Libre | 16.9 | 5.9% | 17.1 | 5.9% | 17.5 | 5.7% |
| Barranco | 17.0 | 5.9% | 16.6 | 6.0% | 18.0 | 5.6% |
| San Miguel | 17.4 | 5.7% | 16.4 | 6.1% | 16.8 | 6.0% |
| Jesús María | 17.5 | 5.7% | 16.5 | 6.0% | 16.8 | 6.0% |
| San Borja | 17.6 | 5.7% | 18.3 | 5.5% | 20.3 | 4.9% |
| Miraflores | 17.8 | 5.6% | 17.1 | 5.9% | 18.5 | 5.4% |
| Surco | 18.2 | 5.5% | 18.1 | 5.5% | 19.6 | 5.1% |
| **Promedio** | **16.7** | **6.0%** | 16.5 | 6.1% | — | — |

(PER tomado del BCRP; las rentabilidades, los promedios y las medias son cálculo propio)

- **Evolución del PER promedio del BCRP** — [misma API](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD41940PQ-PD41941PQ-PD41942PQ-PD41943PQ-PD41944PQ-PD41945PQ-PD41946PQ-PD41947PQ-PD41948PQ-PD41949PQ-PD41950PQ-PD41951PQ-PD41952PQ/json/2013-1/2026-4)

  | Fecha | PER promedio |
  |---|---|
  | T1-14 | 16.5 |
  | T1-16 | 16.7 |
  | T1-18 | 17.1 |
  | T1-20 | 16.6 |
  | T1-21 | 19.6 |
  | T1-22 | 19.2 |
  | T1-23 | 18.0 |
  | T1-24 | 17.7 |
  | T1-25 | 17.1 |
  | T1-26 | 16.7 |

  - Rango histórico 2013–2026: 15.9 (mínimo) a 21.2 (máximo, en 2021-22).
  - El PER volvió a su media de largo plazo: la rentabilidad bruta subió de ~5.1% (2021) a ~6.0% (2026).
- **Urbania, julio 2025** (avisos del portal; alquiler de un departamento estándar de 100 m²) — [Urbania, julio 2025](https://urbania.pe/blog/wp-content/uploads/2025/08/INDEX_LIMA_REPORTE_2025-07.pdf)
  - Rentabilidad de Lima: **5.29% bruta**, 18.9 años para repagar.
  - "Lince y Surquillo son los distritos con mayor retorno" (~6.1% y ~6.0%).
  - En la cola están San Borja, San Isidro, Miraflores y Surco (~4.8–4.9%). Pueblo Libre ~5.2%, alrededor del promedio.
  - "Lince Comercial es la mejor zona para los inversores que buscan renta" (7.0%), seguida de San Miguel Costanera (6.6%).
- **Alquileres por distrito, Urbania julio 2025** (S/ por mes, departamento de 100 m², y variación a 12 meses) — [Urbania, julio 2025](https://urbania.pe/blog/wp-content/uploads/2025/08/INDEX_LIMA_REPORTE_2025-07.pdf)

  | Distrito | S/ por mes | Var. 12m |
  |---|---|---|
  | Barranco | 4,181 | +4.8% |
  | San Isidro | 3,806 | +4.1% |
  | Lince | 3,618 | +10.0% |
  | Miraflores | 3,602 | +6.4% |
  | Surquillo | 3,497 | +8.1% |
  | Magdalena | 3,449 | **+16.0%** |
  | Jesús María | 3,398 | +10.1% |
  | **Lima** | **3,206** | **+6.8%** |
  | Cercado | 3,063 | +5.0% |
  | San Miguel | 2,887 | +11.2% |
  | San Borja | 2,875 | +5.9% |
  | Pueblo Libre | 2,786 | +6.1% |
  | Surco | 2,675 | +4.1% |
  | Chorrillos | 2,473 | +8.5% |
  | La Molina | 2,370 | +2.3% |
  | Los Olivos | 1,595 | +8.7% |

  - Mapeo de nombres a cifras validado con el texto: "Magdalena del Mar es el distrito con mayor incremento: +16.0%".
  - Según el informe, el alquiler subió "muy por arriba de la inflación": +5.3% real a 12 meses.
- **Urbania, noviembre 2025** — [Urbania, noviembre 2025](https://urbania.pe/blog/wp-content/uploads/2025/12/INDEX_LIMA_REPORTE_2025-11.pdf)
  - Rentabilidad de Lima: 5.25%; 19.1 años para repagar.
  - "La Molina y Surquillo son los distritos con mayor retorno".
  - Alquiler de 100 m²: S/ 3,185 por mes.
- **Último dato de 2026, índice Urbania** (Infobae, 21/22-ago-2026; alquiler a julio-2026) — [Infobae, ago-2026](https://www.infobae.com/peru/2026/08/22/comprar-departamentos-para-alquilar-en-lima-que-distritos-ofrecen-mayor-rentabilidad/)
  - Lima: rentabilidad bruta **5.53%**, 18.1 años para repagar.
  - Alquiler de 100 m²: **S/ 3,439 al mes**. Los alquileres suben **+6.6% en 2026**, frente a una inflación acumulada de 3.7%.
  - Por distrito:

    | Distrito | Rentabilidad bruta |
    |---|---|
    | Surquillo | **6.3%** |
    | Cercado de Lima | **6.3%** |
    | Lince | 5.9% |
    | San Miguel | 5.9% |
    | Magdalena | 5.8% |
    | La Molina | 5.7% |
    | San Borja | 5.6% |
    | Jesús María | 5.6% |

  - Por zona: Lince Comercial 7.3%, Surquillo Centro 7.1%, San Miguel Noroeste 6.8%.
  - El artículo no da la cifra de Pueblo Libre, Miraflores, San Isidro, Barranco ni Surco.
- **Otra edición de 2026** (índice M2 de Urbania, may-2026, vía resumen de buscador; no verificado en el texto original) — [Urbania blog](https://urbania.pe/blog/cercado-y-lince-muestran-la-mayor-rentabilidad/); [Construir](https://construir.com.pe/cercado-de-lima-y-surquillo-son-los-distritos-con-la-mayor-rentabilidad-de-lima/)
  - Rentabilidad de Lima: 5.2%.
  - Cercado de Lima ~6.9%; San Isidro y San Borja 4.1%.

### Inferences
- **El BCRP da ~0.5–0.8 pp más rentabilidad que Urbania** para el mismo mes y la misma fuente de avisos (6.0% vs 5.3–5.5%). Probablemente se debe al método: medianas de m² en venta y en alquiler por distrito, frente a un departamento estándar de 100 m². Recomiendo tratar 5.5–6% como rango central de Lima.
- **El ranking relativo es estable entre fuentes y años.**
  - Más renta: Surquillo, Lince, Magdalena y Cercado (+ San Miguel).
  - Menos renta: Surco, San Borja, Miraflores y San Isidro.
  - La Molina es inestable: alta en 2025-26 en ambas fuentes, pero con PER medio de 19.5 a 10 años.
- **Pueblo Libre no destaca por renta.** Su PER medio de 10 años (17.5) es peor que el de Lince, Surquillo, San Miguel, Jesús María y Magdalena.
- **Son rentabilidades brutas sobre precios de oferta.** Si el precio de cierre es menor que el de oferta, la rentabilidad sobre el precio pagado sería algo mayor. Vacancia, mantenimiento, arbitrios e impuestos la reducen (cubiertos en la nota financiamiento_costos_impuestos.md).

### Gaps
- No hay PER oficial para distritos fuera de la muestra BCRP: Breña, Chorrillos, Los Olivos, Callao/Bellavista. Urbania da cifras puntuales para Chorrillos (~5.4%), Los Olivos (~5.0%) y Cercado, pero los PDF están desalineados y la precisión es de ±0.1–0.2 pp.
- No encontré datos de tasas de vacancia ni de tiempo medio para alquilar por distrito.

## 3. Momentum 2024–2026: precios, ventas, absorción — ¿Pueblo Libre está superando al resto?

### Takeaway
En 2025-26 los **precios en US$** se aceleraron con fuerza en Lima Moderna y en San Isidro: Jesús María +12%, San Miguel +9%, Magdalena +9%, San Isidro +8.5% y Pueblo Libre +6.6% a/a, promedio de 4 trimestres. **En soles reales casi todo ese impulso desaparece** por la apreciación del sol (~10% en 2025): solo Jesús María (+2.6%) y San Miguel (+0.1%) suben en términos reales. Por volumen, el líder de ventas de Lima Moderna en 2026 es **Jesús María**, seguido de San Miguel y Surquillo; **Pueblo Libre es 4.º**. Pueblo Libre lideró el *crecimiento* de ventas en 2024 (+53.5%), pero no lidera ni en precio ni en volumen en 2025-26.

### Cited Findings
- **US$/m² por trimestre, BCRP** — [API BCRP precios por distrito](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD17459PQ-PD17460PQ-PD17461PQ-PD17462PQ-PD17463PQ-PD17464PQ-PD17465PQ-PD17466PQ-PD17467PQ-PD17468PQ-PD37957PQ-PD37958PQ/json/2007-4/2026-4)

| Distrito | T1-23 | T1-24 | T1-25 | T2-25 | T3-25 | T4-25 | T1-26 | a/a T1 (US$) | a/a prom. 4T (US$) | a/a prom. 4T (S/ real) |
|---|---|---|---|---|---|---|---|---|---|---|
| Jesús María | 1,651 | 1,781 | 1,749 | 1,805 | 1,949 | 2,086 | 2,103 | +20.3% | **+12.1%** | **+2.6%** |
| San Miguel | 1,419 | 1,417 | 1,418 | 1,464 | 1,537 | 1,697 | 1,637 | +15.5% | +9.3% | +0.1% |
| Magdalena | 1,726 | 1,743 | 1,730 | 1,820 | 1,818 | 1,880 | 1,986 | +14.8% | +8.6% | −0.5% |
| Barranco | 2,200 | 2,095 | 2,376 | 2,490 | 2,373 | 2,463 | 2,556 | +7.6% | +8.6% | −0.4% |
| San Isidro | 2,136 | 2,300 | 2,144 | 2,300 | 2,272 | 2,461 | 2,605 | +21.5% | +8.5% | −0.6% |
| Pueblo Libre | 1,474 | 1,652 | 1,653 | 1,653 | 1,667 | 1,717 | 1,875 | +13.4% | +6.6% | −2.4% |
| Miraflores | 2,149 | 2,177 | 2,230 | 2,212 | 2,250 | 2,400 | 2,464 | +10.5% | +5.5% | −3.4% |
| Surquillo | 1,683 | 1,708 | 1,732 | 1,753 | 1,768 | 1,849 | 1,856 | +7.2% | +5.3% | −3.5% |
| San Borja | 1,929 | 1,845 | 1,944 | 1,912 | 1,962 | 2,000 | 2,099 | +7.9% | +4.7% | −4.1% |
| Surco | 1,750 | 1,676 | 1,706 | 1,700 | 1,730 | 1,873 | 1,818 | +6.6% | +4.6% | −4.2% |
| Lince | 1,871 | 1,828 | 1,838 | 1,798 | 1,850 | 1,970 | 1,894 | +3.1% | +3.0% | −5.6% |
| La Molina | 1,411 | 1,538 | 1,451 | 1,500 | 1,510 | 1,392 | 1,510 | +4.1% | −2.3% | −10.4% |

(las variaciones son cálculo propio; IPC Lima T1-26 vs T1-25: +2.58%)

- **Ventas 2024 (Capeco)** — [Gestión, 28-feb-2025](https://gestion.pe/economia/venta-de-viviendas-en-lima-los-distritos-y-tamanos-de-departamentos-que-destacan-construccion-creditos-hipotecaros-noticia/)
  - Lima: 20,975 viviendas (+23.3%), "mejor resultado en once años".
  - Mayores aumentos de ventas por distrito: **Pueblo Libre +53.5%**, Cercado de Lima +50.9%, Miraflores +41.8%, Lince +37.6%, Jesús María +32.3%. El artículo no da unidades por distrito.
  - Precio por m² en 2024: +1.3%, por debajo de la inflación de 2.0%.
  - Indicador de Capeco: por encima de 2.5 hay sobreoferta; el mercado "aún" estaba en sobreoferta, pero tendía a estabilizarse.
- **Ventas 1S-2025 (CODIP)** — [El Comercio, 02-oct-2025](https://elcomercio.pe/economia/crecimiento-en-peligro-sin-mas-oferta-el-boom-del-sector-construccion-en-lima-top-y-moderna-podria-volverse-insostenible-y-disparar-el-precio-de-los-departamentos-noticia/)
  - Lima Top: 3,473 unidades. Lima Moderna: 4,796 unidades. Ambas por encima de 1S-2024.
  - Según Capeco (II-T 2025), los indicadores de oferta y venta están "en niveles de equilibrio", con riesgo de escasez si sigue bajando el ingreso de proyectos nuevos.
- **Ventas ene–abr 2026, Lima Moderna (CODIP, Real Estate Data Analytics)** — [Costos Perú, 08-jun-2026](https://revista-ps.costosperu.com/venta-de-viviendas-en-lima-moderna-crece-25-y-supera-las-4200-unidades-en-el-2026/)
  - Total: 4,271 unidades (**+25% a/a**).
  - Por distrito:

    | Distrito | Unidades vendidas |
    |---|---|
    | **Jesús María** | **1,070** |
    | San Miguel | 889 |
    | Surquillo | 724 |
    | **Pueblo Libre** | **619** |
    | Magdalena | 559 |

  - Valor de ventas: S/ 1,787 millones, frente a S/ 1,462 millones un año antes.
- **Distritos premium, ene–feb 2026 (CODIP)** — [Gestión](https://gestion.pe/economia/empresas/ventas-de-departamentos-en-distritos-premium-crecen-en-primera-etapa-del-2026-noticia/); [Construir](https://construir.com.pe/ventas-de-viviendas-en-distritos-premium-crecen-6-6-a-inicios-de-2026-en-lima/)
  - Miraflores, San Isidro, Surco, San Borja y Barranco: 1,099 ventas (+6.6% a/a).
  - Precio medio de Lima Top: S/ 8,625 por m², "ligeramente por debajo de 2025".
  - Cifras tomadas del resumen del buscador; no abrí el texto completo.
- **Mercado total 1S-2026 (CODIP)**: 15,477 viviendas nuevas vendidas en Lima Metropolitana y Callao (+26% a/a) — [Infobae, 13-oct-2026](https://www.infobae.com/peru/2026/10/13/millennials-lideran-la-compra-de-departamentos-este-2026-estos-son-los-distritos-a-los-que-apuntan/). Tomado del resumen del buscador; no verifiqué el texto completo.
- **Departamentos de 1 dormitorio (Tinsa, datos 2025).** Las ventas se concentran en Cercado de Lima (18.0%), Miraflores (13.4%), San Isidro (10.2%), Lince (8.9%), Surquillo (7.8%) y Jesús María — [Gestión](https://gestion.pe/economia/empresas/uno-de-cada-4-departamentos-que-se-venden-tiene-1-dormitorio-que-distritos-concentran-la-oferta-noticia/). Tomado del resumen del buscador.
- **Momentum fuera de la muestra BCRP (Urbania)** — [Urbania, julio 2025](https://urbania.pe/blog/wp-content/uploads/2025/08/INDEX_LIMA_REPORTE_2025-07.pdf); [Urbania, noviembre 2025](https://urbania.pe/blog/wp-content/uploads/2025/12/INDEX_LIMA_REPORTE_2025-11.pdf)
  - Variación a 12 meses en julio 2025: La Victoria **+13.5%**, Cercado +8.9%, Breña +8.7%, La Perla +7.7%.
  - En noviembre 2025, "La Victoria es el de mayor incremento: +14.9%", y solo el 42% de los distritos subía a/a.
  - En la cola estaban Callao (−5.8%), SMP (−6.0%) y Los Olivos (−2.8%).
- **Proyección de BBVA Research** (Observatorio Inmobiliario, nov-2025, citado por un portal de bienes raíces de lujo): precios reales +2% a +4% en 2026 — [Penthouse.pe](https://penthouse.pe/burbuja-o-ciclo-mercado-lujo-lima-2026-bcrp-asei/). Fuente secundaria y además una proyección; no la verifiqué en el original.

### Inferences
- **Veredicto sobre Pueblo Libre: hipótesis parcialmente refutada.**
  - Lo que sí: Pueblo Libre supera a Miraflores, Barranco, San Isidro, Surco, San Borja y La Molina en valorización real a 10 años (−0.4% vs −0.6% a −2.5%). Fue el distrito con mayor crecimiento de ventas en 2024.
  - Lo que no: no es el mejor de su grupo.
    - Precio, 5 y 10 años: lo superan Jesús María y San Miguel, y Lince a 10 años.
    - Momentum de 2025-26 (en US$ y en soles reales): lo superan Jesús María, San Miguel y Magdalena.
    - Volumen de ventas de 2026: es 4.º.
    - Renta: tiene un PER más alto (menos renta) que Lince, Surquillo, Magdalena, San Miguel y Jesús María.
- **El "salto" de Pueblo Libre en T1-26** (1,717 → 1,875 US$/m², +9% en un trimestre) es un solo dato de mediana trimestral. Hasta ver T2/T3-2026 no lo trataría como cambio de tendencia: el PER de Pueblo Libre en T4-25 cayó a 14.9 y volvió a 16.9, señal de ruido muestral.
- **El distrito con evidencia más consistente de momentum es Jesús María.** Lidera la CAGR real a 5 años, la variación a/a real de 2025-26 y las ventas de 2026; a 10 años es el que menos cayó desde el pico (−3.6% real). San Miguel es segundo en casi todo y además es el más barato de la muestra del BCRP (S/ 5,546 por m²).
- **Momentum atípico fuera de la muestra BCRP: La Victoria, Cercado y Breña**, en el índice de Urbania de 2025. Sin series largas no se puede distinguir si es tendencia o efecto de composición (proyectos nuevos que entran al índice).
- **Para un inversor que gana en soles, el fuerte alza en US$ de 2025-26 es en buena parte una ilusión cambiaria.** Si el sol se depreciara, el efecto se invertiría a su favor.

### Gaps
- **No encontré datos públicos de meses de oferta ni de absorción mensual por distrito para 2025-2026** de Tinsa, Capeco, BBVA Research ni Nexo. Solo están el indicador agregado de Capeco (sobreoferta > 2.5) y una tasa de absorción de un blog comercial (AAMI) que no considero fiable.
- No tengo ventas por distrito de 2026 para Lince, Cercado, Breña, Chorrillos ni Lima Top desagregado.
- No consulté YouTube por limitación de presupuesto de herramientas.

## 4. Ciclo completo: el pico de 2014-2016, la pandemia y si Lima le ganó a la inflación

### Takeaway
Depende del punto de entrada.
- **Desde 2007**, la valorización real fue muy alta: 3.0–6.1%/año, por el boom 2007-2014: entre T4-2007 y T1-2013 el US$/m² se multiplicó ×2.4–3.0.
- **Comprando en el pico de 2014-2016**, hoy se pierde en términos reales en todos los distritos. Las caídas van de −4% (Jesús María) a −20/−26% (Barranco, Lince, Surco, La Molina). En dólares nominales, el sector medio sí superó el pico (de +6% en Lince a +29% en Jesús María) y el sector alto apenas (−9% a +11%).
- **Solo con renta incluida** el ciclo completo de 10 años bate al IPC (ver sección 6).

### Cited Findings
- **Boom 2007-2013 (US$/m², BCRP)** — [API BCRP precios por distrito](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD17459PQ-PD17460PQ-PD17461PQ-PD17462PQ-PD17463PQ-PD17464PQ-PD17465PQ-PD17466PQ-PD17467PQ-PD17468PQ-PD37957PQ-PD37958PQ/json/2007-4/2026-4)

  | Distrito | T4-07 | T1-13 |
  |---|---|---|
  | Miraflores | 720 | 2,000 |
  | San Isidro | 720 | 1,999 |
  | Pueblo Libre | 493 | 1,188 |
  | Lince | 400 | 1,161 |
  | Jesús María | 489 | 1,382 |

- **CAGR desde T4-2007 hasta T1-2026** (cálculo propio sobre BCRP)

  | Distrito | Real en soles (%/año) | US$ nominal (%/año) |
  |---|---|---|
  | Lince | 6.1 | 8.9 |
  | Magdalena | 5.6 | 8.3 |
  | Jesús María | 5.5 | 8.3 |
  | Pueblo Libre | 4.8 | 7.6 |
  | San Isidro | 4.5 | 7.3 |
  | Miraflores | 4.2 | 7.0 |
  | San Miguel | 4.1 | 6.8 |
  | San Borja | 3.6 | 6.4 |
  | La Molina | 3.5 | 6.2 |
  | Surco | 3.0 | 5.7 |

  - Real desde T1-2010: 1.6% (La Molina) a 3.9% (Magdalena).
  - Real desde T1-2013: −0.6% (Surco) a 2.6% (Lince); Pueblo Libre 2.4%, 2.º.
- **Desde el pico 2013-2016 hasta T1-2026** (cálculo propio sobre BCRP; el máximo es de un solo trimestre, así que exagera la caída por ruido)

  | Distrito | Pico real (S/ de T1-26) | Hoy | Var. real | Pico US$ | Hoy US$ | Var. US$ |
  |---|---|---|---|---|---|---|
  | Jesús María | T1-16: 7,388 | 7,123 | **−3.6%** | T4-14: 1,630 | 2,103 | **+29.0%** |
  | San Miguel | T3-15: 5,922 | 5,546 | −6.4% | T1-14: 1,330 | 1,637 | +23.1% |
  | Pueblo Libre | T1-16: 6,983 | 6,351 | −9.1% | T1-16: 1,467 | 1,875 | +27.8% |
  | Magdalena | T4-16: 7,648 | 6,728 | −12.0% | T4-16: 1,669 | 1,986 | +19.0% |
  | Surquillo | T3-15: 7,293 | 6,287 | −13.8% | T3-15: 1,616 | 1,856 | +14.9% |
  | San Isidro | T1-16: 10,543 | 8,822 | −16.3% | T2-14: 2,357 | 2,605 | +10.5% |
  | San Borja | T1-16: 8,639 | 7,108 | −17.7% | T2-14: 2,017 | 2,099 | +4.0% |
  | Miraflores | T1-16: 10,220 | 8,345 | −18.3% | T2-14: 2,328 | 2,464 | +5.9% |
  | Barranco | T4-16: 10,829 | 8,656 | −20.1% | T4-16: 2,363 | 2,556 | +8.2% |
  | Lince | T3-16: 8,144 | 6,415 | −21.2% | T3-16: 1,789 | 1,894 | +5.8% |
  | Surco | T4-15: 8,191 | 6,158 | −24.8% | T2-14: 1,991 | 1,818 | −8.7% |
  | La Molina | T4-16: 6,875 | 5,116 | **−25.6%** | T1-14: 1,604 | 1,510 | **−5.8%** |

- **Agregados oficiales del BCRP** — [API BCRP agregados](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD37944PQ-PD37945PQ-PD37946PQ-PD37941PQ-PD37942PQ-PD37943PQ-PD38028PQ-PD38029PQ-PD38030PQ-PD37940PQ/json/2007-4/2026-4)
  - "12 distritos" en S/ constantes de 2009 (deflactados por el BCRP):

    | Fecha | S/ constantes 2009 |
    |---|---|
    | T1-13 | 3,921.8 |
    | T1-16 (máximo) | 4,995.6 |
    | T1-21 | 5,048.7 |
    | T1-26 | 4,088.3 |

  - En US$, el máximo previo a 2017 fue T2-14 (1,951.5) y hoy está en 2,042.2.
  - Índice hedónico: máximo de T2-14 en 111.4, mínimo cercano a 100 en 2016 y 119.0 en T1-26.
- **Pandemia y post-pandemia (2020-2025)** — [API BCRP IPC](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN38705PM-PN01273PM/json/2007-1/2026-10); [API BCRP tipo de cambio](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01205PM-PN01206PM-PN01207PM-PN01210PM/json/2007-1/2026-10)
  - Tipo de cambio promedio de T4: 3.363 (2019), 3.603 (2020), **4.024 (2021)**, 3.895 (2022), 3.780 (2023), 3.756 (2024), **3.384 (2025)**.
  - Inflación de Lima, T4 contra T4: 1.95% (2020), 5.97% (2021), **8.39% (2022)**, 3.74% (2023), 2.08% (2024), 1.41% (2025).
  - Con precios estables en US$, la depreciación de 2020-21 elevó los precios en soles: el agregado real del Sector Medio subió a 4,399 en T1-21.
  - Después, la inflación de 2021-23 y la apreciación del sol de 2025 los bajaron: Sector Medio real 3,780 en T1-26 (−14% desde T1-21).
- **Urbania:** en 2025 el precio de venta medio en soles acumuló +0.9% a +1.1%, "por debajo de la inflación derivando en una caída real", mientras los alquileres subían por encima de la inflación — [Urbania, julio 2025](https://urbania.pe/blog/wp-content/uploads/2025/08/INDEX_LIMA_REPORTE_2025-07.pdf); [Urbania, noviembre 2025](https://urbania.pe/blog/wp-content/uploads/2025/12/INDEX_LIMA_REPORTE_2025-11.pdf)

### Inferences
- **En términos reales, Lima tuvo un solo gran episodio de valorización: 2007-2014.** Desde entonces el precio real ha caído o, en el mejor caso, se ha mantenido. Un comprador que entra en 2026 no debería extrapolar las CAGR desde 2007.
- **La pandemia no produjo una caída en US$.** Los precios en US$ se mantuvieron; el efecto en soles fue cambiario: subida en 2020-21 y luego reversión. El golpe real vino de la inflación de 2021-22 (~14% acumulado) sin traslado a precios en US$.
- **Durante 10 años el precio real de Lima Top cayó ~1.5–2.5%/año mientras el PER bajaba de ~20 a ~17.** Es decir, el ajuste se hizo vía precio y no vía alquileres. Hoy el precio está "barato" frente a su historia reciente, pero sin evidencia de reversión.

### Gaps
- La muestra del BCRP empieza en 2007 (Barranco y Surquillo, en 2013); no hay series de largo plazo para Lima Norte, Lima Este, Lima Sur ni Callao.
- No pude calcular los rendimientos reales en dólares (falta el IPC de EE.UU.; ver sección 1).

## 5. Precio típico hoy de un departamento de 1-2 dormitorios (60-80 m²) por distrito y alcance de una inicial de S/ 50,000

### Takeaway
Con precios de oferta de T1-2026, un departamento de 70 m² cuesta:
- **Lima Moderna:** S/ 390–500 mil. Una inicial de S/ 50k es ~10–13% del precio.
- **Lima Top:** S/ 430–620 mil. Es 8–12%.
- **Lima Norte y Callao:** S/ 205–290 mil. Es 17–24%.

En proyectos nuevos de Lima Moderna, las unidades más pequeñas parten de S/ 154–249 mil (CODIP, 2026).

### Cited Findings
- **Precio implícito por superficie, mediana de oferta BCRP T1-2026** (cálculo propio: S/ por m² × m²) — [API BCRP precios por distrito](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD17459PQ-PD17460PQ-PD17461PQ-PD17462PQ-PD17463PQ-PD17464PQ-PD17465PQ-PD17466PQ-PD17467PQ-PD17468PQ-PD37957PQ-PD37958PQ/json/2007-4/2026-4)

| Distrito | S/ por m² | 60 m² | 70 m² | 80 m² | S/ 50k como % del de 70 m² |
|---|---|---|---|---|---|
| San Isidro | 8,822 | 529k | 618k | 706k | 8.1% |
| Barranco | 8,656 | 519k | 606k | 692k | 8.3% |
| Miraflores | 8,345 | 501k | 584k | 668k | 8.6% |
| Jesús María | 7,123 | 427k | 499k | 570k | 10.0% |
| San Borja | 7,108 | 426k | 498k | 569k | 10.0% |
| Magdalena | 6,728 | 404k | 471k | 538k | 10.6% |
| Lince | 6,415 | 385k | 449k | 513k | 11.1% |
| Pueblo Libre | 6,351 | 381k | 445k | 508k | 11.2% |
| Surquillo | 6,287 | 377k | 440k | 503k | 11.4% |
| Surco | 6,158 | 369k | 431k | 493k | 11.6% |
| San Miguel | 5,546 | 333k | 388k | 444k | 12.9% |
| La Molina | 5,116 | 307k | 358k | 409k | 14.0% |

- **Distritos fuera de la muestra BCRP** (S/ por m² de Urbania, julio 2025, × m²; cálculo propio) — [Urbania, julio 2025](https://urbania.pe/blog/wp-content/uploads/2025/08/INDEX_LIMA_REPORTE_2025-07.pdf)

| Distrito | S/ por m² | 60 m² | 70 m² | 80 m² | S/ 50k como % del de 70 m² |
|---|---|---|---|---|---|
| La Victoria | 6,752 | 405k | 473k | 540k | 10.6% |
| Cercado de Lima | 6,120 | 367k | 428k | 490k | 11.7% |
| Chorrillos | 5,637 | 338k | 395k | 451k | 12.7% |
| Breña | 5,309 | 319k | 372k | 425k | 13.5% |
| Ate | 4,517 | 271k | 316k | 361k | 15.8% |
| La Perla | 4,279 | 257k | 300k | 342k | 16.7% |
| Bellavista | 4,138 | 248k | 290k | 331k | 17.3% |
| San Juan de Miraflores | 3,692 | 222k | 258k | 295k | 19.3% |
| Los Olivos | 3,643 | 219k | 255k | 291k | 19.6% |
| Callao | 3,374 | 202k | 236k | 270k | 21.2% |
| San Martín de Porres | 2,934 | 176k | 205k | 235k | 24.3% |

- **Coherencia entre fuentes.** El BCRP de T1-26 y Urbania de julio 2025 están muy cerca para Pueblo Libre (S/ 6,351 vs 6,323 por m²); ambos usan avisos de Urbania. Para Jesús María (7,123 vs 7,384) y Miraflores (8,345 vs 8,768) la diferencia es de 3–5%, por método (mediana del BCRP vs índice de Urbania).
- **Referencias de Urbania para Lima.**
  - Abril 2026: departamento de 2 dormitorios y 60 m², **S/ 429 mil**; de 3 dormitorios y 100 m², S/ 661 mil — [Infobae, 09-may-2026](https://www.infobae.com/peru/2026/05/09/este-es-el-nuevo-distrito-mas-caro-para-comprar-un-departamento-supero-a-barranco-con-un-precio-promedio-de-s-9268/)
  - Julio 2025: S/ 424 mil y S/ 657 mil, respectivamente — [Urbania, julio 2025](https://urbania.pe/blog/wp-content/uploads/2025/08/INDEX_LIMA_REPORTE_2025-07.pdf)
- **Precios "desde" en proyectos nuevos, ene–abr 2026 (CODIP)**: San Miguel S/ 154,261; Lince S/ 205,540; Pueblo Libre S/ 212,710; Jesús María S/ 217,785; Surquillo S/ 246,500; Magdalena S/ 248,762 — [Costos Perú, 08-jun-2026](https://revista-ps.costosperu.com/venta-de-viviendas-en-lima-moderna-crece-25-y-supera-las-4200-unidades-en-el-2026/). Corresponden a las unidades más pequeñas (posiblemente de 1 dormitorio o menos de 50 m²), no a 60–80 m².
- **Contexto de tamaños.** El 17.9% de las viviendas ofertadas mide hasta 50 m² y el tamaño medio viene cayendo, con más fuerza en Lima Top (Capeco 2024) — [Gestión, 28-feb-2025](https://gestion.pe/economia/venta-de-viviendas-en-lima-los-distritos-y-tamanos-de-departamentos-que-destacan-construccion-creditos-hipotecaros-noticia/)

### Inferences
- **Con S/ 50k de inicial y financiamiento al 90%, el techo realista para 60–70 m² es S/ 500k.** Alcanza Lima Moderna completa (San Miguel, Surquillo, Pueblo Libre, Lince, Magdalena, y Jesús María justo en el límite) y Surco o La Molina. Miraflores, Barranco y San Isidro a 70 m² requieren 8–9% de inicial; a 60 m² o menos sí son accesibles.
- **Al 10% de inicial**, S/ 50k da para unos S/ 500k de precio. **Al 20%**, el tope baja a S/ 250k, que en 60–70 m² solo se encuentra en Lima Norte, Callao, San Juan de Miraflores o con unidades de menos de 40 m² en Lima Moderna. El detalle de financiamiento está en financiamiento_costos_impuestos.md.
- **Son precios de oferta y medianas de stock mixto** (nuevo y usado). Un proyecto nuevo en Jesús María o Magdalena suele cotizar por encima de la mediana distrital; un usado de los años 70–90, por debajo.

### Gaps
- No encontré el descuento típico entre el precio de oferta y el de cierre en Lima, ni datos de tasación por distrito para 2026.
- Las cifras para distritos fuera de la muestra BCRP son de julio 2025 (S/ por m² de Urbania). No tengo un corte por distrito de 2026 equivalente y completo; la prensa de mayo-2026 trae cifras parciales y contradictorias.

## 6. Retorno total (valorización + renta) por distrito y veredicto sobre la hipótesis "distritos emergentes > Miraflores/Barranco"

### Takeaway
Combinando la CAGR real de precio y la rentabilidad bruta media del período, el **retorno total real bruto a 10 años** sale de unos **6% en Lince, Jesús María y San Miguel** frente a **~4% en Miraflores y San Isidro** y **2.5–3% en Surco y La Molina**. La hipótesis del usuario se **confirma para el sector medio en conjunto**, pero **no para Pueblo Libre en particular**: es 5.º de 12 (5.3%), detrás de Lince, Jesús María, San Miguel y Magdalena.

### Cited Findings
- **Retorno total real bruto ≈ (1 + CAGR real suavizada) × (1 + rentabilidad bruta media del período) − 1.** Cálculo propio con las series BCRP de precio, PER, IPC y tipo de cambio citadas en las secciones 1 y 2 — [API BCRP precios por distrito](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD17459PQ-PD17460PQ-PD17461PQ-PD17462PQ-PD17463PQ-PD17464PQ-PD17465PQ-PD17466PQ-PD17467PQ-PD17468PQ-PD37957PQ-PD37958PQ/json/2007-4/2026-4); [API BCRP PER](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD41940PQ-PD41941PQ-PD41942PQ-PD41943PQ-PD41944PQ-PD41945PQ-PD41946PQ-PD41947PQ-PD41948PQ-PD41949PQ-PD41950PQ-PD41951PQ-PD41952PQ/json/2013-1/2026-4)

| Distrito | Precio real 10a | Rent. bruta media 10a | **Retorno total real 10a** | Precio real 5a | Rent. media 5a | **Retorno total real 5a** | Rent. bruta actual (prom. 4T) |
|---|---|---|---|---|---|---|---|
| Lince | 0.0% | 6.2% | **6.3%** | −2.9% | 5.9% | 2.8% | 6.9% |
| Jesús María | −0.1% | 6.0% | **5.9%** | −1.3% | 5.8% | **4.4%** | 6.0% |
| San Miguel | −0.1% | 6.0% | **5.8%** | −1.8% | 5.7% | 3.8% | 6.1% |
| Magdalena | −0.3% | 5.9% | 5.5% | −3.1% | 5.8% | 2.5% | 6.4% |
| **Pueblo Libre** | −0.4% | 5.7% | **5.3%** | −2.4% | 5.4% | **2.9%** | 5.9% |
| Barranco | −0.6% | 5.6% | 4.9% | −4.3% | 5.6% | 1.0% | 6.0% |
| Surquillo | −1.1% | 6.0% | 4.9% | −3.8% | 5.9% | 1.9% | 6.7% |
| San Isidro | −1.4% | 5.4% | 3.9% | −3.2% | 5.7% | 2.3% | 6.1% |
| Miraflores | −1.5% | 5.4% | 3.8% | −3.7% | 5.3% | 1.4% | 5.9% |
| San Borja | −1.8% | 4.9% | 3.1% | −3.8% | 4.9% | 0.8% | 5.5% |
| La Molina | −2.3% | 5.1% | 2.7% | −4.8% | 5.2% | 0.1% | 6.1% |
| Surco | −2.5% | 5.1% | 2.5% | −4.5% | 5.1% | 0.4% | 5.5% |

### Inferences
- **La parte "Miraflores/Barranco no es la mejor inversión" de la hipótesis queda confirmada**, a 10 y a 5 años, con valorización y con valorización + renta.
  - Miraflores está en la mitad inferior en ambas métricas.
  - Barranco está en la mitad: buen precio a 10 años, pero mal a 5.
- **La parte "Pueblo Libre es el que más se valoriza" no se sostiene con los datos del BCRP.**
  - Pueblo Libre es un buen distrito medio, superior a todo Lima Top.
  - Jesús María domina en precio (5 años y momentum), San Miguel combina precio y renta con el ticket más bajo de la muestra, y Lince domina en renta y a 10 años.
  - En ventas de 2026, Pueblo Libre es 4.º de Lima Moderna. Su única métrica líder es el crecimiento de ventas en 2024 (+53.5%), un dato de demanda y no de precio.
- **El retorno total real bruto de ~5–6% del sector medio es casi todo renta (≈ 6%) con precio real ≈ 0.** Para el dueño del proyecto, la tesis de inversión defendible en Lima hoy es de *carry* (renta) y no de *apreciación*. La apreciación real ha sido nula o negativa durante 10 años. El valor está en distritos con PER bajo y demanda de alquiler profunda: Lince, Surquillo, Magdalena, San Miguel, Jesús María y Cercado.
- **Sesgos de la estimación.**
  - Es bruta: no descuenta vacancia, mantenimiento, impuestos ni costos de transacción.
  - Usa precios de oferta.
  - Supone que la rentabilidad media del PER se obtuvo cada año.
  - El retorno neto real probablemente queda 1–2 pp por debajo. Ver financiamiento_costos_impuestos.md.
  - Las diferencias entre distritos del sector medio (5.3–6.3%) están dentro del ruido de medianas trimestrales; la brecha "sector medio vs sector alto" (~2–3 pp/año) sí es robusta.

### Gaps
- No pude calcular el retorno total para Breña, Cercado, Chorrillos, Los Olivos, Callao/Bellavista ni La Victoria: no hay series de precio y PER de 5 o 10 años. Con datos puntuales (Urbania 2025-26), Cercado (rentabilidad 6.0–6.9%) y La Victoria/Breña (alzas de precio de +8.7% a +14.9% en 2025) son candidatos a investigar, pero sin serie no se puede afirmar que superen al sector medio.
- No hay serie pública de rentabilidad neta ni de vacancia por distrito para pasar de bruto a neto con datos.
