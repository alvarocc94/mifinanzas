# Alpaca para residentes en Perú, Hapi frente a IBKR y comparativas de brókers en YouTube (corte: 31-oct-2026, vigente para noviembre de 2026)

> Notas para `PLAN.md`: núcleo de ~US$ 6,800 en un ETF del S&P 500 con 1–2 aportes al año, y una cuenta de trading de ~US$ 1,850 (acciones y ETFs de EE.UU., cash, sin apalancamiento). El dueño es domiciliado en Perú, con ~S/ 130,000 brutos al año y marginal de 14%. Ahora acepta un bróker solo-app como Hapi, porque no lo instalaría en su celular de uso diario.
>
> Parten de [`comisiones_fondeo_y_brokers_trading.md`](comisiones_fondeo_y_brokers_trading.md), [`youtube_bolsillos_llenos.md`](youtube_bolsillos_llenos.md), [`brokers_vias_acceso.md`](brokers_vias_acceso.md) e [`impuestos_y_etfs.md`](impuestos_y_etfs.md). No repiten lo que ya está ahí salvo lo necesario para comparar.
>
> **Supuestos de cálculo, propios, no son cotizaciones:**
> - Tipo de cambio S/ 3.40 por US$, constante.
> - Retorno bruto del S&P 500 de 7% nominal en US$ y rendimiento por dividendo de 1.07% (VOO, TTM, ver `impuestos_y_etfs.md`).
> - UIT de S/ 5,500 constante.
> - Script: `C:\Users\Alvar\AppData\Local\Temp\claude\D--PROYECTOS-QUANTAC\edfccc14-4595-4f32-ae31-011384142197\scratchpad\calc\paquetes.py` (temporal). Con el perfil de S/ 84,000 reproduce el +1.5% de `PLAN.md`.
>
> **Videos nuevos en `raw/youtube/`** (`<id>.txt`, `<id>.description`, `<id>.es.vtt`): SEwvYdLJqbk, phB9YGq0erI, Oth8KlmEX14, Rfnyja_upaA, qYgp_jDhghs, KeLvBY2R3Is, XFwW_oP8MlE, hakbpzyn9Ow, FCWyNitbzfY, TQFX5tHC6h4, Y6fhdMWKD4o y 8VnWJNAvgmI. Son subtítulos autogenerados, tratados como afirmaciones no confiables; las vistas son las del 31-oct-2026.
>
> **Acceso a fuentes:** las páginas de precios de IBKR siguen devolviendo HTTP 403. Algunas páginas de Alpaca ocultan el correo de soporte en la versión leída. El tarifario PDF de Hapi se leyó completo convirtiéndolo a texto con pypdf.

---

## 1. ¿Acepta Alpaca Securities a residentes peruanos en cuentas *live* individuales en 2026?

### Takeaway
No hay confirmación pública ni a favor ni en contra. Alpaca no publica una lista de países:
- Su página de países, de feb-2026, remite a soporte.
- Su guía para no residentes, del 11-mar-2026, dice "195+ countries", excluye a Canadá y advierte que "does not support every jurisdiction".

Ningún hilo del foro ni ningún video encontrado menciona a Perú.

Hay dos datos duros que sí afectan el plan:
1. La conversión en moneda local (CurrencyCloud) no incluye Perú, así que el fondeo sería por **wire en USD**.
2. La cuenta se abre como *margin*, pero se puede fijar `max_margin_multiplier = "1"` y `no_shorting = true`, que en la práctica la deja sin apalancamiento.

La prueba definitiva cuesta 10 minutos: iniciar la solicitud *live* desde el dashboard que ya tiene y ver si Perú aparece como país de residencia fiscal (pasos en "Recomendación").

### Cited Findings
**Elegibilidad**
- La página "Countries Alpaca is available" (fechada en febrero de 2026) no tiene lista de países y dice: "Please contact support… for more information regarding whether your country is supported". El correo aparece ofuscado en la versión leída. — [Alpaca Support, Countries](https://alpaca.markets/support/countries-alpaca-is-available)
- Guía para no residentes ("last updated on March 11th, 2026"):
  - Dice "We support the services to 195+ countries" y "Canadian residents are not currently supported".
  - Agrega que "Alpaca does not support every jurisdiction" y que la elegibilidad depende del país de residencia.
  - No menciona a Perú ni a Latinoamérica.
  - Fuente: [Alpaca Learn, Live Trading Account as a Non-US Resident](https://alpaca.markets/learn/live-trading-account-non-us/)
- Página de soporte de oct-2025: "We've lifted our $30,000 minimum deposit… allowing all non-US users to fund their accounts with as little as $1" y "KYC documents vary by country, but generally you require a Tax-ID, and document containing your photo and your address". — [Alpaca Support, Is Alpaca available outside the US](https://alpaca.markets/support/is-alpaca-available-outside-the-us)
- **Foro** (extracto del buscador; los hilos no se leyeron completos):
  - Un moderador explica que el país se determina por la dirección física declarada en la solicitud.
  - En otro hilo, un moderador dice que Alpaca no admite cuentas *live* con jurisdicción en Indonesia. Es decir, sí hay países excluidos aunque no se publiquen.
  - Fuentes: [Foro, Country of Tax Residence Indonesia](https://forum.alpaca.markets/t/country-of-tax-residence-indonesia/11836); [Foro, My country is not on the list](https://forum.alpaca.markets/t/my-country-is-not-on-the-list/7362)
- Un hilo del 10-jul-2026 reporta el error "permission denied to update country_of_tax_residence or not recognized" de un usuario que afirma que su país "is allowed". No nombra el país y no tiene respuesta del personal de Alpaca. — [Foro Alpaca](https://forum.alpaca.markets/t/error-submitting-additional-info-permission-denied-to-update-country-of-tax-residence-or-not-recognized/19249)
- **Antecedente histórico:** Alpaca tuvo una beta "invite-only" para no residentes que exigía un acuerdo de no solicitación. La guía de 2026 ya no menciona invitaciones. — [Alpaca blog, Non-US live trading beta](https://alpaca.markets/blog/non-us-live-trading-beta/)

**Requisitos y pasos para no residentes** (guía del 11-mar-2026, [Alpaca Learn](https://alpaca.markets/learn/live-trading-account-non-us/))
- Documento de identidad oficial, por ejemplo pasaporte.
- Comprobante de domicilio (recibo de servicio o estado bancario), "if requested".
- Tax ID del país de residencia fiscal. En algunos países sirve el número de pasaporte o de residencia.
- Selfie en vivo para KYC.
- **W-8BEN**, que se genera y se revisa dentro del onboarding.
- Flujo de la solicitud:
  1. Entrar a la web app y activar MFA.
  2. Elegir Individual.
  3. Responder "Are you a U.S. tax resident?" → No.
  4. Elegir el país de residencia fiscal.
  5. Llenar los datos básicos.
  6. Llenar el perfil laboral y financiero.
  7. Aceptar los *disclosures*.
  8. Revisar y aceptar el W-8BEN.
  9. Tomarse la selfie.
  10. Esperar la aprobación.
  11. Fondear con "Deposit Funds".

**Fondeo y retiro para clientes internacionales**
- Guía de fondeo ("last updated on January 26, 2026"):
  - Los wires internacionales deben venir en USD: "Alpaca does not accept wires in other currencies".
  - La transferencia en moneda local vía CurrencyCloud cobra 1.5% con tope de US$ 40.
  - Los depósitos cripto (BTC, ETH, tokens ERC-20) solo están disponibles en regiones soportadas y con el acuerdo cripto firmado.
  - Wire saliente: US$ 25 doméstico y US$ 50 internacional.
  - Fuente: [Alpaca Learn, How to fund](https://alpaca.markets/learn/fund-live-trading-account/)
  - El fee schedule del 12-oct-2026 dice US$ 35 para el wire internacional. Se toma como vigente (ver `comisiones_fondeo_y_brokers_trading.md`). — [Alpaca Fee Schedule (PDF)](https://files.alpaca.markets/disclosures/library/BrokFeeSched.pdf)
- La transferencia en moneda local solo funciona en 29 regiones: 26 países de la UE/EEE, Reino Unido, Canadá y el Vaticano. **Perú no figura.** La página está fechada en abril de 2025. — [Alpaca Support, Local Currency Transfer](https://alpaca.markets/support/currencycloud-transfer-questions)
- No se encontró ninguna fuente de 2026 sobre depósitos vía Rapyd para Latinoamérica. Un hilo antiguo reporta fallas de Rapyd en Países Bajos e Italia. — [Foro, Rapyd doesn't work for me](https://forum.alpaca.markets/t/rapyd-doesnt-work-for-me/7154)

**Tipo de cuenta y apalancamiento**
- "All accounts are opened as margin accounts". — [Alpaca Docs, Account Plans](https://docs.alpaca.markets/docs/account-plans)
- La configuración de la cuenta admite `max_margin_multiplier` = "1", "2" o "4", y `no_shorting` ("If true, account becomes long-only mode"). — [Alpaca API, Account Configurations](https://docs.alpaca.markets/reference/patchaccountconfig-1)
- La regla PDT fue reemplazada por estándares de margen intradía desde el 4-jun-2026, y Alpaca los aplicó. — [FINRA RN 26-10](https://www.finra.org/rules-guidance/notices/26-10/); [Alpaca blog](https://alpaca.markets/blog/finra-retires-the-pdt-rule-introducing-alpacas-new-intraday-margin-framework/) (ver `comisiones_fondeo_y_brokers_trading.md`)

**YouTube**
- La búsqueda "alpaca broker peru" (yt-dlp, 31-oct-2026) no devuelve ningún video de un creador peruano sobre cuentas *live* de Alpaca. Solo aparecen una comparación genérica de BrokerChooser Español (`wsVWKLZ65uk`), un tutorial de bot en Python (`a-_e_7CRhwI`) y videos sin relación. — búsqueda propia, sin URL fija

### Inferences
- **Fondeo de una cuenta de trading en Alpaca:** como Perú no está en la lista de moneda local, sería un wire en USD aparte del de IBKR (Interbank cobra US$ 30 hasta US$ 3,000, más corresponsales). El retiro cuesta US$ 35 más US$ 25 por la recepción en Interbank. Se confirma la tabla de `comisiones_fondeo_y_brokers_trading.md`: el primer año sale ≈S/ 130–230 y el cierre suma ≈S/ 230.
- **Tax ID peruano:** probablemente sea el DNI o el RUC, que para una persona natural es "10" + DNI + dígito verificador. Si el formulario no acepta ninguno de los dos en el campo de Tax ID, es señal de que el país no está habilitado o de que el tipo de documento no está soportado. Es inferencia; no hay fuente para Perú.
- **Cuenta sin apalancamiento:** `max_margin_multiplier = "1"` y `no_shorting = true` eliminan el apalancamiento y los cortos, que es el equivalente funcional a una cuenta cash para Quantac. No se verificó si la configuración está disponible para no residentes ni cómo interactúa con el nuevo margen intradía; hay que preguntarlo.
- **Iniciar la solicitud es la prueba más barata.** No obliga a fondear. El único costo es entregar documentos y una selfie a Alpaca, que de todos modos haría falta para operar.

### Gaps
- Estado de Perú para cuentas *live* individuales. No existe fuente pública: solo lo resuelve el formulario o una respuesta escrita de soporte.
- Si Alpaca tiene un método de fondeo local para Perú (Rapyd u otro) y si cobra por recibir wires internacionales. Ninguna página lo dice.
- Si el multiplicador 1 está permitido para no residentes y si hay un "Non-Leverage Margin" equivalente a cash. La FAQ citada en las notas previas no se leyó.

---

## 2. Hapi frente a Interactive Brokers para este usuario, y los dos paquetes completos para el núcleo

### Takeaway
**Hapi no puede comprar SPYL, CSPX ni VWRA.** Solo ofrece "stocks and ETFs listed on US stock exchanges", así que el paquete A (SPYL) es imposible en Hapi.

**Hapi sí tiene versión web**, pero está pensada alrededor de la app:
- El depósito en soles se describe con pasos "in the Hapi app".
- La seguridad se basa en la biometría del dispositivo (passkey con FaceID o huella).
- No se documenta TOTP.

Tarifario de Hapi (29-abr-2026):
- Comisión US$ 0, más un *clearing fee* de US$ 0.10 por operación con acciones enteras y US$ 0.15 con fracciones.
- US$ 2.99 por operación en horario extendido.
- Retiro por wire: US$ 20.
- Inactividad: US$ 4.99 al mes, solo con saldo menor a US$ 100 y 60 días sin entrar.
- ACATS saliente: US$ 75, cobrado por Apex.
- **La salida por DTC hacia una SAB no aparece en el tarifario oficial.** Los creadores dan US$ 25 por valor (mar-2026) o US$ 5 (ene-2025).

Comparación de los paquetes con los ingresos reales del dueño (marginal 14%, tasa media 8.6%) y con todos los costos:
- **B (Hapi + VOO → DTC → BVL al 6.25%)** termina **+1.8% a +2.4%** por encima de **A (IBKR + SPYL vendido por tramos al 14%)** a 20 años. Son ≈US$ 400–540 sobre el depósito único, unos 0.1 pp/año.
- Con SPY en lugar de VOO, la ventaja baja a **+1.2%**.
- El primer año, B cuesta S/ 200–340 y A S/ 290–395.

La ventaja de B depende de cuatro datos no verificados (tarifa DTC de Hapi, comisión de venta de la SAB, liquidez de VOO en la BVL y criterio de SUNAT) y trae exposición al *estate tax* si los aportes llevan el saldo por encima de US$ 60k.

### Cited Findings
**Hapi: qué se puede comprar**
- "Available investments in Hapi" (1-oct-2024): "over 12,000 securities", "most stocks and Exchange Traded Funds (ETFs) listed on US stock exchanges", 17 criptomonedas, sin *penny stocks* ni OTC. No menciona bolsas europeas ni UCITS. — [Hapi Help Center](https://help.hapi.trade/en/articles/8977445-available-investments-in-hapi)
- El tarifario oficial titula la sección de acciones "US Listed Securities (including ETFs)", y la comisión cero aplica a "U.S. listed securities (including ETFs) via the app or website". — [Hapi Fee Schedule (PDF, creado el 29-abr-2026)](https://hapi-public-documents.s3.us-east-1.amazonaws.com/hapi-fees-schedule.pdf)
- Una creadora peruana lo confirma en la práctica: "yo no puedo invertir en bolsa europea con Happy porque no tiene". Por eso compra UCITS en XTB. — [Karicats, Rfnyja_upaA, 22-ago-2025](https://www.youtube.com/watch?v=Rfnyja_upaA); [Karicats, Oth8KlmEX14, 17-abr-2026](https://www.youtube.com/watch?v=Oth8KlmEX14)

**Hapi: web, seguridad y regulación**
- **Versión web:**
  - La página oficial de tutoriales dice que se puede acceder desde iOS, Android "y también en la versión web" (extracto del buscador). — [Hapi, Tutoriales](https://hapi.trade/en/learning/hapi-learning-tutoriales)
  - El tarifario habla de operar "via the app or website". — [Hapi Fee Schedule](https://hapi-public-documents.s3.us-east-1.amazonaws.com/hapi-fees-schedule.pdf)
  - "How safe is my money in Hapi?" (10-jul-2026) limita a "one mobile app and one web session at a time". — [Hapi Help Center](https://help.hapi.trade/en/articles/8981762-how-safe-is-my-money-in-hapi)
  - Según un creador, la web replica la app. — [Ingenio Inversiones, KeLvBY2R3Is, 26-ene-2025](https://www.youtube.com/watch?v=KeLvBY2R3Is)
- **El depósito en soles se explica solo en la app:** "Follow these steps in the Hapi app". La comisión "is always shown in the app or on the web before you confirm your deposit". — [Hapi, Cross Payments](https://help.hapi.trade/en/articles/12631400-what-is-cross-payments-and-how-to-use-it-to-deposit-into-hapi)
- **Segundo factor:**
  - El artículo de passkey (14-mar-2025) solo habla de biometría ("FaceID or fingerprint"). No menciona llaves FIDO2, TOTP ni SMS. — [Hapi, Passkey](https://help.hapi.trade/en/articles/9554995-passkey-upgrade-your-account-security)
  - "How safe…" recomienda "Enable biometric authentication on your device" y no menciona 2FA. — [Hapi Help Center](https://help.hapi.trade/en/articles/8981762-how-safe-is-my-money-in-hapi)
  - Una nota de prensa dice que Hapi implementó "autenticación de dos factores", sin detalle (secundaria). — [Infomercado](https://infomercado.pe/hapi-el-broker-con-mas-de-400-mil-clientes-que-revoluciona-la-inversion-desde-latinoamerica/)
  - Los retiros cripto exigen biometría (ver `comisiones_fondeo_y_brokers_trading.md`).
- **Regulación y custodia:**
  - Hapi Securities LLC es "a registered broker-dealer", "Member FINRA/SIPC (CRD #311868)".
  - Apex Clearing Corporation hace "Custody and clearing of your securities account".
  - SIPC cubre hasta US$ 500,000, con hasta US$ 250,000 en efectivo. Apex da "additional protection that supplements SIPC coverage", sin monto publicado.
  - Fuentes: [Hapi, How safe is my money (10-jul-2026)](https://help.hapi.trade/en/articles/8981762-how-safe-is-my-money-in-hapi); [Hapi y Apex (14-nov-2024)](https://help.hapi.trade/en/articles/10136248-what-is-the-relationship-between-hapi-and-apex)

**Hapi: tarifas vigentes** (tarifario PDF creado el 29-abr-2026, salvo indicación) — [Hapi Fee Schedule](https://hapi-public-documents.s3.us-east-1.amazonaws.com/hapi-fees-schedule.pdf)

| Concepto | Monto |
|---|---|
| Comisión (cuenta cash, acciones y ETFs de EE.UU.) | US$ 0 |
| *Clearing house fee*, horario regular | US$ 0.10 por operación con acciones enteras; US$ 0.15 con fracciones (Prime: US$ 0.05) |
| Horario extendido y nocturno | US$ 2.99 por operación (Prime: US$ 0.05) |
| Tasas regulatorias en ventas | 0.0000206 × valor; la de FINRA con tope de US$ 9.79. El PDF parece intercambiar las etiquetas SEC y FINRA |
| Depósitos | "shown in the App or Website at the moment of deposit"; wires entrantes US$ 0 ("Hapi nor Hapi's bank or custodian charge") |
| Retiro por wire, doméstico o internacional | US$ 20 |
| Mantenimiento | US$ 0 |
| Inactividad | US$ 4.99 al mes, "only to inactive accounts 60 days inactive with more than $0 and less than $100 balance" |
| Suscripción Prime | US$ 9.99 al mes |
| ACATS saliente (cobrado por Apex) / entrante | US$ 75 / US$ 0 |
| Salida DTC hacia una SAB | **No figura en el tarifario** |
| Estados de cuenta y confirmaciones en papel | US$ 5 / US$ 2 |

- **Inactividad:** el artículo (fecha mostrada: 14-jul-2026) lo confirma. Se cobra solo a cuentas no Prime con menos de US$ 100 y sin entrar durante 60 días o más; "you only need to log in to your account at least once every 60 days". — [Hapi, Maintenance Fee](https://help.hapi.trade/en/articles/8982192)
- **Depósito desde Perú:**
  - Cross Payments: "flat fee of US$1.99 per deposit" en PEN; 0.45% con mínimo de US$ 2.99 en USD.
  - **El tipo de cambio no se publica.**
  - Acreditación en hasta 4 horas hábiles si se deposita antes de las 12 pm ET.
  - El artículo dice "Updated over 3 weeks ago", con capturas del 11-jun-2026.
  - Fuente: [Hapi, Cross Payments](https://help.hapi.trade/en/articles/12631400-what-is-cross-payments-and-how-to-use-it-to-deposit-into-hapi)
- **Retiro a Perú** (31-ago-2026): US$ 7.99 por transferencia local en USD, US$ 4.99 por AIRTM y US$ 20 por transferencia internacional (ver `comisiones_fondeo_y_brokers_trading.md`).
- **Salida DTC de Hapi**, solo según creadores:
  - US$ 25 por valor hacia una SAB peruana y US$ 75 hacia brókers de EE.UU. Lo ejecutaron hacia Renta 4 en mar-2026. — [Bolsillos Llenos, NXKKWVudXuw](https://www.youtube.com/watch?v=NXKKWVudXuw); [ZkskDYeDcyw](https://www.youtube.com/watch?v=ZkskDYeDcyw)
  - "$5 así te transfieras un solo valor o toda tu cartera". — [Ingenio Inversiones, KeLvBY2R3Is, 26-ene-2025](https://www.youtube.com/watch?v=KeLvBY2R3Is)
  - **Las dos cifras se contradicen y el tarifario oficial solo lista el ACATS de US$ 75.**
- **Fracciones:** en las transferencias *entrantes*, Hapi solo acepta valores enteros; las fracciones se venden antes (extracto del buscador). Se infiere que lo mismo vale para la salida. — [Hapi, Transfer stocks to Hapi](https://help.hapi.trade/en/articles/9350655-how-to-transfer-your-investment-portfolio-to-hapi)

**IBKR: lo que faltaba en las notas**
- **Comisión de SPYL en la LSE: no verificada en fuente oficial** (403). Las secundarias no coinciden:
  - 0.05% del valor con mínimo de US$ 4 en Fixed. — [Bankeronwheels](https://www.bankeronwheels.com/?p=109736) (vía buscador)
  - US$ 1.70 por operación en Fixed y desde US$ 0.35 en Tiered. — [The Kopi Notes, 2026](https://thekopinotes.com/articles/etfs/ibkr-singapore-review/) (vía buscador)
  - Sobre US$ 6,800, cualquiera de los dos da entre US$ 1.70 y 4.
- SPYL cotiza en USD en la LSE, así que no hay conversión de divisa dentro de IBKR. Ficha: ISIN IE000XZSV718, TER 0.03%. — [justETF](https://www.justetf.com/en/etf-profile.html?isin=IE000XZSV718)
- Ya documentado en `comisiones_fondeo_y_brokers_trading.md` y `brokers_vias_acceso.md`, sin cambios:
  - IB LLC (entidad para Perú, confirmada solo por fuentes secundarias);
  - custodia e inactividad US$ 0;
  - un retiro gratis al mes, luego US$ 10;
  - salida FOP por DTC sin cargo de IBKR;
  - TOTP ("Mobile Authenticator") sujeto a elegibilidad regional;
  - SafetyPay desde el 18-ago-2026, sin tarifa publicada;
  - SIPC más el exceso con Lloyd's.
- **Wise para fondear IBKR desde Perú:** según un creador, la opción "transferencia desde balance de Wise" del Client Portal funciona en Argentina, Chile, Colombia, Costa Rica, España, Perú y Uruguay. No se verificó en fuente oficial. — [El Planeta Financiero, hakbpzyn9Ow, 10-ene-2026](https://www.youtube.com/watch?v=hakbpzyn9Ow)
- **Wire por la app del BCP:** según un creador, cuesta US$ 10 hasta US$ 500 y US$ 30 de ~US$ 5,000 a 8,000, frente a ~US$ 70 en ventanilla y ~US$ 50 por la web. La app no permite marcar OUR, así que los corresponsales pueden descontar. No verificado; lo probó con US$ 100. — [Opciones Financieras, FCWyNitbzfY, 20-abr-2026](https://www.youtube.com/watch?v=FCWyNitbzfY)

**Comisión de venta en la BVL**, el dato que faltaba para la ruta B (todo según creadores, sin tarifario oficial leído)
- **Renta 4:**
  - Comisión mínima de S/ 40 o US$ 15. La comisión SAB es de 0.43% y, sumando BVL, SMV, Fondo de Garantía, CAVALI e IGV, el total ronda **~0.6%**. — [Luis Ccaccya, SEwvYdLJqbk, 01-feb-2026](https://www.youtube.com/watch?v=SEwvYdLJqbk)
  - Otra versión: mínimo de US$ 25 para valores en dólares o extranjeros, con 0.43% y 0.65%. — [Ingenio Inversiones, KeLvBY2R3Is, ene-2025](https://www.youtube.com/watch?v=KeLvBY2R3Is)
  - **Las dos versiones se contradicen.**
- **Trii (Kallpa):** US$ 3 hasta US$ 500 y 0.6% total por encima, sin cobro por depósito ni retiro. — [Luis Ccaccya, SEwvYdLJqbk](https://www.youtube.com/watch?v=SEwvYdLJqbk)
- **Coril:** 0.4% SAB, ~0.57% total y sin mínimo, **solo con el convenio del canal** (para sus alumnos de pago). Para el público general hay comisión mínima y cobro de mantenimiento. — [Luis Ccaccya, SEwvYdLJqbk](https://www.youtube.com/watch?v=SEwvYdLJqbk)

### Inferences

**Modelo de los dos paquetes.** Ambos reciben US$ 6,800 en un solo depósito y se mantienen 20 años; los aportes van como variante.
- **A:** IBKR + SPYL.
  - Entrada: cambio en Kambista (0.4%) + wire de Interbank (US$ 42) + corresponsales (US$ 0–30) + comisión en la LSE (~US$ 4).
  - Mantenimiento: TER de 0.03% más la retención de 15% sobre los dividendos dentro del fondo; nada tributa en Perú hasta la venta.
  - Venta en 3 tramos (años distintos) al 14%: comisión de 0.05% más US$ 25 de recepción en Interbank por tramo.
  - Variante: venta en un solo año, aplicando la escala sobre la renta de trabajo.
- **B:** Hapi + VOO.
  - Entrada: depósito en PEN por Cross Payments (US$ 1.99) + diferencial no publicado (0.4% en el caso bajo, 1.0% en el alto) + *clearing* de US$ 0.25.
  - Dividendos: 1.07% con retención de 30% en EE.UU. más un residual peruano de 14% − 8.58% = **5.42%** (crédito con tope en la tasa media del art. 88 e), ver `youtube_bolsillos_llenos.md`).
  - Salida:
    - DTC de Hapi: US$ 25 (creador);
    - migración en la SAB: US$ 20 (Renta 4, creador);
    - venta en la BVL: 0.6% total;
    - 6.25% sobre la ganancia bruta.

| Paquete (US$ 6,800, 20 años, 7%) | Primer año (entrada + fondo + IR sobre dividendos) | Patrimonio neto final | Frente a A |
|---|---|---|---|
| **A: IBKR + SPYL, venta en 3 tramos al 14%, fondeo bajo** | US$ 86 = **S/ 293** | **US$ 22,457** (≈S/ 76,350) | referencia |
| A, fondeo alto (corresponsal US$ 30) | US$ 116 = S/ 395 | US$ 22,356 | −0.4% |
| A, venta en un solo año (la ganancia sube al 17%) | S/ 293 | US$ 22,118 | −1.5% |
| **B: Hapi + VOO → DTC → BVL al 6.25%, diferencial de 0.4%** | US$ 59 = **S/ 200** | **US$ 22,995** | **+2.4%** |
| B, diferencial de 1.0% | US$ 100 = S/ 339 | US$ 22,856 | +1.8% |
| B, con 0.5% de descuento por falta de liquidez de VOO en la BVL | S/ 200 | US$ 22,874 | +1.9% |
| B con SPY (TER 0.0945%, liquidez documentada) | US$ 63 = S/ 215 | US$ 22,724 | +1.2% |

| Variante con aporte de US$ 3,000 al año (20 aportes) | Patrimonio neto final | Frente a A |
|---|---|---|
| A, venta en 3 tramos al 14% | US$ 132,674 | referencia |
| A, venta en un solo año | US$ 125,899 | **−5.1%** |
| B con VOO | US$ 135,870 | +2.4% |
| B con SPY | US$ 134,842 | +1.6% |

Notas al modelo:
- **Por qué B gana más que el +1.5% de `PLAN.md`:** esa cifra usaba el perfil de S/ 84,000, con tasa media de 5.6% y residual de 8.4% sobre los dividendos. Con S/ 130,000 la tasa media es 8.6% y el residual baja a 5.4%, así que VOO pierde menos por dividendos. Antes de fricciones, el mismo modelo da +2.18% (comprobado con `drag.py`).
- **La disciplina de venta pesa más que el bróker.** Vender A en un solo año cuesta 1.5% sobre el depósito único y 5.1% con aportes, más que toda la ventaja de B.
- **Estate tax en B con aportes:** el saldo en activos de EE.UU. pasa de US$ 60k hacia el año 11–12 y llega a ~US$ 141k. Si el titular muriera con ese saldo, el impuesto sería de ≈US$ 16,400 (11.7%), según la tabla del art. 2001 con un crédito de US$ 13,000 (`impuestos_y_etfs.md`). El modelo no lo pondera por probabilidad. Sin aportes, B nunca pasa de ~US$ 24k, así que el riesgo es nulo.

**Otras diferencias que el modelo no captura:**
- **Declaración anual.** B obliga a declarar cada año los dividendos de VOO como renta extranjera con crédito. A no genera renta en Perú hasta la venta.
- **Proceso de salida en B:**
  - transferencia de 1 a 3 semanas;
  - informar el costo promedio a la SAB, porque CAVALI pone costo cero;
  - certificado de CAVALI, que tarda 1 a 1.5 meses;
  - pagar el 1.25% en la declaración;
  - vender las fracciones del DRIP dentro de Hapi, que tributan a la escala por su monto mínimo.
- **Operación en Hapi:**
  - fondear exige la app (en el celular dedicado);
  - el segundo factor es biométrico y no hay TOTP documentado;
  - conviene entrar cada 60 días, aunque con más de US$ 100 no se cobra inactividad;
  - si algún día se quiere migrar a otro bróker de EE.UU., el ACATS cuesta US$ 75.
- **Ventajas de A:**
  - se opera por web y el TOTP puede vivir en un gestor de contraseñas (a confirmar para Perú);
  - sin *estate tax*;
  - sin dependencia de SUNAT ni de la SAB;
  - si el dueño emigra, la ganancia extranjera deja de tributar en Perú.

**Cómo leer las cifras:**
- **Lectura en dinero:** B gana ≈US$ 400–540 (S/ 1,400–1,800) sobre el depósito único a 20 años, o ≈US$ 3,200 con aportes de US$ 3,000 al año. A cambio, B suma los cuatro riesgos no cuantificados ya listados y la carga anual de declarar. Es la misma conclusión de `PLAN.md` ("empate en retorno, SPYL gana por riesgo y simplicidad"), con una ventaja de B algo mayor que la anotada allí.
- **Aportes:** en fondeo, Hapi es más barato que un wire. Con US$ 3,000 al año, A paga ≈US$ 993 de entradas en 20 años y B ≈US$ 314. La diferencia se cierra si SafetyPay en IBKR cuesta menos de ~0.7%, o si el wire por la app del BCP cuesta lo que dice el creador (no verificado).

### Gaps
- Tarifa oficial de Hapi por DTC saliente hacia el custodio de una SAB peruana: US$ 25 o US$ 5 según los creadores; el tarifario no la lista.
- Tipo de cambio que aplica Hapi en Cross Payments; no está publicado.
- Si la web de Hapi permite depositar, retirar y pedir la transferencia DTC sin la app, y si Hapi ofrece TOTP o SMS en lugar de biometría.
- Tarifario oficial de Renta 4, Coril y Kallpa: hay dos versiones contradictorias de Renta 4 entre creadores.
- Liquidez de VOO en la BVL. Solo se documentó la de SPY (Bolsillos Llenos).
- Comisión oficial de IBKR por comprar SPYL en la LSE (403).
- El modelo no trata el efecto del tipo de cambio en la base imponible en soles, la indexación de la UIT ni la probabilidad de muerte.

---

## 3. Comparativas de brókers en YouTube para peruanos (2025–2026)

### Takeaway
Sí hay varias comparativas, pero ninguna de 2025–2026 hecha por un creador peruano compara IBKR con Hapi para un núcleo de largo plazo, y ninguna habla de Alpaca. Las comparativas directas "IBKR vs Hapi" son de 2024 (Juan Hun, FinanzasPlus y Kayser Pravia, este último panameño).

En 2025–2026 los creadores peruanos comparan sobre todo **Hapi frente a XTB**:
- dos de los creadores revisados se pasan, total o parcialmente, a XTB para comprar UCITS irlandeses;
- un tercero recomienda Hapi para hacer DCA en el S&P 500;
- otro hace un ranking de SAB para la BVL.

**Casi todos llevan enlaces de referido**, y la plataforma recomendada suele coincidir con el enlace. Las cifras de Hapi que dan los creadores de 2026 coinciden con el tarifario oficial. Las de 2025 están desactualizadas (inactividad y salida de títulos).

### Cited Findings
**Videos revisados**, ordenados por relevancia. Fechas de subida y vistas al 31-oct-2026, tomadas con yt-dlp.

| Video | Canal (país) | Fecha | Vistas | Qué compara | Qué recomienda y por qué | Enlaces comerciales en la descripción |
|---|---|---|---|---|---|---|
| [SEwvYdLJqbk](https://www.youtube.com/watch?v=SEwvYdLJqbk) | Luis Ccaccya, Invertir para el Futuro (PE) | 2026-02-01 | 6,877 | SAB para la BVL: Coril, Renta 4, Trii | 1.º Coril (4.4/5: 0.57% total sin mínimo y depósito inmediato desde BCP), 2.º Renta 4 (3.7), 3.º Trii (3.4). **Las condiciones de Coril son las del convenio del canal**, solo para quien paga su bootcamp o club | Referido de IBKR (`src=luisPY1`), XTB (geolink) y Trii (`aliadospe.trii.ai/?ref=`); convenio comercial con Coril; cursos de pago |
| [phB9YGq0erI](https://www.youtube.com/watch?v=phB9YGq0erI) | Renzo Peche, Papá Financiero (PE) | 2026-06-21 | 10,138 | Hapi vs XTB | Formalmente neutral ("no elijas solo por cuál suena más barata"), pero cierra invitando a probar XTB | Enlace de beneficio de XTB (`latam.xtb.com/condiciones-beneficio-papafinanciero`) |
| [Oth8KlmEX14](https://www.youtube.com/watch?v=Oth8KlmEX14) | Karicats (PE) | 2026-04-17 | 8,812 | XTB vs Hapi | Pasa su ETF del Nasdaq-100 a XTB para comprar un UCITS irlandés (15% de retención frente a 30%). Critica el costo de los depósitos en Hapi | Códigos de regalo de Hapi y Trii (`bit.ly/RegaloHapi`, `bit.ly/RegaloTrii`); escuela de pago |
| [Rfnyja_upaA](https://www.youtube.com/watch?v=Rfnyja_upaA) | Karicats (PE) | 2025-08-22 | 19,689 | Cómo invertir en el S&P 500 desde Perú | UCITS en XTB porque Hapi "no tiene" bolsa europea | Bono de XTB (`latam.xtb.com/condiciones-beneficio-karicats-finanzas`) |
| [XFwW_oP8MlE](https://www.youtube.com/watch?v=XFwW_oP8MlE) | Karicats (PE) | 2025-03-14 | 87,108 | Dónde comprar acciones (BVL o extranjero) | Empezar por la BVL; afuera prefiere XTB a Hapi porque Hapi cobra por depositar | Códigos de Hapi y Trii |
| [qYgp_jDhghs](https://www.youtube.com/watch?v=qYgp_jDhghs) | César AT (PE) | 2026-03-09 | 2,094 | S&P 500: Trii, fondo mutuo (Flip) o Hapi | **Hapi**: fracciones, DCA desde US$ 40 y sin comisión de gestión. Al fondo mutuo le atribuye ~1.28% al año con IGV | **Código de Hapi `CESATU1`** ("podrás ganar hasta 500 dólares"), referido de Trii y asesoría pagada |
| [KeLvBY2R3Is](https://www.youtube.com/watch?v=KeLvBY2R3Is) | Ingenio Inversiones (PE) | 2025-01-26 | 23,845 | Schwab, IBKR, Renta 4, Trii, Hapi y XTB | Sin ganador. Da montos mínimos para que el costo quede por debajo de 1%; para IBKR o Schwab, fondear por Global66 + Wise | Referidos de XTB, Hapi, IBKR, Renta 4, Global66 y Wise (`clic.ingenioinversiones.com/...`) |
| [hakbpzyn9Ow](https://www.youtube.com/watch?v=hakbpzyn9Ow) | El Planeta Financiero, Kayser Pravia (Panamá) | 2026-01-10 | 28,824 | Cómo depositar en IBKR | IBKR. El balance de Wise está disponible para Perú | Referido de IBKR (`src=kaysery5`); dice no tener otra afiliación |
| [FCWyNitbzfY](https://www.youtube.com/watch?v=FCWyNitbzfY) | Opciones Financieras (PE) | 2026-04-20 | 2,226 | Fondear Schwab desde Perú | Wire por la app del BCP (ver la sección 2) | Sin referidos; vende un programa por WhatsApp |
| [8VnWJNAvgmI](https://www.youtube.com/watch?v=8VnWJNAvgmI) | Esteban Inversiones (Argentina) | 2025-11-17 | 3,800 | ¿Vale la pena IBKR desde Latinoamérica? | Sí, pero es complejo y fondear no es "un solo clic". Él tiene ~50% ahí | Referidos de IBKR, XTB ("hasta $200 USD de regalo"), Balanz e IOL |
| [TQFX5tHC6h4](https://www.youtube.com/watch?v=TQFX5tHC6h4) | Alternativa Inversiones (Colombia) | 2025-03-04 | 84,616 | XTB vs Hapi vs Trii (contexto colombiano) | XTB por los UCITS | Embudo propio; no se vio referido de bróker |
| [Y6fhdMWKD4o](https://www.youtube.com/watch?v=Y6fhdMWKD4o) | Makers Lat | 2025-09-07 | 105 | IBKR, Schwab y Hapi | Descripción genérica, sin recomendación | — |

- **Encontrados pero no transcritos** (anteriores a 2025 o fuera de tema):
  - [SZMYyiU6DQ0](https://www.youtube.com/watch?v=SZMYyiU6DQ0): Kayser Pravia, "Debate definitivo: Hapi vs Interactive Broker", 15-sep-2024, 12,945 vistas.
  - [IgxEzcn5iaI](https://www.youtube.com/watch?v=IgxEzcn5iaI): Juan Hun, "Interactive Brokers vs Hapi", 22-ago-2024, 35,744 vistas.
  - [0uOrdGe4JjQ](https://www.youtube.com/watch?v=0uOrdGe4JjQ): FinanzasPlus, 30-abr-2024, 33,295 vistas.
  - [7yGOtQynd_E](https://www.youtube.com/watch?v=7yGOtQynd_E): Ingenio, "Hapi vs XTB", 23-dic-2024, 41,303 vistas.
  - [dSmRN8yulCg](https://www.youtube.com/watch?v=dSmRN8yulCg): Luis Ccaccya, BVL vs bolsa extranjera, 23-mar-2025, 27,577 vistas.
  - [zQQsNGPeqjg](https://www.youtube.com/watch?v=zQQsNGPeqjg): Trader Geek, "Mejores brokers de TRADING para Perú", 28-mar-2025, 19,373 vistas; por el título, orientado a forex o CFD.
- **Ya transcritos en notas anteriores:**
  - Bolsillos Llenos (comparativa del 23-feb-2026 y ruta BVL; ver `youtube_bolsillos_llenos.md`).
  - Luis Ccaccya, [IacmrD3u_F8](https://www.youtube.com/watch?v=IacmrD3u_F8), "¿XTB o Interactive Brokers?", 01-mar-2026. Cierra con una lista de criterios sin elegir y enlaza referidos de IBKR y de XTB, este con el código `INVFUTURO`.

**Contraste de las cifras de los videos con las fuentes oficiales**

| Afirmación (video, fecha) | Fuente oficial | Veredicto |
|---|---|---|
| Hapi cobra US$ 0.10 por acción entera y US$ 0.15 por fracción; US$ 2.99 en horario extendido; Prime US$ 9.99 al mes; inactividad US$ 4.99 al mes tras 60 días; retiro por wire US$ 20 ([phB9YGq0erI](https://www.youtube.com/watch?v=phB9YGq0erI), jun-2026) | [Tarifario de Hapi, 29-abr-2026](https://hapi-public-documents.s3.us-east-1.amazonaws.com/hapi-fees-schedule.pdf) | **Coincide.** La inactividad solo aplica con menos de US$ 100. Omite el retiro local de US$ 7.99 en Perú |
| Hapi cobra por depósito "2.99 o 0.90%" ([qYgp_jDhghs](https://www.youtube.com/watch?v=qYgp_jDhghs), mar-2026; [KeLvBY2R3Is](https://www.youtube.com/watch?v=KeLvBY2R3Is), ene-2025) | [Hapi, Cross Payments](https://help.hapi.trade/en/articles/12631400-what-is-cross-payments-and-how-to-use-it-to-deposit-into-hapi) | **Parcial.** Corresponde a la vía Koywe en USD; en PEN por Cross Payments son US$ 1.99 fijos |
| Inactividad de Hapi: US$ 1.99 al mes con menos de US$ 1,000 ([KeLvBY2R3Is](https://www.youtube.com/watch?v=KeLvBY2R3Is), ene-2025) | [Hapi, Maintenance Fee](https://help.hapi.trade/en/articles/8982192) | **Desactualizado:** hoy son US$ 4.99 con menos de US$ 100 |
| Hapi cobra US$ 5 por transferir títulos, uno o toda la cartera ([KeLvBY2R3Is](https://www.youtube.com/watch?v=KeLvBY2R3Is), ene-2025) | El tarifario solo lista el ACATS de US$ 75; Bolsillos Llenos pagó US$ 25 por valor en mar-2026 | **Contradictorio**, sin confirmación oficial |
| IBKR: primer retiro del mes gratis y luego US$ 10; transferencia de títulos US$ 0 ([KeLvBY2R3Is](https://www.youtube.com/watch?v=KeLvBY2R3Is)) | [IBKR, IMPACT pricing](https://impact.ibkr.com/en/pricing.php); [IBKR KB, FOP](https://ibkb.interactivebrokers.com/de/node/1002) (extractos) | **Coincide** |
| XTB: inactividad de €10 al mes tras 365 días sin operar ([phB9YGq0erI](https://www.youtube.com/watch?v=phB9YGq0erI)) | [XTB Commission Table INT, 14-mar-2026](https://www.xtbofficial.com/int/actual_commission_table.pdf): 365 días sin operar **y** 90 sin depositar | **Coincide en lo grueso**; omite la condición de depósito |
| Los UCITS irlandeses pagan 15% de retención en lugar de 30% ([Oth8KlmEX14](https://www.youtube.com/watch?v=Oth8KlmEX14)) | Ver `impuestos_y_etfs.md` (Taxes for Expats y otras) | **Coincide** |
| Renta 4: mínimo S/ 40 o US$ 15, ~0.6% total ([SEwvYdLJqbk](https://www.youtube.com/watch?v=SEwvYdLJqbk), feb-2026), frente a mínimo US$ 25 y 0.65% en dólares ([KeLvBY2R3Is](https://www.youtube.com/watch?v=KeLvBY2R3Is), ene-2025) | Tarifario de Renta 4 no leído | **Sin verificar y contradictorio** |
| Wire por la app del BCP: ~US$ 15 por US$ 1,000 y US$ 30 hasta US$ 8,000 ([FCWyNitbzfY](https://www.youtube.com/watch?v=FCWyNitbzfY), abr-2026) | Tarifario del BCP no disponible (403 en la sesión anterior) | **Sin verificar** |
| Wise sirve para fondear IBKR desde Perú ([hakbpzyn9Ow](https://www.youtube.com/watch?v=hakbpzyn9Ow), ene-2026) | Sin fuente oficial de IBKR (403). Coincide con [Tl43fYsfKyo](https://www.youtube.com/watch?v=Tl43fYsfKyo) ("ya se puede crear cuentas nuevamente") | **Plausible**, sin verificar |

### Inferences
- **Hay un sesgo comercial sistemático.** XTB y Hapi pagan bonos por registro (XTB "hasta $200", Hapi "de 1 a 500 dólares" en cripto) y son los más recomendados en los videos de 2025–2026. IBKR aparece con referido en Luis Ccaccya, Ingenio, Kayser Pravia y Esteban, pero ningún creador peruano lo recomienda como núcleo para alguien que no hace DCA con montos pequeños. El canal con mejor contenido fiscal (Bolsillos Llenos) ya estaba documentado y tampoco es neutral.
- **La tendencia de 2025–2026 entre creadores peruanos coincide con el informe:** el que quiere UCITS sale de Hapi, porque no los ofrece. Karicats lo hizo hacia XTB, una entidad de Belice, ya descartada en `brokers_vias_acceso.md` por su protección. Para este usuario, el equivalente regulado en EE.UU. es IBKR.
- **Lo útil de los videos para el plan son cuatro cifras a verificar:**
  1. la comisión de venta en la BVL (~0.6% total), que entra en el modelo de B;
  2. el wire por la app del BCP (~US$ 30 por US$ 6,800–8,650), que abarataría el fondeo de A frente a los US$ 42 de Interbank;
  3. Wise como vía de aportes a IBKR;
  4. la tarifa DTC de Hapi.
- **Ningún creador habla de Alpaca para peruanos.** La pregunta 1 no se puede contrastar en YouTube.

### Gaps
- No se transcribieron los videos de 2024 que comparan IBKR con Hapi; están fuera de la ventana pedida y sus tarifas ya cambiaron.
- No se pudo confirmar si los enlaces pagan comisión al creador, aunque los códigos, bonos y parámetros `src=`/`ref=` lo sugieren.
- Las tablas mostradas en pantalla (por ejemplo, el rango de US$ 501–3,000 del BCP) no están en los subtítulos.

---

## Recomendación

### Takeaway
1. **Núcleo: Interactive Brokers + SPYL**, operado por web. Se mantiene la decisión de `PLAN.md`.
   - Hapi no puede comprar SPYL.
   - El paquete Hapi + VOO con salida por la BVL gana +1.8% a +2.4% a 20 años (≈US$ 400–540 sobre US$ 6,800), unos 0.1 pp/año. Esa ventaja depende de cuatro datos no verificados, obliga a declarar dividendos cada año y, con aportes, expone al *estate tax*.
   - Los aportes van por defecto a SPYL en IBKR, con uno o dos wires al año de US$ 3,000 o más, o por SafetyPay o Wise si cuestan menos de ~0.7%.
   - La ruta B solo se activa, para los aportes nuevos y con SPY comprado en IBKR (FOP gratis), si el ingreso pasa de forma sostenida de ~S/ 148,500, como ya dice `PLAN.md`.
2. **Trading: Alpaca si acepta Perú.** La razón es que Quantac ya está integrado y la API no pasa por el 2FA. Hay que configurar `max_margin_multiplier = "1"` y `no_shorting = true`.
   - Si Alpaca no acepta Perú, o no permite multiplicador 1 a no residentes, la alternativa es una **segunda cuenta cash en IBKR**, fondeada en el mismo wire que el núcleo (US$ 8,650 caben en el tramo de US$ 42 de Interbank).
   - **Hapi no sirve para trading** aunque sea solo-app: no tiene API pública y cobra US$ 2.99 por operación en horario extendido.
3. **Hapi tiene un uso posible, no necesario:** canal barato para aportes pequeños (US$ 1.99 en PEN) si SafetyPay resulta caro. Esa parte quedaría en VOO o SPY, con dividendos que tributan cada año, y saldría por DTC a US$ 25–75.

### Cited Findings
- Hapi solo ofrece valores listados en EE.UU. — [Hapi, Available investments](https://help.hapi.trade/en/articles/8977445-available-investments-in-hapi); [Hapi Fee Schedule](https://hapi-public-documents.s3.us-east-1.amazonaws.com/hapi-fees-schedule.pdf)
- Alpaca no publica lista de países y remite a soporte. El país de residencia fiscal se elige en la solicitud. Perú no está en la lista de moneda local. — [Alpaca Support](https://alpaca.markets/support/countries-alpaca-is-available); [Alpaca Learn](https://alpaca.markets/learn/live-trading-account-non-us/); [Alpaca, Local Currency Transfer](https://alpaca.markets/support/currencycloud-transfer-questions)
- Alpaca permite `max_margin_multiplier` "1" y `no_shorting`. — [Alpaca API](https://docs.alpaca.markets/reference/patchaccountconfig-1)
- Resultados del modelo de paquetes: sección 2 de estas notas.

### Inferences
**Lo que debes comprobar tú (noviembre de 2026), en este orden:**

1. **Alpaca, en el dashboard que ya tienes** (unos 10 minutos, sin fondear):
   1. Entra a la web app de Alpaca con tu usuario de paper y abre la opción de cuenta *live*. Según la guía oficial: activar MFA → elegir Individual → "Are you a U.S. tax resident?" → **No** → "Country of tax residence". Los nombres del menú pueden variar.
   2. Abre la lista de países. **Si Perú no aparece, o el formulario rechaza la dirección o el Tax ID (DNI o RUC), Alpaca no te acepta:** queda la segunda cuenta en IBKR.
   3. Si Perú aparece, avanza hasta los datos básicos y el Tax ID. Detente antes de la selfie si aún no quieres enviar KYC.
   4. Desde el botón de soporte del dashboard, abre un ticket con tres preguntas y pide respuesta escrita:
      - (a) ¿Aceptan cuentas *live* individuales de residentes fiscales en Perú?
      - (b) ¿Qué métodos de fondeo hay para Perú? ¿Solo wire en USD? ¿Cobran por recibirlo?
      - (c) ¿Puedo fijar `max_margin_multiplier` = 1 y `no_shorting` en una cuenta de no residente, y cómo me aplica el margen intradía que reemplazó a la PDT?
   5. Si aprueban: en el dashboard *live* o vía `PATCH /v2/account/configurations`, fija el multiplicador en 1 y activa `no_shorting` **antes** de fondear.
2. **IBKR, al abrir la cuenta:**
   1. En los acuerdos de apertura, comprueba que la entidad sea **Interactive Brokers LLC**.
   2. Llena el W-8BEN dentro de la solicitud.
   3. En Settings → Security → Secure Login System, comprueba si se ofrece "**Mobile Authenticator app**" (TOTP) para Perú. Si se ofrece, regístralo en tu gestor de contraseñas. Si no, usa IB Key en el celular dedicado.
   4. En Transfer & Pay → Deposit → nuevo método, mira si aparecen **SafetyPay** y "transferencia desde Wise" para Perú, y anota su comisión y su tipo de cambio. Si alguna cuesta menos de ~0.7%, ese es el canal de los aportes.
   5. Antes de mandar el wire, simula la transferencia al exterior en la banca del BCP (app o web) por US$ 8,650 y compárala con Interbank (US$ 42 + corresponsales). Un creador afirma ~US$ 30 por la app del BCP.
   6. Para la compra: busca **SPYL**, elige la línea **LSE en USD** (ISIN IE000XZSV718), usa una orden límite y revisa la comisión en el *order preview* antes de transmitir. Sobre ~US$ 6,800 debería ser de US$ 1.70–4.
   7. Si el trading va a IBKR: Settings → "Open an Additional Account", tipo **cash**.
3. **Solo si algún día activas la ruta BVL:**
   1. Pide a la SAB que elijas (Renta 4, Coril o Kallpa) su tarifario escrito: recepción DTC, "migración", comisión de venta de valores extranjeros, mínimo y liquidez de SPY y VOO.
   2. Pide a IBKR por ticket la confirmación de un FOP saliente hacia el custodio de esa SAB.
   3. Haz la prueba con una acción, como propone `comisiones_fondeo_y_brokers_trading.md`.
   4. Hapi solo entra si vas a usarlo para aportes. En ese caso, pregunta por escrito la tarifa DTC hacia una SAB peruana (US$ 25 o US$ 5 según creadores; el tarifario solo lista el ACATS de US$ 75) y si la web permite depositar y retirar sin la app.

**Pendientes para `PLAN.md`:**
- Corregir la tabla del ETF: con S/ 130,000, la vía VOO-BVL da +2.2% antes de fricciones y +1.8% a +2.4% después, no +1.5%. La decisión no cambia.
- Añadir que vender SPYL en un solo año cuesta 1.5–5% del patrimonio final. Vender por tramos es obligatorio.

### Gaps
- Ninguna de las tres comprobaciones críticas (Alpaca y Perú, TOTP de IBKR en Perú, tarifa de SafetyPay) se puede cerrar con fuentes públicas: requieren la cuenta del dueño.
- La comisión de venta en la BVL y la tarifa DTC de Hapi vienen solo de creadores. Si la venta en la SAB costara 1% en lugar de 0.6%, la ventaja de B bajaría unos 0.4 puntos.
