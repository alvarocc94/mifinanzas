# PLAN — asignación de los S/ 100,000

> El fondo de emergencia está aparte y no entra en este monto.
> Fuentes: los tres informes de `reports/` y las notas de `research_notes/`. Cada cifra con su
> fecha está allí; aquí solo va la decisión y su porqué.

## Propuesta inicial del dueño (2026-10-29)

| Bloque | Monto |
|---|---|
| Inmueble (inicial de departamento o terreno) | S/ 50,000 |
| Ahorro / DPF | S/ 20,000 |
| ETFs | S/ 20,000 |
| Trading | S/ 10,000 |

## Decisión v1 (2026-10-31)

| Bloque | Monto | Dónde | Por qué |
|---|---|---|---|
| Reserva de ahorro | S/ 20,000 | 3 DPF de S/ 5,000 en Alfin a 360 días (5.65% TREA, en agencia, sin app ni tarjeta) + S/ 5,000 en Pibank (5%) con la app solo en un celular dedicado que no sale de casa | Informe 1. Con este monto el FSD cubre el principal; el riesgo real es el robo del celular, así que primero va el canal y después la tasa |
| Fondo de vivienda | S/ 40,000 | DPF en soles a 360 días, repartido en dos entidades A- (p. ej. S/ 20k en Alfin y S/ 20k en Caja Arequipa, Caja Huancayo o Efectibank) | No comprar todavía (ver abajo). Es dinero que puede convertirse en inicial en 2–5 años, así que va en soles y sin riesgo de mercado |
| Inmuebles sin deuda | S/ 10,000 | FIBRA Prime (BVL), por **Renta 4 SAB** (ver "SAB para FIBRA Prime") | Exposición inmobiliaria sin hipoteca: ~7.3% neto en US$ (TTM de distribuciones a nov-2026; en oct-2026 se tomó 7.6–8.3% de la guía). No más, porque es un solo emisor y está en dólares |
| Núcleo indexado | S/ 23,500 | **SPYL** (S&P 500, Irlanda, acumulación, TER 0.03%) en Interactive Brokers, operado por web (ver abajo) | Informe 3 y su actualización. Con Quantac, el índice fue la vara que nada superó |
| Experimento de trading | S/ 6,500 | Alpaca live si acepta residentes peruanos; si no, una segunda cuenta *cash* (sin margen) en IBKR. Solo después de 8 semanas en paper, con las reglas del informe 3 | Da la misma información que S/ 10,000 y pierde menos. Pérdida máxima ≈ S/ 2,250 con el kill switch al −30% |
| **Total** | **S/ 100,000** | | |

Por moneda: ~S/ 60k en soles (reserva y fondo de vivienda) y ~S/ 40k en dólares (FIBRA, ETF y
trading). Tu sueldo y tu vivienda futura están en soles, así que la renta variable va en dólares
sin cubrir y la parte defensiva queda en soles.

## Por qué no se compra vivienda ahora

- **Puedes volver a usar el crédito MiVivienda, pero no el bono.** El Fondo financia como
  máximo dos veces a una persona, y "solo el primer crédito… podrá contar con el subsidio"
  (fichas del Fondo en gob.pe, vistas el 31-oct-2026). Tu intuición de que "como ya no tengo
  nada, vuelvo a calificar" vale para el crédito, no para el subsidio. La "penalidad" que
  pagaste al vender fue la devolución del bono: ~S/ 16,500 descontados en la liquidación
  (confirmado por el dueño el 2026-11-07), por cancelar antes de los 5 años. No encontré una
  regla que devuelva la elegibilidad a quien reembolsó el bono, pero se pregunta por escrito
  (ver pendientes).
- **Sin bono, la cuenta cambia de signo.** El informe 2 recomendaba la vivienda propia porque
  el bono (S/ 21–28k) y la inicial de 7.5% le ganaban a todo. Sin bono, a 5 años comprar en
  Lince, Jesús María, Pueblo Libre o Magdalena solo conviene si la vivienda se aprecia
  3.2–5.7% nominal al año. Esos distritos subieron ~1–3% al año en soles en los últimos 5 años
  (BCRP). **En el escenario base gana alquilar.**
- **Lo que sí vale:** el segundo crédito MiVivienda da plazo de 25 años. Es una opción para más
  adelante, no un motivo para comprar ya.
  - **Corrección del 2026-11-12:** la inicial no es 7.5%. El reglamento vigente (v26, RGG
    000054-2025-FMV/GG) presta como máximo el 90% del valor, así que sin bono la inicial real es
    10%, igual que un hipotecario convencional. Falta que un banco lo confirme por escrito.
  - Con S/ 50k el techo baja de ~S/ 460k a ~S/ 395k, dejando S/ 5k de colchón.
  - El umbral de plusvalía no cambia, porque el modelo ya suponía 10% de inicial.
  - Detalle en `reports/Proyectos de departamentos en Lima Moderna.md`.
- **Plan de vivienda:** cuando te mudes, alquila cerca del trabajo. Un departamento de
  45–65 m² cuesta ~S/ 1,600–2,400 en Lince o Jesús María y ~S/ 1,350–2,000 en Pueblo Libre o
  San Miguel (estimado con Urbania). El fondo de S/ 40k queda en soles. **Revisa en 2027–2028**
  con los precios del BCRP de 2026, tu ingreso de entonces y la tasa hipotecaria. Si para
  entonces está claro que no comprarás en los próximos 5 años, pasa parte de ese fondo al
  núcleo indexado.
- **El loft de 2022 (Barranco, 33 m², revisado el 2026-11-12 con los datos reales):** la plata
  propia rindió **~25–27% al año**, o ~13% si el primer año no tuvo renta. Las razones fueron
  tres:
  - se compró ~17% bajo la mediana de Barranco (S/ 7,273 frente a S/ 8,712 por m²) y se vendió en
    la mediana. El distrito no subió en soles;
  - un Airbnb y luego una renta amoblada que dejaban ~9.5% del precio al año, más que el 6.4% de
    interés;
  - el bono.
  Para un 2D en el que vives, el veredicto no cambia: a 5 años necesitas ~4.1% de plusvalía anual
  para que tu plata gane 8%. Detalle en
  `research_notes/Vivienda con apalancamiento/loft_2022_2026_y_modelo.md`.
- **Descartado:** el departamento de inversión con hipoteca, porque con alquiler de largo plazo el
  flujo es negativo y necesita 4.5% de plusvalía anual solo para empatar con FIBRA.
  - **Reabierto el 2026-11-12:** un loft de 33 m² en Barranco con renta neta de S/ 1,850 rinde
    ~10% al año si se compra 15% bajo la mediana y la plusvalía es de 2%. Si se paga la mediana
    (S/ 286k) rinde ~4–5%, y en ese caso no conviene.
  - La condición es comprar con descuento: en preventa o una unidad terminada con rebaja.
  - Iría con hipotecario convencional, porque el NCMV exige vivir ahí 3 años.
- **También descartado:** el terreno cerca de
  megaproyectos: el riesgo dominante es el título, y los precios de oferta de Chancay están
  planos en 2026.

## ETF: SPYL en IBKR (decidido el 2026-10-31)

Ingreso bruto ~S/ 130,000 al año, así que la marginal es **14%**. El tramo de 14% llega hasta
~S/ 148,500 brutos, con la deducción de 7 UIT. Con esa marginal, las vías comparadas a 20
años quedan así (modelo con US$ 6,800, 7% anual, todos los costos incluidos y tu ingreso de
S/ 130k; recalculado en `alpaca_peru_y_hapi_vs_ibkr.md`):

| Vía | Patrimonio final frente a SPYL | Riesgos |
|---|---|---|
| **SPYL** (Irlanda) en IBKR, vendido **por tramos** a tu escala | referencia (US$ ~22,460) | ninguno estructural. Venderlo todo en un año cuesta −1.5%, y −5.1% si hubo aportes |
| VOO en Hapi → DTC a una SAB → venta en la BVL al 6.25% | +1.8% a +2.4% (US$ 400–540) | Hapi no publica su tipo de cambio; las cifras del costo DTC se contradicen; la liquidez de VOO en la BVL no está verificada |
| SPY por la misma vía (liquidez documentada, US$ 50–100k diarios) | +1.2% | en ambas vías BVL: estate tax de EE.UU. por encima de US$ 60k (con aportes, hacia el año 11–12) y que SUNAT no se ha pronunciado |

La ventaja de la vía BVL, ~2% en 20 años, cabe dentro de la incertidumbre de sus propios
costos no verificados. Por eso SPYL gana por riesgo y simplicidad. Además, **Hapi no puede
comprar SPYL**: su tarifario del 29-abr-2026 dice "US Listed Securities", así que SPYL exige
IBKR. Otras razones a favor de SPYL:
- No tiene exposición al estate tax de EE.UU.
- No depende de un criterio de SUNAT sobre la vía BVL.
- No requiere transferir títulos para vender.
- Si algún día te vas del Perú y dejas de ser domiciliado, una ganancia de fuente extranjera
  deja de tributar aquí; una venta por la BVL es renta peruana.

**Al vender:** la ganancia se suma a tu sueldo. Con ~S/ 130k brutos te quedan ~S/ 18,500 de
renta neta antes de pasar al tramo de 17%. Vende por tramos en años distintos para no saltar
de tramo.

**Si tu ingreso sube de ~S/ 148,500 de forma sostenida** (marginal de 17% o más), la vía BVL
gana unos 3 puntos a 20 años. En ese caso, **los aportes nuevos** van a SPY para venderlos por
la BVL, y lo ya comprado en SPYL se queda donde está. La decisión se toma aporte por aporte y no
obliga a vender nada.

**Pendiente de una respuesta de Renta 4 (2026-11-07): SPYL también está listado en la BVL.** El
boletín de la BVL lista SPYL y CSPX como valores extranjeros, con Inteligo SAB como agente
promotor. Si una SAB puede comprar SPYL y, años después, venderlo en la rueda, se juntan tres
cosas:
- la salida al 6.25% de la vía BVL;
- la ausencia de estate tax;
- la acumulación.

Estimado: ~+6% de patrimonio a 20 años frente a IBKR, incluso con marginal de 14%. El problema es
la liquidez: SPYL cotizó en el 5% de las sesiones. Regla de decisión:
- **Sí, en la rueda, en ambos sentidos,** con ≤0.7% por lado todo incluido y sin custodia: el
  núcleo va a SPYL en Renta 4 y no se abre IBKR para el núcleo.
- **Solo SPY:** se mantiene SPYL en IBKR. *Revisado el 2026-11-16: con compra directa en la BVL,
  VOO le gana a SPYL en IBKR por ~2–3% a 20 años y evita abrir IBKR. Ver el Historial de ese día.*
- **Sin venta asegurada en la rueda:** se mantiene SPYL en IBKR.

Detalle en `research_notes/Elegir SAB/sab_fibra_y_via_bvl.md`.

## Brokers y costos de mover el dinero (verificado el 2026-10-31)

Detalle en `research_notes/Invertir en bolsa desde Perú/comisiones_fondeo_y_brokers_trading.md`.

- **Depósito inicial:** el costo lo ponen el banco peruano y el tipo de cambio, no el bróker. Lo
  recomendado es cambiar en una fintech (Kambista o Rextie, ~0.4%) y mandar **un solo wire**
  desde Interbank (US$ 42 en el tramo de US$ 3,001–10,000, más US$ 0–30 de corresponsales).
  Cuesta ~1.0–1.5%, unos S/ 240–340 por US$ 6,800. IBKR no cobra por recibir.
- **Retiros:** IBKR da uno gratis al mes; los siguientes cuestan US$ 10. Interbank cobra US$ 25
  por recibir del exterior, así que conviene evitar retiros pequeños.
- **Aportes futuros:** no mandes wires de US$ 300, porque cuestan ~10% cada uno. Acumula en soles
  y manda **uno o dos wires al año de más de US$ 3,000**. La otra opción es SafetyPay en IBKR
  (anunciado el 18-ago-2026), cuyas comisiones no están publicadas. Hapi cobra US$ 1.99 por
  depósito en soles, pero funciona por app.
- **Salida por DTC hacia una SAB**, si algún día usas la vía BVL: IBKR no cobra la transferencia
  y la SAB cobra US$ 15–24 por valor al recibirla. Solo se puede enviar al custodio en EE.UU.
  de la SAB.
- **Seguridad:** IBKR funciona por web, y su "Mobile Authenticator" acepta TOTP de un gestor de
  contraseñas (KeePass, 1Password). Está sujeto a elegibilidad regional, así que hay que
  confirmarlo para Perú. Ningún bróker revisado acepta llaves FIDO2.
- **Trading:** Alpaca y una segunda cuenta cash en IBKR cuestan parecido, S/ 130–365 en el
  primer año. Alpaca reutiliza la infraestructura de Quantac y su API no pasa por el segundo
  factor. IBKR evita un segundo wire y un segundo bróker. Decide si Alpaca acepta Perú.
  Tastytrade podría ser una opción, pero no se confirmó que acepte Perú. Hapi y Tyba no tienen
  API, y XTB y eToro están descartados.
- **Alpaca y Perú:** el formulario de cuenta live acepta Perú como "Country of Tax Residence"
  (comprobado por el dueño el 2026-10-31). La aprobación final depende del KYC, el último paso.
  - **Retiros:** wire internacional US$ 35, más US$ 0–30 de corresponsales y US$ 25 que cobra
    Interbank por recibir: ≈US$ 60–90 por retiro (6.4% sobre US$ 1,000). Conviene un solo
    retiro, al cerrar el experimento.
  - **Salida de títulos:** DTC US$ 5 por valor, ACATS US$ 25.
  - Solo acepta depósitos en USD. La conversión local de 1.5% no incluye Perú.
  - Entrar y salir cuesta ≈US$ 100–150 en total, unos S/ 200–350 más que una segunda cuenta en
    IBKR, que va en el mismo wire del núcleo y tiene un retiro gratis al mes. A cambio reutiliza
    Quantac y su API.
  - Si acepta, el depósito mínimo es US$ 1 y se fondea con un wire en USD aparte. Abrir sin
  apalancamiento por API: `max_margin_multiplier="1"` y `no_shorting=true`.
- **Hapi:** Hapi Securities LLC (FINRA/SIPC, custodia en Apex).
  - Tarifas (29-abr-2026): comisión US$ 0 más US$ 0.10–0.15 de clearing; depósito en soles
    US$ 1.99 sin tipo de cambio publicado; retiro US$ 7.99 a cuenta peruana o US$ 20 por
    wire; ACATS saliente US$ 75.
  - Tiene versión web, pero el segundo factor es biométrico (passkey) y el depósito en soles
    se hace desde la app. Sin TOTP documentado.
  - Solo tendría sentido para la vía VOO→BVL, y esa vía no se elige con marginal de 14%.

## SAB para FIBRA Prime: Renta 4 (decidido el 2026-11-07)

Detalle y fuentes en `research_notes/Elegir SAB/sab_fibra_y_via_bvl.md`: los 20 tarifarios de la
SMV y los boletines de la BVL.

- **Lo que separa a las SAB con S/ 10,000 es el costo de tener los valores**, no la comisión
  por operación. Hay quien cobra S/ 4–35 al mes de mantenimiento o custodia, o un porcentaje de
  cada dividendo. A 5 años eso es 4–21% de la posición:
  - Seminario: S/ 4 al mes si no operas.
  - Grupo Coril: US$ 3 al mes más 3% de cada dividendo.
  - Inteligo: hasta US$ 5 al mes más US$ 1.30 por dividendo.
  - BBVA Bolsa y Credicorp: S/ 15 al mes.
  - Scotia: hasta S/ 35 al mes.
- **Renta 4** es la única cuyo tarifario oficial dice que no cobra custodia, mantenimiento ni
  cobro de dividendos.
  - **Comisión web:** 0.43%, mínimo US$ 15, más IGV y ~0.105% de cargos de BVL, CAVALI y SMV.
    Sobre S/ 10,000: **~US$ 20.7 (0.72%) por lado**.
  - **Retirar:** S/ 20 o US$ 7 por transferencia, así que conviene una vez al año.
  - **Atención:** plataforma web y oficina en San Isidro. Según el contrato (jun-2026), está en
    Calle Las Orquídeas 621, Platinum Plaza, Torre 1, of. 621. La de Av. Víctor Andrés
    Belaúnde 147 venía de un perfil de 2023.
- **Cuenta abierta el 2026-11-09.** El contrato está en `privado/renta4/`, fuera de git, porque
  trae DNI y número de cuenta. La revisión está en `research_notes/Elegir SAB/revision_contrato_renta4.md`.
  Lo que cambia:
  - **Cuenta en dólares:** la única cuenta bancaria registrada es de ahorro en soles en el BCP, y
    el dinero solo sale hacia cuentas tuyas registradas. Hay que registrar una cuenta en dólares
    antes de que FIBRA empiece a pagar.
  - **Tipo de cambio:** Renta 4 vende dólares como contraparte. Hay que comparar su cotización
    con Kambista o Rextie antes de convertir los S/ 10,000, porque un 1% peor cuesta ~S/ 100.
  - **Efectivo:** el que quede ocioso va a Renta 4 Cash, un overnight a nombre de Renta 4 que se
    queda con 10–20% del interés, y que probablemente no tiene FSD para ti. Nunca mandes una orden
    sin los fondos ya en la cuenta: Renta 4 puede compensar deudas y vender tus valores.
  - **SPYL:** el contrato confirma que, si la BVL excluye un valor extranjero inscrito por agente
    promotor, no hay oferta pública de compra.
- **trii** (Kallpa) cuesta parecido y retirar es gratis, pero va primero por app. Además, el
  tarifario formal de Kallpa incluye mantenimiento de S/ 10 al mes y S/ 5 por cobro de dividendo.
  Antes de elegirla habría que descartar por escrito que eso aplique.
- **Ejecución:**
  - Una sola orden límite de ~423 certificados a ~US$ 6.85, válida varios días. FIBPRIME negocia
    US$ 3–35 mil al día y su formador de mercado (Grupo Coril) cotiza con ~4% de spread.
  - Al vender, informa tu costo a la SAB para que la retención de 5% sea sobre la ganancia.
- **El piso de la comisión (validado el 2026-11-09).** El mínimo de Renta 4 se cobra por orden
  ejecutada, no por depósito, y depende de la moneda: S/ 40 en soles y US$ 15 en dólares.
  - **Regla:** cada orden en dólares (FIBRA, SPYL) idealmente de **US$ 3,500 o más
    (~S/ 12,000)**, que es donde empieza la tarifa plena de 0.43% (US$ 15 / 0.43% = US$ 3,488).
    **Nunca de menos de ~US$ 2,000 (~S/ 7,000).** A US$ 1,000 el mínimo cuesta 1.5% y a
    US$ 500, 3%, sin IGV.
  - **Lo que circula, S/ 9,302 y S/ 6,667, está bien calculado pero es para órdenes en soles.** En
    dólares, Renta 4 le gana a trii desde US$ 2,500 (~S/ 8,600), o desde US$ 2,950 si el 0.6% de
    trii incluye IGV.
  - **FIBRA:** la compra (US$ 2,898) queda debajo del piso y paga ~US$ 3 de más. No se sube a
    S/ 12,000, porque el tope es por concentración, no por comisión. Lo que importa es una sola
    orden.
  - **Distribuciones:** las de FIBRA (~US$ 17 al mes) no se reinvierten en órdenes chicas.
  - **Aportes:** si el núcleo pasa a SPYL en Renta 4, se acumulan en soles y se compran en
    órdenes de US$ 2,000–3,500 o más. Con S/ 2,000 al mes eso es cada 4–6 meses. Pasado el piso
    la comisión ya no baja, y esperar solo cuesta rendimiento.
- **Acciones de EE.UU. en Renta 4 (2026-11-12):**
  - **Pestaña "Estados Unidos":** 0.65% con mínimo de US$ 25 (sin IGV; tarifario: 0.05–1.50%,
    mínimo US$ 25). Salir del mínimo exige órdenes de **US$ 3,850 o más**. Con IGV cuesta ~0.77%
    por lado; a US$ 1,000, 2.95%. Se vende en el exterior, así que la ganancia **se suma al
    sueldo: 14% marginal**, no 6.25%. Las pérdidas del exterior no compensan ganancias peruanas.
  - **Pestaña BVL:** la misma acción listada en Lima (p. ej. NVDAUS) paga 0.43% con mínimo de
    US$ 15 (órdenes de US$ 3,500 o más) y **6.25% fijo** al vender por la BVL. Antes de comprar,
    hay que revisar el libro de órdenes.
- **Fondos mutuos en Renta 4 (revisado el 2026-11-12):** Blum USA 500 invierte en CSPX y se
  rescata en ~3 días hábiles sin depender de la rueda. Pero cobra 1.77% al año con IGV en la
  serie B, y a 20 años deja ~29% menos que SPYL. **No se usa para el núcleo.** Los fondos de
  liquidez (Blum Cash Soles serie O, 4.01% a 1 año al 10-nov) sirven solo para efectivo en
  espera. Detalle: `research_notes/Elegir SAB/fondos_mutuos_renta4.md`.
- **Rendimiento revisado:** TTM de US$ 0.52 por certificado: 7.6% bruto y ~7.3% neto a US$ 6.83.
  Más de un tercio es "exceso de caja", y el pago de noviembre (US$ 0.025) es el más bajo del año,
  tras la sexta colocación (US$ 40 millones).

## Ahorro en dólares y Binance Earn (consultado el 2026-10-31)

No forma parte del plan, por dos razones:

1. **El plan no necesita ahorro defensivo en dólares.** Ya hay ~40% en dólares (FIBRA, ETF,
   trading) y los gastos son en soles. Un ahorro en dólares le pondría riesgo cambiario justo a
   la parte que debe ser estable.
2. **Binance Earn no es un depósito.** Es un préstamo sin garantía a un exchange offshore,
   en una stablecoin:
   - No tiene FSD ni SIPC, y el fondo SAFU es discrecional.
   - En una insolvencia, eres acreedor común. Es lo que congeló los productos "Earn" de
     Celsius, BlockFi, Voyager y FTX en 2022.
   - Las stablecoins pueden perder la paridad: USDC llegó a ~US$ 0.88 en marzo de 2023.
   - Las transferencias cripto son irreversibles y no hay reclamo posible ante la SBS o
     INDECOPI.
   - En el Perú los exchanges solo se registran para prevención de lavado de activos; no hay
     supervisión prudencial.

Si en algún momento hay dólares que estacionar, por ejemplo mientras esperan para entrar a
IBKR, las opciones con respaldo son dos:
- Un DPF en dólares cubierto por el FSD (Alfin pagaba 3.65% a 360 días en oct-2026).
- Letras del Tesoro de EE.UU. en IBKR. Para un no residente, el interés de los Treasuries no
  sufre la retención del 30%, aunque falta confirmar en IBKR cómo lo aplica.

Binance Earn, si se usa, va dentro del presupuesto de riesgo (como el trading), no del ahorro.

## Calendario

| Cuándo | Qué |
|---|---|
| **Jue 12 – dom 15-nov-2026** | Feria Nexo Inmobiliario (Costa Verde, Magdalena, 11:00–21:00), para cotizar y no para comprar. Hay 7 proyectos para cotizar y un checklist en el informe "Proyectos de departamentos en Lima Moderna". Solo se separa si una unidad cumple las cinco condiciones, y se decide antes del 17-nov |
| **Mar 17-nov-2026** | Último día de la campaña de Alfin, renovada del 03 al 17-nov con las mismas tasas, o antes si capta S/ 20 MM (verificado el 2026-11-05). Lleva las preguntas del informe 1: TREA en la cartilla, sin renovación automática, sin tarjeta ni usuario digital. Los otros S/ 20k del fondo de vivienda van a Financiera Confianza a 361 días (5.00%, solo en oficinas, campaña hasta el 30-nov) |
| Noviembre 2026 | Renta 4 SAB, abierta el 09-nov:<br>1. Registrar una cuenta en dólares.<br>2. Comparar su tipo de cambio con Kambista.<br>3. ~~Comprar FIBRA Prime en una sola orden~~: hecho el 16-nov, 440 certificados a US$ 6.82 (US$ 3,000.80).<br>4. Mandar por escrito las preguntas sobre SPYL y las del contrato (ver pendientes).<br> Con su respuesta se decide si se abre IBKR para el núcleo. Preguntar a Alpaca si abre cuentas live a residentes en Perú. Configurar Pibank en el celular dedicado |
| Nov–dic 2026 | Cambiar soles a dólares en una fintech, mandar un solo wire a IBKR y comprar SPYL. Si el trading va en IBKR, incluir los ~US$ 1,850 en el mismo wire. 8 semanas de trading en paper con las reglas escritas en git |
| 31-dic-2026 | Vence la exoneración del IR sobre intereses de depósitos (la prórroga, PL 509, no está aprobada) |
| 02-ene-2027 | Si el paper salió bien en disciplina, arranca el trading live con S/ 6,500, sin reponer nunca |
| Dos semanas antes de cada vencimiento de DPF | Alarma: decidir la renovación a mano, nunca en automático |
| 2027–2028 | Revisión de vivienda: comprar con el segundo crédito MiVivienda o seguir alquilando |

## Verificaciones pendientes

- [x] Tasa marginal del dueño: ingreso bruto de ~S/ 130,000 al año (2026-10-31), así que la
      marginal es 14% y el ETF es SPYL. Revisar si pasa de ~S/ 148,500.
- [x] Venta del loft: exenta como casa habitación y tramitada en notaría (confirmado por el
      dueño el 2026-10-31).
- [ ] Consultar en INDECOPI ("Mira a quién le compras") los RUC de Grupo Caral y Grupo T&C,
      sobre todo Sarasota Real Estate Group (Mural, 20611195843) y GC Angamos (Villa Elenia,
      20612083321). La lista está en `research_notes/Barrido de precios por m2/`.
- [x] ~~Barrido automático de Nexo~~: descartado el 19-nov. Sus términos (cláusula 3.2) prohíben la
      extracción automatizada; se retiró la herramienta y se borraron los datos.
- [ ] Pedir por escrito al Fondo MiVivienda:
      - si el crédito de 2022 cuenta para el límite de dos veces;
      - qué tasa e inicial aplican a un segundo crédito sin bono;
      - si haber devuelto el bono íntegro con intereses (~S/ 16,500) te vuelve a habilitar para
        el subsidio. Si la respuesta es sí, el análisis de vivienda cambia de signo;
      - si el préstamo máximo del 90% deja la inicial real en 10% cuando no hay bono.
      Se puede preguntar en su stand de la feria Nexo (12–15 nov).
- [x] La "penalidad" fue la devolución del bono: ~S/ 16,500 descontados en la liquidación
      (confirmado por el dueño el 2026-11-07).
- [x] Tarifario de la SAB: Renta 4 cobra 0.43% web (mínimo US$ 15) y no cobra custodia ni
      mantenimiento. SPY en la rueda costaría ~0.6% por lado (2026-11-07).
- [ ] Preguntar por escrito a Renta 4:
      - si puede comprar **SPYL** (IE000XZSV718) o CSPX en la rueda de la BVL, y venderlos años
        después también en la rueda;
      - cómo ejecuta si no hay oferta y a qué precio frente a Londres;
      - si la custodia de valores extranjeros es sin costo;
      - qué pasa si la BVL excluye el valor;
      - si SPYL comprado en la rueda queda a tu nombre en CAVALI o en su cuenta global;
      - cuánto cuesta transferir a tu cuenta bancaria;
      - si una orden que se ejecuta en partes, en varias operaciones o en varios días, paga el
        mínimo de US$ 15 en cada parte.
      La regla de decisión está en la sección del ETF.
- [x] Abrir la cuenta en Renta 4 (2026-11-09). Contrato revisado; el PDF está en `privado/`.
- [ ] Renta 4, sobre la cuenta (ver `revision_contrato_renta4.md`):
      - registrar una cuenta bancaria en dólares;
      - pedir el código CAVALI (RUT);
      - preguntar si hay doble factor (TOTP) en la web;
      - cargo por operar en la plataforma (acceso ADM, cl. 18.12): respondido el 2026-11-11,
        Renta 4 no cobra nada aparte de la comisión;
      - preguntar en qué bancos tienen cuentas de intermediación y a qué tipo de cambio venden
        dólares.
- [~] Datos reales del loft: recibidos el 2026-11-12. Falta saber si hubo renta durante el año
      de espera de la independización, que define si el loft rindió ~26% o ~13% al año.
- [ ] IBKR: entidad para Perú, TOTP disponible para Perú y comisiones de SafetyPay para
      aportes en soles.
- [~] Alpaca: el formulario acepta Perú (2026-10-31); falta la aprobación del KYC. Revisar el
      estado del nuevo margen intradía, que reemplazó a la regla PDT. Si se confirma, actualizar el CLAUDE.md de Quantac ("Restricción PDT activa").

## Historial

- 2026-10-29: propuesta inicial del dueño.
- 2026-10-31: decisión v1 tras los informes 1–3, la actualización con Bolsillos Llenos y la
  verificación de MiVivienda (`research_notes/Recompra de vivienda tras usar Mivivienda/`).
- 2026-10-31: el dueño confirma ingresos de ~S/ 130k (marginal 14%) y que la venta del loft
  fue exenta. Con 14% la vía BVL empata con SPYL, así que el núcleo va a SPYL; si el ingreso
  pasa de ~S/ 148.5k, los aportes nuevos irán a SPY con salida por la BVL. Se agrega la
  comparación de brokers y de costos de fondeo.
- 2026-11-05: se reverifican los DPF.
  - Alfin renovó su campaña hasta el 17-nov con las mismas tasas.
  - Confianza paga 5.00% desde 361 días.
  - La inflación de Lima a octubre fue 5.25%.
  - La vista de lectura se publica como artefacto.
- 2026-11-07: el dueño confirma que devolvió el bono (~S/ 16,500).
  - Se elige Renta 4 SAB para FIBRA Prime tras revisar los 20 tarifarios de la SMV.
  - Se revisa el rendimiento de FIBRA a ~7.3% neto (TTM).
  - Se encuentra SPYL listado en la BVL, una posible mejora del núcleo que depende de la respuesta
    de Renta 4.
- 2026-11-09: se valida el piso de la comisión mínima de Renta 4 contra su tarifario.
  - En soles es S/ 9,302. En dólares, que es como se compran FIBRA y SPYL, es US$ 3,488.
  - Regla: órdenes de US$ 3,500 o más, y nunca de menos de ~US$ 2,000.
- 2026-11-09: el dueño abre su cuenta en Renta 4 y se revisa el contrato.
  - El PDF queda en `privado/`, fuera de git.
  - Lo que sale de la revisión: falta una cuenta en dólares, hay que comparar el tipo de cambio,
    se corrige la dirección de la oficina y se suman preguntas (TOTP, cargo ADM, código RUT).
- 2026-11-12: informe "Proyectos de departamentos en Lima Moderna", para la feria Nexo del
  12–15 nov.
  - Hay 7 proyectos para cotizar, un semáforo de inmobiliarias (Grupo T&C en rojo) y un
    checklist.
  - El reglamento del NCMV presta como máximo el 90%, así que la inicial real sin bono es 10%. El
    veredicto de alquilar no cambia.
  - Se revisan los fondos mutuos de Renta 4: Blum USA 500 no sirve para el núcleo, por su
    comisión de 1.77% al año.
- 2026-11-12: el BCRP sube su tasa de 4.25% a 4.50%, la primera alza desde ene-2023
  ([Gestión](https://gestion.pe/economia/empresas/bcrp-rompe-pausa-de-14-meses-y-sube-su-tasa-de-referencia-a-que-nivel-noticia/)).
  - **Contexto:** inflación de 5.3% en octubre (4.5% en setiembre) y expectativas a 12 meses de
    3.1%. El BCRP dice que no es necesariamente el inicio de un ciclo de alzas. Próxima reunión:
    10-dic ([Forbes Perú](https://forbes.pe/economia-y-finanzas/2026-11-12/el-bcrp-sube-la-tasa-de-referencia-a-45-ante-el-repunte-de-la-inflacion)).
  - **Efecto en el plan:** ninguna decisión cambia.
    - DPF: se abren igual antes del 17-nov y a 360 días.
    - FIBRA Prime: está en dólares y sin deuda en soles, así que el alza casi no la toca.
    - Hipotecas: se fijan con los bonos soberanos y no necesariamente suben (Hugo Perea, BBVA
      Research, en
      [El Comercio](https://elcomercio.pe/economia/bcr-sube-su-tasa-de-interes-a-450-por-primera-vez-desde-2023-que-efectos-tendra-noticia/)).
- 2026-11-12: se revisa el caso del loft de 2022 con un modelo de apalancamiento. Se reabre el
  departamento de inversión en Airbnb, pendiente de los datos reales.
- 2026-11-19: el dueño quiere invertir ya en un inmueble para alquilar y revender. Cotizó Mural
  (T&C, Lince, con desembolso postergado) y Villa Elenia (Caral, Surquillo). Nota en
  `research_notes/Barrido de precios por m2/mural_y_barrido_2026-11-19.md`.
  - **Mural 1511** (40.95 m², S/ 258k ofrecido): para no perder hay que cerrar la venta en ~S/
    286.5k (S/ 7,000 por m²) con corredor. La mediana de Lince es 6,415 de lista.
  - **El 1D de ~43–45 m²** (modelo 15 o el 2312), por casi la misma plata, baja ese equilibrio a
    6,500–6,700 por m².
  - **Villa Elenia** exige ~S/ 70k propios por las cuotas antes de la entrega: peor para revender.
  - **Riesgos:** T&C sigue en rojo para comprar en planos. Mural no tiene banco promotor y Nexo dice
    "En excavación" con entrega en oct-2027.
  - **Barrido:** Nexo lo cortó tras 37 fichas, y sus términos (3.2) prohíben la extracción
    automatizada. Se descartó y se retiró la herramienta.
    Urbania no permite el acceso automático.
  - **Tras la visita:** BBVA desembolsa con el departamento terminado; la inicial va a un
    fideicomiso; van 11 de 23 pisos; la independización toma 12–18 meses; no se puede ceder el
    contrato.
    - Sin amoblar, la plata propia baja de ~S/ 49k a ~S/ 41k y el equilibrio, a ~S/ 278k.
    - Falta en la minuta: la penalidad si el crédito no sale, la fecha de entrega, la penalidad
      por retraso y la resolución con devolución.
  - **Condiciones del dueño** (sin corredor, sin muebles, venta a S/ 300k en feb-2029): el 1511
    deja ~S/ 31k netos sobre ~S/ 39k propios, ~36% anual. El equilibrio es ~S/ 267k.
  - **Eucalipto** (Abril, JM, entrega dic-2028) solo funciona con desembolso postergado: ~20–31%
    anual vendiendo en 2030 a S/ 7,300 por m². Con desembolso inmediato, −5% a +4%.
- 2026-11-16: el dueño compra FIBRA Prime en Renta 4: 440 certificados a US$ 6.82 (US$ 3,000.80),
  en una sola orden. Pasa a elegir el ETF del S&P 500 en la BVL.
  - **Libro de órdenes del 16-nov.** En la tabla, "Prec. Comp." es lo que ofrecen otros
    compradores, no el precio al que uno compra. Se leyó al revés y se corrigió el mismo día.
    - **VOO:** compran a 678.29 (500) y venden a 681.06 (495): diferencia de 0.4%. Hubo 15
      operaciones por US$ 10,246.
    - **CSPX:** hay compradores a 811 (12) y entre 810 y 795, pero **nadie vende**. Hoy no se puede
      comprar.
    - **SPYL:** sin posturas. SPY no salió en la búsqueda.
  - **Recomendación revisada el mismo día:** VOO en Renta 4, en dos órdenes límite de 5 (~US$
    3,405 cada una). La primera se hace con lo que ya está en Renta 4 y la segunda cuando llegue
    el resto del núcleo. Dos órdenes de 5 cuestan ~US$ 30 y una de 10, ~US$ 29.
    - **Rompe la regla de arriba** ("Solo SPY: se mantiene SPYL en IBKR"). Esa regla es del
      31-oct, cuando la vía BVL pasaba por Hapi y DTC con costos sin verificar. Ahora la compra
      es directa, con el tarifario conocido. El libro muestra a alguien cotizando ~500 VOO a cada
      lado con 0.4% de diferencia. La plata ya está en Renta 4 y IBKR no está abierto.
    - **Patrimonio neto tras vender,** con US$ 6,900, todos los costos y la marginal de 14% (por
      tramos en IBKR), a 7% y a 9% anual. Frente a SPYL en IBKR:

      | Vía | 10 años | 20 años |
      |---|---|---|
      | VOO en la BVL | +2.3% / +3.0% | **+2.1% / +2.7%** (~US$ 480–890) |
      | SPY en la BVL | +1.9% / +2.6% | +1.1% / +1.7% |
      | CSPX en la BVL (hoy sin vendedores) | +3.8% / +4.4% | +5.3% / +5.9% |
      | VOO, si SUNAT cobrara 14% y no 6.25% | −1.0% / −1.2% | −3.1% / −3.4% |

      Modelo en el scratchpad (`tools/nucleo_vias.py`). Si en IBKR se vende todo en un año, la
      ventaja de la BVL sube ~1.5 puntos.
    - **Corrección:** a los dividendos de VOO se les suma el residual peruano de la tasa media.
      Con S/ 130k brutos, 14% − 8.6% = 5.4%, así que el total es ~35% y no 30%. Frente a CSPX, VOO
      pierde ~0.2 puntos al año (~3% a 20 años), no 0.13. Los dividendos se declaran cada año en
      el Formulario 709: ~US$ 78 brutos al año con 10 VOO, unos US$ 4 de impuesto peruano.
    - **Riesgos y salvaguardas:**
      - **Estate tax:** cuando los activos de EE.UU. (VOO, acciones sueltas, Alpaca) se acerquen a
        US$ 50k, los aportes nuevos van a CSPX o SPYL.
      - **Exclusión:** el agente promotor de VOO es la propia BVL. Si lo excluye, se transfiere
        por DTC (US$ 25) y se vende fuera al 14%, como en IBKR.
      - **SUNAT:** CAVALI ya retiene 5% y la cartilla 2025 aplica el 6.25%.
    - **CSPX:** cuando aparezca un vendedor a ≤ 1.186 × VOO, los aportes nuevos van ahí.
  - **No vale la vía de Bolsillos Llenos** (comprar en Hapi o IBKR y traer los valores a Renta 4
    por DTC) para una orden de este tamaño.
    - Ahorra ~0.6–0.8% de comisión y spread, ~US$ 25.
    - Pero Renta 4 cobra US$ 25 por recibir los valores (tarifario).
    - Hay que sumar la comisión de salida del otro bróker y su tipo de cambio.
    - Sigue sin verificarse que la transferencia funcione.
    - Se revisa solo si los aportes futuros son chicos y frecuentes.
- 2026-11-12: se anotan los costos y el impuesto de las acciones de EE.UU. en Renta 4.
  - NVIDIA cayó ~34% desde su máximo del 5-oct, tras la renuncia de Jensen Huang el 12-nov
    ([Fortune](https://fortune.com/2026/11/12/jensen-huang-downfall-is-nvidia-a-buy-or-sell/)).
  - No cambia el plan: compras sueltas solo dentro del experimento de trading.
