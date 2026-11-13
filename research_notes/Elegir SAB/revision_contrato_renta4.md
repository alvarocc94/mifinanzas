# Revisión del contrato de Renta 4 SAB (2026-11-09)

El dueño abrió su cuenta en Renta 4 SAB el 2026-11-09 y compartió el "Contrato de intermediación y
servicios - persona natural" que le entregaron: ficha de cliente, términos y condiciones en 10
páginas y declaración FATCA.

**El PDF no está en el repo.** Trae DNI, número de cuenta bancaria, domicilio, celular, correo e
ingresos, así que se guarda en `privado/renta4/2026-11-09_contrato_intermediacion_persona_natural.pdf`,
carpeta que git ignora. Esta nota no copia ninguno de esos datos.

## Lo que dice la ficha (sin datos personales)

- **Registro:** 09-nov-2026, por internet. Plantilla del contrato: PDF de junio de 2026.
- **Productos activados:** divisas, compra y venta de valores, valores extranjeros, fondos y
  "Renta 4 ON", el depósito overnight de Renta 4 Cash.
- **Cuenta bancaria registrada:** una sola, de ahorro en **soles**, en el BCP. No hay una cuenta en
  dólares.
- **Estados de cuenta:** por la plataforma y por correo.
- **Ejecutivo:** la ficha tiene un ejecutivo asignado y la cláusula 18.10 habla de "su ejecutivo".
  Eso confirma en parte lo del "gestor asignado". El contrato no dice nada de asesoría.
- **Datos que todavía no tiene:**
  - El **código CAVALI (RUT)** está vacío: "para ser llenado por la SAB".
  - El campo de **firma** también está vacío en esta copia. La copia que vale es la que se firmó
    electrónicamente (cl. 1.2), así que conviene guardar el correo de confirmación.

## Lo que hay que hacer

1. **Registrar una cuenta en dólares.**
   - FIBRA Prime paga en dólares, y el dinero solo puede salir hacia cuentas bancarias tuyas
     registradas en la ficha (cl. 3.6). Si retiras a la cuenta en soles, alguien convierte, y lo
     hace a su tipo de cambio.
   - Mantener las cuentas actualizadas es responsabilidad tuya (cl. 4.2).
2. **Comparar el tipo de cambio antes de convertir los S/ 10,000.**
   - Renta 4 vende dólares actuando como contraparte (cl. 10 e.2). Un tipo de cambio 1% peor
     cuesta ~S/ 100, cinco veces la comisión de compra.
   - Hay que comparar su cotización con Kambista o Rextie (~0.4%). Ver también en qué bancos tiene
     Renta 4 sus cuentas de intermediación, para no pagar transferencias interbancarias.
3. **Pedir el código CAVALI (RUT).** Con él puedes comprobar tus valores en CAVALI sin depender de
   la SAB. FIBRA Prime queda anotada a tu nombre ahí.
4. **Seguridad.**
   - El acceso es con usuario y contraseña. Toda orden que entre con ellos vale como tu firma
     (cl. 18.5).
   - Renta 4 no responde si alguien usa tus claves (cl. 18.3), así que la pérdida de las claves se
     reporta de inmediato a contacto@renta4.pe.
   - El contrato no menciona doble factor. Hay que preguntarlo, y usar una contraseña única guardada
     en el gestor.
5. **Opcional: retirar el permiso de publicidad.** La cl. 16.3 autoriza ofertas propias y de
   terceros vinculados, y dice que esa autorización se puede retirar.

## Lo que el contrato confirma o agrega a los riesgos

- **Costos que no están en el tarifario (cl. 18.12).** Operar por la plataforma "implica costos
  adicionales por parte de la BVL", los de los "Clientes ADM" (acceso directo), "asumidos por el
  Cliente".
  - El tarifario de Renta 4 no los lista.
  - En el de la BVL (boletín del 06-nov-2026), la conexión ADM cuesta S/ 274 al mes por conexión y
    se le cobra a la SAB, no por orden.
  - **Respuesta (2026-11-11, de Renta 4 al dueño):** no cobran nada por operar en la plataforma
    aparte de la comisión.
- **Cambios de tarifas.**
  - Renta 4 puede cambiar sus tarifas por su cuenta, avisando con 15 días (cl. 4.3).
  - Los cambios al contrato requieren 30 días de aviso, y puedes resolverlo sin costo antes de que
    entren en vigor (cl. 15).
  - Las condiciones del servicio web las puede cambiar en cualquier momento; si sigues usando el
    servicio, se dan por aceptadas (cl. 18.16 iii).
  - Implicancia: lo de "custodia sin costo" puede cambiar. Revisa el tarifario una vez al año.
- **Valores extranjeros (cl. 11.2).**
  - **Cuenta global:** se registran en una cuenta global, ómnibus (a).
  - **Sin Fondo de Garantía:** las operaciones en el exterior no están cubiertas (e).
  - **Sin OPA:** si la BVL excluye un valor extranjero inscrito por agente promotor, como SPYL, "no
    habrá oferta pública de adquisición, ni oferta pública de compra" (j). Confirma el riesgo de
    exclusión de la sección 5 de `sab_fibra_y_via_bvl.md`: no hay salida garantizada.
  - Pregunta nueva: si SPYL comprado en la rueda queda a tu nombre en CAVALI o en la cuenta global.
- **Compensación y venta forzosa (cl. 3.5, 4.6 y 8).**
  - Renta 4 puede usar tu efectivo para cubrir lo que le debas, y vender tus valores si una compra
    no se fondea.
  - Si no hay fondos suficientes, puede ejecutar solo parte de la orden (cl. 5.6 c).
  - Regla: nunca mandar una orden sin el dinero ya en la cuenta.
- **Renta 4 Cash** (sección "Servicio Renta 4 Cash" y tarifario):
  - El efectivo ocioso se junta en un depósito overnight **a nombre de Renta 4**, por cuenta de sus
    clientes, que se renueva solo.
  - Renta 4 se queda con 10–20% de los intereses.
  - Mi inferencia, no verificada con la SBS: al ser un depósito a plazo de una persona jurídica, el
    FSD no te cubre a ti.
  - Con saldos chicos da igual. Solo hay que tener presente que ese efectivo no está a tu nombre.
- **Impuestos (cl. 4.8).** Renta 4 no da asesoría tributaria. Al vender en la BVL, CAVALI retiene,
  pero informar el costo para que la retención sea sobre la ganancia corre por tu cuenta.
- **Responsabilidad y reclamos.**
  - Las obligaciones de Renta 4 son "de medios y no de resultados" (cl. 5).
  - No responde por fallas de la plataforma, salvo dolo o negligencia grave (cl. 18.8 y
    18.13–18.14).
  - Las controversias van a los jueces de Lima Cercado, sin arbitraje (cl. 17).
  - Los reclamos van a contacto@renta4.pe. El supervisor es la SMV (Av. Santa Cruz 315,
    Miraflores, 610-6300).
- **Lo que está bien:**
  - Plazo indefinido (cl. 7).
  - Estados de cuenta y pólizas gratis por la web (cl. 5.1 y 9).
  - Prohibición de entregar efectivo a la SAB o a sus representantes (cl. 4.7).
  - Las órdenes también se pueden dar por correo con confirmación (cl. 2.1), útil si la plataforma
    falla.

## Dirección de Renta 4

El contrato da como domicilio de Renta 4 SAB **Calle Las Orquídeas 621, Centro Empresarial
Platinum Plaza, Torre 1, oficina 621, San Isidro**. La dirección que el plan usaba hasta hoy (Av.
Víctor Andrés Belaúnde 147, Edificio Real Uno) viene de un perfil de empresa actualizado en 2023
([EMIS](https://www.emis.cn/php/company-profile/PE/Renta_4_Sociedad_Agente_De_Bolsa_SA_en_4153967.html)).
Vale la del contrato, pero conviene confirmarla con el ejecutivo antes de ir.

## Preguntas que se suman a las de SPYL

- ¿Hay doble factor (TOTP) para entrar a la plataforma web?
- ~~¿Cobran algún cargo por orden por el acceso ADM de la BVL (cl. 18.12)?~~ No (2026-11-11).
- ¿Cuál es mi código CAVALI (RUT)?
- ¿En qué bancos tienen cuentas de intermediación en soles y en dólares?
- ¿A qué tipo de cambio venden dólares hoy, frente a Kambista o Rextie?
- Si compro SPYL en la rueda, ¿queda anotado a mi nombre en CAVALI o en la cuenta global?
