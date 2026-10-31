# CLAUDE.md — Proyecto Finanzas

## Contexto
Plan de inversión personal del dueño, residente en Perú. Capital a asignar: **S/ 100,000**.
El fondo de emergencia está **aparte** y no forma parte de este monto.
El dueño tiene formación en física-matemática y data science: explica a nivel técnico, con
números, sin simplificar de más y sin tono de folleto comercial.

Asignación tentativa del dueño (2026-10-29), **pendiente de validar con la investigación**:

| Bloque | Monto | Nota del dueño |
|---|---|---|
| Inmueble (inicial de departamento o terreno) | S/ 50,000 | buscar dónde se valoriza más, no solo Barranco/Miraflores |
| Ahorro / DPF | S/ 20,000 | protección por encima de rendimiento |
| ETFs | S/ 20,000 | |
| Trading | S/ 10,000 | dinero que está dispuesto a perder; tope que mencionó: S/ 20,000 |

La decisión vigente vive en `PLAN.md`, no aquí.

Situación de vivienda (dicha por el dueño el 2026-10-31):
- Vive en casa de sus padres en Los Olivos y aporta ~S/ 1,500 al mes. No paga alquiler.
- Su trabajo está en San Isidro/Lince. Quiere mudarse cerca: San Isidro, Lince, Jesús María o
  Pueblo Libre, cualquiera antes que seguir viajando desde el cono norte.
- Piensa quedarse en Lima al menos 5 años.
- Hoy no tiene inmuebles a su nombre. Tuvo un loft en Barranco comprado en 2022 con
  **Nuevo Crédito MiVivienda** (S/ 240k, inicial S/ 24k), vendido a inicios de 2026 en
  S/ 288k, pagando una penalidad a MiVivienda. Cree que puede volver a acceder a MiVivienda:
  **no está verificado** y condiciona toda la recomendación inmobiliaria.

## Preferencias del dueño
- **Seguridad antes que rendimiento** en ahorro: prefiere no tener apps bancarias en el
  celular. Operar solo por web, o con un DPF que exija ir en persona, es una ventaja, no un
  costo. Pibank (~5% en ahorro) le interesa, pero no quiere tenerla en el celular.
- Quiere que lo aconsejen, no solo que le listen opciones: da una recomendación y su porqué.

## Reglas duras
- **Todo dato de mercado lleva fecha y fuente.** Tasas, precios por m² y comisiones caducan
  en semanas. Una cifra sin fecha no se usa.
- **Fuentes primarias primero:** SBS (tasas, FSD, entidades supervisadas), BCRP (precios
  inmobiliarios, tipo de cambio), SMV (SABs, fondos, crowdfunding), SUNAT (impuestos),
  SUNARP (títulos). YouTube y blogs sirven para descubrir opciones y opiniones, nunca como
  fuente única de una cifra.
- **Retornos siempre netos** de comisiones, impuestos, inflación (real vs nominal) y, si
  aplica, tipo de cambio.
- Nunca se guardan en el repo números de cuenta, claves, tokens, DNI ni estados de cuenta.
  Si un archivo va a contener datos así, detente y avisa.
- Git y GitHub **solo con la cuenta personal** `alvarocc94` / `alvarocc94@gmail.com`; el
  correo de UTEC nunca aparece en este repo.

## Evidencia previa que hay que respetar
El proyecto Quantac (`D:\PROYECTOS\QUANTAC`, catálogo en `IDEAS.md` de la rama
`exp/event-drift`) probó 424 variantes de estrategias de trading sobre US equities 2016-2026
con costos x2: **ninguna le ganó a SPY comprar y mantener**; el 60/40 SPY/AGG fue lo único que
lo dominó en Sharpe. Cualquier propuesta de trading activo parte de esa vara.

## Estructura
- `PLAN.md` — asignación decidida y su porqué; se actualiza cuando cambia.
- `reports/<título>.md` — informe final de cada investigación profunda.
- `research_notes/<título>/` — notas de los investigadores detrás de cada informe;
  `raw/` (subtítulos y descargas) está gitignoreado.
- `README.md` — índice y "Estado actual".

## Flujo de trabajo
1. Investigación profunda con la skill `deep-research`; para YouTube, la skill de usuario
   `youtube-investigacion` (yt-dlp vía uvx).
2. Cada informe termina en una recomendación concreta y se enlaza desde README.md.
3. Cada decisión de asignación → entrada fechada en PLAN.md (contexto, alternativas, elección).
4. Al terminar una sesión, actualiza README.md sección "Estado actual" y haz push.
