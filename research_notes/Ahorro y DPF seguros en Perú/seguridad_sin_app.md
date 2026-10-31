# Ahorro y DPF en Perú sin app bancaria en el celular: modelo de amenaza y configuraciones seguras (estado a 29-oct-2026)

Convención de etiquetas usada en estas notas:
- **[DOC OFICIAL]** = leído por mí en el documento primario (contrato, cartilla, T&C, web oficial de la entidad, resolución).
- **[PRENSA]** = leído por mí en el artículo de prensa completo.
- **[SNIPPET]** = solo visto en el resumen/fragmento del buscador; no pude abrir la fuente completa. Tratar con más cautela.
- Todas las fechas son de publicación o de consulta (consulta = 29-oct-2026).

---

## 1. ¿Cuáles son los modos de fraude dominantes contra clientes bancarios en Perú en 2025-2026?

### Takeaway
El vector dominante y de más rápido crecimiento es el **robo del celular con acceso a las apps financieras** (transferencias, préstamos a nombre de la víctima, uso de billeteras), seguido de la ingeniería social (llamadas o mensajes falsos que crean urgencia, suplantación de la entidad, premios falsos). ASBANC dice que hoy la cuenta de ahorros es el producto más amenazado porque las billeteras digitales se vinculan a ella. No encontré estadística oficial de SBS ni de la PNP que desglose las pérdidas por modalidad (robo de celular, SIM swap, smishing, vishing, apps falsas, Yape/Plin).

### Cited Findings
**Robo de celular → vaciado de cuentas**
- Según el Observatorio del Crimen y la Violencia (Banco de Ideas Credicorp, BCP y CHS Alternativo), a diciembre de 2025 unos **5,45 millones** de personas fueron víctimas de vaciado de cuentas tras robo de celular **o conocen a alguien que lo fue**, frente a 2,97 millones en diciembre de 2024 (+80 % interanual). En el norte la proporción pasó de 7 % a 18 %; en Lima subió 13 p.p. Ojo: es una encuesta con la métrica "víctima o conoce a una víctima", no un conteo de casos — [Gestión](https://gestion.pe/tu-dinero/cuentan-bancarias-cinco-millones-son-afectadas-por-robo-de-celulares-para-vulnerarlas-noticia/); [Panamericana](https://panamericana.pe/nacionales/464350-robo-celulares-acceso-cuentas-bancarias-incremento-80-ano); [Microfinanzas](https://microfinanzas.pe/robo-de-celulares-abre-la-puerta-al-fraude-bancario-casos-aumentan-mas-del-80-en-un-ano/) [SNIPPET].
- El gerente de Riesgo Operacional, Tecnológico y de Seguridad de la Información de Banco Pichincha (Diego Rodríguez) describe la mecánica así: el delincuente entra a las aplicaciones financieras de la víctima desde el celular robado, transfiere dinero a cuentas propias o de terceros, suplanta a la víctima para pedir préstamos y, si no logra entrar, pide dinero a sus contactos — [El Comercio, 18-jun-2025](https://elcomercio.pe/tecnologia/actualidad/robo-de-celular-como-evitar-que-saquen-dinero-de-tus-cuentas-bancarias-o-pidan-prestamos-a-tu-nombre-noticia/) [PRENSA].
- OSIPTEL registró en promedio **4.046 celulares robados por día** entre enero y abril de 2025 — [El Comercio, 18-jun-2025](https://elcomercio.pe/tecnologia/actualidad/robo-de-celular-como-evitar-que-saquen-dinero-de-tus-cuentas-bancarias-o-pidan-prestamos-a-tu-nombre-noticia/) [PRENSA]. En agosto de 2026 se reportaron 115.531 equipos robados (~3.727 por día), menos que en el mismo mes de 2025 — [América TV](https://www.americatv.com.pe/noticias/actualidad/osiptel-informo-que-roban-casi-4-mil-celulares-al-dia-pais-n518031) [SNIPPET].
- Un ejecutivo citado por Gestión dice que hoy hay organizaciones criminales muy especializadas capaces de vaciar cuentas en minutos — [Gestión](https://gestion.pe/tu-dinero/cuentan-bancarias-cinco-millones-son-afectadas-por-robo-de-celulares-para-vulnerarlas-noticia/) [SNIPPET].

**Cifras de ASBANC (Gestión, 17-sep-2026) [PRENSA]** — [Gestión](https://gestion.pe/tu-dinero/fraude-digital-amenaza-cuentas-de-ahorro-por-s-257-millones-por-donde-atacan-delincuentes-noticia/)
- La línea de emergencia **1820** opera desde julio de 2024. Participan todos los bancos del sistema más Caja Ica y Banco de la Nación.
- Los bancos hicieron **más de 230.000 bloqueos** desde julio de 2024. **Cerca del 40 %** de esos casos vienen del robo o pérdida de celular o de tarjetas.
- ASBANC estima pérdidas evitadas por **S/ 96 millones** entre julio de 2024 y julio de 2025, y proyecta más de S/ 353 millones hasta diciembre de 2026. Los "S/ 257 millones" del titular son una resta hecha por el periodista, no una cifra de ASBANC.
- Bloquear una cuenta toma en promedio unos **3,5 minutos**.
- Las operaciones no reconocidas son el **principal motivo de reclamo**. La **cuenta de ahorros es hoy el producto más amenazado** porque las billeteras digitales se vinculan a ella; los reclamos por tarjeta de crédito bajaron.
- ASBANC describe tres tácticas de ingeniería social: mensajes de urgencia ("tu cuenta será bloqueada"), suplantación de entidades conocidas y promociones o premios falsos con enlaces fraudulentos.

**Otras cifras (fuentes no comparables entre sí)**
- ASBANC: los fraudes bancarios digitales crecieron 32 % en 2024 y los ataques con malware 113 %. La pérdida promedio tras el robo de un celular ronda los S/ 2.450 — [Infobae, 13-ago-2025](https://www.infobae.com/peru/2025/08/13/codigos-qr-phishing-y-robo-de-cuentas-delitos-informaticos-en-peru-podrian-duplicarse-este-2025/) [SNIPPET].
- PNP: 4.349 denuncias por delitos informáticos en 2025 hasta agosto. El phishing es la modalidad más denunciada y el vishing sigue activo — [Infobae, 13-ago-2025](https://www.infobae.com/peru/2025/08/13/codigos-qr-phishing-y-robo-de-cuentas-delitos-informaticos-en-peru-podrian-duplicarse-este-2025/) [SNIPPET].
- Fiscalía Especializada en Ciberdelincuencia, corte a septiembre de 2025: 21.371 denuncias por fraude informático (phishing y otros), 7.508 por smishing y técnicas similares y 941 por delitos contra datos y sistemas; en total unas 31.028 — [ebiz.pe](https://ebiz.pe/noticias/especial-confianza-digital-para-un-peru-seguro-fraude-informatico/) [SNIPPET].
- Experian/Edelman (julio de 2026): el 74 % de los peruanos encuestados dijo haber recibido intentos de fraude, la cifra más alta de los cinco mercados analizados — [SNIPPET, sin URL primaria verificada].
- INDECOPI: el sistema financiero concentra el 90 % de las sanciones por operaciones no reconocidas; de 2021 a marzo de 2025 impuso 2.891 sanciones a 271 proveedores — [Andina](https://andina.pe/agencia/noticia-indecopi-sistema-financiero-concentra-90-sanciones-operaciones-no-reconocidas-1026373.aspx) [SNIPPET]. INDECOPI informó también más de 800 reportes ciudadanos de operaciones no reconocidas por robo de celulares — [gob.pe/Indecopi](https://www.gob.pe/institucion/indecopi/noticias/654739-indecopi-se-registraron-mas-de-800-reportes-de-operaciones-bancarias-no-reconocidas-debido-a-robo-de-celulares) (solo el titular; la página devolvió error 418).

**SIM swapping (marco OSIPTEL)**
- Desde el 12-sep-2022 los operadores deben alertar al usuario cuando se repone su chip. Además, la verificación biométrica se limita a 5 intentos por persona, día y trámite — [DPL News](https://dplnews.com/peru-operadoras-telefonicas-deberan-alertar-a-usuarios-cuando-se-reponga-chip-movil/) [SNIPPET].
- Desde el 12-ene-2023 la contraseña única es obligatoria para contratar, cambiar de titular y reponer chip, y el chip repuesto se activa a las 4 horas, no de inmediato — [Gestión](https://gestion.pe/economia/contrasena-unica-para-cambio-de-chip-movil-o-compra-de-equipos-sera-obligatorio-desde-enero-2023-compra-de-equipos-chip-movil-noticia/) [SNIPPET].
- Una modificación posterior exige que la reposición de chip se haga solo en centros de atención presencial, con biometría, DNI físico y contraseña o preguntas de validación. No pude confirmar la fecha de vigencia — [DPL News](https://dplnews.com/peru-osiptel-publica-norma-para-prevenir-contrataciones-y-reposiciones-no-solicitadas-de-chips/) [SNIPPET].

**Billeteras (Yape/Plin)**
- La Res. SBS 00704-2026 (marzo de 2026) subió los topes de las cuentas de dinero electrónico simplificadas: 0,6 UIT por operación (~S/ 3.300), saldo consolidado de 1,9 UIT y transacciones mensuales de 2,8 UIT — [El Peruano](https://www.elperuano.pe/noticia/291038-usas-billeteras-digitales-revisa-los-nuevos-topes-de-transacciones-y-saldos-aprobados-por-la-sbs) [SNIPPET].

### Inferences
- El modelo de amenaza del usuario está bien calibrado. El riesgo dominante no es un ataque remoto sofisticado sino el acceso físico a un celular con apps abiertas o con sesión y biometría guardadas. Ese 40 % de ASBANC (celular o tarjetas) es la porción que se elimina si el celular de uso diario no tiene apps bancarias ni billeteras vinculadas al ahorro.
- Que ASBANC diga que "la cuenta de ahorros es el producto más amenazado porque las billeteras se vinculan a ella" apoya directamente separar la reserva de cualquier cuenta asociada a Yape o Plin.
- Quitar la app del celular **no protege** contra ingeniería social (vishing o smishing que lleva a la víctima a autorizar una operación). Esa defensa es conductual y de configuración de límites.
- El SIM swap está más acotado en Perú desde 2023 (contraseña única, activación diferida, biometría), pero sigue siendo relevante para entidades que usan OTP por SMS como segundo factor.

### Gaps
- No encontré cifras oficiales de la SBS ni de la DIVINDAT sobre montos perdidos por modalidad en 2025-2026. Las cifras de vaciado vienen de encuestas (Observatorio) o de bloqueos (ASBANC), no de pérdidas confirmadas.
- No hallé estadística específica de apps bancarias falsas ni del abuso de Yape o Plin tras el robo de celular.
- No pude abrir la nota oficial de INDECOPI sobre los "más de 800 reportes" (error 418) para ver período y detalle.

---

## 2. ¿Qué dice la regulación sobre quién asume la pérdida en operaciones no reconocidas, y cómo han resuelto INDECOPI/SBS en la práctica?

### Takeaway
La **Res. SBS 02286-2024** modificó el Reglamento de Tarjetas de Crédito y Débito (y los de Conducta de Mercado y de Reclamos). Con ella, la entidad asume las pérdidas por operaciones no reconocidas **realizadas sin autenticación reforzada**, salvo que pruebe la responsabilidad del usuario. Rige desde el 1-jul-2025 para tarjetas nuevas; para las antiguas, desde su renovación o desde el **1-jun-2026** (Res. SBS 00771-2026), lo que ocurra antes. Para transferencias desde la app no ligadas a tarjeta, la protección viene sobre todo del deber de idoneidad del Código del Consumidor. INDECOPI viene exigiendo que **el banco pruebe técnicamente** que la operación fue autenticada y autorizada; no basta con decir que se usó el token. Aun así, no hay responsabilidad automática del banco.

### Cited Findings
**Norma SBS**
- La Res. SBS 02286-2024 modifica el Reglamento de Tarjetas de Crédito y Débito, el Reglamento de Gestión de Conducta de Mercado y el Reglamento de Reclamos. Las entidades deben cubrir las pérdidas por operaciones digitales no reconocidas (pagos y transferencias) cuando no puedan acreditar la responsabilidad del usuario, en especial si se hicieron sin un segundo factor de autenticación. La responsabilidad por pérdidas rige desde el 1-jul-2025 — [Infobae, 6-jul-2024](https://www.infobae.com/peru/2024/07/06/bancos-deberan-asumir-perdidas-de-operaciones-no-reconocidas-en-tarjetas-de-clientes-desde-cuando/) [PRENSA].
- Las tarjetas emitidas antes del 1-jul-2025 "solo estarán obligadas a cumplir con el nuevo proceso de autenticación reforzada en el momento de su renovación" (literal b.2 del art. séptimo de la Res. 2286-2024). La responsabilidad por pérdidas en esas tarjetas rige desde la renovación o desde el 1-jun-2026, lo que ocurra primero. Hubo dos prórrogas: al 1-abr-2026 (junio de 2025) y al 1-jun-2026 (Res. SBS 00771-2026, marzo de 2026) — [Infobae, 18-mar-2026](https://www.infobae.com/peru/2026/03/18/sbs-a-partir-de-junio-bancos-deberan-responder-por-fraudes-en-tarjetas-de-credito-emitidas-antes-de-julio-de-2025/) [PRENSA]; [Infobae, 25-jun-2025](https://www.infobae.com/peru/2025/06/25/sbs-da-mayor-plazo-a-bancos-para-asumir-perdidas-de-operaciones-no-reconocidas-por-usuarios/); [TyTL sobre la Res. 00771-2026](https://tytl.com.pe/wp-content/uploads/2026/03/Consumidor-informa-RESOLUCION-SBS-N-00771-2026-1.pdf) [SNIPPET].
- El PIN pasó a ser obligatorio también en tarjetas de crédito presenciales, y las compras en línea exigen un segundo factor — [Andina](https://andina.pe/agencia/noticia-bancos-tienen-hasta-abril-del-2026-para-renovar-tarjetas-y-exigir-uso-clave-secreta-1035873.aspx) [SNIPPET].
- La Res. SBS 814-2025 (marzo de 2025) exige que las transferencias, los pagos interoperables y el pago de planillas por banca por internet, app y billeteras tengan planes de recuperación de 3 a 5 horas, y que se informe a los usuarios de los canales alternativos durante una caída — [El Comercio](https://elcomercio.pe/economia/sbs-establece-medidas-para-atenuar-el-impacto-de-interrupciones-de-canales-digitales-en-usuarios-ultimas-noticia/) [SNIPPET].
- Revisé la Res. SBS 01741-2026 (julio de 2026), que modifica Conducta de Mercado y Comisiones. Trata de información, canales de pago y comisiones; **no** cambia el régimen de operaciones no reconocidas — [Res. SBS 01741-2026 (LP Derecho)](https://img.lpderecho.pe/wp-content/uploads/2026/07/Resolucion-SBS-01741-2026-LPDerecho.pdf) [DOC OFICIAL, lectura parcial por palabras clave].

**Cómo lo traducen los contratos (ejemplos verificados)**
- **Caja Arequipa**, contrato aprobado por Res. SBS 00790-2026 y publicado en mayo de 2026 [DOC OFICIAL] — [Contrato de Depósitos y Servicios Complementarios](https://www.cajaarequipa.pe/wp-content/uploads/2026/05/CONTRATO-DE-DEP%C3%93SITOS-Y-SERVICIOS-COMPLEMENTARIOS.pdf):
  - Cl. 64: el cliente se obliga a custodiar "la Tarjeta, el equipo móvil, la tarjeta SIM", las claves y los factores de autenticación, y a comunicar de inmediato la pérdida o robo del equipo móvil. Hecho ese aviso, "no será responsable por el uso irregular o fraudulento". Además: "LA CAJA será responsable de las pérdidas por operaciones realizadas a través de los canales de atención, **salvo que acredite la responsabilidad de EL CLIENTE** por incumplimiento de las obligaciones antes detalladas".
  - Cl. 55: la Caja responde, entre otros casos, por clonación, mal funcionamiento de canales, suplantación en agencias, operaciones posteriores al bloqueo, servicios no habilitados por el cliente y cuando "el esquema de autenticación… no cumpla con los requerimientos mínimos de seguridad".
  - Cl. 54: las operaciones hechas antes del bloqueo son responsabilidad del cliente, salvo los supuestos de la cl. 55.
- **Pibank (Banco Pichincha)**, T&C de la App actualizados el 28-09-2026 [DOC OFICIAL] — [T&C App Pibank](https://prdpistdoceastus2.blob.core.windows.net/documentos1/ONBOARDING/TerminosCondiciones_App.pdf):
  - Ante pérdida o robo del dispositivo, el cliente debe avisar de inmediato al call center. "De no dar aviso oportuno al BANCO, el Cliente será responsable por las operaciones que se realicen con su dispositivo móvil… por lo que EL BANCO reputará como válidas dichas operaciones, a pesar de que las mismas hayan sido efectuadas por terceros."
  - Toda operación validada con Token Digital "se reconoce como efectuada y aceptada por EL TITULAR" — [Contrato Pibank, cl. 28.2](https://prdpistdoceastus2.blob.core.windows.net/documentos1/ONBOARDING/Contrato_CuentaSolesPibank.pdf).

**Casos INDECOPI**
- **Banco de la Nación**, Res. 101-2026/PS0-INDECOPI-SAM (San Martín). Tras una llamada de alguien que se hizo pasar por la entidad, salió por la app una transferencia de S/ 1.550 que el cliente no reconoció. El banco alegó que la operación pasó sus controles, pero no aportó registros de autenticación, logs ni grabaciones. INDECOPI ordenó devolver los S/ 1.550, impuso una multa de 1 UIT más costas y concluyó que **la carga de la prueba es del banco** — [Gestión, 8-may-2026](https://gestion.pe/economia/aplicativos-bancarios-quien-debe-probar-que-una-transferencia-fue-autorizada-por-el-usuario-indecopi-responde-noticia/) [PRENSA]; [LP Derecho](https://lpderecho.pe/si-te-sustraen-dinero-a-traves-del-aplicativo-del-banco-este-tiene-que-probar-que-la-operacion-fue-tuya-resolucion-101-2026-ps0-indecopi-sam/) [SNIPPET].
  - En la misma nota, el abogado Víctor Valdez dice que "no existe una responsabilidad automática de la entidad financiera solo porque el consumidor desconozca la operación". El banco debe mostrar cómo funcionaron sus mecanismos (IP, dispositivo, factores, alertas). Waldo Borda añade que, si el cliente no resguardó sus claves, su dispositivo o su token, parte de la responsabilidad puede trasladarse al consumidor — [Gestión, 8-may-2026](https://gestion.pe/economia/aplicativos-bancarios-quien-debe-probar-que-una-transferencia-fue-autorizada-por-el-usuario-indecopi-responde-noticia/) [PRENSA].
- **BBVA**, Res. 0156-2025/PS0-INDECOPI-CHT (Áncash/Chimbote). Fueron 4 operaciones no reconocidas por S/ 5.700 (11 y 12 de abril de 2025) por banca móvil, que el banco dijo validadas con DNI, clave, contraseña y token digital. INDECOPI rechazó que el token sirviera a la vez como factor de autenticación y como control contra ataques de "hombre en el medio", porque el banco no probó que la clave se generara "fuera de banda" como exigía un oficio de la SBS. Multa de 3,78 UIT (~S/ 20.790) y orden de devolución — [La República, 24-may-2026](https://larepublica.pe/sociedad/2026/05/24/indecopi-multa-a-bbva-con-s20790-transferencia-no-reconocida-validada-con-token-digital-en-banca-movil-de-clienta-1794936) [PRENSA].
- **Scotiabank**, caso de celular robado. El robo fue en septiembre de 2022 y el cliente bloqueó de inmediato su línea, la app y sus cuentas. Aun así, días después se tramitó por la app un préstamo de S/ 33.700 que se abonó en una cuenta que el cliente no pidió, y pasaron 4 operaciones por S/ 17.000. INDECOPI multó con 30,09 UIT y ordenó anular el préstamo y la cuenta (segunda instancia). En un segundo caso multó con 22,83 UIT porque no se activó ninguna alerta ante un cargo de S/ 20.000 atípico — [RPP, 24-jul-2025](https://rpp.pe/economia/economia/indecopi-multa-a-scotiabank-por-prestamos-no-autorizados-tras-robo-de-celular-noticia-1647560) [PRENSA].
- **Alfin Banco**. INDECOPI ordenó devolver S/ 264.179,90 (cargos, comisiones, ITF e intereses legales) por 27 cargos no reconocidos. El banco le atribuyó al cliente 5 cuentas que no pidió y cambió sin permiso el correo vinculado a la banca móvil. Multa de 22,63 UIT, en segunda y última instancia — [Andina, 29-dic-2025](https://andina.pe/agencia/noticia-indecopi-ordena-a-banco-devolver-mas-s-264000-operaciones-no-reconocidas-1057368.aspx) [PRENSA].

### Inferences
- En la práctica la carga de la prueba se ha desplazado hacia el banco, pero recuperar el dinero exige reclamar (a la entidad, luego a INDECOPI o la SBS) y esperar meses o años. El caso Scotiabank es de 2022 y se resolvió en 2025. Para un fondo de reserva, "me lo devolverán eventualmente" no reemplaza "no se lo pueden llevar".
- Las cláusulas como la de Pibank ("reputará como válidas" las operaciones sin aviso oportuno) son la posición contractual del banco. INDECOPI ha mostrado que el uso del token por sí solo no exime (caso BBVA), así que esas cláusulas no son la última palabra. Aun así, marcan cómo responderá el banco al primer reclamo.
- La norma SBS 2286-2024 está diseñada en torno a las tarjetas. Una cuenta como Pibank, sin tarjeta de débito, queda bajo el régimen general de seguridad de canales digitales y del Código del Consumidor, no bajo los supuestos taxativos del Reglamento de Tarjetas. Esto es interpretación mía y no lo encontré dicho explícitamente.
- Lo que más protege legalmente en caso de robo es **avisar rápido** (línea 1820 de ASBANC o la entidad). Varios contratos, como la cl. 64 de Caja Arequipa, liberan al cliente desde el aviso.

### Gaps
- No pude confirmar si hubo una tercera prórroga después del 1-jun-2026 para las tarjetas antiguas. No encontré ninguna nota que la mencione.
- No leí el texto oficial de la Res. SBS 02286-2024 (solo la prensa), así que no puedo citar literalmente qué operaciones sin tarjeta (transferencias por app desde la cuenta) cubre.
- No encontré resoluciones de INDECOPI de 2026 sobre robo de celular con el teléfono desbloqueado, que es el escenario exacto del usuario.

---

## 3. ¿Pibank funciona sin su app? ¿Tiene banca web? ¿Cómo autentica? ¿Qué pasa si desinstalas la app?

### Takeaway
**No. Pibank Perú es app-only para operar.** El contrato define los "Canales Digitales" como "el App" más los que el banco habilite a futuro. El Token Digital vive dentro de la app, es obligatorio y no se puede desafiliar sin cerrar la cuenta. La web (pibank.pe / registro.pibank.pe) sirve para darse de alta y pedir el cierre por formulario, y solo con saldo cero. No hay agencias, cajeros, tarjeta de débito ni efectivo. Sin la app, el dinero solo sale por el plan de contingencia (llamada o videollamada), y solo cuando el canal digital está caído. **Usar Pibank con cero app es inviable; la variante realista es la app en un teléfono dedicado que no sale de casa.**

### Cited Findings
**Lanzamiento y producto**
- Pibank es la marca digital de Banco Pichincha Perú (RUC 20100105862) y empezó a operar en Perú alrededor del 30-sep-2026. Lanzó la Cuenta Soles Pibank al 5 % TEA/TREA, sin comisiones y sin monto mínimo. Atiende por teléfono de lunes a domingo de 8:00 a 20:00 y prevé una cuenta en dólares "en las próximas semanas". No se mencionan DPF — [Infobae, 30-sep-2026](https://www.infobae.com/peru/2026/09/30/pibank-aterriza-en-peru-con-un-modelo-de-banca-sin-oficinas-para-quienes-esta-dirigido/); [Peru Retail, 30-sep-2026](https://www.peru-retail.com/banco-pichincha-pone-en-marcha-pibank-en-peru-y-apuesta-por-la-banca-100-digital/) [PRENSA]. (Ninguna de las dos notas menciona la app; los documentos oficiales sí.)
- La web oficial enlaza la app en Google Play (`pe.pibank.bm`) y en App Store (id6772352038), y dice: "Accede a tu cuenta desde nuestra app Pibank y realiza tus operaciones" — [pibank.pe](https://pibank.pe/) [DOC OFICIAL, consultado 29-oct-2026].
- Texto legal de la web: "Cuenta… 100% digital y permite realizar operaciones **exclusivamente a través de canales digitales Pibank**. No permite operaciones en efectivo, uso de agencias, cajeros automáticos, agentes corresponsales, ni emisión de tarjeta de débito, cheques u otros títulos valores." Está cubierta por el FSD — [Cuenta Soles Pibank](https://pibank.pe/cuenta-soles-pibank/) [DOC OFICIAL].

**FAQ oficial (página de producto, 29-oct-2026) [DOC OFICIAL]** — [pibank.pe/cuenta-soles-pibank](https://pibank.pe/cuenta-soles-pibank/)
- "Puedes realizar transferencias y operaciones **desde la app**… al abrirla se habilita tu acceso a la app."
- Requisitos de apertura: mayor de edad, DNI, **celular y correo electrónico**. Se abre en la web con "Hazte cliente": validas celular y correo, verificas identidad y creas usuario y contraseña "para acceder a la app".
- Transferencias: "**Desde tu App Pibank** puedes realizar transferencias… hacia tus cuentas propias, a terceros y a otros bancos." Si el acumulado del día supera **S/ 30.000**, algunas operaciones solo pueden ir a cuentas propias y por horarios.
- No hay transferencias internacionales; solo al sistema local y "siempre de forma digital desde la app".
- Cancelación: "Puedes cancelar tu cuenta desde la App Pibank o a través de la web mediante el siguiente formulario. Antes de solicitar el cierre, **asegúrate de que tu cuenta no tenga saldo disponible**."

**Contrato de Condiciones Generales de Cuentas y/o Depósitos Pibank (aprobado por Res. SBS N° 01047-2026) [DOC OFICIAL]** — [Contrato](https://prdpistdoceastus2.blob.core.windows.net/documentos1/ONBOARDING/Contrato_CuentaSolesPibank.pdf)
- Cl. 28: "se consideran como Canales Digitales **el App**, así como cualquier otro canal que EL BANCO ponga a disposición… en el futuro."
- Cl. 28.1: se entra con usuario y Clave Digital de 6 dígitos o más. El banco puede usar biometría (facial, huella, voz), Token Digital, OTP por correo o código QR como factores.
- Cl. 28.2: el TOKEN DIGITAL es de 6 dígitos, dinámico y se muestra "en el mismo Canal Digital". "EL TITULAR **no podrá desafiliarse al TOKEN DIGITAL** porque sino no podrá realizar ninguna operación… la única forma de poder dejar de tener el TOKEN DIGITAL es que TITULAR… cancele/cierre definitivamente su cuenta."
- Condición particular 5: la cuenta no permite disponer de efectivo, ni depósitos o retiros en agencia, agentes o cajeros, porque no tiene tarjeta de débito. Si los Canales Digitales quedan indisponibles, el banco activa un plan de contingencia por llamada o videollamada, con validación de identidad. Según la cartilla, ese plan sirve para "que éste solicite transferencias a cuentas de otras entidades **donde sea titular**" — [Cartilla](https://prdpistdoceastus2.blob.core.windows.net/documentos1/ONBOARDING/CartillaInformacion_CuentaSolesPibank.pdf).
- Cl. 22: se puede cancelar por "el App PIBANK y otros que se tenga para esta finalidad".

**T&C del App Pibank (actualizados 28-09-2026) [DOC OFICIAL]** — [T&C App](https://prdpistdoceastus2.blob.core.windows.net/documentos1/ONBOARDING/TerminosCondiciones_App.pdf)
- Se pueden afiliar hasta **3 dispositivos** a la app, pero el **Token Digital solo puede estar instalado en uno**.
- Para activar el Token Digital hay que validar la identidad dentro de la app, por ejemplo con reconocimiento facial. "La activación de Token Digital dentro de la App es una **condición obligatoria**… para que pueda ejecutar las operaciones." El banco puede usar además una OTP por correo o SMS.
- Para vincular un **dispositivo nuevo o cambiar credenciales**, el banco puede enviar una OTP **por correo electrónico**.
- Operaciones disponibles: transferencias propias, a terceros e interbancarias (inmediatas o diferidas); **envíos a contactos por número de celular o QR** (interoperabilidad BCRP, tipo Yape/Plin); abrir y cancelar cuentas; **"Personalizar límites de operaciones con terceros y con otras entidades"**; activar o desactivar biometría y notificaciones; gestionar favoritos.
- Límites del banco por día: hasta S/ 30.000 de forma inmediata o diferida. De S/ 30.000 a S/ 240.000, solo a cuentas propias y diferidas. Por encima de S/ 240.000 se tramita como solicitud con **videollamada** de validación, en un máximo de 1 día hábil.
- La interoperabilidad (envío a contacto por celular) requiere **afiliación previa** con Token Digital; sin afiliarse no se puede usar.
- **Favoritos**: una vez guardada una transferencia propia o a terceros como favorita, en las siguientes veces "no será necesario el Token Digital, biometría u otro factor de autenticación". Para eliminar un favorito sí se pide token.
- Robo del dispositivo: hay que avisar al call center para bloquear el ingreso a la app; sin aviso oportuno, el cliente responde (ver pregunta 2).

**Observación operativa (29-oct-2026)**
- El Centro de Ayuda muestra en "Ayuda urgente" ("si has sido víctima de un robo…") el número **+34 91 111 00 00**, que es un prefijo de España, aparentemente heredado de Pibank España. La banca telefónica peruana es el **0-800-71626**, de lunes a domingo de 8:00 a 20:00 — [Centro de Ayuda](https://pibank.pe/centro-de-ayuda/) [DOC OFICIAL].

### Inferences
- **Sin la app no puedes retirar dinero.** El cierre por formulario web exige saldo cero, y el saldo solo se vacía transfiriendo desde la app. El plan de contingencia solo aplica cuando el canal está caído, no como opción del cliente. Si desinstalas la app, para recuperar el acceso tienes que reinstalarla, entrar con usuario y clave, pasar validación biométrica u OTP por correo y reactivar el Token Digital en ese dispositivo. No verifiqué el procedimiento exacto de reinstalación.
- **Ventaja estructural de Pibank para este modelo de amenaza:** no tiene tarjeta de débito ni efectivo, así que no le aplican el robo de tarjeta, la clonación ni el retiro en cajero. Toda la superficie de ataque está en la app y en las credenciales. Si la app está en un teléfono que nunca sale de casa, el escenario del "celular robado en la calle" desaparece.
- **Vector residual crítico: el correo electrónico.** La OTP para vincular un dispositivo nuevo o cambiar credenciales llega por correo. Si el celular de uso diario (el que se puede robar) tiene sesión abierta en ese correo, un ladrón podría intentar vincular un dispositivo nuevo. Le faltarían usuario y clave, y probablemente la biometría facial al activar el token. Conviene usar para Pibank un correo que no esté abierto en el celular diario, con 2FA.
- **Límites:** el cliente puede personalizar los límites con terceros desde la app. No verifiqué si se pueden bajar a cero. El tope de S/ 30.000 al día hacia terceros es el máximo que un atacante con acceso completo podría mover en un día si no se baja.
- **No afiliar la interoperabilidad** (envío a contacto por celular) ni registrar favoritos a terceros. Los favoritos se saltan el token.
- **Riesgo de producto nuevo:** el lanzamiento tiene un mes. El número de emergencia español en el Centro de Ayuda es señal de que la operación aún se está ajustando. Esto es inferencia.

### Gaps
- No pude leer las secciones de FAQ "Seguridad" y "App Pibank" (se cargan por JS). Pueden tener detalles de bloqueo, límites mínimos o reinstalación.
- No confirmé si el límite con terceros puede fijarse en S/ 0, ni si los favoritos funcionan desde un dispositivo afiliado sin Token Digital.
- No confirmé si Pibank participa en la línea 1820 de ASBANC. Es probable, porque Banco Pichincha es un banco del sistema, pero no está verificado.
- Pibank Perú no ofrece DPF a la fecha (solo la Cuenta Soles; dólares anunciado).

---

## 4. Cajas municipales, financieras, Alfin, BanBif, GNB, Pichincha: ¿DPF presencial en Lima? ¿Cancelación solo presencial? ¿Banca web con token sin app?

### Takeaway
Abrir un DPF en agencia es universal. El problema es que **cada vez más entidades permiten abrir y operar DPF desde la app o la banca web**, así que "lo abrí en ventanilla" no garantiza que solo se pueda cancelar en ventanilla. No encontré ninguna entidad que ofrezca explícitamente un "DPF solo ventanilla" como producto. Lo más parecido es tener el DPF en una entidad donde **nunca te afilias a la banca digital** ni recibes tarjeta de débito. Hay entidades donde la afiliación a la banca por internet exige ir a agencia (por ejemplo Caja Maynas). El token físico casi ha desaparecido en favor del token digital dentro de la app (GNB) o del SMS.

### Cited Findings
**Caja Arequipa**
- La página de DPF (consultada 29-oct-2026) dice: "Abre tu depósito **desde la app, la web o visitando tu agencia**". También dice "Puedes disponer de los intereses de tu cuenta a plazo fijo **por cualquier canal**" y, en la sección del DPF Creciente, "tendrás acceso a la **Tarjeta de Débito Visa** y a nuestra red de canales". El DPF Creciente permite retiros de hasta el 30 % del monto de apertura — [Caja Arequipa – Plazo Fijo](https://www.cajaarequipa.pe/personas/ahorros/plazo-fijo/) [DOC OFICIAL].
- FAQ de enero de 2024: el DPF se puede abrir en agencia, en la App ("Adquirir un Nuevo Producto") o en la Banca por Internet. Cancelación anticipada del DPF tradicional: antes de 30 días no paga rendimiento; entre 31 y 89 días paga la tasa de ahorro; después, la tasa del tramo inmediato anterior — [FAQ Productos Pasivos](https://www.cajaarequipa.pe/wp-content/uploads/2024/01/preguntas-frecuentes-ahorros-18-01-2024.pdf) [DOC OFICIAL, 2024].
- Contrato (Res. SBS 00790-2026):
  - Cl. 50: el cliente puede **habilitar o deshabilitar** en la tarjeta las compras POS, por internet y en el exterior, los retiros en cajeros y agentes y el **servicio PLIN**.
  - Cl. 66: lo mismo vale para las operaciones por canales.
  - Cl. 83: al vencimiento, el DPF se renueva o se cancela y los fondos se ponen a disposición del cliente.
  - El contrato **no** fija un canal exclusivo para cancelar el DPF.
  — [Contrato](https://www.cajaarequipa.pe/wp-content/uploads/2026/05/CONTRATO-DE-DEP%C3%93SITOS-Y-SERVICIOS-COMPLEMENTARIOS.pdf) [DOC OFICIAL].
- Además, la tarjeta de débito se entrega en agencia y ahí se elige qué cuenta queda autorizada para débitos; cambiar esa elección es "en forma personal en cualquiera de nuestras agencias" — [FAQ 2024](https://www.cajaarequipa.pe/wp-content/uploads/2024/01/preguntas-frecuentes-ahorros-18-01-2024.pdf) [DOC OFICIAL].

**Caja Trujillo**
- Con cuenta de ahorros previa, el DPF se puede abrir por la app Caja Trujillo Móvil y por Homebanking. Los DPF abiertos por esos canales "solo son de tipo 'al vencimiento'". La cancelación anticipada paga la tasa mínima de la cartilla — [Caja Trujillo – Plazo Fijo](https://www.cajatrujillo.com.pe/ahorros_pfijo_.html) [DOC OFICIAL].

**Caja Huancayo**
- Abrió el DPF digital en su web en julio de 2024 ("Apertura tu cuenta digital") — [Exitosa, 11-jul-2024](https://www.exitosanoticias.pe/caja-huancayo/atencion-caja-huancayo-anuncia-apertura-plazo-fijo-digital-n130588) [PRENSA].
- Perú21 tiene una nota titulada "Un retiro trabado en Caja Huancayo: un caso de abuso": clientes que intentaron usar su DPF en plena crisis y encontraron obstáculos para transferir el dinero — [Perú21](https://peru21.pe/economia/un-retiro-trabado-en-caja-huancayo-un-caso-de-abuso-noticia/) [SNIPPET; la página devolvió 403 y la fecha es desconocida].

**Caja Metropolitana de Lima** (ejemplo de DPF con condición presencial)
- La campaña DPF Soles de enero de 2026 es "válida únicamente en las agencias", y "No aplica para aperturas… desde el canal Banca por Internet y/o App Móvil". Si se cancela antes de tiempo, se pierde la tasa de campaña y se aplica el tarifario de cancelación anticipada de la red de agencias — [Campaña DPF Soles Enero 2026](https://www.cajametropolitana.com.pe/repositorioaps/0/0/jer/at-campanas/files/Campa%C3%B1a%20DPF%20SOLES%20ENERO%202026.pdf) [DOC OFICIAL].
- Un fragmento del buscador atribuye a Caja Metropolitana: "Para la cancelación de la cuenta Depósito a Plazo Fijo, el canal de atención es mediante la red de agencias a nivel nacional" — [Caja Metropolitana – Plazo Fijo](https://www.cajametropolitana.com.pe/principal/categoria/plazo-fijo/29/c-29) [SNIPPET, no verificado en el documento].

**Caja Maynas** (ejemplo de banca web con afiliación presencial)
- Para usar Caja Maynas Online "previamente deberá **afiliarse de manera presencial** en cualquiera de nuestras Agencias", y el canal está dirigido a clientes con Tarjeta de Débito Visa. Las transferencias entre cuentas por banca web no alcanzan a las cuentas de Depósito a Plazo Fijo — [Caja Maynas – Banca por Internet](https://www.cajamaynas.pe/banca-por-internet/) [DOC OFICIAL; lo de que las transferencias no alcanzan a DPF viene del fragmento del buscador].

**Bancos: autenticación en banca web**
- **Banco GNB**: el Token Digital está integrado en la app móvil (6 dígitos, se renueva cada 35 segundos). Quien tenga Token Físico puede cambiarlo por el digital desde la Banca Móvil, y **al activar el digital se deshabilita el físico** — [GNB – Token digital](https://www.bancognb.com.pe/inicio/canales/canales-digitales/Token-digital) [SNIPPET].
- **BanBif**: confirma operaciones con **SMS Token** y con una Tarjeta Virtual de Coordenadas que se activa en la banca por internet — [BanBif – Banca por Internet](https://m.banbif.com.pe/bancaporinternet) [SNIPPET].
- **Banco de la Nación**: tiene token físico que cambia cada minuto. La página puede estar desactualizada — [BN – Clave Token](https://www.bn.com.pe/clientes/banca-internet/token.asp) [SNIPPET].
- **Banco Pichincha (banca tradicional)**: la antigua "Cuenta de Ahorros Efectivo", orientada a ventanilla, figura como no vigente; las alternativas son la Cuenta Preferente y el DPF. La cartilla unificada (octubre de 2025) lista como canales las ventanillas, los cajeros Global Net y los agentes — [Pichincha – Cuenta Efectivo](https://www.pichincha.pe/personas/productos-y-servicios/ahorros-y-depositos/cuentas-de-ahorro/efectivo); [Cartilla unificada](https://www.pichincha.pe/sites/default/files/2025-10/CARTILLA%20DE%20INFORMACION%20UNIFICADA%20VF.pdf) [SNIPPET].
- **Alfin**: no encontré información sobre su token o su banca web. Su caso INDECOPI incluye que el banco **cambió el correo vinculado a la banca móvil sin autorización** del cliente (ver pregunta 2).

### Inferences
- **El DPF en sí no es transferible directamente.** Para mover el dinero hay que cancelarlo y abonarlo en una cuenta de ahorros. La protección real depende de si la entidad permite **cancelar o liquidar el DPF por app o web**. En Caja Arequipa, Trujillo y Huancayo los DPF ya se abren por canales digitales, y es razonable esperar que en algún grado también se gestionen por ellos. No confirmé la cancelación digital en ninguna de las tres.
- La configuración más robusta es una entidad donde: (a) **no tienes usuario de banca digital creado**; (b) **no tienes tarjeta de débito**, porque en muchas entidades la tarjeta más su PIN es la llave para darse de alta solo en la app; y (c) el DPF está a nombre tuyo, con intereses al vencimiento. Si no existe usuario digital, un ladrón con tu celular no tiene nada que abrir. Le quedaría intentar el alta remota con tu DNI y tu SIM, que es más difícil sin tarjeta.
- Pedir en agencia **por escrito** que la cancelación del DPF solo se atienda en ventanilla, con DNI físico y huella biométrica. No vi este mecanismo en ningún documento: el contrato de Caja Arequipa no lo contempla. Hay que preguntarlo, sin dar por hecho que existe.
- El caso Caja Huancayo (Perú21) y el condicionamiento a la agencia de Caja Metropolitana muestran el costo opuesto: **cuanto más "bloqueado" está el DPF, más fricción tiene la liquidez de emergencia**.

### Gaps
- No verifiqué en documentos los canales de cancelación del DPF en Caja Huancayo, Piura, Cusco, Ica, Trujillo (más allá de la apertura), Alfin, BanBif, GNB ni Pichincha. Hay que pedir la cartilla y el contrato de DPF de cada una o preguntarlo directamente.
- No verifiqué cuántas agencias tiene cada caja de provincia en Lima Metropolitana.
- No encontré ningún banco o caja peruana que hoy entregue **token físico nuevo** a clientes nuevos. GNB lo está retirando a favor del digital.

---

## 5. ¿Qué configuraciones de producto existen para blindar el dinero contra el robo remoto?

### Takeaway
Hay palancas verificadas: activar o desactivar funcionalidades de tarjeta y PLIN (contrato de Caja Arequipa), personalizar límites con terceros en la app (Pibank), no afiliar la interoperabilidad (Pibank), tener una cuenta sin tarjeta de débito (Pibank lo es por diseño) y bloquear rápido por la línea 1820. No encontré ninguna norma SBS que obligue a ofrecer "canales digitales apagados" o límites en cero a voluntad del cliente, ni un producto que se anuncie como "retiro solo por ventanilla". La palanca más fuerte es estructural: **no crear la llave digital** (ni usuario web/app ni tarjeta) en la entidad donde vive la reserva.

### Cited Findings
- **Activar o desactivar funcionalidades:** en Caja Arequipa, el cliente puede "habilitar o deshabilitar… (i) compras presenciales… (ii) compras por internet, (iii) compras en el exterior, (iv) retiros de efectivo en cajeros automáticos o agentes corresponsales, (v) servicio PLIN" — [Contrato Caja Arequipa, cl. 50](https://www.cajaarequipa.pe/wp-content/uploads/2026/05/CONTRATO-DE-DEP%C3%93SITOS-Y-SERVICIOS-COMPLEMENTARIOS.pdf) [DOC OFICIAL]. La FAQ recomienda activar las compras por internet solo para cada compra y desactivarlas después — [FAQ 2024](https://www.cajaarequipa.pe/wp-content/uploads/2024/01/preguntas-frecuentes-ahorros-18-01-2024.pdf) [DOC OFICIAL].
- **Autenticación reforzada para cambiar límites:** en Caja Arequipa, registrar un beneficiario de confianza o modificar límites y condiciones puede requerir autenticación reforzada, es decir, factores de categorías distintas — [Contrato, cl. 66](https://www.cajaarequipa.pe/wp-content/uploads/2026/05/CONTRATO-DE-DEP%C3%93SITOS-Y-SERVICIOS-COMPLEMENTARIOS.pdf) [DOC OFICIAL].
- **Límites personalizables:** el App Pibank permite "Personalizar límites de operaciones con terceros y con otras entidades". Por encima de S/ 30.000 al día solo hay transferencias diferidas a cuentas propias; por encima de S/ 240.000, videollamada — [T&C App Pibank](https://prdpistdoceastus2.blob.core.windows.net/documentos1/ONBOARDING/TerminosCondiciones_App.pdf) [DOC OFICIAL].
- **Interoperabilidad opcional:** en Pibank, el envío o recepción por número de celular exige afiliación previa — [T&C App Pibank](https://prdpistdoceastus2.blob.core.windows.net/documentos1/ONBOARDING/TerminosCondiciones_App.pdf) [DOC OFICIAL].
- **Sin tarjeta de débito:** la Cuenta Soles Pibank "no tiene asociada tarjeta débito ni pagos" — [Cuenta Soles Pibank](https://pibank.pe/cuenta-soles-pibank/) [DOC OFICIAL].
- **Afiliación presencial a la banca web:** Caja Maynas solo afilia en agencia — [Caja Maynas](https://www.cajamaynas.pe/banca-por-internet/) [DOC OFICIAL].
- **Bloqueo rápido:** la línea 1820 de ASBANC enruta a la entidad y bloquea tarjetas y usuarios digitales. El bloqueo toma unos 3,5 minutos en promedio — [Gestión, 17-sep-2026](https://gestion.pe/tu-dinero/fraude-digital-amenaza-cuentas-de-ahorro-por-s-257-millones-por-donde-atacan-delincuentes-noticia/); [El Comercio, 18-jun-2025](https://elcomercio.pe/tecnologia/actualidad/robo-de-celular-como-evitar-que-saquen-dinero-de-tus-cuentas-bancarias-o-pidan-prestamos-a-tu-nombre-noticia/) [PRENSA].
- **Recomendaciones de ASBANC:** claves distintas para las apps bancarias y el correo, alertas activadas, solo canales oficiales y todos los factores de autenticación disponibles — [Gestión, 17-sep-2026](https://gestion.pe/tu-dinero/fraude-digital-amenaza-cuentas-de-ahorro-por-s-257-millones-por-donde-atacan-delincuentes-noticia/) [PRENSA].
- **Contraseñas guardadas:** no guardar claves de apps financieras en notas, apps o chats — [El Comercio, 18-jun-2025](https://elcomercio.pe/tecnologia/actualidad/robo-de-celular-como-evitar-que-saquen-dinero-de-tus-cuentas-bancarias-o-pidan-prestamos-a-tu-nombre-noticia/) [PRENSA].
- **SIM:** ante una pérdida repentina de señal, sospechar SIM swap y pedir la reposición para desactivar el chip en manos de terceros. El operador debe suspender el servicio de inmediato si se reclama una reposición no reconocida — [DPL News](https://dplnews.com/peru-osiptel-publica-norma-para-prevenir-contrataciones-y-reposiciones-no-solicitadas-de-chips/) [SNIPPET].

### Inferences
Checklist de palancas, con su estado de verificación:
- **Celular diario sin apps bancarias, sin billeteras con acceso a la reserva y sin sesión del correo que recibe las OTP bancarias** (verificado como vector en los T&C de Pibank: la OTP de vinculación llega por correo).
- **Yape/Plin solo en una cuenta-bolsillo aparte con saldo bajo**, nunca la cuenta de la reserva. Lo respalda que ASBANC señale que las cuentas vinculadas a billeteras son las más atacadas.
- **Sin tarjeta de débito en la entidad de la reserva**, o con todas sus funcionalidades deshabilitadas (cl. 50 de Caja Arequipa).
- **Límite con terceros al mínimo** en la app (Pibank). No verifiqué que admita cero.
- **No afiliar la interoperabilidad por celular** ni crear favoritos a terceros (Pibank).
- **PIN de SIM** y bloqueo fuerte del teléfono (contraseña alfanumérica, no un patrón). Es práctica estándar; no lo verifiqué en fuentes peruanas.
- **Teléfono dedicado en casa** para la app bancaria: anula el robo callejero, pero no el robo domiciliario ni la ingeniería social.
- **"Retiro solo por ventanilla" / "DPF sin canales digitales"**: no lo encontré como producto. Hay que pedirlo y conseguir confirmación escrita.
- **Token físico**: prácticamente en extinción en la banca peruana. No contar con él.

### Gaps
- No verifiqué si alguna entidad permite "deshabilitar todos los canales digitales" de una cuenta específica. Por la cl. 66 de Caja Arequipa (las operaciones por canales se pueden habilitar o deshabilitar) parece posible por operación, pero no sé si por cuenta completa.
- No encontré ninguna norma SBS que obligue a permitir que el cliente fije límites en cero.

---

## 6. Recomendación: 2-3 configuraciones concretas con sus trade-offs

### Takeaway
Para una reserva de seguridad, la combinación más defendible es **híbrida**: un tramo pequeño y líquido en Pibank, con la app solo en un teléfono dedicado que no sale de casa, y el grueso en un **DPF abierto en agencia en una entidad donde no exista usuario digital ni tarjeta**. "Pibank vía web sin app" **no existe** como opción (ver pregunta 3).

### Cited Findings
- Pibank es app-only, tiene el Token Digital en un único dispositivo, sin tarjeta ni agencias, y permite hasta 3 dispositivos afiliados — [Contrato Pibank](https://prdpistdoceastus2.blob.core.windows.net/documentos1/ONBOARDING/Contrato_CuentaSolesPibank.pdf); [T&C App](https://prdpistdoceastus2.blob.core.windows.net/documentos1/ONBOARDING/TerminosCondiciones_App.pdf) [DOC OFICIAL].
- Hay DPF en agencia en todas las entidades revisadas, y en algunas la tasa de campaña solo vale en agencia (Caja Metropolitana, enero de 2026) — [Campaña Caja Metropolitana](https://www.cajametropolitana.com.pe/repositorioaps/0/0/jer/at-campanas/files/Campa%C3%B1a%20DPF%20SOLES%20ENERO%202026.pdf) [DOC OFICIAL].
- Penalidad por cancelación anticipada (ejemplo de Caja Arequipa): antes de 30 días, sin rendimiento; entre 31 y 89 días, tasa de ahorro — [FAQ Caja Arequipa](https://www.cajaarequipa.pe/wp-content/uploads/2024/01/preguntas-frecuentes-ahorros-18-01-2024.pdf) [DOC OFICIAL].

### Inferences

**Setup A: "Pibank en teléfono dedicado de casa" (reserva líquida)**
- Cómo:
  - Celular viejo con Android o iOS actualizado, bloqueo fuerte y solo la app Pibank con Token Digital. El token solo puede estar en un dispositivo.
  - Nunca sale de casa. El celular diario no tiene la app.
  - El correo registrado en Pibank no tiene sesión abierta en el celular diario y tiene su propio 2FA.
  - Límite con terceros al mínimo, sin interoperabilidad por celular y sin favoritos a terceros. Única salida habitual: transferencia a una cuenta propia en otro banco.
  - Anotar el 0-800-71626 y la línea 1820, no el +34 de la web.
- Seguridad: alta frente al robo callejero. Media frente a la ingeniería social (si te convencen por teléfono de autorizar algo). Media-baja frente al robo en casa (por eso el bloqueo fuerte).
- Liquidez: alta (transferencia inmediata a cuenta propia, 24/7) siempre que estés en casa.
- Comodidad: media; no puedes operar fuera de casa.
- Riesgos propios:
  - Producto lanzado hace un mes.
  - Sin canal presencial si la app falla, salvo la contingencia por llamada o videollamada, que solo transfiere a cuentas propias.
  - Si el teléfono dedicado se daña, hay que revincular otro dispositivo (OTP por correo más validación de identidad).
  - Tope de FSD: lo cubren otros investigadores.

**Setup B: "DPF en agencia en entidad sin llave digital" (reserva bloqueada)**
- Cómo:
  - Abrir el DPF en una agencia en Lima de una entidad donde no tengas ninguna otra relación. No crear usuario de app ni de banca web. No aceptar tarjeta de débito, o, si es obligatoria, deshabilitar todas sus funcionalidades (como en la cl. 50 de Caja Arequipa).
  - Intereses al vencimiento.
  - Pedir por escrito: cómo se cancela, si existe la opción de cancelación solo presencial con DNI y biometría, y a qué cuenta se abona al vencimiento (idealmente renovación automática o abono en una cuenta tuya de otro banco).
  - Elegir una entidad con agencia cerca en Lima.
- Seguridad: la más alta frente al robo remoto, porque no hay nada que abrir desde un celular. El riesgo residual es la suplantación en agencia, que la cl. 55-e de Caja Arequipa pone a cargo de la entidad, y que alguien logre darte de alta en la app a distancia (más difícil sin tarjeta; no verificado).
- Liquidez: baja. Hay que ir a la agencia, se paga penalidad por cancelación anticipada y el retiro puede tener fricciones (caso Perú21/Caja Huancayo, no verificado). Recibir el dinero en efectivo crea riesgo físico; es mejor pedir transferencia a una cuenta propia.
- Comodidad: baja. Además, algunas cajas de provincia tienen pocas agencias en Lima (no verificado por entidad).

**Setup C (recomendado): híbrido A + B**
- Cómo:
  - Tramo de liquidez de emergencia (por ejemplo 1-3 meses de gastos) en el Setup A.
  - El grueso en uno o varios DPF del Setup B, escalonados por vencimiento para que siempre haya uno venciendo pronto (ladder) y así no pagar penalidad.
  - Yape/Plin en una cuenta-bolsillo separada con saldo bajo en el celular diario.
- Trade-off: combina disponibilidad inmediata (A) con un grueso que no se puede vaciar remotamente (B). Cuesta algo de gestión (renovaciones, visitas a agencia) y quizá una tasa algo menor en el DPF que en la cuenta digital de Pibank. Comparar tasas queda fuera de este alcance.

**Variante descartada: "Pibank vía web sin app".** No es posible: la web solo sirve para el registro y para cerrar la cuenta con saldo cero; operar exige la app y el Token Digital (verificado en el contrato y los T&C).

### Gaps
- Falta confirmar en cada entidad candidata a DPF: (i) si el DPF se puede cancelar o liquidar por app o web; (ii) si se puede pedir la cancelación solo presencial; (iii) si se puede tener DPF sin tarjeta de débito y sin usuario digital; (iv) agencias en Lima. Lo más eficiente es pedir en agencia la cartilla y el contrato de DPF y preguntar estos cuatro puntos.
- Falta confirmar en Pibank: el límite mínimo con terceros, el procedimiento exacto de revinculación si se pierde el teléfono dedicado y el contenido de las FAQ de Seguridad y App.
