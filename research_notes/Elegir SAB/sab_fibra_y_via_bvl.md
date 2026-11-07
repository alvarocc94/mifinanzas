# Qué SAB usar para FIBRA Prime, y la vía BVL para el ETF

> Notas de investigación del 2026-11-07. Responde dos preguntas del dueño: en qué SAB comprar los
> S/ 10,000 de FIBRA Prime (`PLAN.md`), y qué consultarle a esa SAB sobre el S&P 500 en la BVL.
> Fuentes primarias: los tarifarios que cada SAB remite a la SMV y los boletines diarios de la BVL.
> Las descargas están en el scratchpad de la sesión, no en el repo.

## Takeaway

- **Renta 4 SAB.** En los 20 tarifarios vigentes de la SMV, es la única con todo esto a la vez:
  - custodia, mantenimiento y cobro de dividendos sin costo, por escrito;
  - tarifa web publicada: 0.43%, con mínimo de US$ 15;
  - plataforma web;
  - oficina en San Isidro.
- **Lo que separa a las SAB es el costo de tener los valores, no la comisión por operación.** Con
  una posición de ~US$ 2,900, varias cobran entre S/ 4 y S/ 35 al mes de mantenimiento o
  custodia, o un porcentaje de cada dividendo. A 5 años eso equivale a 4–21% de la posición.
- **trii (Kallpa) es el segundo.** Retirar es gratis y la comisión es parecida. En contra:
  - va primero por app;
  - el tarifario formal de Kallpa en la SMV incluye mantenimiento de S/ 10 al mes (hasta 5%
    anual) y S/ 5 por cobro de dividendos, y trii no dice si eso aplica a sus clientes.
- **Hallazgo:** SPYL y CSPX, los UCITS irlandeses del S&P 500, están listados en la BVL, con
  Inteligo SAB como agente promotor. El informe 3 no pudo confirmarlo (`impuestos_y_etfs.md`).
  - Si una SAB puede comprarlos y venderlos en la rueda, se juntan tres ventajas: el 6.25% de
    salida de la vía BVL, la ausencia de estate tax y la acumulación.
  - Esa combinación le ganaría a SPYL en IBKR incluso con marginal de 14%.
  - Su liquidez en la BVL es mínima (frecuencia de cotización de 5%), así que todo depende de
    cómo ejecute la SAB.
- **FIBRA Prime rinde algo menos de lo supuesto en el PLAN:** el TTM es US$ 0.52 por certificado,
  7.6% bruto y ~7.3% neto a US$ 6.83, frente al 7.6–8.3% neto que se tomó de la guía de 2026.
  Más de un tercio de lo distribuido es "exceso de caja".
- **Bono MiVivienda:** el dueño confirmó (2026-11-07) que en la liquidación de la venta le
  descontaron ~S/ 16,500 por devolución del bono. Queda cerrada la verificación pendiente.

## 1. Costos regulatorios por operación

Fuente: [BVL, Boletín Diario del 06-nov-2026](https://documents.bvl.com.pe/pubdif/boldia/20261106.pdf),
sección 20, "Retribuciones, Contribuciones y Comisiones". Renta variable al contado, sobre el monto
efectivo, en cada compra y en cada venta:

| Concepto | Tarifa |
|---|---|
| Retribución BVL | 0.021% |
| Fondo de Garantía | 0.0075% |
| CAVALI | 0.04095%, mínimo S/ 5 por póliza (nota 4). En 2026 no hay mínimo hasta S/ 7,000, y entre S/ 7,000 y S/ 12,210 rige el mínimo de S/ 5 |
| Contribución SMV | 0.0135% |
| IGV | 18% sobre las comisiones (BVL, CAVALI y SAB) |
| Comisión SAB | libre (nota 3) |

**Para una póliza de S/ 10,000** (US$ 2,898 a S/ 3.45, el tipo implícito en el mismo boletín), los
cargos regulatorios suman ≈ **US$ 3.04 (0.105%) por lado**:
- BVL: US$ 0.61
- Fondo de Garantía: US$ 0.22
- CAVALI, al mínimo de S/ 5: US$ 1.45
- SMV: US$ 0.39
- IGV: US$ 0.37

## 2. Tarifarios de las SAB

Fuente: [SMV, Tarifarios de agentes de intermediación](https://www.smv.gob.pe/SIMV/Frm_Tarifario?data=8C93EECED675AC488FAAB2549ECA5DD339FC11615B),
22 documentos descargados el 2026-11-07. La lista de las 20 SAB activas y sus códigos está en la
sección 24 del boletín del 06-nov-2026. Montos sin IGV, salvo que se diga otra cosa. Los rangos
porcentuales son los máximos del tarifario. La tarifa real al cliente se publica aparte (web) o se
pacta.

| SAB (tarifario vigente desde) | Renta variable al contado | Tener los valores | Cobro de dividendos | Transferir a otro banco |
|---|---|---|---|---|
| **Renta 4** (24-oct-2024 / 21-may-2025) | 0.05–1.50%, mín. S/ 40 o US$ 15. **Web: 0.43%** ([renta4.pe](https://www.renta4.pe/que-necesitas/tarifas-bolsas)) | **Sin costo** (custodia y mantenimiento) | **Sin costo** | S/ 20 o US$ 7 |
| **Kallpa / trii** (01-sep-2025) | Kallpa: 0.10–10%, mín. S/ 80 o US$ 25. trii: S/ 12.5 o US$ 3 hasta S/ 2,000 o US$ 500; arriba, 0.6% ([trii.pe](https://trii.pe/)) | Kallpa: S/ 10 al mes, "hasta 5% anual" (k). trii no menciona cargo | Kallpa: S/ 5 "ante empresas emisoras" | Kallpa: S/ 25–100 o US$ 9–50. trii: gratis |
| **Inviu Perú** (02-sep-2026) | 0–1.5%, mín. S/ 30 o US$ 10 | Mantenimiento "bonificado"; custodia CAVALI 0–2% "a definir" | "Costo del proveedor" | "Costo del proveedor" |
| **Seminario** (22-jul-2024) | 0–1.5%, mín. S/ 40 o US$ 12.50 | S/ 4 por valor al mes (máx. S/ 20) si no operas en el mes | Sin costo | S/ 30 o US$ 10 |
| **Grupo Coril** (22-oct-2026) | 0–1%, mín. S/ 10 o US$ 2.50 | US$ 3 al mes | **3% del dividendo** (máx. US$ 90) | Sin costo |
| **Inteligo** (11-may-2026) | 0.05–2% personas naturales, mín. S/ 35 o US$ 10 | Custodia hasta S/ 15 o US$ 5 al mes | US$ 1.30 por dividendo | S/ 20 o US$ 6 |
| **Credicorp Capital** (29-dic-2025) | 0.01–1.50%, mín. S/ 100 o US$ 35 | Custodia básica S/ 15 + IGV al mes | — | S/ 25 o US$ 7.50 |
| **BBVA Bolsa** (01-oct-2024) | mín. S/ 100 | S/ 15 o US$ 4.50 al mes por cuenta valor | Sin costo | — |
| **Scotia** (18-sep-2024) | mín. S/ 100 o US$ 35 | S/ 35 al mes (por tramos de valor) | — | — |
| BNB Valores (04-sep-2026) | mín. S/ 25 o US$ 10 | hasta S/ 10 o US$ 3 al mes | Sin costo | — |
| BTG Pactual (09-ago-2024) | mín. S/ 50 | Sin cobro | — | S/ 35 |
| IND (02-sep-2024) | mín. S/ 70 o US$ 20 | — | Sin costo | — |
| Magot (11-oct-2024) | mín. S/ 70 | — | — | — |
| Investa (16-jul-2025) | mín. S/ 50 o US$ 15 | Hay cargo de mantenimiento (no extraído) | — | — |
| Tradek (12-dic-2017) | 1.00–1.50%, mín. S/ 50 o US$ 20 | Custodia %, mín. S/ 5 al mes | — | — |
| Diviso (26-jul-2022) | mín. S/ 150 | — | — | — |

No se extrajeron: SURA (PDF escaneado), Acres, Larraín Vial y Cartisa (tarifario de 2014). "—"
significa que no se buscó o no figura. Ninguna es candidata con mínimos de S/ 50 o más.

## 3. Costo de los S/ 10,000 de FIBRA Prime

Supuestos: 423 certificados a US$ 6.85 (US$ 2,898), 5 años de tenencia, una compra, una venta, 60
distribuciones (~US$ 18 brutos al mes) y un retiro al año.

**Por operación** (comisión de la SAB + IGV + US$ 3.04 regulatorios):
- **Renta 4:** 0.43% × 2,898 = US$ 12.46, debajo del mínimo, así que se paga **US$ 15 + IGV =
  US$ 17.70**. Con los regulatorios, **US$ 20.74 (0.72%) por lado**. El mínimo deja de pesar desde
  ~US$ 3,490 (~S/ 12,000) por orden.
- **trii:** 0.6% = US$ 17.39, más IGV si no está incluido (trii no lo dice). Con los regulatorios,
  **US$ 20.4–23.6 (0.70–0.81%)**.

**Costo fijo a 5 años** (tener los valores, cobrar dividendos y 5 retiros), sin la comisión
porcentual de compra y venta ni el IGV:

| SAB | 5 años | % de la posición |
|---|---|---|
| Renta 4 | US$ 35 (solo retiros) | 1.2% |
| trii | US$ 0, o ~US$ 174 si aplica el mantenimiento de Kallpa | 0–6% |
| Seminario | ~US$ 113 | 3.9% |
| Grupo Coril | ~US$ 213 | 7.3% |
| BBVA Bolsa | ~US$ 270 | 9.3% |
| Credicorp Capital | ~US$ 298 | 10.3% |
| Inteligo | hasta ~US$ 408 | hasta 14% |
| Scotia | hasta ~US$ 609 | hasta 21% |

Frente a un rendimiento neto de ~7.3% anual, Renta 4 cuesta ~0.24 pp al año. Grupo Coril cuesta
~1.5 pp, aunque es el formador de mercado de FIBPRIME y pertenece al mismo grupo que su
titulizadora. Inteligo cuesta hasta ~2.8 pp.

## 4. FIBRA Prime: precio, liquidez y distribuciones

Fuente: boletines diarios de la BVL de 2026 (06-feb, 06-mar, 07-abr, 06-may, 05-jun, 06-jul,
15-jul, 31-jul, 05/07-ago, 04-sep, 06-oct y 06-nov).

**Precio y liquidez:**
- **Cierre:** US$ 6.83 el 05-nov-2026; rendimiento bursátil 2026 de +11.11%.
- **Formador de mercado:** Grupo Coril SAB (GCO), con cantidades mínimas de 277 (compra) y
  554 (venta) certificados. Su spread suele ser ancho: US$ 6.65 / 6.94 el 06-nov.
- **Montos diarios:** en los días muestreados fueron de US$ 2,750 (05-feb) a US$ 35,417 (05-oct);
  el 05-nov, US$ 4,846.
- **Total del año:** el segmento FIBRAS negoció US$ 5.05 millones en 2026 (4,288 operaciones),
  ~US$ 24k por sesión.
- **Implicancia:** una orden de 423 certificados es entre 0.1 y 0.6 días de volumen, así que va
  con orden límite y no a mercado.

**Distribuciones por fecha de corte** (US$ por certificado; "Exc. Caja" = exceso de caja):

| Corte | Monto | Composición | Pago |
|---|---|---|---|
| 18-dic-2025 | 0.063590 | — | — |
| 04-mar-2026 | 0.067425 | 0.040626 a cuenta 2025 + 0.026798 exc. caja | 30-mar |
| 18-mar-2026 | 0.044606 | 0.020418 a cuenta 2026 + 0.024188 exc. caja | 13-abr |
| 05-may-2026 | 0.044844 | 0.016458 "Feb. 2026" + 0.028385 exc. caja | 20-may |
| 20-may-2026 | 0.045309 | 0.023238 + 0.022071 exc. caja | 16-jun |
| 26-jun-2026 | 0.045237 | 0.015618 + 0.029620 exc. caja | 14-jul |
| 03-ago-2026 | 0.044688 | 0.015068 + 0.029620 exc. caja | 27-ago |
| 31-ago-2026 | 0.041357 | 0.022934 + 0.018424 exc. caja | 29-set |
| 20-oct-2026 | 0.099703 | a cuenta 2026 | 29-oct |
| 20-nov-2026 | 0.024948 | 0.008860 + 0.016088 exc. caja | 01-dic |

- **TTM** (cortes del 21-nov-2025 al 20-nov-2026): **US$ 0.5217**. Es **7.64% bruto** a
  US$ 6.83 y, con la retención definitiva de 5%, **~7.26% neto**. Sobre S/ 10,000 son ~US$ 17.5
  netos al mes, ~S/ 60 en promedio. El monto varía mucho de un mes a otro.
- **Exceso de caja:** al menos US$ 0.195 del TTM (37%). En inmuebles es normal, porque la
  depreciación no sale de caja, pero quiere decir que la utilidad contable distribuida es menor
  que el pago.
- **Noviembre:** el pago (US$ 0.025) es el más bajo del año. Llega después de la sexta colocación.
- **Sexta colocación:** captó US$ 40.37 millones para prepagar el préstamo puente de Scotiabank y
  BCI por el Parque Logístico Lima Sur, con 1,048 órdenes de 12 SAB
  ([Infobae, 05-nov-2026](https://www.infobae.com/peru/2026/11/05/fibra-prime-recauda-usd-40-millones-en-bolsa-para-reducir-deuda-por-megaproyecto-al-sur-de-lima-desde-cuanto-invertir/)).
  La oferta se lanzó a US$ 6.65 por certificado, debajo del precio de bolsa (Gestión, vía
  búsqueda; no leí la nota completa).
- **El 06-oct-2026** hubo un cruce extrabursátil de 48,322 certificados a US$ 7.45 entre cuentas
  de Grupo Coril SAB.

**Régimen tributario:** la Ley 31650 prorrogó la tasa de 5% de los FIRBI hasta el 31-dic-2026
([EY Perú](https://www.ey.com/es_pe/technical/tax-alert/regimen-depreciacion-beneficios-tributarios-firbi)).
Al 07-nov-2026 no encontré ningún proyecto que la extienda. Si el régimen vence, la renta
atribuida a una persona natural seguiría pagando del orden de 5% como renta de capital. Esto es una
inferencia que no revisé con un tributarista.

## 5. Hallazgo: el S&P 500 en UCITS está listado en la BVL

Fuente: boletín del 06-nov-2026, "Valores extranjeros inscritos a través de un agente promotor".
Referencias de cierre del 05-nov-2026:

| Valor | Agente promotor | Precio | Negociado ese día | Frecuencia de cotización | Rend. 2026 |
|---|---|---|---|---|---|
| **SPYL** (SPDR S&P 500 UCITS Acc, IE000XZSV718) | ITG (Inteligo) | US$ 18.36 | nada | **5%** | +10.80% |
| **CSPX** (iShares Core S&P 500 UCITS Acc) | ITG (Inteligo) | US$ 802.75 | nada | 40% | +8.77% |
| SPY | CON (BBVA Bolsa) | US$ 736.00 | 4,600 acciones, US$ 3.39 millones, 54 operaciones | 100% | +7.70% |
| VOO | BVL | US$ 676.66 | US$ 44,346, 5 operaciones | 60% | +7.44% |
| IVV | BVL | US$ 740.28 | nada | 35% | +7.52% |

Inteligo también promueve otros UCITS (AGGU, CBU0, CBU7, CRPU, CSKR…).

**Lo que eso significa:**
- **Inscripción:** se rigen por el Reglamento de Inscripción y Exclusión de Valores en el RPMV y
  en la Rueda (R. SMV 031-2012). Es el mismo régimen que permite vender SPY por la BVL al 6.25%:
  art. 51, segundo párrafo, de la LIR (`impuestos_y_etfs.md`).
- **Ventaja sobre SPY por la BVL:** sin estate tax de EE.UU., con 15% de retención dentro del
  fondo en lugar de 30%, y de acumulación.
- **Estimado frente a IBKR** (modelo del PLAN: US$ 6,800, 7% anual, 20 años):
  - Bajar el impuesto de salida de 14% a 6.25% vale ≈ US$ 1,440 sobre ~US$ 18,600 de ganancia.
  - Las comisiones más altas de la SAB cuestan ≈ US$ 60–130 netos de los wires que se ahorran.
  - Resultado: **del orden de +6% de patrimonio final (≈ US$ 1,300)**. Con marginal de 17% la
    ventaja crece.
  - Es mi estimado; no es una cifra recalculada en la hoja del PLAN.

**Riesgos y desconocidos:**
- **Liquidez:** SPYL cotizó en 5% de las sesiones. Comprarlo y, sobre todo, venderlo en la rueda
  depende de que la SAB cruce contra Londres o Xetra, o de que el agente promotor dé contraparte.
  Ningún tarifario dice a qué precio.
- **Exclusión:** la BVL excluye valores extranjeros. El mismo 06-nov retiró TLTW (art. 37-A de
  la R. SMV 031-2012). Si se excluye SPYL, habría que venderlo fuera, como renta de fuente
  extranjera, o trasladarlo.
- **Criterio de SUNAT:** que la venta de un UCITS por la BVL vaya a la canasta de 6.25% sigue la
  misma regla que la de SPY, y SUNAT no se ha pronunciado sobre ninguna de las dos.
- **Custodia de valores extranjeros:** Renta 4 dice "sin costo" en general. Inteligo cobra hasta
  US$ 5 al mes.

## 6. Bono MiVivienda

- **Lo confirmado:** el dueño confirmó el 2026-11-07 que en la liquidación de la venta del loft le
  descontaron ~S/ 16,500 por devolución del bono.
- **Frente al estimado:** `mivivienda_reacceso.md` había estimado ≈ S/ 11,600–12,400 (BBP de
  S/ 10,800 más interés legal). La diferencia cuadra con un Bono MiVivienda Sostenible sumado al
  BBP, o con otro tramo de BBP. No cambia la conclusión.
- **Elegibilidad:** no encontré ninguna regla que devuelva la elegibilidad al subsidio a quien
  reembolsó el BBP.
  - El BBP se otorga "por única vez", y quien ya recibió apoyo habitacional del Estado no
    califica ([perugestiona](https://perugestiona.pe/bonos-del-estado/bono-buen-pagador/);
    [tramitesperu](https://tramitesperu.com/mivivienda/bono-buen-pagador/); blogs).
  - El reglamento del BBP en mivivienda.com.pe no se pudo leer (PDF comprimido).
  - Como la devolución fue total, vale la pena preguntarlo por escrito al Fondo. Si la respuesta
    fuera sí, el análisis de vivienda cambia de signo (informe 2).

## Pendiente

- Preguntas a Renta 4, por escrito:
  - si puede comprar y vender SPYL o CSPX en la rueda, cómo ejecuta y a qué precio frente a
    Londres;
  - si la custodia de valores extranjeros no tiene costo;
  - qué pasa si la BVL excluye el valor;
  - cuánto cuesta retirar a Interbank.
- trii: si a sus clientes les aplica el mantenimiento de S/ 10 al mes y el cobro de S/ 5 por
  dividendo de Kallpa, y si la comisión incluye IGV y los cargos de BVL y CAVALI.
- Inviu: su tarifa real de renta variable y de custodia.
- Atención al cliente: no encontré datos públicos comparables (reclamos por SAB en SMV o INDECOPI)
  que pudiera verificar. Las reseñas de Renta 4 en HelpMyCash son de España.
