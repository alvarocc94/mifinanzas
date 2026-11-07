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
- **Lo que sí vale:** el segundo crédito MiVivienda te da inicial de 7.5% y plazo de 25 años.
  Con S/ 50k alcanza hasta ~S/ 460k, pero con un apalancamiento de ~12x. Es una opción para
  más adelante, no un motivo para comprar ya.
- **Plan de vivienda:** cuando te mudes, alquila cerca del trabajo. Un departamento de
  45–65 m² cuesta ~S/ 1,600–2,400 en Lince o Jesús María y ~S/ 1,350–2,000 en Pueblo Libre o
  San Miguel (estimado con Urbania). El fondo de S/ 40k queda en soles. **Revisa en 2027–2028**
  con los precios del BCRP de 2026, tu ingreso de entonces y la tasa hipotecaria. Si para
  entonces está claro que no comprarás en los próximos 5 años, pasa parte de ese fondo al
  núcleo indexado.
- **Descartado:** el departamento de inversión con hipoteca, porque el flujo es negativo y
  necesita 4.5% de plusvalía anual solo para empatar con FIBRA. También el terreno cerca de
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
- **Solo SPY:** se mantiene SPYL en IBKR.
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
  - **Atención:** plataforma web y oficina en San Isidro (Av. Víctor Andrés Belaúnde 147).
- **trii** (Kallpa) cuesta parecido y retirar es gratis, pero va primero por app. Además, el
  tarifario formal de Kallpa incluye mantenimiento de S/ 10 al mes y S/ 5 por cobro de dividendo.
  Antes de elegirla habría que descartar por escrito que eso aplique.
- **Ejecución:**
  - Una sola orden límite de ~423 certificados a ~US$ 6.85, válida varios días. FIBPRIME negocia
    US$ 3–35 mil al día y su formador de mercado (Grupo Coril) cotiza con ~4% de spread.
  - Al vender, informa tu costo a la SAB para que la retención de 5% sea sobre la ganancia.
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
| **Mar 17-nov-2026** | Último día de la campaña de Alfin, renovada del 03 al 17-nov con las mismas tasas, o antes si capta S/ 20 MM (verificado el 2026-11-05). Lleva las preguntas del informe 1: TREA en la cartilla, sin renovación automática, sin tarjeta ni usuario digital. Los otros S/ 20k del fondo de vivienda van a Financiera Confianza a 361 días (5.00%, solo en oficinas, campaña hasta el 30-nov) |
| Noviembre 2026 | Abrir Renta 4 SAB y comprar FIBRA Prime; antes, hacerle por escrito las preguntas sobre SPYL en la BVL (ver pendientes). Con su respuesta se decide si se abre IBKR para el núcleo. Preguntar a Alpaca si abre cuentas live a residentes en Perú. Configurar Pibank en el celular dedicado |
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
- [ ] Pedir por escrito al Fondo MiVivienda:
      - si el crédito de 2022 cuenta para el límite de dos veces;
      - qué tasa e inicial aplican a un segundo crédito sin bono;
      - si haber devuelto el bono íntegro con intereses (~S/ 16,500) te vuelve a habilitar para
        el subsidio. Si la respuesta es sí, el análisis de vivienda cambia de signo.
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
      - cuánto cuesta transferir a Interbank.
      La regla de decisión está en la sección del ETF.
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
