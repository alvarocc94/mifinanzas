"""Genera la plantilla de Excel para llevar un préstamo con cuota fija (francés), periodo de gracia
y anticipos a capital.

Hojas:
- Datos: lo que se pacta (monto, TEA, fechas, número de cuotas, tipo de gracia y qué pasa tras un
  anticipo a capital).
- Cronograma: el plan de pagos original, que se recalcula al cambiar Datos.
- Pagos: lo que de verdad paga el deudor, y de aquí sale el saldo oficial.
  - Una cuota cubre primero los intereses y luego el capital (Código Civil, art. 1257).
  - Un anticipo a capital va íntegro a capital. El interés corrido hasta ese día queda pendiente
    y se cobra con la siguiente cuota.
  - El interés corre solo sobre el capital: el interés pendiente no genera más interés
    (art. 1249).
  - Pagos y Cronograma cuentan los días igual (base 30/360, con un primer periodo irregular si
    la primera cuota no cae el mismo día que el desembolso). Si las cuotas se pagan en su fecha,
    los dos coinciden al céntimo.
- Resumen: deuda a hoy, cuotas pagadas y atrasadas, la próxima cuota (recalculada si hubo
  anticipos) e intereses cobrados por año para la declaración anual.

Uso (necesita openpyxl):
    uv run --no-project --with openpyxl python -I herramientas/prestamo_plantilla.py privado/prestamo/prestamo.xlsx

El archivo lleno va en privado/, que git ignora, porque tiene datos de una persona.
"""

import sys
from datetime import date

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

FUENTE = "Arial"
AZUL = Font(name=FUENTE, color="0000FF")
NEGRO = Font(name=FUENTE)
NEGRITA = Font(name=FUENTE, bold=True)
TITULO = Font(name=FUENTE, bold=True, size=13)
SUBTITULO = Font(name=FUENTE, bold=True, size=11)
GRIS = Font(name=FUENTE, italic=True, color="666666", size=9)
AMARILLO = PatternFill("solid", fgColor="FFFF00")
CABECERA = PatternFill("solid", fgColor="D9E1F2")
LINEA = Border(bottom=Side(style="thin", color="999999"))
SOLES = '"S/ "#,##0.00;("S/ "#,##0.00);"-"'
FECHA = "dd/mm/yyyy"
PCT = "0.00%"
PCT4 = "0.0000%"
FILAS_CRONO = 120  # meses de gracia + cuotas
FILAS_PAGOS = 200
FIN_P = 6 + FILAS_PAGOS
CR = f"Cronograma!$B$5:$B${4 + FILAS_CRONO}"  # fechas del cronograma
ULT = f"MATCH(9.99E+307,Pagos!$A$6:$A${FIN_P})"  # posición del último movimiento
TIPOS = ("Cuota", "Pago parcial", "Anticipo a capital")

# Celdas de Datos que usan las otras hojas
TEA, R, G, N, CUOTA, OPCION = ("Datos!$B$6", "Datos!$B$14", "Datos!$B$15", "Datos!$B$9",
                               "Datos!$B$18", "Datos!$B$12")


def celda(ws, ref, valor, fuente=NEGRO, formato=None, relleno=None, comentario=None):
    c = ws[ref]
    c.value = valor
    c.font = fuente
    if formato:
        c.number_format = formato
    if relleno:
        c.fill = relleno
    if comentario:
        c.comment = Comment(comentario, "plantilla", width=320, height=120)
    return c


def cabecera(ws, fila, titulos):
    for j, t in enumerate(titulos, start=1):
        c = ws.cell(row=fila, column=j, value=t)
        c.font, c.fill, c.border = NEGRITA, CABECERA, LINEA
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[fila].height = 30


def anchos(ws, columnas, medidas):
    for col, w in zip(columnas, medidas):
        ws.column_dimensions[col].width = w


def lista(ws, opciones, rango):
    dv = DataValidation(type="list", formula1='"' + ",".join(opciones) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(rango)


def hoja_datos(wb):
    ws = wb.active
    ws.title = "Datos"
    celda(ws, "A1", "Préstamo: datos pactados", TITULO)
    celda(ws, "A2", "Edita solo las celdas azules con fondo amarillo; todo lo demás se calcula. "
          "Pasa el mouse sobre cada una para ver de dónde sale el dato.", GRIS)
    entradas = [
        ("Deudor", "Familiar", None,
         "Nombre o alias del deudor. El archivo vive en privado/, fuera de git."),
        ("Monto prestado", 25000, SOLES, "Dato del dueño: S/ 25,000."),
        ("Tasa efectiva anual (TEA)", 0.09, PCT, "Dato del dueño: 9% TEA."),
        ("Fecha de desembolso", date(2026, 11, 20), FECHA, "Dato del dueño: 20-nov-2026."),
        ("Fecha de la primera cuota", date(2027, 2, 28), FECHA,
         "Dato del dueño: 28-feb-2027. Las siguientes vencen el 28 de cada mes."),
        ("Número de cuotas", 12, "0",
         "Dato del dueño: 12 cuotas mensuales, la primera el 28-feb-2027. Si eran 12 además de "
         "la primera, pon 13."),
        ("Tipo de gracia", "Total", None,
         "Dato del dueño: total. No paga nada hasta la primera cuota y ese interés se cobra dentro "
         "de las cuotas. Parcial: en la gracia paga solo el interés de cada mes."),
        ("IR sobre los intereses", 0.05, PCT,
         "Renta de segunda categoría: 6.25% sobre el 80% del interés cobrado = 5% efectivo. "
         "Por confirmar con SUNAT o un contador."),
        ("Tras un anticipo a capital", "Reducir plazo", None,
         "Reducir plazo: la cuota sigue igual y el préstamo termina antes (la última cuota sale "
         "menor). Reducir cuota: se mantiene la fecha final y la cuota baja. Lo decide el deudor."),
    ]
    for i, (rotulo, valor, fmt, nota) in enumerate(entradas, start=4):
        celda(ws, f"A{i}", rotulo, NEGRITA)
        celda(ws, f"B{i}", valor, AZUL, fmt, AMARILLO, nota)
    lista(ws, ("Total", "Parcial"), "B10")
    lista(ws, ("Reducir plazo", "Reducir cuota"), "B12")

    celda(ws, "A13", "Calculado", TITULO)
    inicio = 'IF(B10="Total",B7,EDATE(B7,B15))'  # desde cuándo corre el interés sin pagar
    calculos = [
        ("Tasa efectiva mensual", "=(1+B6)^(1/12)-1", PCT4),
        ("Meses de gracia", "=MAX(0,(YEAR(B8)-YEAR(B7))*12+MONTH(B8)-MONTH(B7)-1)", "0"),
        ("Deuda el día de la primera cuota (antes de pagarla)",
         f"=B5*(1+B6)^YEARFRAC({inicio},B8,4)", SOLES),
        ("Pago mensual en la gracia", '=IF(B10="Parcial",B5*B14,0)', SOLES),
        ("Cuota mensual", "=PMT(B14,B9,-B16,0,1)", SOLES),
        ("Total a cobrar", "=B18*B9+B17*B15", SOLES),
        ("Intereses totales", "=B19-B5", SOLES),
        ("IR estimado sobre todos los intereses", "=B20*B11", SOLES),
        ("Fecha de la última cuota", "=EDATE(B8,B9-1)", FECHA),
    ]
    for i, (rotulo, formula, fmt) in enumerate(calculos, start=14):
        f = NEGRITA if i == 18 else NEGRO
        celda(ws, f"A{i}", rotulo, f)
        celda(ws, f"B{i}", formula, f, fmt)
    celda(ws, "A24", "Supuestos: las cuotas vencen cada mes el mismo día que la primera; interés a la "
          "TEA contando meses de 30 días (base 30/360); sin comisiones, seguros ni moras.", GRIS)
    anchos(ws, "AB", (46, 18))


def hoja_cronograma(wb):
    ws = wb.create_sheet("Cronograma")
    celda(ws, "A1", "Cronograma pactado (se recalcula con la hoja Datos)", TITULO)
    celda(ws, "A2", "Es el plan original. Si hay anticipos a capital, la próxima cuota vigente está "
          "en Resumen. En la gracia total la deuda crece y la amortización sale negativa.", GRIS)
    cabecera(ws, 4, ["N°", "Fecha", "Tipo", "Saldo inicial", "Interés", "Amortización", "Cuota",
                     "Saldo final"])
    for r in range(5, 5 + FILAS_CRONO):
        k, vacio = f"A{r}", f'B{r}=""'
        previa = "Datos!$B$7" if r == 5 else f"B{r - 1}"
        valores = {
            "A": "=ROW()-4",
            "B": f'=IF({k}>{G}+{N},"",IF({k}<={G},EDATE(Datos!$B$7,{k}),'
                 f"EDATE(Datos!$B$8,{k}-{G}-1)))",
            "C": f'=IF({vacio},"",IF({k}<={G},"Gracia","Cuota "&({k}-{G})))',
            "D": f'=IF({vacio},"",Datos!$B$5)' if r == 5 else f'=IF({vacio},"",H{r - 1})',
            "E": f'=IF({vacio},"",D{r}*((1+{TEA})^YEARFRAC({previa},B{r},4)-1))',
            "F": f'=IF({vacio},"",G{r}-E{r})',
            "G": f'=IF({vacio},"",IF({k}<={G},Datos!$B$17,{CUOTA}))',
            "H": f'=IF({vacio},"",D{r}-F{r})',
        }
        for col, v in valores.items():
            celda(ws, f"{col}{r}", v, NEGRO, FECHA if col == "B" else SOLES if col in "DEFGH" else None)
    fin = 4 + FILAS_CRONO
    celda(ws, "J4", "Totales", NEGRITA)
    for i, (rot, col) in enumerate([("Intereses", "E"), ("Capital", "F"), ("Cobrado", "G")], start=5):
        celda(ws, f"J{i}", rot)
        celda(ws, f"K{i}", f"=SUM({col}5:{col}{fin})", NEGRO, SOLES)
    anchos(ws, "ABCDEFGHIJK", (6, 12, 11, 14, 12, 14, 13, 14, 3, 12, 14))
    ws.freeze_panes = "A5"


def hoja_pagos(wb):
    ws = wb.create_sheet("Pagos")
    celda(ws, "A1", "Pagos recibidos (el saldo oficial sale de aquí)", TITULO)
    celda(ws, "A2", "Anota cada pago en la siguiente fila libre, sin dejar filas vacías (celdas "
          "amarillas). Tipo: Cuota, Pago parcial (si una cuota llega en partes: las primeras son "
          "parciales y la última es Cuota) o Anticipo a capital.", GRIS)
    celda(ws, "A3", "Ejemplo de formato: 28/02/2027 | 2218.03 | Cuota | Transferencia BCP | Cuota 1", GRIS)
    cabecera(ws, 5, ["Fecha", "Monto pagado", "Tipo", "Medio", "Nota", "Días",
                     "Interés del periodo", "Interés cobrado", "Capital amortizado",
                     "Capital pendiente", "Interés pendiente", "Deuda total"])
    celda(ws, "A6", "=Datos!B7", NEGRO, FECHA)
    celda(ws, "C6", "Desembolso")
    celda(ws, "J6", "=Datos!B5", NEGRO, SOLES)
    celda(ws, "K6", 0, NEGRO, SOLES)
    celda(ws, "L6", "=J6+K6", NEGRO, SOLES)
    for r in range(7, 7 + FILAS_PAGOS):
        p, v = r - 1, f'A{r}=""'
        for col, fmt in (("A", FECHA), ("B", SOLES), ("C", None), ("D", None), ("E", None)):
            celda(ws, f"{col}{r}", None, AZUL, fmt, AMARILLO)
        cobra = (f'IF(C{r}="{TIPOS[2]}",MIN(MAX(0,B{r}-J{p}),K{p}+G{r}),MIN(B{r},K{p}+G{r}))')
        formulas = {
            "F": (f'=IF({v},"",A{r}-A{p})', "0"),
            "G": (f'=IF({v},"",J{p}*((1+{TEA})^YEARFRAC(A{p},A{r},4)-1))', SOLES),
            "H": (f'=IF({v},"",{cobra})', SOLES),
            "I": (f'=IF({v},"",B{r}-H{r})', SOLES),
            "J": (f'=IF({v},"",J{p}-I{r})', SOLES),
            "K": (f'=IF({v},"",K{p}+G{r}-H{r})', SOLES),
            "L": (f'=IF({v},"",J{r}+K{r})', SOLES),
        }
        for col, (f, fmt) in formulas.items():
            celda(ws, f"{col}{r}", f, NEGRO, fmt)
    lista(ws, TIPOS, f"C7:C{FIN_P}")
    ws["G5"].comment = Comment("Interés sobre el capital pendiente entre el pago anterior y este, a la "
                               "TEA, contando meses de 30 días (base 30/360).", "plantilla",
                               width=300, height=80)
    ws["H5"].comment = Comment("Cuota o pago parcial: cubre primero el interés pendiente y el resto va a "
                               "capital. Anticipo a capital: va íntegro a capital y el interés queda "
                               "pendiente para la siguiente cuota.", "plantilla", width=300, height=100)
    anchos(ws, "ABCDEFGHIJKL", (12, 14, 17, 18, 18, 7, 13, 13, 13, 14, 13, 14))
    ws.freeze_panes = "A6"


def hoja_resumen(wb):
    ws = wb.create_sheet("Resumen")
    celda(ws, "A1", "Resumen al día de hoy", TITULO)
    filas = {
        3: ("Hoy", "=TODAY()", FECHA),
        4: ("Último movimiento", f"=INDEX(Pagos!$A$6:$A${FIN_P},{ULT})", FECHA),
        5: ("Capital pendiente", f"=INDEX(Pagos!$J$6:$J${FIN_P},{ULT})", SOLES),
        6: ("Interés pendiente al último pago", f"=INDEX(Pagos!$K$6:$K${FIN_P},{ULT})", SOLES),
        7: ("Interés corrido desde el último pago",
            f"=IF(B3>B4,B5*((1+{TEA})^YEARFRAC(B4,B3,4)-1),0)", SOLES),
        8: ("Deuda total a hoy (para cancelar hoy)", "=B5+B6+B7", SOLES),
        9: ("Total cobrado", f"=SUM(Pagos!$B$7:$B${FIN_P})", SOLES),
        10: ("Intereses cobrados", f"=SUM(Pagos!$H$7:$H${FIN_P})", SOLES),
        12: ("Cuotas pagadas", f'=COUNTIF(Pagos!$C$7:$C${FIN_P},"{TIPOS[0]}")', "0"),
        13: ("Cuotas vencidas a hoy (cronograma)", f'=MAX(0,MIN({N},COUNTIF({CR},"<="&B3)-{G}))', "0"),
        14: ("Cuotas atrasadas", "=IF(B8<0.5,0,MAX(0,B13-B12))", "0"),
        15: ("Estado", '=IF(B8<0.5,"Pagado",IF(B14>0,"Atrasado: "&B14&" cuota(s)","Al día"))', None),
        18: ("N° de la próxima cuota", "=B12+1", "0"),
        19: ("Fecha", f'=IF(OR(B8<0.5,B18>{N}),"",INDEX({CR},{G}+B18))', FECHA),
        20: ("Deuda ese día (antes de pagarla)",
             f'=IF(B19="",0,B5*(1+{TEA})^IF(B19>B4,YEARFRAC(B4,B19,4),0)+B6)', SOLES),
        21: ("Cuotas que quedan con el plazo original", f"=IF(B19=\"\",0,{N}-B12)", "0"),
        22: ("Cuota si reduce la cuota (mismo plazo)",
             f'=IF(B19="",0,PMT({R},B21,-B20,0,1))', SOLES),
        23: ("Cuota si reduce el plazo (misma cuota)", f'=IF(B19="",0,MIN({CUOTA},B20))', SOLES),
        24: ("Cuotas que quedan si reduce el plazo",
             f'=IF(B19="",0,ROUNDUP(NPER({R},-{CUOTA},B20,0,1)-0.000001,0))', "0"),
        25: ("Última cuota si reduce el plazo", f'=IF(B19="","",EDATE(B19,B24-1))', FECHA),
        26: ("Próxima cuota a cobrar", f'=IF({OPCION}="Reducir cuota",B22,B23)', SOLES),
    }
    for i, (rotulo, formula, fmt) in filas.items():
        f = NEGRITA if i in (8, 15, 26) else NEGRO
        celda(ws, f"A{i}", rotulo, f)
        celda(ws, f"B{i}", formula, f, fmt)
    celda(ws, "A17", "Próxima cuota", SUBTITULO)
    celda(ws, "A27", "La próxima cuota usa la opción elegida en Datos (Tras un anticipo a capital). "
          "Sin anticipos, las dos opciones dan la cuota del cronograma.", GRIS)

    celda(ws, "A30", "Intereses cobrados por año (para la declaración anual)", TITULO)
    cab = 31
    for col, t in zip("ABC", ("Año", "Interés cobrado", "IR estimado")):
        celda(ws, f"{col}{cab}", t, NEGRITA, relleno=CABECERA)
    for i, anio in enumerate(range(2026, 2032), start=cab + 1):
        celda(ws, f"A{i}", str(anio))
        celda(ws, f"B{i}", f'=SUMIFS(Pagos!$H$7:$H${FIN_P},Pagos!$A$7:$A${FIN_P},">="&DATE({anio},1,1),'
              f'Pagos!$A$7:$A${FIN_P},"<="&DATE({anio},12,31))', NEGRO, SOLES)
        celda(ws, f"C{i}", f"=B{i}*Datos!$B$11", NEGRO, SOLES)
    celda(ws, f"A{cab + 8}", "El interés se declara en el año en que se cobra.", GRIS)
    anchos(ws, "ABC", (46, 16, 14))


def main():
    wb = Workbook()
    hoja_datos(wb)
    hoja_cronograma(wb)
    hoja_pagos(wb)
    hoja_resumen(wb)
    wb.calculation.fullCalcOnLoad = True
    wb.save(sys.argv[1])
    print("ok", sys.argv[1])


if __name__ == "__main__":
    main()
