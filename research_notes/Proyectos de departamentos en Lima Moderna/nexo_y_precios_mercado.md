# Feria Nexo Inmobiliario (noviembre 2026) y precios de mercado de departamentos nuevos de 2 dormitorios en Lima Moderna

Fecha de corte: 12-nov-2026 (jueves). Notas en español. Convenciones:
- **Precio de lista / "desde"**: el que publica el portal o la inmobiliaria.
- **Precio feria / promo**: descuento o beneficio exclusivo de la feria.
- **Precio de oferta (BCRP)**: mediana de los precios pedidos en avisos de departamentos en venta. Mezcla unidades nuevas y usadas; no son precios de cierre.
- **[NV]** = no verificado en la fuente primaria (sale solo de un snippet de búsqueda o de un agregador).
- **Archivos descargados** (datos no confiables, leídos con `python -I`): `D:/PROYECTOS/FINANZAS/research_notes/Proyectos de departamentos en Lima Moderna/raw/nexo_mercado/`. Ahí están `feria_inmobiliaria.html`, `ferianexo.html` (idéntico al anterior), `venta_<distrito>.html` (6 archivos), `bcrp_mercado_inmobiliario_trim.html`, `bcrp_api_A.json` (PER) y `bcrp_api_B.json` (US$/m²).

---

## 1. Datos prácticos de la feria: fechas, sede, horario, entrada, modalidad y organizador

### Takeaway
La Feria Nexo Inmobiliario 2026 **empieza hoy**. Va del jueves 12 al domingo 15 de noviembre de 2026, de 11:00 a 21:00, en la Explanada de la Costa Verde (Magdalena del Mar). Es presencial y el ingreso es gratuito. La organiza **CODIP** (Confederación de Desarrolladores Inmobiliarios del Perú), el gremio que nació en 2025 de la fusión de **ASEI** con ADI. ASEI ya no es la marca que figura como organizadora.

### Cited Findings
- La landing oficial dice "Feria Inmobiliaria 2026", "12, 13, 14 y 15 de Noviembre", "Ingreso gratuito", "Explanada de la Costa Verde, Magdalena", "11am a 9pm" y "de 11:00 am. a 9:00 pm." (página leída el 12-nov-2026) — [Nexo – Feria Inmobiliaria](https://nexoinmobiliario.pe/feria-inmobiliaria)
- Organizador, según la misma FAQ: "La Feria Nexo Inmobiliario es organizada por la Confederación de Desarrolladores Inmobiliarios del Perú (CODIP) que reúne durante cuatro días, a más de 180 inmobiliarias […]. Encontrarás más de 30,000 opciones entre departamentos, casas y lotes" — [Nexo – Feria Inmobiliaria](https://nexoinmobiliario.pe/feria-inmobiliaria)
- La nota oficial del blog (30-oct-2026) confirma las fechas y lo demás: "Del 12 al 15 de noviembre", de 11:00 a. m. a 9:00 p. m., Explanada de la Costa Verde, más de 180 participantes y más de 30 mil opciones — [Blog Nexo, 30-oct-2026](https://nexoinmobiliario.pe/blog/feria-nexo-noviembre-2026/)
- Infobae (10-nov-2026) también la atribuye a CODIP, del 12 al 15 de noviembre en la Explanada de la Costa Verde de Magdalena del Mar — [Infobae, 10-nov-2026](https://www.infobae.com/peru/2026/11/10/los-departamentos-de-entre-40-y-60-m-concentraron-el-39-de-las-ventas-en-lima/)
- ASEI y ADI se fusionaron y formaron CODIP. Gestión lo publicó el 30-abr-2025. ASEI representaba ~85% de la oferta inmobiliaria formal de Lima. Preside CODIP José Espantoso [NV: dato del resumen de búsqueda] — [ProActivo](https://proactivo.com.pe/asei-y-adi-se-unen-para-crear-la-confederacion-de-desarrolladores-inmobiliarios-del-peru/)
- El portal sigue marcando la membresía antigua. Cada proyecto del buscador lleva el campo `socio_asei`, y 140 de los 144 proyectos que muestreé en los 6 distritos tienen `socio_asei=1`. El texto de autorización de datos del portal sigue nombrando a la "Asociación de Empresas Inmobiliarias (ASEI)" — fuente: `venta_<distrito>.html`, descargado de [nexoinmobiliario.pe/venta-de-inmuebles/jesus-maria](https://nexoinmobiliario.pe/venta-de-inmuebles/jesus-maria) el 12-nov-2026
- Hay buses de acercamiento gratuitos del 12 al 15-nov, de 10:00 a 20:00, que terminan antes que la feria. Paraderos: Open Plaza (Surquillo), Plaza San Miguel, "Javier Prado" (Av. Paseo de la República 2500, Lince) y "Jesús María" (Av. Brasil 2260, Pueblo Libre). La landing dice por error "jueves 12 a domingo 16", pero el domingo es el 15 — [Nexo – Feria Inmobiliaria](https://nexoinmobiliario.pe/feria-inmobiliaria); [Blog Nexo, 30-oct-2026](https://nexoinmobiliario.pe/blog/feria-nexo-noviembre-2026/)
- El mapa embebido de la sede usa el plus code "WW2G+8J4, San Miguel 15076". La sede está en el borde Magdalena/San Miguel de la Costa Verde — `feria_inmobiliaria.html` ([fuente](https://nexoinmobiliario.pe/feria-inmobiliaria))
- La modalidad es presencial: la FAQ habla de "conocer, comparar y conversar directamente con asesores", y la feria tiene un plano de stands ("Ver plano"). No encontré una edición virtual paralela para Lima. En paralelo existe una "Feria Nexo Arequipa" (código de campaña `Feria_Nexo_Arequipa_Noviembre_26`) — [Nexo – Feria Inmobiliaria](https://nexoinmobiliario.pe/feria-inmobiliaria)
- Las fuentes se contradicen en algunos datos:
  - Un TikTok de @nexoinmobiliario.pe habla del 13–16 de noviembre en "Arena 1" — [TikTok Nexo](https://www.tiktok.com/@nexoinmobiliario.pe) [NV].
  - Una guía del blog menciona el "Hotel Los Delfines" — [Blog Nexo – Ferias 2026](https://nexoinmobiliario.pe/blog/ferias-nexo-inmobiliario-2026/) [NV: resumen de búsqueda].
  - La landing oficial y la nota del 30-oct-2026 dicen Costa Verde, 12–15-nov.
- Existe un video "FERIA NEXO INMOBILIARIO 2025 - DOMINGO 16 DE NOVIEMBRE", es decir, la edición 2025 terminó el 16-nov-2025 — [YouTube](https://www.youtube.com/watch?v=_wYITKoPF2E)

### Inferences
- Lo más probable es que el TikTok del "13–16 de noviembre" corresponda a la edición 2025, que terminó el domingo 16-nov-2025. Para 2026, las fuentes oficiales y fechadas (landing y nota del 30-oct-2026) coinciden en 12–15-nov en la Costa Verde.
- Hoy es el día de apertura. Quedan 4 días: jueves 12, viernes 13, sábado 14 y domingo 15.
- Si el comprador quiere más espacio para negociar, conviene ir entre semana (jueves o viernes): el fin de semana suele haber más público. Esto es una inferencia general sin fuente.

### Gaps
- No encontré la dirección postal exacta ni el número de stands.
- No encontré si hay estacionamiento en la sede.
- No encontré un comunicado de CODIP con la cifra oficial de expositores. La landing muestra +122 logos, pero su texto dice "más de 180 inmobiliarias".

---

## 2. Inmobiliarias y proyectos participantes en los 6 distritos y filtros del portal

### Takeaway
La landing oficial lista **unos 122 desarrolladores** y cuenta **256 proyectos en feria** en los seis distritos: San Miguel 66, Jesús María 52, Magdalena 42, Pueblo Libre 33, Lince 32 y Surquillo 31. El buscador de Nexo **sí** filtra por distrito, dormitorios (mín./máx.), precio, área, baños, estacionamientos, banco financiador y **etapa** (En planos / En construcción / Entrega inmediata). También tiene un interruptor para ver solo proyectos de la feria. Abajo están los proyectos con 2D en su rango: salen de la primera página del buscador (24 proyectos por distrito).

### Cited Findings
- Proyectos en feria por distrito, según la landing (12-nov-2026): Santiago de Surco 76, Miraflores 71, **San Miguel 66, Jesús María 52, Magdalena del Mar 42**, Cercado 41, San Isidro 35, **Pueblo Libre 33**, Chorrillos 32, **Lince 32, Surquillo 31**, La Victoria 24, San Borja 18, Breña 13, Barranco 11. La misma página dice "+610 proyectos" y "+300 proyectos" en lugares distintos — [Nexo – Feria Inmobiliaria](https://nexoinmobiliario.pe/feria-inmobiliaria)
- Desarrolladores listados (+122), entre ellos: Ciudaris, Edifica, Actual, Madrid, Albamar, Invent, Cygnus, Imagina, Cosapi, Evergran, Lugano, Inhouse, Tribeca, V&V, Aster Homes, Grupo Lar, Sembra, Gratto, San Charbel, Edifikarte, Vitain, Grupo MG, Conforta, Vive+, Tale, GDC, Abril, Paz, Urbana Perú, Grupo T&C, Casaideal, Quatro, Beca, La Muralla, Ter, IFI, Los Portales, Vienna, Grupo Sol, Avenir, Tempus, Libre, My Home, Grupo Caral, Eficaxx, Redbay, Inarco, Grupo Binda, Ortiz, Pionero, Make, Senda, Andiamo, Verdant, Prospera, Granadero, Arteco, Maxx, Multiurbe, Balance, Lima Metro Cuadrado, Oled, Triada, Morada, Franca, Infinity, Maas, DKasa, Kallpa, Padova, Brocksa, GHS, CP Building, HL Desarrollos, Urbalima, Initalia, Vidarq, Cantabria, Decal, Beeyond, Taurus, Efron, AMMA, RB, Fundamenta, 2K, Domun, NOI, Cádiz, Procity, Vivans, Tectónica, Checor, Paqari, MYE y Anida — [Nexo – Feria Inmobiliaria](https://nexoinmobiliario.pe/feria-inmobiliaria)
- Filtros del buscador, según el HTML de `nexoinmobiliario.pe/venta-de-inmuebles/<distrito>` (12-nov-2026):
  - El objeto `pagination_filters` tiene `feria_nexo_filtrado`, `property_type_id`, `price_min/price_max`, `moneda`, `etapa`, `ids_ubigeo` (distrito), `area_min/area_max`, `room_min/room_max` (dormitorios), `banio_*`, `parking_*`, `bancos` y `areas_comunes`.
  - Etiquetas de etapa: value 1 = "En planos", 2 = "En construcción", 3 = "Entrega inmediata".
  - Fuente: [Nexo – Jesús María](https://nexoinmobiliario.pe/venta-de-inmuebles/jesus-maria); [Lince](https://nexoinmobiliario.pe/venta-de-inmuebles/lince); [San Miguel](https://nexoinmobiliario.pe/venta-de-inmuebles/san-miguel); [Pueblo Libre](https://nexoinmobiliario.pe/venta-de-inmuebles/pueblo-libre); [Magdalena](https://nexoinmobiliario.pe/venta-de-inmuebles/magdalena-del-mar); [Surquillo](https://nexoinmobiliario.pe/venta-de-inmuebles/surquillo)
- Proyectos totales de departamentos en el buscador (`totalProyectos`, 12-nov-2026): Jesús María 69, San Miguel 71, Magdalena 48, Pueblo Libre 46, Lince 43, Surquillo 36. En total son 313; 256 de ellos están en feria según la landing — mismas URLs.
- Muestra que extraje: la primera página de cada distrito, 24 proyectos × 6 = **144 proyectos** (46% del universo). La página siguiente se carga por AJAX (`home/search/getProjectsPagination`), que respondió 403 a mis consultas. **Sesgo posible**: el orden por defecto (`principal_order_general`) parece priorizar a los proyectos destacados o patrocinados.
  - De los 144 proyectos, 127 tienen `visibility_ferianexo=1`, es decir, están en la feria.
  - 68 tienen el campo `tiene_promo_fn` con un valor. Lo interpreto como "tiene promoción Feria Nexo" (inferencia, no está documentado).
- Ejemplo de precio de lista frente al precio del portal:
  - Ciudaris anuncia **Mondrian (Jesús María) "desde S/ 411,000, 54 m²"** y Tuliv (Lince, en construcción) desde S/ 351,000, 40 m² — [Ciudaris](https://www.ciudaris.com/venta-departamentos/) [NV: resumen de búsqueda; fecha sin confirmar].
  - El buscador de Nexo muestra Mondrian **desde S/ 386,000, 54 m²** (12-nov-2026), con `tiene_promo_fn` marcado — [Nexo – Mondrian](https://nexoinmobiliario.pe/proyecto/4262-mondrian)
  - La diferencia es de S/ 25,000 (−6%). Puede ser descuento de feria o actualización de precio; no está verificado.

### Proyectos con 2 dormitorios en su rango (buscador Nexo, 1.ª página, 12-nov-2026)
Cómo leer las columnas:
- "Precio desde" y "Precio máx" son `val_price1`/`val_price2` del JSON del portal, precios de lista publicados. El portal no aclara si el "desde" ya incluye el descuento de feria.
- "S/ m² (desde)" = precio desde ÷ área mínima. Es el precio por m² de la unidad más chica, normalmente un 1D o el 2D más pequeño, y por eso sobreestima algo el S/m² de un 2D.
- "Feria" = `visibility_ferianexo`. "Promo FN" = `tiene_promo_fn` no nulo (interpretación propia).
- Fuente de todas las filas: los archivos `venta_<distrito>.html` (URLs arriba). Cada proyecto lleva el enlace a su ficha.

#### Jesús María (24 proyectos con 2D en su rango, de 24 en la 1.ª página)

| Proyecto | Inmobiliaria | Dirección | Etapa | Dorm. | Área m² | Precio desde S/ | Precio máx S/ | S/ m² (desde) | Feria | Promo FN |
|---|---|---|---|---|---|---|---|---|---|---|
| [ALLURE - JESÚS MARÍA](https://nexoinmobiliario.pe/proyecto/3899-allure-jesus-maria) | GRUPO MG | Av. Húsares de Junín Nº 661 | Planos | 1–2 | 40–58 | 266,580 | 416,480 | 6,664 | sí | no |
| [Eucalipto](https://nexoinmobiliario.pe/proyecto/3942-eucalipto) | ABRIL GRUPO INMOBILIARIO | Av. Brasil 1857, Jesús María | Constr. | 1–3 | 36–70 | 246,090 | 459,969 | 6,748 | sí | sí |
| [Torre Nápoles](https://nexoinmobiliario.pe/proyecto/3900-torre-napoles) | Cygnus Grupo Inmobiliario | Av. 28 De Julio 232 | Planos | 1–3 | 35–69 | 234,572 | 453,168 | 6,783 | sí | sí |
| [Union Sq Park](https://nexoinmobiliario.pe/proyecto/4327-union-sq-park) | TRIBECA INMOBILIARIA | Av. Horacio Urteaga 468 | Planos | 2–3 | 43–71 | 294,136 | 656,767 | 6,861 | sí | no |
| [Bugambilias](https://nexoinmobiliario.pe/proyecto/3784-bugambilias) | ABRIL GRUPO INMOBILIARIO | Av. Brasil 1007, Jesús María | Constr. | 1–3 | 32–75 | 220,348 | 533,632 | 6,920 | sí | sí |
| [Ímpettu](https://nexoinmobiliario.pe/proyecto/4068-impettu) | BARQUEROS INMOBILIARIA | Jiron Huamachuco 1664 | Planos | 1–4 | 42–148 | 294,486 | 1,100,092 | 7,022 | no | no |
| [MONDRIAN](https://nexoinmobiliario.pe/proyecto/4262-mondrian) | CIUDARIS | Av. Talara 726 Jesús María | Planos | 1–3 | 54–154 | 386,000 | 861,000 | 7,089 | sí | sí |
| [Allegra Living](https://nexoinmobiliario.pe/proyecto/3749-allegra-living) | BARQUEROS INMOBILIARIA | Jirón Río de Janeiro 257, Jesús María | Constr. | 1–3 | 41–75 | 297,452 | 640,000 | 7,337 | no | no |
| [MONTECARLO](https://nexoinmobiliario.pe/proyecto/4039-montecarlo) | ABRIL GRUPO INMOBILIARIO | Av. San Felipe 871, Jesús María | Planos | 1–3 | 40–70 | 295,200 | 526,500 | 7,374 | sí | sí |
| [Modena](https://nexoinmobiliario.pe/proyecto/3736-modena) | Cygnus Grupo Inmobiliario | Av. Olavegoya 1846 | Constr. | 1–3 | 40–125 | 298,730 | 1,052,938 | 7,465 | sí | sí |
| [Bugambilias - Bloque B](https://nexoinmobiliario.pe/proyecto/4260-bugambilias-bloque-b) | ABRIL GRUPO INMOBILIARIO | Av. Brasil 1007, Jesús María | Constr. | 1–3 | 33–90 | 251,530 | 601,205 | 7,511 | sí | sí |
| [Gran Manzano](https://nexoinmobiliario.pe/proyecto/3697-gran-manzano) | ABRIL GRUPO INMOBILIARIO | Av. San Felipe 1110, Jesús María | Constr. | 1–3 | 36–79 | 270,263 | 504,220 | 7,604 | sí | sí |
| [LLUMS FAMILY STYLE](https://nexoinmobiliario.pe/proyecto/4149-llums-family-style) | HL DESARROLLOS INMOBILIARIOS | Av. Cuba 667-687 y Av. Salaverry 1020  - 1034 | Constr. | 1–2 | 40–76 | 322,000 | 653,064 | 8,050 | sí | sí |
| [SÁENZ](https://nexoinmobiliario.pe/proyecto/4223-saenz) | LUGANO | Jirón Luis N. Saenz 555, Jesús María, Perú 555 | Planos | 1–4 | 40–166 | 322,500 | 1,339,280 | 8,062 | sí | no |
| [PRIME SANTA CRUZ](https://nexoinmobiliario.pe/proyecto/4065-prime-santa-cruz) | GRUPO SOL | Av. Gral. Sta. Cruz 721 | Constr. | 1–3 | 40–138 | 323,000 | 1,047,000 | 8,063 | sí | sí |
| [Cannelle](https://nexoinmobiliario.pe/proyecto/3472-cannelle) | ABRIL GRUPO INMOBILIARIO | Av de la Policía 603 | Inmediata | 1–2 | 47–66 | 382,500 | 506,700 | 8,152 | sí | sí |
| [Edificio Sialia](https://nexoinmobiliario.pe/proyecto/3325-edificio-sialia) | Cygnus Grupo Inmobiliario | Av. 6 de Agosto 1184, Jesús María | Constr. | 1–3 | 40–151 | 329,909 | 1,174,753 | 8,248 | sí | sí |
| [Olivo](https://nexoinmobiliario.pe/proyecto/3927-olivo) | ABRIL GRUPO INMOBILIARIO | Jr. Inca Ripac 134 | Constr. | 2–3 | 52–84 | 441,900 | 717,300 | 8,422 | sí | sí |
| [EL OLIVAR](https://nexoinmobiliario.pe/proyecto/3686-el-olivar) | LUGANO | Av. San Felipe N° 499 | Constr. | 1–3 | 54–122 | 464,000 | 980,500 | 8,551 | sí | no |
| [Arteco | DuMont](https://nexoinmobiliario.pe/proyecto/3312-arteco-dumont) | ARTECO | Av. República de Chile 675 | Constr. | 1–3 | 40–69 | 346,000 | 572,000 | 8,691 | sí | sí |
| [EDIFICIO BLEND](https://nexoinmobiliario.pe/proyecto/3362-edificio-blend) | LUGANO | AVENIDA HORACIO URTEAGA 1060 | Constr. | 1–3 | 40–73 | 355,000 | 641,700 | 8,875 | sí | no |
| [Matera](https://nexoinmobiliario.pe/proyecto/3859-matera) | Cygnus Grupo Inmobiliario | Inca Ripac 346 | Constr. | 1–3 | 36–141 | 328,291 | 1,119,043 | 9,041 | sí | sí |
| [Capadocia](https://nexoinmobiliario.pe/proyecto/3690-capadocia) | Cygnus Grupo Inmobiliario | Jr. Luis N. Saenz 445 | Constr. | 1–3 | 31–153 | 305,233 | 1,138,143 | 9,799 | sí | sí |
| [LUNA](https://nexoinmobiliario.pe/proyecto/3503-luna) | LUGANO | Jirón Inca Ripac 350 - 372 | Constr. | 2–3 | 54–87 | 534,000 | 896,000 | 9,889 | sí | no |

#### San Miguel (23 proyectos con 2D en su rango, de 24 en la 1.ª página)

| Proyecto | Inmobiliaria | Dirección | Etapa | Dorm. | Área m² | Precio desde S/ | Precio máx S/ | S/ m² (desde) | Feria | Promo FN |
|---|---|---|---|---|---|---|---|---|---|---|
| [Costa Living](https://nexoinmobiliario.pe/proyecto/4438-costa-living) | Colindante | Av. La Paz 2607 | Planos | 1–3 | 46–76 | 213,000 | 386,000 | 4,658 | sí | no |
| [ALBORADA - SAN MIGUEL](https://nexoinmobiliario.pe/proyecto/2115-alborada-san-miguel) | GRUPO MG | Av. La Paz 1150 | Inmediata | 2–3 | 58–97 | 337,800 | 495,300 | 5,824 | sí | no |
| [ALBORADA III - SAN MIGUEL](https://nexoinmobiliario.pe/proyecto/3342-alborada-iii-san-miguel) | GRUPO MG | Av. La paz 839 | Inmediata | 1–3 | 57–86 | 332,960 | 423,470 | 5,841 | sí | no |
| [ALBORADA II - SAN MIGUEL](https://nexoinmobiliario.pe/proyecto/2744-alborada-ii-san-miguel) | GRUPO MG | Av. La Paz 1147 | Inmediata | 1–3 | 57–95 | 335,850 | 461,540 | 5,872 | sí | no |
| [ESSENZA](https://nexoinmobiliario.pe/proyecto/4310-essenza) | GRUPO BINDA | Av. De los Patriotas 586,San Miguel | Planos | 2–3 | 45–94 | 272,192 | 513,200 | 6,035 | sí | sí |
| [Park Harrison](https://nexoinmobiliario.pe/proyecto/4291-park-harrison) | GDC INMOBILIARIA | Jorge castro harrison 451 | Planos | 1–3 | 43–89 | 268,366 | 579,383 | 6,205 | sí | no |
| [MAR DE PLATA II - SAN MIGUEL](https://nexoinmobiliario.pe/proyecto/1693-mar-de-plata-ii-san-miguel) | GRUPO MG | Avenida Universitaria 838 | Inmediata | 1–3 | 67–104 | 419,350 | 653,250 | 6,297 | sí | no |
| [Edificio New Limit](https://nexoinmobiliario.pe/proyecto/4002-edificio-new-limit) | VITAIN | Jr. San Martín 650 | Planos | 1–3 | 40–72 | 259,000 | 479,000 | 6,475 | sí | sí |
| [KAI](https://nexoinmobiliario.pe/proyecto/4197-kai) | REYNA INMOBILIARIA | Ca. Putumayo 129, San Miguel | Planos | 1–3 | 40–117 | 259,300 | 779,800 | 6,482 | sí | no |
| [Arteco | Beacon](https://nexoinmobiliario.pe/proyecto/4390-arteco-beacon) | ARTECO | Av La Marina 1305. Esquina con Unamuno. | Planos | 2–3 | 54–121 | 353,047 | 712,562 | 6,519 | sí | sí |
| [INSPIRIA](https://nexoinmobiliario.pe/proyecto/2438-inspiria) | URBALIMA | Av. Razuri 243 - 247 | Constr. | 2–3 | 50–78 | 325,000 | 499,000 | 6,533 | sí | sí |
| [Sauce Zen](https://nexoinmobiliario.pe/proyecto/3724-sauce-zen) | ABRIL GRUPO INMOBILIARIO | Calle Carlos Gonzales Candamo 224, San Miguel | Constr. | 1–3 | 35–72 | 231,182 | 470,034 | 6,613 | sí | sí |
| [Costanova](https://nexoinmobiliario.pe/proyecto/3892-costanova) | GRUPO T&C | Av. Costanera 1650 | Planos | 1–3 | 23–108 | 156,943 | 645,873 | 6,704 | sí | no |
| [Patio La Paz](https://nexoinmobiliario.pe/proyecto/2769-patio-la-paz) | PAZ | Av. La Paz 2551 | Inmediata | 1–3 | 40–78 | 277,000 | 515,000 | 6,887 | sí | no |
| [Madison Park](https://nexoinmobiliario.pe/proyecto/3854-madison-park) | TRIBECA INMOBILIARIA | C. Teniente Cesar Lopez Rojas 201, San Miguel | Constr. | 1–3 | 29–99 | 206,010 | 736,820 | 7,000 | sí | no |
| [Amalfi](https://nexoinmobiliario.pe/proyecto/2198-amalfi) | PAZ | Av. Costanera 2558 | Inmediata | 1–3 | 49–97 | 345,000 | 594,000 | 7,054 | sí | no |
| [Loto](https://nexoinmobiliario.pe/proyecto/3578-loto) | ABRIL GRUPO INMOBILIARIO | Av. La Marina 2600 | Constr. | 1–3 | 25–69 | 180,000 | 452,700 | 7,112 | sí | sí |
| [PATRIOTAS SAN MIGUEL](https://nexoinmobiliario.pe/proyecto/2894-patriotas-san-miguel) | PROYEC INMOBILIARIA | Av. Los Patriotas 305 | Inmediata | 2–3 | 53–67 | 381,210 | 481,896 | 7,147 | sí | no |
| [Marena](https://nexoinmobiliario.pe/proyecto/4188-marena) | PAZ | Jiron Fedrico Gallese 399 - San Miguel | Planos | 1–3 | 40–100 | 295,000 | 748,000 | 7,375 | sí | no |
| [Quatro | Supra Tower](https://nexoinmobiliario.pe/proyecto/3202-quatro-supra-tower) | QUATRO INMOBILIARIA | Avenida Los Patriotas 415 | Inmediata | 1–3 | 34–85 | 273,514 | 485,627 | 8,165 | sí | sí |
| [Edificio Incentric](https://nexoinmobiliario.pe/proyecto/3678-edificio-incentric) | VITAIN | Calle Carlos Gonzales Cándamo 212 | Constr. | 1–3 | 32–70 | 266,000 | 517,000 | 8,333 | sí | sí |
| [Edificio Cálamo](https://nexoinmobiliario.pe/proyecto/3510-edificio-calamo) | VITAIN | Jr. Crnel. Francisco Bolognesi 326 | Constr. | 1–3 | 28–66 | 248,000 | 521,000 | 8,782 | sí | sí |
| [OCEANIKA](https://nexoinmobiliario.pe/proyecto/3345-oceanika) | SAN CHARBEL EDIFICACIONES | Avenida Bertolloto 570. San Miguel | Constr. | 1–3 | 24–72 | 225,592 | 925,897 | 9,400 | sí | sí |

#### Lince (18 proyectos con 2D en su rango, de 24 en la 1.ª página)

| Proyecto | Inmobiliaria | Dirección | Etapa | Dorm. | Área m² | Precio desde S/ | Precio máx S/ | S/ m² (desde) | Feria | Promo FN |
|---|---|---|---|---|---|---|---|---|---|---|
| [ZENTRO](https://nexoinmobiliario.pe/proyecto/3384-zentro) | CENTRAL INMOBILIARIA | JR BARTOLOME HERRERA 250 LINCE | Inmediata | 1–3 | 62–141 | 444,500 | 886,400 | 7,174 | sí | sí |
| [Residencial Casanova](https://nexoinmobiliario.pe/proyecto/3045-residencial-casanova) | PALACE | Jirón Domingo Casanova 568, Lima 15046 | Inmediata | 2–3 | 69–77 | 514,270 | 612,650 | 7,471 | no | no |
| [Be Happy](https://nexoinmobiliario.pe/proyecto/4084-be-happy) | SAN CHARBEL EDIFICACIONES | Av. Arequipa 1711 | Planos | 1–3 | 40–67 | 307,818 | 471,216 | 7,642 | sí | sí |
| [Beli 465](https://nexoinmobiliario.pe/proyecto/3677-beli-465) | GRUPO SOL | Jr. Belisario Flores 465, Lince | Constr. | 2–3 | 66–143 | 512,000 | 1,004,000 | 7,726 | sí | sí |
| [LOMBARDIA](https://nexoinmobiliario.pe/proyecto/2393-lombardia) | TORATTO GRUPO INMOBILIARIO | Jr. Manuel Gómez N° 390 | Inmediata | 2–3 | 64–121 | 498,145 | 771,779 | 7,810 | no | no |
| [Aura](https://nexoinmobiliario.pe/proyecto/4130-aura) | VIENNA GRUPO INMOBILIARIO | Av. Arequipa 2083 | Planos | 1–3 | 40–72 | 319,200 | 549,300 | 7,964 | sí | no |
| [Cross](https://nexoinmobiliario.pe/proyecto/3392-cross) | GRANADERO INMOBILIARIA | Calle Las Lilas 104, Esquina con Av. Prolongación Iquitos 2301. | Constr. | 1–3 | 38–67 | 305,280 | 503,500 | 8,049 | sí | sí |
| [Bosque Real](https://nexoinmobiliario.pe/proyecto/4096-bosque-real) | ABRIL GRUPO INMOBILIARIO | Jr. Sinchi Roca 2637-2639, Lince | Constr. | 2–3 | 45–100 | 397,060 | 759,786 | 8,767 | sí | sí |
| [Park Orquídeas](https://nexoinmobiliario.pe/proyecto/3666-park-orquideas) | ACTUAL | Calle Los Geranios 208 Lince | Constr. | 1–2 | 39–60 | 339,800 | 673,300 | 8,824 | sí | no |
| [Los Lirios](https://nexoinmobiliario.pe/proyecto/3009-los-lirios) | CHECOR INMOBILIARIA | Av. Petit Thouars 1737 | Constr. | 1–2 | 26–56 | 230,000 | 420,000 | 8,833 | sí | sí |
| [MIDGO](https://nexoinmobiliario.pe/proyecto/3029-midgo) | COSAPI | av arequipa 1890 | Constr. | 1–2 | 36–67 | 324,456 | 454,940 | 8,963 | sí | no |
| [Mural Lince](https://nexoinmobiliario.pe/proyecto/3469-mural-lince) | GRUPO T&C | Av. Arequipa 1936, Lince | Constr. | 1–2 | 22–75 | 201,224 | 482,823 | 9,201 | sí | sí |
| [LIVORNO](https://nexoinmobiliario.pe/proyecto/2199-livorno) | TORATTO GRUPO INMOBILIARIO | Av. Trinidad Moran 331 | Inmediata | 2–2 | 63–77 | 593,992 | 657,578 | 9,422 | no | no |
| [Vizuale 3](https://nexoinmobiliario.pe/proyecto/3945-vizuale-3) | ORTIZ INMOBILIARIA | Jirón Soledad 534 | Constr. | 2–2 | 46–67 | 449,777 | 599,777 | 9,786 | sí | sí |
| [Vizuale 5](https://nexoinmobiliario.pe/proyecto/4198-vizuale-5) | ORTIZ INMOBILIARIA | Prolongación Iquitos 1766 - Lince | Planos | 1–3 | 29–64 | 289,777 | 629,777 | 9,866 | sí | sí |
| [INFINITE](https://nexoinmobiliario.pe/proyecto/3565-infinite) | MW GRUPO INMOBILIARIO | Av. Arequipa 2510 | Constr. | 1–3 | 32–67 | 337,524 | 583,987 | 10,611 | sí | no |
| [VIRIDIAN](https://nexoinmobiliario.pe/proyecto/3429-viridian) | EUREKA | Calle Los Geranios 244 -248 | Constr. | 1–3 | 30–80 | 365,000 | 739,000 | 12,114 | no | no |
| [MASIAS](https://nexoinmobiliario.pe/proyecto/3326-masias) | ORTIZ INMOBILIARIA | Calle Francisco Masías 2806, Lince | Constr. | 1–2 | 41–56 | 549,777 | 749,777 | 13,558 | sí | sí |

#### Pueblo Libre (20 proyectos con 2D en su rango, de 24 en la 1.ª página)

| Proyecto | Inmobiliaria | Dirección | Etapa | Dorm. | Área m² | Precio desde S/ | Precio máx S/ | S/ m² (desde) | Feria | Promo FN |
|---|---|---|---|---|---|---|---|---|---|---|
| [Hernández 1273](https://nexoinmobiliario.pe/proyecto/3198-hernandez-1273) | RB GRUPO INMOBILIARIO | Jirón Daniel Hernández N° 1273 | Constr. | 1–3 | 41–82 | 244,900 | 502,000 | 5,937 | sí | sí |
| [Villa Alba](https://nexoinmobiliario.pe/proyecto/3610-villa-alba) | GRUPO CARAL | Av. Cipriano Dulanto 1085 | Constr. | 1–3 | 40–76 | 246,000 | 473,379 | 6,116 | sí | sí |
| [LIRI - PUEBLO LIBRE](https://nexoinmobiliario.pe/proyecto/1646-liri-pueblo-libre) | GRUPO MG | Av Antonio José de Sucre 1301 | Inmediata | 2–2 | 67–67 | 416,800 | 416,800 | 6,193 | sí | no |
| [View Park](https://nexoinmobiliario.pe/proyecto/4382-view-park) | GRUPO BINDA | Av. Mariano Cornejo 1495 | Planos | 1–3 | 41–114 | 268,941 | 681,302 | 6,618 | sí | sí |
| [MONTAIRE](https://nexoinmobiliario.pe/proyecto/4345-montaire) | TER INMOBILIARIA | Av. Bahia 110 | Planos | 1–3 | 40–66 | 270,074 | 454,151 | 6,685 | sí | no |
| [Avellana](https://nexoinmobiliario.pe/proyecto/3322-avellana) | ABRIL GRUPO INMOBILIARIO | Av. Brasil 1350 | Constr. | 1–3 | 37–74 | 250,200 | 521,100 | 6,713 | sí | sí |
| [Edificio Piana](https://nexoinmobiliario.pe/proyecto/3036-edificio-piana) | ANDIAMO | AV. SIMÓN BOLIVAR 105 PUEBLO LIBRE | Constr. | 2–2 | 55–55 | 373,000 | 373,000 | 6,733 | sí | no |
| [TOP LIVING](https://nexoinmobiliario.pe/proyecto/3422-top-living) | MS INMOBILIARIA | Av. Manuel Cipriano Dulanto 1390 | Constr. | 2–3 | 66–150 | 448,275 | 994,700 | 6,741 | sí | no |
| [Belalba](https://nexoinmobiliario.pe/proyecto/3305-belalba) | URBANA PERÚ | CALLE LORETO 150 – PUEBLO LIBRE | Constr. | 1–2 | 35–125 | 237,494 | 775,558 | 6,793 | sí | no |
| [Residencial Valenti](https://nexoinmobiliario.pe/proyecto/2759-residencial-valenti) | BARQUEROS INMOBILIARIA | Calle América 260 - Pueblo libre | Inmediata | 1–3 | 52–144 | 355,416 | 950,925 | 6,880 | no | no |
| [Ascenza](https://nexoinmobiliario.pe/proyecto/3017-ascenza) | Mohëm Inmobiliaria | Av. Mariano Cornejo 1685 | Inmediata | 2–3 | 59–77 | 406,957 | 534,574 | 6,933 | no | no |
| [Casa Brío](https://nexoinmobiliario.pe/proyecto/4433-casa-brio) | Colindante | Toledo 145 | Planos | 1–3 | 40–106 | 280,000 | 685,000 | 6,969 | sí | no |
| [Bonsái](https://nexoinmobiliario.pe/proyecto/3831-bonsai) | ABRIL GRUPO INMOBILIARIO | Av. Sucre 760 | Constr. | 1–3 | 34–69 | 236,700 | 451,800 | 6,980 | sí | sí |
| [Leguia 860](https://nexoinmobiliario.pe/proyecto/4298-leguia-860) | GRUPO SOL | Av. Jose Leguia y Melendez 860 | Planos | 1–3 | 40–122 | 287,000 | 818,000 | 7,173 | sí | sí |
| [Florencia](https://nexoinmobiliario.pe/proyecto/2805-florencia) | PAZ | Avenida Mariano Cornejo 1455 | Inmediata | 1–2 | 57–167 | 413,000 | 1,063,000 | 7,211 | sí | no |
| [Torre Bolivar](https://nexoinmobiliario.pe/proyecto/4226-torre-bolivar) | TALE INMOBILIARIA | Av. Bolívar 2005, Pueblo Libre | Planos | 1–4 | 42–118 | 306,000 | 735,000 | 7,243 | sí | no |
| [VIANOVA](https://nexoinmobiliario.pe/proyecto/3991-vianova) | MAKE INMOBILIARIA | ARNALDO PANIZO 195 | Constr. | 1–2 | 39–85 | 288,000 | 524,000 | 7,317 | sí | no |
| [Savia](https://nexoinmobiliario.pe/proyecto/2216-savia) | PAZ | Av. Brasil 1470 | Inmediata | 2–2 | 64–71 | 473,000 | 512,000 | 7,377 | sí | no |
| [OCEAN AVENUE](https://nexoinmobiliario.pe/proyecto/2506-ocean-avenue) | SERVIPRO | Av. Sucre 425-437 | Inmediata | 2–3 | 57–71 | 419,950 | 559,950 | 7,404 | no | no |
| [Arteco | Elysée](https://nexoinmobiliario.pe/proyecto/2953-arteco-elysee) | ARTECO | Av. Brasil 2260 | Constr. | 2–3 | 56–72 | 435,453 | 536,900 | 7,707 | sí | sí |

#### Magdalena del Mar (18 proyectos con 2D en su rango, de 24 en la 1.ª página)

| Proyecto | Inmobiliaria | Dirección | Etapa | Dorm. | Área m² | Precio desde S/ | Precio máx S/ | S/ m² (desde) | Feria | Promo FN |
|---|---|---|---|---|---|---|---|---|---|---|
| [Lumina](https://nexoinmobiliario.pe/proyecto/3544-lumina) | RB GRUPO INMOBILIARIO | Calle Echenique 875 Limite con San Miguel | Planos | 1–3 | 43–72 | 239,900 | 461,000 | 5,624 | sí | sí |
| [Catleya](https://nexoinmobiliario.pe/proyecto/3664-catleya) | ABRIL GRUPO INMOBILIARIO | Av. Antonio José de Sucre 973 | Constr. | 1–3 | 38–71 | 257,440 | 488,021 | 6,743 | sí | no |
| [ANDIAMO](https://nexoinmobiliario.pe/proyecto/4266-andiamo) | PROCITY | Jr. Ayacucho  571, Magdalena del Mar | Planos | 1–3 | 40–116 | 283,600 | 780,000 | 7,020 | sí | sí |
| [Villa Convivium 3](https://nexoinmobiliario.pe/proyecto/3782-villa-convivium-3) | GRUPO CARAL | Jiron Salaverry 245, magdalena | Planos | 1–3 | 43–109 | 304,000 | 878,859 | 7,136 | sí | sí |
| [Entrenos](https://nexoinmobiliario.pe/proyecto/2830-entrenos) | PROMSAL | jr tacna 655 | Inmediata | 2–3 | 60–71 | 429,502 | 499,560 | 7,172 | no | no |
| [Malena Family Apartments](https://nexoinmobiliario.pe/proyecto/3909-malena-family-apartments) | HL DESARROLLOS INMOBILIARIOS | Jr. Comandante Espinar N° 102 - 104- 110  Esq. Av. Brasil (Cuadra 40) | Constr. | 2–3 | 46–96 | 339,593 | 678,126 | 7,439 | sí | sí |
| [Landart](https://nexoinmobiliario.pe/proyecto/3482-landart) | BECA INMOBILIARIA | Calle 28 de Julio 629 | Constr. | 2–3 | 58–78 | 430,265 | 590,000 | 7,443 | sí | no |
| [ZENTRA](https://nexoinmobiliario.pe/proyecto/3990-zentra) | MAKE INMOBILIARIA | Jirón Manco Capac & Jirón Ayacucho | Planos | 1–3 | 29–73 | 216,000 | 532,000 | 7,469 | sí | sí |
| [ARBORA](https://nexoinmobiliario.pe/proyecto/3233-arbora) | LUGANO | AV BRASIL 3502-3520 | Constr. | 2–3 | 56–78 | 420,000 | 548,000 | 7,534 | sí | no |
| [Bilancia](https://nexoinmobiliario.pe/proyecto/3729-bilancia) | URBANA PERÚ | Jr. Inclan 202-212 | Constr. | 1–2 | 37–107 | 286,247 | 698,774 | 7,728 | sí | no |
| [Único Magdalena](https://nexoinmobiliario.pe/proyecto/3171-unico-magdalena) | GDC INMOBILIARIA | Av. Faustino Sanchez Carrión 280 | Constr. | 1–3 | 40–74 | 327,964 | 549,810 | 8,195 | sí | no |
| [PEREZ WALK](https://nexoinmobiliario.pe/proyecto/3415-perez-walk) | F INMOBILIARIA | Av. Del Ejercito 2398, Magdalena | Constr. | 1–3 | 42–155 | 348,840 | 952,850 | 8,249 | no | no |
| [Proyecto Vanguardia](https://nexoinmobiliario.pe/proyecto/2494-proyecto-vanguardia) | FAI INMOBILIARIA | Av del Ejercito 251 Magdalena | Inmediata | 1–3 | 41–76 | 338,662 | 583,925 | 8,250 | no | no |
| [TOP LIFE JUAN DE ALIAGA](https://nexoinmobiliario.pe/proyecto/3399-top-life-juan-de-aliaga) | Val Grupo Inmobiliario | Av. Antonio Miroquesada 419 (Ex Juan de Aliaga) | Constr. | 1–3 | 52–145 | 461,000 | 1,044,800 | 8,893 | sí | no |
| [Salaverry I](https://nexoinmobiliario.pe/proyecto/4007-salaverry-i) | ACTUAL | Av.Salaverry 2650 Magdalena | Planos | 1–3 | 40–120 | 375,400 | 836,300 | 9,385 | sí | no |
| [ALIAGA 750](https://nexoinmobiliario.pe/proyecto/2819-aliaga-750) | V&V GRUPO INMOBILIARIO | juan de aliaga 750 | Constr. | 1–3 | 40–83 | 383,000 | 846,000 | 9,490 | sí | sí |
| [ALIAGA 442](https://nexoinmobiliario.pe/proyecto/3403-aliaga-442) | Vive+ Grupo inmobiliario | Av. Juan de Aliaga 442 | Inmediata | 1–3 | 44–78 | 466,225 | 703,000 | 10,625 | sí | sí |
| [MUM 363](https://nexoinmobiliario.pe/proyecto/3180-mum-363) | TALE INMOBILIARIA | Av. Javier Prado Oeste 2291 | Constr. | 1–3 | 41–126 | 481,000 | 1,336,000 | 11,737 | sí | no |

#### Surquillo (21 proyectos con 2D en su rango, de 24 en la 1.ª página)

| Proyecto | Inmobiliaria | Dirección | Etapa | Dorm. | Área m² | Precio desde S/ | Precio máx S/ | S/ m² (desde) | Feria | Promo FN |
|---|---|---|---|---|---|---|---|---|---|---|
| [Bromelia](https://nexoinmobiliario.pe/proyecto/3855-bromelia) | ABRIL GRUPO INMOBILIARIO | Av. Angamos Este 1669 | Constr. | 1–3 | 42–69 | 237,600 | 406,800 | 5,713 | sí | sí |
| [Villa Elenia](https://nexoinmobiliario.pe/proyecto/3886-villa-elenia) | GRUPO CARAL | Av. Angamos Este 1425 | Constr. | 1–3 | 40–134 | 248,000 | 787,984 | 6,152 | sí | sí |
| [MIRALTO](https://nexoinmobiliario.pe/proyecto/4373-miralto) | ANDIAMO | Av. República de Panamá 4670 | Planos | 1–3 | 40–110 | 267,300 | 630,500 | 6,653 | sí | no |
| [Las Begonias](https://nexoinmobiliario.pe/proyecto/4143-las-begonias) | ABRIL GRUPO INMOBILIARIO | Av. Republica de Panamá 4055 | Planos | 1–3 | 42–72 | 283,900 | 501,794 | 6,774 | sí | sí |
| [MARSANO PARK](https://nexoinmobiliario.pe/proyecto/3561-marsano-park) | TER INMOBILIARIA | Av. Tomas Marsano 1855 | Constr. | 2–2 | 48–56 | 331,179 | 430,530 | 6,828 | sí | no |
| [Buenavista - Panama 5110](https://nexoinmobiliario.pe/proyecto/3801-buenavista-panama-5110) | GRUPO BINDA | Av. Republica de Panama 5110 | Constr. | 1–3 | 33–70 | 225,975 | 458,595 | 6,831 | sí | sí |
| [SQ2 Work & Living Apartments](https://nexoinmobiliario.pe/proyecto/4230-sq2-work-living-apartments) | HL DESARROLLOS INMOBILIARIOS | Av. Paseo de la República N° 4061 - 4069 - 4071 Esq. Ca. Los Gorriones N° 109 | Planos | 1–3 | 41–58 | 280,000 | 466,730 | 6,869 | sí | sí |
| [Capulí](https://nexoinmobiliario.pe/proyecto/4000-capuli) | ABRIL GRUPO INMOBILIARIO | Av. Tomás Marsano 242-248, Surquillo | Constr. | 1–3 | 40–74 | 279,767 | 549,408 | 6,991 | sí | sí |
| [TORRE GERMANIA](https://nexoinmobiliario.pe/proyecto/3637-torre-germania) | V&V GRUPO INMOBILIARIO | Av. Angamos 1869, Surquillo | Constr. | 1–3 | 40–71 | 289,000 | 593,000 | 7,225 | sí | sí |
| [High Life](https://nexoinmobiliario.pe/proyecto/3331-high-life) | MADRID INMOBILIARIA | Av. Tomás Marsano 2353 | Constr. | 2–2 | 60–60 | 442,000 | 442,000 | 7,426 | sí | no |
| [Park 55](https://nexoinmobiliario.pe/proyecto/3992-park-55) | GRUPO BINDA | Av. República de Panamá 5555 | Constr. | 1–3 | 40–76 | 315,158 | 561,367 | 7,879 | sí | sí |
| [DORUE ETAPA 2](https://nexoinmobiliario.pe/proyecto/4060-dorue-etapa-2) | DESARROLLADORA | Av. Domingo Orué 230, Surquillo | Constr. | 1–2 | 36–62 | 288,000 | 537,000 | 8,085 | sí | no |
| [Residencial Sukha](https://nexoinmobiliario.pe/proyecto/3241-residencial-sukha) | VIENNA GRUPO INMOBILIARIO | Av. Tomás Marsano 2293 | Constr. | 1–3 | 35–87 | 282,900 | 636,600 | 8,191 | sí | no |
| [Aurora 4](https://nexoinmobiliario.pe/proyecto/3602-aurora-4) | VIENNA GRUPO INMOBILIARIO | Av. sergio Bernales 258. Barrio Medico, Surquillo | Constr. | 2–3 | 51–77 | 419,400 | 537,700 | 8,241 | sí | no |
| [Tasca](https://nexoinmobiliario.pe/proyecto/4044-tasca) | URBANA PERÚ | Av Paseo de la República 5223 | Planos | 1–3 | 40–63 | 338,807 | 506,120 | 8,470 | sí | no |
| [AURORA LOFT21](https://nexoinmobiliario.pe/proyecto/4102-aurora-loft21) | GRUPO TOSCANA | AV. Sergio Bernales 209, Barrio Medico Surquillo | Constr. | 1–3 | 40–90 | 358,000 | 720,000 | 8,897 | no | no |
| [Quatro | Vista Tower](https://nexoinmobiliario.pe/proyecto/3679-quatro-vista-tower) | QUATRO INMOBILIARIA | Av. Tomas Marsano 2619, Surquillo | Constr. | 1–3 | 28–68 | 253,705 | 515,229 | 9,061 | sí | sí |
| [BERNALES 442](https://nexoinmobiliario.pe/proyecto/3552-bernales-442) | Vive+ Grupo inmobiliario | Av. Sergio Bernales 442 | Inmediata | 1–3 | 46–126 | 420,000 | 924,000 | 9,128 | sí | sí |
| [Torre Marsano 28](https://nexoinmobiliario.pe/proyecto/3590-torre-marsano-28) | AMMA INMOBILIARIA | Av. Angamos Este 1795 | Constr. | 1–3 | 27–71 | 249,000 | 500,000 | 9,257 | sí | sí |
| [Mora](https://nexoinmobiliario.pe/proyecto/3944-mora) | ABRIL GRUPO INMOBILIARIO | Av. Aramburu 638 | Constr. | 1–3 | 40–65 | 372,600 | 541,800 | 9,278 | sí | sí |
| [Element](https://nexoinmobiliario.pe/proyecto/3476-element) | EDIFICA | Avenida Tomás Marsano 385 | Constr. | 1–2 | 29–106 | 294,058 | 840,636 | 10,171 | sí | sí |

### Inferences
- Los seis distritos están bien representados en la feria (256 proyectos). San Miguel y Jesús María son los que más proyectos tienen, lo que coincide con que CODIP los señala como líderes de ventas en Lima Moderna (ver sección 5).
- En la muestra, el desarrollador más presente en Jesús María es **Abril Grupo Inmobiliario** (5 proyectos en Av. Brasil y Av. San Felipe). En San Miguel, en cambio, la oferta está más repartida entre varios desarrolladores.
- Para comparar con datos, conviene usar en el portal el filtro "Feria Nexo" + dormitorios 2–2 + etapa + distrito, y pedir en el stand la **lista de precios por unidad** (piso, vista, área techada y libre) en lugar del "desde".

### Gaps
- No pude bajar las páginas 2 y siguientes del buscador (403 en el endpoint AJAX). Faltan unos 169 proyectos de los 313.
- La ficha de proyecto no se pudo leer con el fetcher (devolvía una página genérica). Por eso no hay por proyecto: fecha de entrega, precio de feria frente a lista, ni si el precio incluye estacionamiento.
- No encontré el plano de stands en texto.

---

## 3. Promociones exclusivas de feria, bancos asistentes y tasas o campañas (incluido Nuevo Crédito MiVivienda)

### Takeaway
Las promociones oficiales son genéricas y "referenciales":
- más de S/ 90,000 de descuento (tope, no garantizado);
- separación desde S/ 500;
- "50% de descuento en tu inicial";
- cocina equipada;
- sorteo de un auto o gift card de S/ 30 mil y un combo de electrodomésticos.

No encontré a nivel feria **estacionamiento gratis, gastos de cierre pagados ni congelamiento de precios**: cada inmobiliaria decide. En la zona financiera están BCP, BanBif, Scotiabank, Interbank, Pichincha, GNB, Pandero, Maquisistema, Fonbienes y el Fondo MIVIVIENDA. **Ningún banco publicó una tasa de feria 2026 verificable.** La referencia de mercado es una TEA hipotecaria en soles de ~7–8%.

### Cited Findings
- Beneficios de la landing (12-nov-2026), textuales: "Más de S/90,000 de descuento", "Cocina equipada", "Separa desde S/500", "%50 de descuento en tu inicial", "*Imágenes y promociones referenciales. Condiciones sujetas a variación". Para el sorteo: "Completa el cupón con tu asesor y participa del sorteo" (auto nuevo con gift card de S/ 30 mil y combo de electrodomésticos) — [Nexo – Feria Inmobiliaria](https://nexoinmobiliario.pe/feria-inmobiliaria)
- La FAQ de la landing describe los beneficios como "descuentos especiales en proyectos inmobiliarios seleccionados", "Precios de feria y condiciones únicas", "Bonos, regalos y beneficios adicionales, según cada inmobiliaria participante" y "Facilidades de pago y opciones de financiamiento" — [Nexo – Feria Inmobiliaria](https://nexoinmobiliario.pe/feria-inmobiliaria)
- La nota del blog (30-oct-2026) dice que los descuentos de "hasta S/ 90 mil" son montos máximos y no garantizados. El sorteo tiene un 1.er premio de S/ 30 mil y un 2.º premio de combo de electrodomésticos. La nota no menciona estacionamiento ni gastos de cierre — [Blog Nexo, 30-oct-2026](https://nexoinmobiliario.pe/blog/feria-nexo-noviembre-2026/)
- Promoción de una inmobiliaria: **IMAGINA** sortea un Tesla Model 3 entre compradores de departamentos. La campaña va del 12-nov-2026 al 31-dic-2027 — [Revista Economía](https://www.revistaeconomia.com/imagina-llega-a-la-feria-nexo-con-una-campana-que-sorteara-un-tesla-model-3-entre-compradores-de-departamentos/) [NV: solo snippet]
- Entidades financieras:
  - La FAQ dice: "La feria contará con una zona financiera […] Participan BCP, BanBif, Scotiabank, Banco Pichincha, Pandero y Fondo Mivivienda."
  - El bloque "Entidades participantes" agrega GNB, Maquisistema, Fonbienes e Interbank.
  - **BBVA no aparece** en la landing 2026. Solo lo menciona una guía del blog, más antigua.
  - Fuentes: [Nexo – Feria Inmobiliaria](https://nexoinmobiliario.pe/feria-inmobiliaria); [Blog Nexo – Ferias 2026](https://nexoinmobiliario.pe/blog/ferias-nexo-inmobiliario-2026/)
- Scotiabank tiene una página "Feria Nexo Inmobiliario" con "tasas exclusivas" para crédito hipotecario a tasa fija:
  - TEA máxima de 15%.
  - Ejemplo: S/ 120,000 a 15 años con 80% de financiamiento → cuota de S/ 1,689.27, con desgravamen de 0.0285% y seguro del bien de 0.028%.
  - "Tasación y gastos notariales a COSTO CERO aplican solo para proyectos habilitados" y periodo de gracia de hasta 6 meses.
  - **La página no tiene fechas en el texto y una ruta de imagen dice "2023/mayo/feria-nexo"**, así que no sé si sigue vigente en nov-2026 [NV] — [Scotiabank – Feria Nexo](https://www.scotiabank.com.pe/Personas/beneficios/promociones/feria-nexo-inmobiliario)
- Tasas de mercado (sin campaña de feria):
  - Gestión cita una tasa hipotecaria promedio en soles de 7.69% "al 14 de septiembre" según la SBS, con Scotiabank como la más baja [NV: no confirmé el año del artículo] — [Gestión](https://gestion.pe/tu-dinero/finanzas-personales/tasas-de-creditos-hipotecarios-podrian-bajar-que-bancos-ofrecen-los-menores-intereses-noticia/)
  - Un comparador lista Scotiabank en 7.23% como la TEA mínima "SBS · Octubre 2026" [NV, agregador] — [ComparaBanca Perú](https://comparabancaperu.com/pages/credito-hipotecario.html)
  - La fuente primaria para comprobarlo es Retasas de la SBS — [SBS](https://www.sbs.gob.pe/app/pp/EstadisticasSAEEPortal/Paginas/TIActivaMercado.aspx?tip=B)
- Bono del Buen Pagador (BBP) 2026, subido por el DS 011-2026-VIVIENDA (jun-2026):
  - S/ 27,800 para viviendas de S/ 69,900–99,600;
  - S/ 23,200 para S/ 99,600–149,200;
  - S/ 21,200 para S/ 149,200–248,300;
  - S/ 7,900 para S/ 248,300–367,600.
  - Fuentes: [Infobae, 20-jun-2026](https://www.infobae.com/peru/2026/06/20/incrementan-bono-del-buen-pagador-del-credito-mivivienda-para-la-casa-propia-hasta-s27800/); [RPP](https://rpp.pe/economia/economia/bono-para-comprar-un-departamento-sube-hasta-s-27800-estos-son-los-nuevos-precios-que-califican-al-credito-mivivienda-noticia-1694081)
- Tope del Nuevo Crédito MIVIVIENDA: las fuentes no coinciden. Una dice que financia viviendas de S/ 69,900 a S/ 496,200 y otra de S/ 64,200 a S/ 464,200. La cuota inicial mínima es 7.5% y el comprador no puede tener otra vivienda [NV: agregadores] — [Tramites Perú](https://tramitesperu.com/mivivienda/credito-mivivienda/); [PeruGestiona](https://perugestiona.pe/vivienda/nuevo-credito-mivivienda/)
- Tasa promocional MIVIVIENDA: varios agregadores citan una **TREA promocional de 4.00% en soles vigente del 07-ene-2026 al 30-jun-2026**. Ya vencería, salvo prórroga [NV] — [Eximia Haus](https://eximiahaus.pe/blog/credito-hipotecario-en-peru-guia-2026); [Tramites Perú – comparador](https://tramitesperu.com/comparadores/bancos-hipotecario/)
- La página oficial `mivivienda.com.pe/portal/nuevo-credito-mivivienda` devolvió 404 el 12-nov-2026 — [Fondo MIVIVIENDA](https://www.mivivienda.com.pe/portal/nuevo-credito-mivivienda)

### Inferences
- Un 2D nuevo en estos distritos cuesta S/ 380k–500k (ver sección 4). Eso queda **por encima del tope del BBP (S/ 367,600)**, así que el bono casi no aplicaría. Algunos 2D de San Miguel, Surquillo o Pueblo Libre de S/ 330–367k sí entrarían en el tramo de S/ 7,900.
- El NCMV podría financiar hasta ~S/ 464–496k, según qué tope sea el correcto, pero con condiciones distintas a las de un hipotecario tradicional. Hay que verificarlo en el stand del Fondo.
- Las promociones están formuladas como topes ("hasta", "más de") y como beneficios por proyecto. Sugerencias para el comprador:
  - Pedir por escrito el precio de lista y el precio de feria de la **misma unidad**.
  - Preguntar si el estacionamiento y el depósito están incluidos o se venden aparte.
  - Preguntar quién paga los gastos notariales/registrales y la tasación.
  - Preguntar hasta qué fecha se mantiene el precio después de separar con S/ 500, y si la separación se devuelve.

### Gaps
- No encontré tasas hipotecarias de feria 2026 publicadas por ningún banco (BCP, BanBif, Interbank, Pichincha) ni la TEA vigente del NCMV en nov-2026 en una fuente oficial.
- No encontré un comunicado de CODIP con promociones de estacionamiento gratis, gastos de cierre o precios congelados.

---

## 4. Precio por m² de proyectos nuevos 2026 por distrito, tamaño y precio típico de un 2D, y comparación con las medianas de oferta del BCRP (T1-2026)

### Takeaway
En el buscador de Nexo, los proyectos nuevos se ofrecen entre **+5% y +32% por encima de la mediana de oferta del BCRP T1-2026**. La prima es menor en Pueblo Libre y Jesús María (~+5–12%), intermedia en Magdalena (~+9–20%) y mayor en San Miguel, Surquillo y Lince (~+18–32%).

Para un **2D nuevo** la referencia práctica es de **55–65 m² y S/ 6,500–8,000/m²**:
- San Miguel ≈ S/ 385k;
- Surquillo ≈ S/ 440k;
- Pueblo Libre ≈ S/ 440k;
- Lince ≈ S/ 470k;
- Magdalena ≈ S/ 495k;
- Jesús María ≈ S/ 500k.

Son medianas estimadas a partir de los rangos publicados (estimación propia, ver método).

### Cited Findings
**BCRP: precios de oferta (avisos de venta; mezcla nuevos y usados), fuente primaria**
- Serie "Venta de departamentos por distrito (dólares corrientes por m²)", descargada por la API de BCRPData el 12-nov-2026 (series PD17464PQ–PD17468PQ y PD37958PQ). La última cifra disponible es T1-2026 — [BCRPData – Mercado inmobiliario trimestral](https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/mercado-inmobiliario):

| Distrito | T1-25 US$/m² | T4-25 | T1-26 | Var. T1-26/T1-25 (cálculo propio) | S/ m² T1-26 (dato del encargo) |
|---|---|---|---|---|---|
| Jesús María | 1,749 | 2,086 | 2,103 | +20.3% | 7,123 |
| Lince | 1,838 | 1,970 | 1,894 | +3.1% | 6,415 |
| Magdalena | 1,730 | 1,880 | 1,986 | +14.8% | 6,728 |
| Pueblo Libre | 1,653 | 1,717 | 1,875 | +13.4% | 6,351 |
| San Miguel | 1,418 | 1,697 | 1,637 | +15.5% | 5,546 |
| Surquillo | 1,732 | 1,849 | 1,856 | +7.2% | 6,287 |

  - Los soles del encargo son coherentes con el dólar del BCRP: 7,123 / 2,103 ≈ 3.39 S/ por US$, y el mismo factor sale en los seis distritos.
- BCRP T2-2026 (reportado por Perú21 y PQS el 11-nov-2026): Magdalena **US$ 2,105/m² (+15.7% a/a)**, Jesús María **US$ 2,096 (+16.1%)**, Lince **US$ 2,052 (+14.1%)**, San Miguel +21.7% y Surquillo +6.7% (el menor). El promedio de los distritos de ingresos medios es US$ 1,958 (+14.9%) — [PQS, 11-nov-2026](https://pqs.pe/actualidad/economia/precios-de-departamentos-en-distritos-de-clase-media-suben-149-y-superan-a-los-de-zonas-exclusivas/); [Construyendo.pe](https://www.construyendo.pe/noticias/construccion/precios-de-departamentos-en-distritos-de-clase-media-sube-14-9-y-supera-a-distritos-exclusivos/)
  - Comprobé la coherencia con la base T2-2025 del BCRP: Jesús María 2,096/1,805 = +16.1%, Magdalena 2,105/1,820 = +15.6% y Lince 2,052/1,798 = +14.1%. Con la misma base, San Miguel T2-26 ≈ 1,464 × 1.217 ≈ **US$ 1,781** y Surquillo ≈ 1,753 × 1.067 ≈ **US$ 1,871**. Estas dos últimas son derivaciones propias.
- Indicador PER del BCRP (precio de venta / alquiler anual, en años), T1-2026: Jesús María 17.5, Lince 15.1, Magdalena 15.4, Pueblo Libre 16.9, San Miguel 17.4, Surquillo 15.0 — [BCRPData](https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/mercado-inmobiliario) (series PD41941PQ–PD41951PQ)
- Metodología: el BCRP publica el "promedio de medianas trimestrales de los precios de departamentos en venta", es decir precios ofertados, no de cierre — [BCRP Nota de Estudios 16-2026, 09-mar-2026](https://www.bcrp.gob.pe/docs/Publicaciones/Notas-Estudios/2026/nota-de-estudios-16-2026.pdf)

**Proyectos nuevos: precios "desde" del buscador Nexo (12-nov-2026; 24 proyectos por distrito; precios de lista publicados)**
- Indicadores: "desde" = precio mínimo ÷ área mínima; "máx" = precio máximo ÷ área máxima. Mediana [p25–p75], en S/ por m²:

| Distrito | S/m² "desde" | S/m² "máx" | Prima vs BCRP T1-26 (rango con 3 métricas) |
|---|---|---|---|
| Jesús María | 7,827 [7,022–8,422] | 7,710 | +8% a +12% |
| San Miguel | 6,658 [6,205–7,127] | 6,537 | +18% a +20% |
| Lince | 8,481 [7,589–9,286] | 7,633 | +19% a +32% |
| Pueblo Libre | 6,974 [6,713–7,317] | 6,674 | +5% a +10% |
| Magdalena | 8,064 [7,172–8,531] | 7,360 | +9% a +20% |
| Surquillo | 7,574 [6,831–8,470] | 7,414 | +18% a +21% |

  - Fuente: `venta_<distrito>.html` ([JM](https://nexoinmobiliario.pe/venta-de-inmuebles/jesus-maria), [SM](https://nexoinmobiliario.pe/venta-de-inmuebles/san-miguel), [Lince](https://nexoinmobiliario.pe/venta-de-inmuebles/lince), [PL](https://nexoinmobiliario.pe/venta-de-inmuebles/pueblo-libre), [Mag](https://nexoinmobiliario.pe/venta-de-inmuebles/magdalena-del-mar), [Surq](https://nexoinmobiliario.pe/venta-de-inmuebles/surquillo)).
  - La 3.ª métrica del rango es el punto medio de las otras dos.
- Estimación del 2D típico por proyecto (método propio):
  - Si el rango del proyecto empieza en 2D, tomo el área mínima; si termina en 2D, la máxima. Si es 1–3D, tomo el punto medio del rango de áreas.
  - Después interpolo el precio linealmente entre el mínimo y el máximo publicados.
  - Resultado por distrito, como mediana [≈p25–p75] del precio y área mediana: Jesús María **S/ 502,525** [416k–676k], 60 m² (n=24); San Miguel **S/ 384,500** [351k–470k], 59 m² (n=23); Lince **S/ 471,789** [434k–552k], 56 m² (n=18); Pueblo Libre **S/ 441,864** [386k–524k], 65 m² (n=20); Magdalena **S/ 496,547** [420k–615k], 61 m² (n=18); Surquillo **S/ 438,263** [384k–460k], 57 m² (n=21).
  - Fuente: los mismos archivos del buscador.
- Proyectos cuyo producto mínimo ya es un 2D (precio desde del 2D más chico):
  - Jesús María: n=3, mediana S/ 441,900, 52 m², S/m² 8,422.
  - Lince: n=6, mediana S/ 505,072, 63 m², 8,289.
  - Magdalena: n=4, mediana S/ 424,751, 57 m², 7,441.
  - Pueblo Libre: n=7, mediana S/ 419,950, 59 m², 6,933.
  - San Miguel: n=5, mediana S/ 337,800, 53 m², 6,519.
  - Surquillo: n=3, mediana S/ 419,400, 51 m², 7,426.
  - Fuente: los mismos archivos del buscador.

**Mercado agregado de vivienda nueva (CODIP)**
- Ene–sep 2026 en Lima Metropolitana y Callao:
  - precio promedio por vivienda vendida **S/ 440,565**;
  - área promedio de 64.3 m² (antes 66.1);
  - las viviendas de 2 y 3 dormitorios son ~78% de las operaciones;
  - las de 40–60 m² son el 49.4% de las unidades vendidas.
  - Fuente: [Forbes Perú, 27-oct-2026](https://forbes.pe/economia-y-finanzas/2026-10-27/venta-de-viviendas-en-lima-y-callao-crece-26-que-zonas-concentran-la-demanda-inmobiliaria)
  - Contradicción: Infobae (10-nov-2026) dice que las de 40–60 m² fueron el **39%** de las ventas de ene–ago — [Infobae, 10-nov-2026](https://www.infobae.com/peru/2026/11/10/los-departamentos-de-entre-40-y-60-m-concentraron-el-39-de-las-ventas-en-lima/). Infobae (27-oct-2026) habla de "70%–80% de las preferencias" — [Infobae, 27-oct-2026](https://www.infobae.com/peru/2026/10/27/furor-por-departamentos-en-lima-ventas-se-disparan-26-hasta-septiembre-y-la-oferta-se-agotaria-siete-meses-antes/)
- El precio promedio por m² de lo vendido subió +2.8%, empujado por más unidades pequeñas, que tienen mayor valor por m². El ticket promedio se mantuvo estable — [Infobae, 27-oct-2026](https://www.infobae.com/peru/2026/10/27/furor-por-departamentos-en-lima-ventas-se-disparan-26-hasta-septiembre-y-la-oferta-se-agotaria-siete-meses-antes/)

**Otras fuentes (más antiguas o agregadoras)**
- Urbania, dic-2025: Lima Metropolitana S/ 6,806/m²; Jesús María S/ 7,574, Lince S/ 7,318, Pueblo Libre S/ 6,279 (datos de **fines de 2025**) [NV: cifras distritales del resumen de búsqueda] — [La República, 31-dic-2025](https://larepublica.pe/economia/2025/12/31/precio-del-m2-sube-a-s6806-en-lima-metropolitana-estos-son-los-distritos-mas-baratos-y-caros-para-vivir-segun-urbania-hnews-3080129)
- Urbania, abr-2026: Lima Metropolitana S/ 6,886/m² (+0.3% en abril) [NV, snippet] — fuente citada en la búsqueda sobre el índice Urbania; ver también [Urbania blog](https://urbania.pe/blog/magdalena-y-lince-son-los-mas-caros/)
- CasasHoot, jul-2026: mediana de 146 avisos en Jesús María = S/ 7,006/m², rango típico S/ 5,882–8,023 (avisos mezclados, agregador) [NV] — [CasasHoot](https://www.casashoot.net/jesus-maria-departamento.html)

### Inferences
- **Prima de lo nuevo sobre la oferta BCRP**: tomando la métrica intermedia, +7% a +25%. Es lógico, porque la mediana del BCRP mezcla usados más antiguos. En Pueblo Libre la prima es baja (+5–10%), así que ahí un nuevo "caro" se nota enseguida. En Lince, a la inversa, la prima es alta (+19–32%): el stock nuevo es de unidades pequeñas y alto S/m², mientras que el usado del distrito es amplio y antiguo.
- **Referencia rápida para evaluar una cotización** de 2D nuevo, en S/ por m² de área techada, con precio de lista y antes del descuento de feria:
  - Jesús María: buena ≤ 7,000; normal 7,000–8,400; cara > 8,400.
  - San Miguel: buena ≤ 6,200; normal 6,200–7,100; cara > 7,100.
  - Lince: buena ≤ 7,600; normal 7,600–9,300; cara > 9,300.
  - Pueblo Libre: buena ≤ 6,700; normal 6,700–7,300; cara > 7,300.
  - Magdalena: buena ≤ 7,200; normal 7,200–8,500; cara > 8,500.
  - Surquillo: buena ≤ 6,800; normal 6,800–8,500; cara > 8,500.
  - Los cortes son el p25 y el p75 de la métrica "desde". Como esa métrica está sesgada hacia unidades chicas, un 2D más grande que el mínimo del proyecto debería salir algo por debajo. Si el S/m² del 2D es mayor que el del 1D del mismo edificio, la cotización está inflada.
- **En total, un 2D de 55–65 m²** se mueve aproximadamente en: San Miguel S/ 350–470k; Surquillo S/ 385–460k; Pueblo Libre S/ 385–525k; Lince S/ 435–550k; Magdalena S/ 420–615k; Jesús María S/ 415–675k. El p75 de Jesús María y Magdalena lo empujan proyectos premium (por ejemplo, Ímpettu y Modena, con unidades de 125–150 m²).
- **Rentabilidad bruta de alquiler** implícita en el PER del BCRP (1/PER): Surquillo ~6.7%, Lince ~6.6%, Magdalena ~6.5%, Pueblo Libre ~5.9%, Jesús María y San Miguel ~5.7%. Comprar nuevo con una prima del 10–25% baja esa rentabilidad de forma proporcional; es relevante si el 2D es para alquilar.
- Las comparaciones en soles entre T1 y T2-2026 tienen ruido cambiario, porque el BCRP mide en US$. El T2-2026 en dólares indica que Jesús María, Magdalena y Lince siguen subiendo (+14–16% a/a). El precio de oferta en soles probablemente siguió al alza, pero no lo verifiqué en soles.

### Gaps
- **No encontré** cifras por distrito de **Tinsa**, de **Capeco** ("El mercado de edificaciones urbanas" 2026) ni del índice Urbania 2026 en una fuente primaria.
- Las series del BCRP en BCRPData llegan solo a T1-2026. El T2-2026 viene de prensa y no hay T3-2026.
- Las medianas de Nexo salen de una muestra de 24 proyectos por distrito, no aleatoria (1.ª página), y usan precios "desde" y rangos, no listas por unidad.
- No sé si los precios "desde" incluyen estacionamiento: en varios proyectos de la muestra el estacionamiento figura como 0–0 (por ejemplo, LUNA, de Lugano). Tampoco sé si ya incluyen el descuento de feria.

---

## 5. Ventas, stock y absorción 2026 por distrito; plazos de entrega por etapa y diferencia de precio entre etapas

### Takeaway
El mercado está caliente:
- **23,626 viviendas** vendidas en ene–sep 2026 en Lima Metropolitana y Callao (+26%), según CODIP.
- **Lima Moderna** vendió **9,575** (+32%) y explica el 47% del aumento.
- La absorción es de 4.5% mensual, con unos **20 meses** para agotar el stock (frente a 27 meses de promedio histórico).
- Jesús María y San Miguel destacan dentro de Lima Moderna, pero **no encontré cifras por distrito**.

En la muestra de Nexo, **"En planos" sale ~13% más barato por m² que "En construcción"**. "Entrega inmediata" no sale más cara, lo que sugiere que hay stock terminado con descuento.

### Cited Findings
- Ene–sep 2026 (CODIP, Real Estate Data Analytics):
  - 23,626 unidades vendidas, frente a 18,679 en el mismo periodo de 2025 (+26%);
  - inventario promedio de 58,315 unidades (+10% a/a);
  - absorción mensual promedio de 4.5% (antes 3.9%);
  - 20 meses para agotar el stock al cierre de septiembre (promedio histórico de cinco años: 27);
  - Lima Moderna: 9,575 unidades (+32%), 47% del aumento total;
  - Lima Este: de 536 a 800 unidades (+49%);
  - VIS rango 4 (hasta S/ 367,600): 43.8% de las ventas acumuladas.
  - Fuente: [Forbes Perú, 27-oct-2026](https://forbes.pe/economia-y-finanzas/2026-10-27/venta-de-viviendas-en-lima-y-callao-crece-26-que-zonas-concentran-la-demanda-inmobiliaria)
- CODIP (Ana Cecilia Gálvez) señala: en Lima Moderna destacan **Jesús María y San Miguel**; el coeficiente de absorción es de 4.5%–4.8% (promedio histórico 3.7%); la morosidad hipotecaria ronda el 3%; descartan por ahora un exceso de oferta. El artículo **no** da cifras para Lince, Pueblo Libre, Magdalena ni Surquillo — [Infobae, 27-oct-2026](https://www.infobae.com/peru/2026/10/27/furor-por-departamentos-en-lima-ventas-se-disparan-26-hasta-septiembre-y-la-oferta-se-agotaria-siete-meses-antes/)
- Primer semestre 2026: 15,477 unidades vendidas (+26%). En junio, el **86% de las viviendas vendidas estaba en planos o en construcción** [NV: snippet] — [Construyendo.pe](https://www.construyendo.pe/noticias/construccion/ventas-de-viviendas-en-lima-crecio-26-en-el-primer-semestre-del-ano/)
- Proyección de Scotiabank (con base en CODIP): unas 28 mil viviendas nuevas vendidas en Lima en 2026, +15% frente a 2025 [NV: snippet] — [El Comercio](https://elcomercio.pe/economia/peru/sector-inmobiliario-registraria-ventas-record-al-cierre-del-2026-estima-scotiabank-l-ultimas-noticia/)
- Mezcla de etapas en la muestra de Nexo (144 proyectos, 12-nov-2026), en planos / construcción / entrega inmediata:
  - Jesús María 7 / 16 / 1
  - San Miguel 8 / 7 / 9
  - Lince 3 / 11 / 10
  - Pueblo Libre 6 / 9 / 9
  - Magdalena 5 / 11 / 8
  - Surquillo 4 / 16 / 4
  - Fuente: archivos `venta_<distrito>.html` (URLs en la sección 2).
- S/m² "desde" por etapa, mediana con los 6 distritos juntos: **En planos 6,969** (n=33) · **En construcción 8,056** (n=70) · **Entrega inmediata 7,377** (n=41). Por distrito (planos / construcción / inmediata):
  - Jesús María 7,022 / 8,155 / 8,152 (n=1)
  - Lince 7,964 / 8,963 / 7,546
  - Magdalena 7,136 / 8,195 / 8,223
  - Pueblo Libre 7,071 / 6,741 / 7,211
  - San Miguel 6,479 / 7,112 / 6,887
  - Surquillo 6,822 / 7,982 / 7,425
  - Fuente: mismos archivos.

### Inferences
- **La diferencia entre etapas** es de ~−13% para "en planos" frente a "en construcción" (6,969 vs 8,056, todo junto), y en la mayoría de distritos va de −9% a −15%. Pueblo Libre es la excepción: ahí planos y construcción están parejos. Es consistente con el descuento usual de preventa, que paga el riesgo de obra y el costo de oportunidad de 18–36 meses sin uso.
  - Ese plazo de 18–36 meses es una inferencia general y no está verificado: no encontré una fuente con los plazos de entrega típicos de 2026.
- Que "Entrega inmediata" salga por debajo de "En construcción" probablemente refleja **composición y stock remanente**: proyectos terminados con unidades grandes o que no rotan y se liquidan con descuento. Por eso el comprador con urgencia puede negociar más en entrega inmediata; es también la etapa sin riesgo de obra.
- Con 20 meses de stock y absorción alta, el poder de negociación del comprador es **moderado** en Jesús María y San Miguel, donde la demanda es fuerte. Probablemente es mayor en proyectos terminados o en distritos con prima alta sobre la oferta del BCRP (Lince y Surquillo).
- Si se compra en planos, conviene exigir: fecha de entrega contractual con penalidad, garantía (fianza o carta fianza o cuenta escrow del banco promotor) y el cronograma de pagos ligado al avance de obra.

### Gaps
- **No encontré** ventas, stock ni absorción **por distrito** de 2026 (CODIP solo da cifras por zona; Tinsa no apareció).
- No encontré plazos de entrega típicos documentados (meses desde la preventa hasta la entrega) para 2026.
- La comparación entre etapas sale de la muestra de Nexo con precios "desde": no controla tamaño de unidad, ubicación fina ni acabados.
