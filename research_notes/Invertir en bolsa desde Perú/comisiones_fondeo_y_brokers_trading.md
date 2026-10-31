# Costos de fondeo y retiro desde Perú, brókers para el núcleo VOO y alternativas a Alpaca para trading (corte: 31-oct-2026)

> Notas de investigación para el plan de `PLAN.md`: un depósito único de S/ 23,500 (≈ US$ 6,800) para VOO, con posibles aportes de US$ 300 al mes y salida por DTC hacia una SAB para vender en la BVL al 6.25%; y una cuenta de trading de S/ 6,500 (≈ US$ 1,850) solo en acciones y ETFs de EE.UU., sin apalancamiento.
>
> Parten de [`brokers_vias_acceso.md`](brokers_vias_acceso.md) y [`youtube_bolsillos_llenos.md`](youtube_bolsillos_llenos.md) y no repiten lo que ya está ahí, salvo lo necesario para la tabla de costos.
>
> **Supuestos de cálculo, propios, no son cotizaciones:**
> - Tipo de cambio de referencia: S/ 3.40 por US$.
> - Costo cambiario en una casa de cambio fintech: ≈0.40% por lado.
> - Costo cambiario en un banco: ≈1.2% por lado.
>
> **Acceso a fuentes:** las páginas oficiales de IBKR (interactivebrokers.com, .ie, .com.au, ibkr.info), Schwab International, BCP y BBVA devolvieron HTTP 403 a la descarga directa. Donde se cita una de ellas, el texto viene del extracto del buscador o de una página espejo oficial (ibkrguides.com). Así se indica en cada caso.
>
> **Videos de YouTube nuevos en `raw/youtube/`**, tratados como afirmaciones no confiables:
> - [NH3akJtkBPw](https://www.youtube.com/watch?v=NH3akJtkBPw), 22-jul-2026
> - [Tl43fYsfKyo](https://www.youtube.com/watch?v=Tl43fYsfKyo), 29-abr-2026
> - [IacmrD3u_F8](https://www.youtube.com/watch?v=IacmrD3u_F8), 01-mar-2026
>
> Los tres son de Luis Ccaccya, "Invertir para el Futuro", Perú. Además, [4oAJxUXeOGE](https://www.youtube.com/watch?v=4oAJxUXeOGE), 22-ene-2026, de "Finanzas con Luis", que es argentino.

---

## 1. Cadena de fondeo desde una cuenta en soles: tipo de cambio, wire, corresponsales, recepción y vías locales

### Takeaway
El costo de llevar US$ 6,800 a un bróker de EE.UU. lo pone el lado peruano, no el bróker. Sale a ≈US$ 70–100, alrededor de 1.0–1.5%, si se cambia en una fintech y se envía un solo wire desde Interbank. IBKR no cobra por recibir y da un retiro gratis al mes.

El problema son los aportes pequeños. Un wire de US$ 300 cuesta ≈US$ 30 fijos, más del 10%. Para esos montos hay vías locales:
- **IBKR + SafetyPay:** anunciado el 18-ago-2026, en moneda local. No se encontró la tarifa.
- **Hapi:** US$ 1.99 fijos por depósito en soles.
- **Takenos → Wise → IBKR:** ≈1% según un creador.
- **Stablecoins en IBKR:** ≈0.35% más el diferencial del P2P. Hay que pasar por un exchange cripto y no se recomienda para este usuario.

### Cited Findings
**Tipo de cambio PEN→USD**
- Kambista, foto sin fecha: compra 3.352 y venta 3.379, es decir S/ 0.027 de diferencial. Rextie: 3.35 y 3.38. Ninguno cobra comisión aparte; el costo está en el diferencial. — [Comparabien, Kambista](https://comparabien.com.pe/producto/cambio-divisas/kambista-usd); [Comparabien, Rextie](https://comparabien.com.pe/producto/cambio-divisas/rextie-usd)
- Diferencial promedio de los últimos 12 meses (fecha del artículo no clara): ≈S/ 0.027 en casas fintech y ≈S/ 0.080 en bancos. — [Revista Economía](https://www.revistaeconomia.com/?p=104369)
- No se encontraron cotizaciones de Tkambio. Rextie mantiene el tipo de cambio 15 minutos tras registrar la operación. — [TrámitesPerú, comparador Rextie](https://tramitesperu.com/comparadores/casa-rextie/)

**Wire saliente y recepción en bancos peruanos**
- **Interbank, envío** (revisado el 03-dic-2025):

  | Monto | Comisión |
  |---|---|
  | Hasta US$ 3,000 | US$ 30 |
  | US$ 3,001–10,000 | US$ 42 |
  | US$ 10,001–25,000 | 0.25% + US$ 15 SWIFT |

  El cargo OUR por banco corresponsal, US$ 45, figura entre las "comisiones adicionales" (no queda claro si se suma o reemplaza). — [Wise blog Perú, Interbank](https://wise.com/pe/blog/transferencia-internacional-interbank)
- **Interbank, recepción del exterior** (misma fuente):

  | Monto recibido | Comisión |
  |---|---|
  | Hasta US$ 25 | 20% del importe (mín. US$ 2, máx. US$ 5) |
  | US$ 25.01–10,000 | US$ 25 |
  | Desde US$ 10,001 | 0.50% (mín. US$ 50, máx. US$ 100) |

  Esto encarece cualquier retiro desde un bróker de EE.UU. que llegue por wire. — [Wise blog Perú, Interbank](https://wise.com/pe/blog/transferencia-internacional-interbank)
- **BCP, BBVA y Scotiabank:** no se obtuvo el tarifario vigente (403 o sin montos en la página).
  - Una guía genérica estima un SWIFT desde BCP o Interbank en "US$ 15–50 más el margen de tipo de cambio". — [ComparaLatam, jun/ago-2026](https://comparalatam.com/pe/transferencia/)
  - BBVA publicó un aviso de modificación de comisiones con un cargo de corresponsal de US$ 35. Solo se vio el extracto del buscador, sin fecha. — [BBVA Perú, aviso](https://bbva.pe/content/dam/public-web/peru/documents/prefooter/avisos-importantes/Aviso-Importante_Modificacion-de-la-Comision-de-Ordenes-de-Pago-Del-Exterior-y-Transferencia-al-Extranjero.pdf)
- Creadores peruanos estiman en "US$ 50 a más" el costo de un wire hacia IBKR. Al retirar, entre la recepción local y los intermediarios, "puede rondar entre 50 y 100 dólares". — [Luis Ccaccya, IacmrD3u_F8, 01-mar-2026](https://www.youtube.com/watch?v=IacmrD3u_F8)

**IBKR: depósito en moneda local (SafetyPay) y otras vías**
- **SafetyPay** (18-ago-2026): permite a "eligible Interactive Brokers clients… transfer funds directly from their personal bank accounts using local currencies".
  - Ningún comunicado publica comisión, diferencial cambiario, límites ni lista de países. Tampoco dice si sirve para retirar.
  - El comunicado oficial de IBKR dio 403.
  - Fuentes: [Finance Magnates, 18-ago-2026](https://www.financemagnates.com/forex/interactive-brokers-adds-safetypay-as-brokers-push-local-payments-in-latin-america/); [RankiaPro LATAM, 27-ago-2026](https://rankiapro.com/latam/noticias/interactive-brokers-amplia-las-opciones-para-inversores-latinoamericanos-con-mas-opciones-para-ingresar-fondos/); [BrokerChooser](https://brokerchooser.com/news/interactive-brokers-expands-latin-american-access-with-safetypay-deposits--990afa4e); [IBKR, comunicado 8-18-26 (403)](https://www.interactivebrokers.com/en/general/about/mediaRelations/8-18-26.php)
- **SafetyPay en Perú, del lado del comercio:** el consumidor paga por transferencia bancaria en PEN, el procesamiento y la liquidación son en USD, y "the consumer… supports the foreign exchange costs". Es documentación para comercios, no términos de IBKR. — [PPRO, Peru banks via SafetyPay](https://developerhub.ppro.com/simple-api/docs/peru-banks-via-safetypay)
- **Stablecoins:** IBKR permite fondear con stablecoins desde enero de 2026. — [Business Wire vía Rutland Herald, 15-ene-2026](https://www.rutlandherald.com/news/business/interactive-brokers-enables-24-7-account-funding-with-stablecoin/article_3b06dca9-6b0f-5ff4-8e98-b38d883b1b86.html)
  - Lo que muestra el creador en pantalla: depósito en USDC con comisión de IBKR de 0.10–0.35% (0.35% hasta US$ 5,000), mínimo US$ 2 y tope de US$ 25,000 por depósito. Compra la stablecoin en P2P con soles a S/ 3.44–3.54 por USDT. Los enlaces de la descripción del video son de referido de IBKR y del exchange MEXC. — [Luis Ccaccya, NH3akJtkBPw, 22-jul-2026](https://www.youtube.com/watch?v=NH3akJtkBPw)
- **Takenos → Wise → IBKR** (abr-2026), según el creador:
  - Se depositan soles en Takenos, que cobra 1% al enviar dólares a la cuenta USD de Wise.
  - La transferencia ACH de Wise a IBKR es gratis.
  - Wise "fue vetado en Perú" y hoy "ya se puede crear cuentas nuevamente".
  - Fuente: [Luis Ccaccya, Tl43fYsfKyo, 29-abr-2026](https://www.youtube.com/watch?v=Tl43fYsfKyo)
- **Wise para residentes peruanos:** solo cuenta en dólares, sin saldo en soles ni conversión local. La fuente es un competidor, Global66. — [Global66, Wise vs Global66](https://www.global66.com/blog/wise-vs-global66-peru/)
- **Global66:**
  - Anuncia envíos PEN→USD, pero no publica una tarifa fija; reseñas de terceros dicen que el costo está en el tipo de cambio. — [Global66, PEN→USD](https://www.global66.com/enviar-dinero/PEN/USD/); [Tucambista](https://tucambista.pe/blog/que-es-global66-y-como-funciona)
  - Un video argentino muestra Global66 → IBKR por ACH con "costo total gratis". — [Finanzas con Luis, 4oAJxUXeOGE, 22-ene-2026](https://www.youtube.com/watch?v=4oAJxUXeOGE)
  - Bolsillos Llenos excluyó a IBKR y Schwab de su comparativa porque el fondeo eficiente "requiere un tercero, Global66". — [MyTOSwXi8sw, 23-feb-2026](https://www.youtube.com/watch?v=MyTOSwXi8sw)

**IBKR: recepción y retiros**
- **Retiros:** un retiro gratis por mes calendario; después, US$ 10 por wire, US$ 1 por ACH y US$ 4 por cheque. Los cargos del banco receptor o del corresponsal no están incluidos.
  - Fuentes: [IBKR, IMPACT pricing](https://impact.ibkr.com/en/pricing.php); [IBKR Canadá, Withdrawal Instructions](https://interactivebrokers.ca/en/accounts/withdrawalInstructions.php); [IBKR Campus, funding](https://www.interactivebrokers.com/campus/gabe-funding-demo/)
  - Las tres se leyeron en el extracto del buscador porque el acceso directo dio 403. Bolsillos Llenos daba la misma cifra en 2022 ([nLUJWaVDaMM](https://www.youtube.com/watch?v=nLUJWaVDaMM)).
- **Depósitos por wire:** según los creadores, IBKR no cobra por recibirlos ("no es que Interactive cobre"). No se pudo leer la página oficial. — [Finanzas con Luis, 4oAJxUXeOGE](https://www.youtube.com/watch?v=4oAJxUXeOGE)

**Hapi: fondeo y retiro desde Perú** (Help Center, "Updated over 3 weeks ago" al 31-oct-2026)

| Vía | Comisión |
|---|---|
| PEN vía Cross Payments | US$ 1.99 fijo |
| PEN vía Koywe/Momento | 0.9%, mínimo US$ 1.99 |
| USD vía Cross Payments | 0.45%, mínimo US$ 2.99 |
| USD vía Koywe | 0.9%, mínimo US$ 2.99 |
| Tarjeta | 3.85%, mínimo US$ 2.99 |
| Wire SWIFT a Apex | Sin cargo de Hapi |

- La página no dice qué tipo de cambio aplica Cross Payments. — [Hapi, How can I fund my account](https://help.hapi.trade/en/articles/8945476-how-can-i-fund-my-account); [Hapi, Cross Payments](https://help.hapi.trade/en/articles/12631400-what-is-cross-payments-and-how-to-use-it-to-deposit-into-hapi)
- **Retiros desde Perú** (actualizado el 31-ago-2026):
  - Transferencia local en USD: US$ 7.99, sin mínimo.
  - AIRTM: US$ 4.99.
  - Transferencia internacional: US$ 20, con mínimo de US$ 35.
  - Plazo de 2 a 5 días.
  - Fuente: [Hapi, How to withdraw funds](https://help.hapi.trade/en/articles/8949332-how-to-withdraw-funds)
- **Tope por retiro:** el blog de Hapi menciona "one withdrawal per approval… maximum of $3,000 per withdrawal". El Help Center asigna ese tope de US$ 3,000 a los retiros cripto, así que la fuente no es consistente. — [Hapi blog](https://hapi.trade/en/blog/how-to-make-deposits-and-withdrawals-on-hapi)

**Tyba** (según Bolsillos Llenos, feb-2026; no se encontró tarifario oficial)
- Depósito solo desde BCP mediante pago de servicios (Monet). Retiro solo a cuentas BCP. Tarda hasta 72 h o 3 días hábiles.
- Cobra 1.5% al depositar y 1.5% al retirar, sin monto mínimo.
- Compra de acciones enteras: sin comisión. Fracciones: 0.3%.
- Fuente: [b9NDw2s1ado, 02-feb-2026](https://www.youtube.com/watch?v=b9NDw2s1ado)

**Alpaca** (fee schedule, plantilla del 12-oct-2026)
- Wire saliente doméstico: US$ 15. Wire saliente internacional: US$ 35.
- "Local Currency Transfers (Inbound and Outbound)": 1.5% de conversión, máximo US$ 40 por transacción.
- ACH return: US$ 25.
- Fuente: [Alpaca Brokerage Fee Schedule (PDF)](https://files.alpaca.markets/disclosures/library/BrokFeeSched.pdf)
- **Contradicción:** la guía de fondeo de Alpaca (actualizada el 26-ene-2026) dice US$ 25 doméstico y US$ 50 internacional. Dice además que la conversión local pasa por CurrencyCloud y no lista países ni monedas; Perú y PEN no aparecen. Se toma como vigente el PDF de octubre, que es más reciente. — [Alpaca Learn, How to fund](https://alpaca.markets/learn/fund-live-trading-account/)

### Inferences
- **US$ 6,800 por wire** (Kambista + Interbank):
  - Cambio 0.40% ≈ US$ 27, wire US$ 42 y corresponsales entre US$ 0 y 30.
  - Total ≈ **US$ 70–100, es decir S/ 238–340 o 1.0–1.5%**.
  - Si se cambia en el banco, se suman ≈US$ 54 por el diferencial.
  - Si se paga OUR (US$ 45), el costo queda predecible en ≈US$ 115.
- **Juntar núcleo y trading en un solo wire:** US$ 6,800 + US$ 1,850 = US$ 8,650 sigue en el tramo de US$ 42 de Interbank. El fondeo de la cuenta de trading sale casi gratis si va a IBKR en el mismo envío. Si va a Alpaca en otro wire, cuesta US$ 30 más corresponsales.
- **Aportes de US$ 300 al mes:**

  | Vía | Costo por aporte |
  |---|---|
  | Wire bancario | ≈US$ 31 (≈10%): inviable |
  | Takenos → Wise → IBKR | ≈US$ 3 + diferencial de Takenos |
  | Hapi | US$ 1.99 + diferencial de Cross Payments (no publicado) |
  | IBKR + SafetyPay | Sin dato |

  La tarifa de SafetyPay es el dato que decide si los aportes van a IBKR.
- **La vía stablecoin no encaja:** exige una app de exchange y P2P con contrapartes. El usuario no quiere apps financieras, y el P2P agrega riesgo de contraparte y de fraude. El precio P2P mostrado (S/ 3.44–3.54) estaría por encima del de Kambista, pero no se puede afirmar porque los tipos de cambio son de fechas distintas.

### Gaps
- Tarifa, tipo de cambio y disponibilidad para Perú de SafetyPay en IBKR. Se resuelve entrando a Client Portal → Transfer & Pay → Deposit, donde aparecen los métodos y costos del país del titular.
- Tarifarios oficiales vigentes de wire saliente y de recepción de BCP, BBVA y Scotiabank.
- Tipo de cambio aplicado por Cross Payments (Hapi) y por Takenos.
- Si Alpaca acepta PEN en "Local Currency Transfers" y si eso evita el wire.
- Si Global66 Perú, y no solo Argentina, permite enviar USD por ACH a cuentas de EE.UU. a nombre propio.

---

## 2. Tabla de costos por bróker para el caso exacto del usuario

### Takeaway
IBKR no es el más barato para fondear: Hapi gana en aportes pequeños. Pero es el único que combina cuatro cosas:
- costo cero en salida DTC, custodia e inactividad;
- un retiro gratis al mes;
- web con TOTP;
- la mejor protección (SIPC más el exceso con Lloyd's).

Para el depósito único, la diferencia de costo frente a Hapi es de ≈US$ 40–70 una sola vez. Alpaca empata con IBKR en fondeo y su salida DTC es barata (US$ 5, frente a US$ 0 en IBKR y US$ 25 en Hapi), pero su elegibilidad para Perú sigue sin confirmar. Tyba, XTB, eToro y comprar directamente por una SAB quedan atrás por costo o por bloqueo de la ruta BVL.

### Cited Findings
Tabla de costos por concepto (US$; fechas y fuentes debajo de la tabla). "s/d" = sin dato verificable.

| Concepto | IBKR Pro (IB LLC) | Hapi | Alpaca | Schwab Intl | Tyba | XTB (Belice) | SAB en BVL (comprar ahí) |
|---|---|---|---|---|---|---|---|
| Acepta Perú | Sí, en la lista de países; entidad sin confirmar ([IBKR](https://www.interactivebrokers.com/en/choose-country-region.php)) | Sí | **Sin confirmar** ([Alpaca](https://alpaca.markets/support/countries-alpaca-is-available)) | **Sin confirmar** | Sí | Sí | Sí |
| (1) Depósito US$ 6,800 | Wire bancario ≈US$ 42 + corresp. + cambio; IBKR US$ 0. SafetyPay s/d | PEN Cross Payments US$ 1.99 + cambio s/d | Wire ≈US$ 42 + corresp. + cambio; conversión local 1.5% (tope US$ 40) si aplica a PEN | Wire bancario; Schwab US$ 0 al recibir (secundaria) | 1.5% = US$ 102 | Depósito sin cargo de XTB (canal, 2025) | Cambio + comisión SAB ≈0.5–1%+ (secundaria) |
| (2) Aporte US$ 300/mes | Wire ≈US$ 31; Takenos+Wise ≈1%; SafetyPay s/d | US$ 1.99 (0.66%) + cambio | Wire US$ 30 + corresp.; 1.5% local si aplica | Wire ≈US$ 31 | 1.5% = US$ 4.50 | s/d | Mínimos por operación (≈S/ 10–40) |
| (3a) Retiro US$ 1,000 | 1.º del mes US$ 0 (luego US$ 10) + Interbank US$ 25 | US$ 7.99 local en USD | US$ 35 + Interbank US$ 25 | US$ 15–25 + Interbank US$ 25 (secundaria) | 1.5% = US$ 15 | US$ 0 si es más de US$ 100 + Interbank US$ 25 + intermediarios | Transferencia local |
| (3b) Retiro US$ 7,000 | US$ 0 + Interbank US$ 25 | US$ 7.99 (×3 si rige el tope de US$ 3,000) | US$ 35 + US$ 25 | US$ 15–25 + US$ 25 | 1.5% = US$ 105 | US$ 0 + US$ 25 + intermediarios | Local |
| (4) Comprar y vender VOO | Fixed US$ 0.005/acción, mín. US$ 1; Tiered mín. US$ 0.35 + tasas | 0% (más clearing fee s/d) | US$ 0 + tasas de traspaso (SEC 0.0000206 × valor en la venta) | US$ 0 en línea (secundaria) | 0% acciones enteras; 0.3% fracciones | 0% hasta €100k al mes | ≈0.5–1% por lado (secundaria); BBVA: S/ 100 por operación en mercado extranjero |
| (5) Salida DTC hacia SAB | **US$ 0** (IBKR "does not assess a fee" por FOP; repercute cargos de terceros) | **US$ 25** por valor hacia SAB peruana; US$ 75 hacia brókers de EE.UU. | **US$ 5** por valor y envío | s/d (ACAT total US$ 50, parcial US$ 0, secundaria) | **No transfiere a Perú**: solo a brókers de EE.UU. | €/US$ 25 por ISIN | No aplica (ya está en la SAB) |
| (6) Custodia, inactividad, mínimos | US$ 0 / US$ 0 / US$ 0 | Tiene artículo de "inactivity fees" (no leído) / mín. US$ 1 | Ninguno en el fee schedule | US$ 0 mínimo (guía abr-2026) | s/d | €10 al mes tras 365 días sin operar **y** 90 sin depositar | Tasa CAVALI sobre la cuenta matriz; repercusión s/d |

Fuentes por fila:
- **IBKR**
  - Comisiones Fixed y Tiered, comparativa fechada el 08-jul-2026: [IBKR Commissions](https://www.interactivebrokers.com/commissions).
  - Custodia e inactividad en cero: [IBKR, Other Fees Overview](https://gdcdyn.interactivebrokers.com/en/pricing/other-fees-overview.php).
  - Retiros: ver sección 1.
  - IBKR Lite (comisión cero) solo para residentes de EE.UU.: [IBKR, Compare Lite/Pro](https://brokerage.ibkr.com/en/general/compare-lite-pro.php).
  - FOP: ver sección 3.
- **Hapi**
  - Depósitos y retiros: [Help Center, fondeo](https://help.hapi.trade/en/articles/8945476-how-can-i-fund-my-account) y [retiros](https://help.hapi.trade/en/articles/8949332-how-to-withdraw-funds).
  - Salida a una SAB por US$ 25 y a EE.UU. por US$ 75: [Bolsillos Llenos, NXKKWVudXuw, 23-mar-2026](https://www.youtube.com/watch?v=NXKKWVudXuw). Los US$ 75 hacia EE.UU. los confirma [ARQ](https://help.arqfinance.com/en/articles/15419794-how-to-move-your-investments-from-hapi-to-arq).
  - Inactividad, artículo no leído: [Hapi](https://hapi.trade/en/support/my-account/inactivity-fees).
- **Alpaca**
  - Wires, conversión local, posiciones (ACATS saliente US$ 25, DTC saliente US$ 5 por valor y envío, DWAC US$ 150) y tasas SEC y CAT: [Fee Schedule, 12-oct-2026](https://files.alpaca.markets/disclosures/library/BrokFeeSched.pdf).
- **Schwab**
  - Mínimo US$ 0 para Schwab One International: [Schwab Pricing Guide](https://www.schwab.com/legal/schwab-pricing-guide-for-individual-investors), extracto del buscador, abr-2026.
  - Wire saliente US$ 25, o US$ 15 en línea, y ACAT: [Brokerage-Review, 20-abr-2026](https://www.brokerage-review.com/online-brokers/fees/charles.aspx) y [Wise US blog](https://wise.com/us/blog/charles-schwab-transfer-limits), ambas secundarias.
- **Tyba:** [Bolsillos Llenos, b9NDw2s1ado](https://www.youtube.com/watch?v=b9NDw2s1ado) y [lyvFdb1PERE](https://www.youtube.com/watch?v=lyvFdb1PERE).
- **XTB:** [XTB Commission Table INT, 14-mar-2026](https://www.xtbofficial.com/int/actual_commission_table.pdf).
- **SAB**
  - BBVA Bolsa (tarifario vigente desde el 01-oct-2024): S/ 100 por operación en mercado extranjero; recepción de valores CAVALI–DTC US$ 15; envío US$ 15; traspaso a otros intermediarios S/ 100. Otra versión del documento dice US$ 24 por envío o recepción vía DTC. Ambas cifras vienen del extracto del buscador. — [BBVA Bolsa, servicios indirectos](https://www.bbva.pe/content/dam/public-web/peru/documents/personas/inversiones/bbva-bolsa/tarifario-servicios-relacionados-indirectamente-actividades-intermediacion.pdf); [BBVA Bolsa, servicios directos](https://bolsa.bbva.pe/content/dam/public-web/fondos-peru/documents/personas/inversiones/bbva-bolsa/tarifario-servicios-relacionados-directamente-actividades-intermediacion.pdf)
  - Apps locales con comisión de "1% o mínimo 40 soles": [Bolsillos Llenos, lyvFdb1PERE](https://www.youtube.com/watch?v=lyvFdb1PERE).
  - Tasas de CAVALI: [Tarifario CAVALI 2026.07.01](https://s3.us-east-1.amazonaws.com/site.documents.cdn.prod.bvl.com.pe/Tarifario_CAVALI_2026.07.01.pdf).
- **Recepción en Interbank, US$ 25:** [Wise blog Perú](https://wise.com/pe/blog/transferencia-internacional-interbank).
- **Intermediarios en retiros de XTB:** entre US$ 25 y 75 según el creador. — [Luis Ccaccya, IacmrD3u_F8](https://www.youtube.com/watch?v=IacmrD3u_F8)

### Inferences
- **Retiro de US$ 1,000**, cambiando a soles en fintech (≈0.4%):

  | Bróker | Costo | % |
  |---|---|---|
  | IBKR | ≈US$ 29 | 2.9% |
  | Hapi | ≈US$ 12 | 1.2% |
  | Alpaca (wire) | ≈US$ 64 | 6.4% |
  | Tyba | ≈US$ 19 | 1.9% |

  En montos pequeños, el US$ 25 que cobra Interbank por recibir del exterior pesa más que lo que cobra el bróker. Conviene tener la cuenta receptora en un banco que no cobre la recepción; BCP no cobraría, según un blog comercial no verificado (ver `brokers_vias_acceso.md`).
- **Retiro de US$ 7,000:**

  | Bróker | Costo | % |
  |---|---|---|
  | IBKR | ≈US$ 53 | 0.76% |
  | Hapi | ≈US$ 36–52 | 0.5–0.7% |
  | Alpaca (wire) | ≈US$ 88 | 1.3% |
  | Tyba | ≈US$ 133 | 1.9% |

  En la ruta BVL el núcleo no se retira desde el bróker, así que este caso aplica sobre todo a la cuenta de trading o a un cambio de plan.
- **Ventaja estructural de IBKR para la salida:** IBKR no cobra la salida DTC, Hapi cobra US$ 25 y Alpaca US$ 5. Sumando la recepción o "migración" de la SAB, US$ 15–24, la salida cuesta ≈US$ 15–24 desde IBKR, ≈US$ 40–49 desde Hapi y ≈US$ 20–29 desde Alpaca. Es un costo único, por valor.
- **XTB no sirve para el núcleo:** la regla de inactividad castiga justo el comprar y mantener. Sin operar en 365 días ni depositar en 90, cobra €10 al mes (≈€120 al año), además de la desventaja de protección ya documentada.

### Gaps
- Comisión de venta en la BVL de la SAB de destino (Renta 4, Kallpa, Credicorp, BBVA). Es el costo variable que falta en la ruta BVL.
- Monto del clearing fee de Hapi y contenido de su política de inactividad.
- Si el tope de US$ 3,000 por retiro de Hapi aplica a retiros bancarios.
- Comisiones de Schwab International para salida DTC y elegibilidad de Perú.

---

## 3. ¿Permite IBKR la salida por DTC hacia el custodio de una SAB peruana? ¿A qué costo?

### Takeaway
Sí es factible y, del lado de IBKR, gratuito. IBKR documenta transferencias salientes Free of Payment (FOP) por DTC hacia "another US bank or broker that is a member of the DTC" y dice no cobrar por procesarlas, aunque repercute lo que cobre la contraparte.

La SAB peruana no es participante DTC: recibe a través de su custodio o intermediario en EE.UU. La transferencia se dirige al número DTC de ese custodio, con la cuenta de la SAB y la subcuenta del cliente.

Que IBKR la acepte hacia una SAB concreta solo está "confirmado por soporte" según Bolsillos Llenos. Ningún caso real documentado parte de IBKR.

### Cited Findings
- **Sin cargo de IBKR:** "IB does not assess a fee to process FOP transfers, other firms may and we therefore recommend that you confirm with the contra-firm their policies". Si la contraparte le cobra a IBKR, "the fee will be passed to the IB account holder". Extracto del buscador; el acceso directo dio 403. — [IBKR KB, Free of Payment (FOP) Transfers](https://ibkb.interactivebrokers.com/de/node/1002); [IBKR KB, Non-ACAT US Transfers](https://ibkb.interactivebrokers.com/de/node/2173)
- **Alcance de la transferencia saliente** (guía oficial de IBKR): va "from your account to another US bank or broker that is a member of the DTC". Cubre "long US stock, warrant and US Bond positions" y pide "account number, account title and account type at the selected broker" y el Tax ID. La guía no nombra ETFs; en la práctica, VOO es un valor de EE.UU. elegible en DTC. — [IBKR Guides, FOP Transfers](https://ibkrguides.com/advisorportal/ug/foptrans.htm); [IBKR Guides, Transfer Positions](https://www.ibkrguides.com/iphone/transfer-positions.htm)
- **Otras tarifas de IBKR** (secundaria, 07-ago-2026): no cobra ACAT saliente; DWAC US$ 100 por transacción; DRS US$ 5. — [Brokerage-Review](https://www.brokerage-review.com/account-fee/acat/interactive-brokers-transfer-fee.aspx)
- **Bolsillos Llenos:** "Charles Schwab, Interactive Brokers, incluso XTB, he podido conversar con sus áreas de soporte y me han confirmado que pueden hacer el proceso". Hapi "ya lo ha hecho". Tyba "solo pueden transferir a brokers de Estados Unidos". — [lyvFdb1PERE, 18-may-2026](https://www.youtube.com/watch?v=lyvFdb1PERE)
- **Caso Hapi → Renta 4** (mar-2026):
  - Fue una transferencia DTC, no ACAT.
  - Costó US$ 25 de salida en Hapi más US$ 20 de "migración" en Renta 4.
  - Tardó entre 1 y 3 semanas.
  - El costo promedio no viaja con los títulos y hay que informarlo a la SAB.
  - Fuente: [ZkskDYeDcyw, 25-may-2026](https://www.youtube.com/watch?v=ZkskDYeDcyw); detalle en `youtube_bolsillos_llenos.md`.
- **Lado receptor en una SAB peruana:** BBVA Bolsa cobra US$ 15 por recepción CAVALI–DTC (otra versión del tarifario dice US$ 24). — [BBVA Bolsa, tarifario](https://www.bbva.pe/content/dam/public-web/peru/documents/personas/inversiones/bbva-bolsa/tarifario-servicios-relacionados-indirectamente-actividades-intermediacion.pdf)
- **Alpaca:** DTC saliente US$ 5 por valor y envío; ACATS saliente US$ 25. — [Alpaca Fee Schedule, 12-oct-2026](https://files.alpaca.markets/disclosures/library/BrokFeeSched.pdf)

### Inferences
- **Qué implica el caso Hapi para IBKR:** el mecanismo es el mismo, un DTC FOP desde un participante de EE.UU. hacia el custodio de la SAB. El costo de origen baja de US$ 25 a US$ 0. El costo total de la salida queda en lo que cobre la SAB (≈US$ 15–24 de recepción o migración) más su comisión de venta en la BVL.
- **Hay un punto operativo que Hapi resolvió y en IBKR está por probar:** IBKR exige que el receptor sea un "US bank or broker… DTC member" y pide el número de cuenta en ese bróker. La SAB debe dar las instrucciones de su custodio (número DTC del participante, cuenta de la SAB, referencia del cliente) y el titular debe coincidir. Si IBKR rechazara la cuenta ómnibus de un tercero extranjero, quedaría como puente un bróker de EE.UU. que sí acepte, por ejemplo Hapi recibiendo por ACAT y enviando por DTC. Ese puente costaría US$ 25 de salida en Hapi más la SAB.
- **El costo promedio:** IBKR muestra el costo promedio en sus reportes (Activity Statement y Tax Lots), así que debería ser más fácil acreditarlo ante la SAB que con Hapi, que obligó a mandar una captura de la app. No verificado.
- **Prueba barata antes de comprometer el núcleo:** comprar 1 acción de VOO en IBKR y transferirla a la SAB elegida. Así se valida el circuito, el costo real y el registro del costo en CAVALI. Cuesta ≈US$ 1 + US$ 15–24.

### Gaps
- No hay confirmación escrita de IBKR para una SAB peruana concreta ni ningún caso documentado desde IBKR. Hay que pedirla por ticket en Client Portal, indicando la SAB y su custodio.
- Qué custodio de EE.UU. usan Renta 4 SAB, Kallpa, Credicorp Capital SAB e Inteligo SAB para recibir por DTC, y cuánto cobra cada una por recepción, migración y venta.
- La página oficial de tarifas de IBKR LLC no se pudo leer (403). El "sin cargo por FOP" viene del extracto del Knowledge Base.

---

## 4. Seguridad y acceso: operar solo por web, sin app financiera en el teléfono

### Takeaway
IBKR y Alpaca se pueden operar 100% por web o escritorio, con TOTP estándar que puede vivir en un gestor de contraseñas de escritorio (KeePass o 1Password), sin app financiera.

En IBKR, el TOTP de terceros ("Mobile Authenticator") existe oficialmente, pero solo para "eligible users" según criterios regionales. Hay que comprobar que se ofrece en Perú.

Ninguno de los brókers revisados admite llaves FIDO2 o passkeys. Hapi tiene versión web según reseñas, pero algunos flujos (retiros cripto) piden biometría en la app. Tyba fondea vía la banca BCP.

### Cited Findings
- **IBKR, Mobile Authenticator (guía oficial):**
  - Permite a "eligible users" usar una app de autenticación de su elección. La elegibilidad depende de criterios regionales ligados a la tasa de éxito de entrega de SMS.
  - Nombra Microsoft Authenticator, Google Authenticator y Authy, y gestores con TOTP como 1Password, KeePass y Keeper.
  - Los códigos se generan "independently from phone carriers or Internet access".
  - No menciona llaves hardware.
  - Fuente: [IBKR Guides, Mobile Authenticator](https://www.ibkrguides.com/brokerportal/sls/mobile-authenticator.htm)
- **IBKR, FAQ de 2FA:** lista IB Key (IBKR Mobile), Mobile Authenticator, SMS, 2FA por email, Digital Security Card+ y dispositivo temporal. No menciona FIDO ni passkeys. — [IBKR Guides, 2FA FAQ](https://ibkrguides.com/securelogin/sls/faq.htm)
- La Digital Security Card+ solo se entrega a cuentas de más de US$ 1 M, y los límites de retiro dependen del método de 2FA (ver `brokers_vias_acceso.md`, sección 5).
- **Alpaca:** TOTP con "standalone authenticator apps or password managers", sin FIDO2 ni passkeys. El MFA es obligatorio para depositar, operar y retirar en cuenta live, y protege el dashboard, no el trading por API. — [Alpaca Learn, MFA, 15-oct-2026](https://alpaca.markets/learn/guide-to-multi-factor-authentication-mfa-account-security-for-alpaca-builders)
- **Hapi:**
  - Tiene versión web en hapi.trade (Safari, Chrome, Firefox y Brave), según reseñas de terceros. — [Rankia Colombia](https://www.rankia.co/blog/trading-desde-cero/5983831-review-opiniones-broker-hapi-colombia); [Guía deTrader, Hapi](https://www.guiadetrader.com/broker/hapi)
  - Los retiros cripto requieren verificación biométrica. — [Hapi, How to withdraw funds](https://help.hapi.trade/en/articles/8949332-how-to-withdraw-funds)
- **Tyba:** el depósito se hace con "pago de servicios" desde la banca móvil o web del BCP. — [Bolsillos Llenos, b9NDw2s1ado](https://www.youtube.com/watch?v=b9NDw2s1ado)
- **Firstrade:** su página internacional no menciona 2FA; solo enlaza a un "Security Center". — [Firstrade, International](https://firstrade.com/accounts/international)

### Inferences
- **Configuración que respeta la preferencia del usuario en IBKR:** Client Portal web o TWS de escritorio, con 2FA por Mobile Authenticator en KeePassXC u otro gestor de escritorio. Si Perú no es elegible para TOTP, quedan el SMS o IB Key. IB Key obliga a instalar IBKR Mobile, aunque solo como autenticador, en el celular dedicado que el plan ya contempla para Pibank.
- **Para trading automatizado en el VPS**, Alpaca tiene una ventaja operativa: sus API keys no pasan por MFA. En IBKR, la API (TWS o IB Gateway, Web API) requiere una sesión autenticada con 2FA que caduca periódicamente. Es inferencia a partir del modelo de sesión de IBKR, no verificada en esta sesión.
- **Sin llaves FIDO2 en ningún bróker revisado**, la defensa contra el phishing en tiempo real recae en el gestor de contraseñas, que solo autocompleta en el dominio correcto, y en que los retiros solo vayan a cuentas propias.

### Gaps
- Si "Mobile Authenticator" (TOTP) está habilitado para residentes en Perú en IBKR. Se resuelve probándolo en la apertura.
- 2FA de Hapi en web, de Tyba y de Schwab International: método y si exige la app.
- Si Hapi permite fondear, retirar y pedir la transferencia DTC desde la web, sin la app.

---

## 5. Alternativas a Alpaca para una cuenta de trading de ~US$ 1,850 en efectivo (acciones y ETFs de EE.UU.)

### Takeaway
Alpaca no es la única opción. La alternativa real es una **segunda cuenta en IBKR**, de tipo cash, bajo el mismo usuario:
- se fondea en el mismo wire que el núcleo, con costo marginal ≈0;
- tiene API completa;
- cobra US$ 0.35–1 por orden;
- su 2FA complica la automatización.

tastytrade ofrece cuentas internacionales cash o margin con API, pero no se confirmó Perú. Hapi, Tyba y Trii no tienen API pública para un sistema cuantitativo. Firstrade y Schwab no tienen elegibilidad confirmada para Perú.

Desde el 4-jun-2026 la regla PDT de FINRA fue reemplazada por estándares de margen intradía. Alpaca los aplicó en esa fecha, así que el "máx. 3 day-trades" del CLAUDE.md de Quantac quedó desactualizado.

### Cited Findings
- **Fin de la regla PDT:** la SEC aprobó el 14-abr-2026 la propuesta SR-FINRA-2025-017. FINRA "adopted new intraday margin standards to replace in their entirety" las reglas de day trading, incluida la prueba de conteo de day trades. Rige desde el 4-jun-2026, con transición opcional para las firmas hasta el 20-oct-2027. — [FINRA, Regulatory Notice 26-10](https://www.finra.org/rules-guidance/notices/26-10/)
- **Alpaca:**
  - Implementó el cambio "in line with" el 4-jun-2026. El equity mínimo para 4x de poder de compra intradía bajó de US$ 25,000 a US$ 2,000.
  - Sus divulgaciones dicen que "All accounts are opened as limited purpose margin accounts".
  - El artículo no dice si incluye cuentas no residentes; enlaza una FAQ sobre cuentas "Non-Leverage Margin" que no se leyó.
  - Fuente: [Alpaca blog, 27-abr-2026, actualizado 04-jun-2026](https://alpaca.markets/blog/finra-retires-the-pdt-rule-introducing-alpacas-new-intraday-margin-framework/)
- **Alpaca, comisiones:** sin comisión en acciones y ETFs, salvo opciones sobre índices, el Elite Smart Router y el flujo "no retail". Tasas que se trasladan al cliente:
  - SEC: 0.0000206 × valor, solo en ventas.
  - FINRA TAF: US$ 0 por acción en ventas.
  - CAT: US$ 0.000003 por acción.
  - Fuente: [Alpaca Fee Schedule, 12-oct-2026](https://files.alpaca.markets/disclosures/library/BrokFeeSched.pdf)
- **IBKR, varias cuentas del mismo titular:** se abren desde Settings → "Open an Additional Account". Comparten usuario y contraseña. Los permisos de trading se configuran por cuenta y se puede mover efectivo y títulos entre cuentas propias.
  - Fuentes: [NoMoneyLah, 04-mar-2026](https://nomoneylah.com/2026/03/04/open-additional-account-ibkr/) (secundaria, de un influencer pagado por IBKR); [foro Mustachian Post](https://forum.mustachianpost.com/t/multiple-portfolios-on-ibkr/15303) (anecdótico).
  - Las cuentas con el mismo titular y el mismo Tax ID se agrupan para el límite de SIPC y de Lloyd's. — [IBKR KB, SIPC con múltiples cuentas](https://ibkb.interactivebrokers.com/hu/tag/regulatory-agencies?page=6)
- **IBKR, comisiones y API:**
  - Un residente peruano queda en IBKR Pro: Fixed US$ 0.005 por acción con mínimo de US$ 1; Tiered desde US$ 0.35 por orden más tasas. — [IBKR Commissions](https://www.interactivebrokers.com/commissions); [IBKR, Lite solo para residentes de EE.UU.](https://brokerage.ibkr.com/en/general/compare-lite-pro.php)
  - IBKR publica una Web API que incluye gestión de cuenta y transferencias de posiciones. — [IBKR Web API docs](https://www.interactivebrokers.com/docs/web-api/account-management/funds-and-banking/position-transfers)
- **tastytrade:** los clientes internacionales pueden abrir "individual margin, individual cash, and joint accounts", fondear por wire, cheque o stablecoins (USDC, USDT, PYUSD, RLUSD), y no hay retiros en stablecoins. La lista de países está en otro artículo, "updated often", que no se leyó; Perú no está confirmado (página actualizada el 19-mar-2026). — [tastytrade, International Account](https://tastytrade.com/learn/accounts/account-types/international-account/)
- **Firstrade:** la lista visible de "Do I qualify?" tiene 12 regiones (China, Hong Kong, India, Israel, Japón, Corea, Macao, Malasia, México, Nueva Zelanda, Singapur y Taiwán), sin Perú. Ofrece comisión US$ 0, sin mínimos ni mantenimiento, y SIPC más un exceso de US$ 150 M en agregado. — [Firstrade, International](https://firstrade.com/accounts/international)
- **Hapi y Tyba:** apps sin API pública documentada. Comisión 0% en Hapi; en Tyba, 0% en acciones enteras y 0.3% en fracciones. — [Hapi Help Center](https://help.hapi.trade/en/articles/8945476-how-can-i-fund-my-account); [Bolsillos Llenos, b9NDw2s1ado](https://www.youtube.com/watch?v=b9NDw2s1ado)
- **XTB y eToro:** entidades offshore (Belice y Seychelles), ya descartadas en `brokers_vias_acceso.md`.

### Inferences
- **Costo de comisiones en IBKR** (Tiered): con posiciones de ≈US$ 300–600 y un mínimo de US$ 0.35 por orden, el costo es ≈0.06–0.12% por lado, ≈0.12–0.23% ida y vuelta. Con ~100 órdenes al año (rebalanceo mensual de ~4 posiciones, con entradas y salidas), son ≈US$ 35 al año. En Fixed serían ≈US$ 100. Alpaca cobra US$ 0, pero su modelo es de pago por flujo de órdenes, así que el costo implícito de ejecución no es cero. No se midió.
- **Punto de equilibrio IBKR frente a Alpaca:** Alpaca necesita su propio wire de entrada (≈US$ 30 + corresponsales + cambio ≈ US$ 37–67) y uno de salida (US$ 35 + US$ 25 de recepción). IBKR va dentro del wire del núcleo y tiene un retiro gratis al mes. La diferencia de fondeo, ≈US$ 30–60, equivale a ~85–170 órdenes al año a US$ 0.35. Por debajo de ese número, IBKR sale más barato en el primer año (con Tiered). Si la cuenta se cierra y se repatria, Alpaca suma ≈US$ 67 más.
- **Cuenta cash frente a margin:** una cuenta cash elimina por construcción el apalancamiento y la llamada de margen. A cambio, impone la liquidación T+1 antes de reutilizar el producto de una venta, con riesgo de *good-faith violations* si se recompra con fondos no liquidados. Con rebalanceo mensual y swing de 2 a 20 días, esa restricción casi no muerde. Esto viene de la regla general de cuentas cash; no se verificó en las páginas de IBKR en esta sesión.
- **Misma cuenta IBKR con disciplina o subcuenta separada:** es razonable siempre que sea una **cuenta aparte** (otro número, tipo cash), no solo disciplina dentro de la cuenta del núcleo. Así:
  1. el kill switch de -30% se mide sobre un NAV limpio;
  2. un error del algoritmo no puede vender VOO;
  3. el registro fiscal queda separado (ver la inferencia siguiente);
  4. no hace falta un segundo wire.

  El costo es acoplar el riesgo operativo: un solo login y un solo 2FA para todo. Hay que configurar la API para que solo opere la cuenta de trading. IBKR permite elegir la cuenta por orden; restringir la API a una cuenta no se verificó.
- **Las ventas de trading y del núcleo caen en canastas fiscales distintas:** las de trading van al art. 51, 1.er párrafo, que se suma al trabajo. El núcleo vendido por la BVL va al 2.º párrafo (6.25%). Tenerlos en cuentas separadas simplifica el costo promedio ponderado por canasta (ver `youtube_bolsillos_llenos.md`).
- **Costo de cambiar de bróker en Quantac:** el proyecto está construido sobre la API de Alpaca, con cron en un VPS. Pasar a IBKR exige un adaptador y resolver el 2FA en el servidor, con IB Gateway o IBC, o OAuth si estuviera disponible para cuentas individuales (no verificado). Es trabajo de ingeniería, no costo monetario, pero es real.

### Gaps
- Elegibilidad de Perú en Alpaca live, tastytrade, Schwab International y Firstrade, en la lista completa. Ninguna fuente pública lo confirma; hay que preguntar por ticket o probar el formulario.
- Si Alpaca permite a un no residente una cuenta sin margen (multiplicador 1, "non-leverage margin") y cómo la trata la nueva regla intradía.
- Si IBKR permite restringir una sesión de API a una sola cuenta del mismo usuario y si ofrece OAuth a cuentas individuales.
- Costos de datos de mercado en tiempo real en IBKR para uso por API, si Quantac los necesitara.
- No se investigaron Webull, moomoo, TradeStation ni Tradier para residentes peruanos.

---

## Recomendación

### Takeaway
1. **Núcleo VOO: Interactive Brokers.** No es por el depósito, que cuesta lo mismo que en Alpaca y un poco más que en Hapi. Es porque:
   - la salida DTC cuesta US$ 0 y no tiene custodia ni inactividad;
   - da un retiro gratis al mes;
   - se opera por web con TOTP (a confirmar para Perú);
   - tiene la protección más fuerte de la lista.
2. **Respuesta directa a "¿IBKR me conviene por las comisiones de depósito y retiro?":**
   - **En el depósito, no hay ventaja.** El costo lo pone el banco peruano (≈US$ 42 + corresponsales) y el cambio, igual que con Alpaca o Schwab.
   - **En los retiros, sí.** IBKR no cobra el primero del mes; Alpaca cobra US$ 35.
   - **En la salida DTC hacia la SAB, es lo mejor.**
   - **En los aportes de US$ 300, es malo por wire.** Solo es bueno si SafetyPay sale barato, o por la vía Takenos → Wise.
3. **Trading: Alpaca no es la única opción.** Si Alpaca confirma Perú, conviene seguir con Alpaca por la integración ya hecha y la automatización sin 2FA. Si no, una segunda cuenta cash en IBKR es la alternativa natural y cuesta lo mismo o menos en el primer año.

### Cited Findings
Insumos de costo (todos citados en las secciones 1 a 3):
- **Fondeo:**
  - Interbank cobra US$ 42 por wire en el tramo de US$ 3,001–10,000, US$ 30 hasta US$ 3,000 y US$ 25 por recibir del exterior. — [Wise blog Perú](https://wise.com/pe/blog/transferencia-internacional-interbank)
  - Kambista: diferencial de S/ 0.027. — [Comparabien](https://comparabien.com.pe/producto/cambio-divisas/kambista-usd)
  - Hapi: US$ 1.99 por depósito en PEN. — [Hapi](https://help.hapi.trade/en/articles/12631400-what-is-cross-payments-and-how-to-use-it-to-deposit-into-hapi)
- **IBKR:** un retiro gratis al mes, luego US$ 10 — [IBKR IMPACT pricing](https://impact.ibkr.com/en/pricing.php). FOP sin cargo de IBKR — [IBKR KB](https://ibkb.interactivebrokers.com/de/node/1002). Custodia e inactividad US$ 0 — [IBKR Other Fees](https://gdcdyn.interactivebrokers.com/en/pricing/other-fees-overview.php).
- **Alpaca:** wire internacional saliente US$ 35, DTC saliente US$ 5 por valor y conversión local 1.5% con tope de US$ 40. — [Alpaca Fee Schedule, 12-oct-2026](https://files.alpaca.markets/disclosures/library/BrokFeeSched.pdf)
- **Hapi:** salida DTC US$ 25 por valor hacia una SAB peruana — [Bolsillos Llenos](https://www.youtube.com/watch?v=NXKKWVudXuw). Retiro US$ 7.99 — [Hapi](https://help.hapi.trade/en/articles/8949332-how-to-withdraw-funds).
- **SAB receptora:** BBVA Bolsa cobra US$ 15 (o US$ 24) por recepción vía DTC — [BBVA Bolsa](https://www.bbva.pe/content/dam/public-web/peru/documents/personas/inversiones/bbva-bolsa/tarifario-servicios-relacionados-indirectamente-actividades-intermediacion.pdf). Renta 4 cobró US$ 20 por la migración — [Bolsillos Llenos](https://www.youtube.com/watch?v=ZkskDYeDcyw).

### Inferences

**(a) Núcleo VOO: US$ 6,800 en un solo depósito, sin venta en el primer año.**

Costo del primer año en soles (S/ 3.40 por US$), con el aporte mensual opcional y la salida futura, que se paga una sola vez.

| # | Opción | Primer año, depósito único | + 12 aportes de US$ 300 | Salida futura a la SAB (por valor) | Por qué en este lugar |
|---|---|---|---|---|---|
| 1 | **IBKR**: cambio en Kambista/Rextie → USD propios → 1 wire Interbank → VOO | **S/ 240–340** (cambio ≈US$ 27 + wire US$ 42 + corresp. US$ 0–30 + comisión US$ 1). Con OUR: ≈S/ 390. Cambiando en el banco: +S/ 185 | Por Takenos+Wise: +≈S/ 160–200 (1% + cambio s/d + US$ 1 por compra). Por SafetyPay: s/d. **Por wire: +≈S/ 1,310, no hacerlo** | **≈S/ 50–80** (IBKR US$ 0 + SAB US$ 15–24) + comisión de venta en la BVL (s/d) | Salida más barata, sin custodia ni inactividad, web con TOTP, SIPC + exceso con Lloyd's, misma cuenta que puede alojar el trading |
| 2 | **Hapi**: depósito en PEN | **S/ 100–240** (US$ 1.99 + diferencial de Cross Payments s/d; con 0.4–1%: US$ 27–68) | +≈S/ 130–205 (12 × US$ 1.99 + cambio) | ≈S/ 135–165 (US$ 25 + SAB US$ 15–24) + venta | La ruta BVL ya está probada por Bolsillos Llenos y el fondeo es el más barato. En contra: más centrado en la app, 2FA no documentado, política de inactividad no leída, posible tope de retiro de US$ 3,000 y es una fintech más chica sobre Apex. **Es la mejor opción para los aportes pequeños**, incluso si el núcleo está en IBKR |
| 3 | **Alpaca**, si acepta Perú | S/ 235–337 (igual que IBKR por wire; comisión US$ 0) | Como IBKR por wire, salvo que la conversión local en PEN funcione (1.5%, tope US$ 40) | ≈S/ 70–100 (US$ 5 + SAB) | Barato, pero la cuenta es de margen por defecto, Perú no está confirmado y mezclaría el núcleo con el proyecto de trading |
| 4 | **Schwab International**, si acepta Perú | ≈S/ 240–340 (wire; comisión US$ 0) | Wire: inviable | s/d | Sin confirmación para Perú ni tarifa de salida DTC |
| 5 | **SAB**: comprar VOO directamente en la BVL | ≈S/ 320–380+ (comisión ≈1% o mínimo S/ 40, más cambio, CAVALI y BVL; secundaria) | Mínimos por operación: caro | S/ 0 de traslado; solo comisión de venta | Evita el paso DTC, pero la liquidez de VOO en la BVL no está demostrada y la comisión vuelve a pagarse en cada compra |
| — | Descartados | **Tyba:** 1.5% al entrar (≈S/ 347) y 1.5% al salir, y no transfiere a Perú. **XTB:** offshore, con €10 al mes de inactividad si solo se mantiene. **eToro:** no transfiere títulos | | | |

Con los aportes en Hapi, la salida de esa parte paga US$ 25 por valor desde Hapi más la SAB. Es un costo fijo que se amortiza mejor si los aportes acumulados superan unos US$ 2–3 mil.

**Variante recomendada:** el depósito único va a IBKR y los aportes mensuales se acumulan en Hapi o, si la tarifa de SafetyPay resulta baja, directamente en IBKR. Al vender, se transfiere VOO desde ambos brókers a la misma SAB. La salida cuesta ≈US$ 15–24 por la parte en IBKR y ≈US$ 40–49 por la parte en Hapi. **Primer año ≈S/ 370–545** (S/ 240–340 del núcleo más S/ 130–205 de los aportes).

**(b) Trading: US$ 1,850, cuenta cash, sin apalancamiento.**

Supuesto: ~100 órdenes al año, sin cerrar la cuenta; el cierre y la repatriación se muestran aparte.

| # | Opción | Primer año | Si se cierra y se repatría | Por qué en este lugar |
|---|---|---|---|---|
| 1 | **Alpaca**, si confirma Perú (cuenta separada, como dice el plan) | **S/ 130–230**: wire Interbank US$ 30 + corresp. US$ 0–30 + cambio US$ 7; comisión US$ 0; tasas de traspaso < US$ 1 | +≈S/ 230 (US$ 35 + recepción US$ 25 + cambio) | Quantac ya está integrado y en paper; las API keys funcionan sin MFA en el VPS; comisión cero y aislamiento total del núcleo. Ya no rige la PDT (margen intradía desde el 4-jun-2026), pero la cuenta es "limited purpose margin": verificar que pueda quedar sin apalancamiento |
| 2 | **IBKR**, segunda cuenta cash bajo el mismo usuario, fondeada en el mismo wire del núcleo | **S/ 145–365**: cambio US$ 7 + wire marginal US$ 0 + comisiones US$ 35 (Tiered) a US$ 100 (Fixed) | +≈S/ 110 (retiro gratis + recepción US$ 25 + cambio) | Sin segundo wire ni segundo bróker, y es cash por construcción. En contra: comisión por orden (≈0.1% por lado en órdenes de US$ 300–600), API más compleja y 2FA en el servidor, y un solo login para núcleo y trading. **Es la opción por defecto si Alpaca no acepta Perú** |
| 3 | **tastytrade**, si acepta Perú | s/d (wire similar a Alpaca; comisiones no leídas) | s/d | Admite cuentas cash internacionales y tiene API, pero falta todo lo de Perú |
| — | Descartados para un sistema cuantitativo | Hapi y Tyba (sin API pública), Trii (solo BVL), Firstrade (Perú no figura), XTB y eToro (offshore) | | |

**Lectura de la tabla:** con menos de ~100 órdenes al año, IBKR y Alpaca cuestan prácticamente lo mismo en el primer año. Lo que decide es la elegibilidad de Perú en Alpaca y el costo de ingeniería de migrar Quantac. Si Alpaca no acepta Perú o exige margen sin posibilidad de desactivarlo, la segunda cuenta en IBKR es la opción correcta, no un parche.

### Gaps
Pendientes que cambian la recomendación, por orden de impacto. Todas se resuelven en noviembre de 2026 sin costo:
1. Tarifa y tipo de cambio de **SafetyPay en IBKR para Perú**. Si salen por debajo de ~0.7%, los aportes van directo a IBKR y Hapi sobra.
2. **Ticket a IBKR:** si acepta un DTC FOP saliente hacia el custodio de la SAB elegida y cuál es ese custodio. Si no lo acepta, Hapi pasa a ser el núcleo o el puente.
3. **Ticket a Alpaca:** si Perú es elegible para cuenta live y si la cuenta puede operar sin apalancamiento.
4. **2FA TOTP de IBKR para Perú:** comprobarlo en la apertura.
5. **Tarifario de la SAB de destino:** recepción DTC, migración, comisión de venta en la BVL y custodia de valores extranjeros.
6. **Tipo de cambio de Cross Payments (Hapi)** y su política de inactividad, que pesa para un núcleo que solo se mantiene.

También hay que actualizar el CLAUDE.md de Quantac: la "Restricción PDT activa" ya no corresponde desde el 4-jun-2026 ([FINRA RN 26-10](https://www.finra.org/rules-guidance/notices/26-10/)).
