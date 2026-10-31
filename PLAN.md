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
| Inmuebles sin deuda | S/ 10,000 | FIBRA Prime (BVL), por una SAB local | Exposición inmobiliaria sin hipoteca: ~7.6–8.3% neto en US$ (oct-2026). No más, porque es un solo emisor y está en dólares |
| Núcleo indexado | S/ 23,500 | **VOO** en Interactive Brokers, operado por web. Al vender, se transfiere a una SAB peruana y se vende por la BVL al 6.25% fijo (ver abajo) | Informe 3 y su actualización. Con Quantac, el índice fue la vara que nada superó |
| Experimento de trading | S/ 6,500 | Cuenta live separada en Alpaca, solo después de 8 semanas en paper, con las reglas del informe 3 | Da la misma información que S/ 10,000 y pierde menos. Pérdida máxima ≈ S/ 2,250 con el kill switch al −30% |
| **Total** | **S/ 100,000** | | |

Por moneda: ~S/ 60k en soles (reserva y fondo de vivienda) y ~S/ 40k en dólares (FIBRA, ETF y
trading). Tu sueldo y tu vivienda futura están en soles, así que la renta variable va en dólares
sin cubrir y la parte defensiva queda en soles.

## Por qué no se compra vivienda ahora

- **Puedes volver a usar el crédito MiVivienda, pero no el bono.** El Fondo financia como
  máximo dos veces a una persona, y "solo el primer crédito… podrá contar con el subsidio"
  (fichas del Fondo en gob.pe, vistas el 31-oct-2026). Tu intuición de que "como ya no tengo
  nada, vuelvo a calificar" vale para el crédito, no para el subsidio. La "penalidad" que
  pagaste al vender fue, muy probablemente, la devolución del Bono del Buen Pagador más
  intereses, porque cancelaste antes de los 5 años. Una comisión por prepago está prohibida.
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

## ETF: VOO con salida por la BVL (decidido el 2026-10-31)

El dueño confirmó que sus ingresos superan ~S/ 66,000 al año, así que su tasa marginal es 14% o
más. Con esa tasa, VOO vendido por la BVL tributa 6.25% fijo, en vez de su escala de 14–30%, y
le gana al UCITS a pesar de la retención de 30% sobre los dividendos.

Antes de comprar falta verificar la liquidez de VOO en la BVL, que no está confirmada. SPY sí
tiene liquidez documentada (US$ 50–100k diarios). Si VOO no tiene liquidez, se usa SPY, que
replica el mismo índice con un TER de 0.0945% frente a 0.03%.

| Si tu marginal es… (ingreso bruto anual aprox.) | ETF | Vía de salida |
|---|---|---|
| 8% (menos de ~S/ 66,000 al año) | **SPYL** o **VWRA** (Irlanda, acumulación) | Venta en IBKR, que tributa a tu escala, baja en este caso |
| 14% o más (más de ~S/ 66,000 al año) | **VOO** (EE.UU.) | Al vender: transferir a una SAB peruana y vender por la BVL al 6.25% fijo. A 20 años deja entre 1.5% y 16% más de patrimonio que el UCITS |

La vía VOO-BVL tiene tres condiciones:
1. **Verificar que IBKR transfiere por DTC a una SAB peruana.** El caso documentado por
   Bolsillos Llenos usó Hapi.
2. **Vigilar el estate tax de EE.UU.** Aplica a partir de US$ 60k en activos estadounidenses;
   hoy estás muy lejos, pero hay que revisarlo cada año.
3. **Aceptar el riesgo regulatorio.** SUNAT no se ha pronunciado sobre esta vía.

Si alguna de las tres falla, se usa VWRA.

## Ahorro en dólares y Binance Earn (consultado el 2026-10-31)

No forma parte del plan, por dos razones:

1. **El plan no necesita ahorro defensivo en dólares.** Ya hay ~40% en dólares (FIBRA, VOO,
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
| **Lun 02-nov-2026** | Último día de la campaña de Alfin (o antes, si capta S/ 20 MM). Si vas, lleva las preguntas del informe 1: TREA en la cartilla, sin renovación automática, sin tarjeta ni usuario digital |
| Noviembre 2026 | Abrir IBKR y confirmar la entidad (IB LLC) y el 2FA sin app. Ticket a Alpaca: ¿cuentas live para Perú? Abrir una SAB para FIBRA Prime y, si aplica, para la vía BVL. Configurar Pibank en el celular dedicado |
| Nov–dic 2026 | Comprar el ETF del núcleo. 8 semanas de trading en paper con las reglas escritas en git |
| 31-dic-2026 | Vence la exoneración del IR sobre intereses de depósitos (la prórroga, PL 509, no está aprobada) |
| 02-ene-2027 | Si el paper salió bien en disciplina, arranca el trading live con S/ 6,500, sin reponer nunca |
| Dos semanas antes de cada vencimiento de DPF | Alarma: decidir la renovación a mano, nunca en automático |
| 2027–2028 | Revisión de vivienda: comprar con el segundo crédito MiVivienda o seguir alquilando |

## Verificaciones pendientes

- [x] Tasa marginal del dueño: ingresos por encima de ~S/ 66,000 al año (confirmado el
      2026-10-31), así que la marginal es 14% o más y el ETF es VOO.
- [x] Venta del loft: exenta como casa habitación y tramitada en notaría (confirmado por el
      dueño el 2026-10-31).
- [ ] Liquidez de VOO en la BVL: preguntarla a la SAB. Si es baja, usar SPY.
- [ ] Pedir por escrito al Fondo MiVivienda: si el crédito de 2022 cuenta para el límite de dos
      veces y qué tasa e inicial aplican a un segundo crédito sin bono.
- [ ] Pedir al banco la liquidación de la cancelación de 2022–2026 para confirmar que la
      "penalidad" fue la devolución del bono.
- [ ] IBKR: entidad para Perú, 2FA sin app y transferencia por DTC a una SAB.
- [ ] Alpaca: cuentas live para Perú y estado del nuevo margen intradía, que reemplazó a la
      regla PDT. Si se confirma, actualizar el CLAUDE.md de Quantac ("Restricción PDT activa").

## Historial

- 2026-10-29: propuesta inicial del dueño.
- 2026-10-31: decisión v1 tras los informes 1–3, la actualización con Bolsillos Llenos y la
  verificación de MiVivienda (`research_notes/Recompra de vivienda tras usar Mivivienda/`).
- 2026-10-31: el dueño confirma una marginal ≥14%, así que el ETF del núcleo es VOO con
  salida por la BVL. La venta del loft fue exenta.
