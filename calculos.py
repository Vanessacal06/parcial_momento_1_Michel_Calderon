def calcular_nomina(lista_empleados):
    print("\n NÓMINA CALCULADA \n")

    SALARIO_MINIMO = 1750000
    AUX_TRANSPORTE = 160000
    DESCUENTO = 0.08

    if len(lista_empleados) == 0:
        print("No hay empleados registrados")
        return

    for emp in lista_empleados:
        try:
            salario_base = emp["salario_base"]
            dias = emp["dias_trabajados"]

            salario_proporcional = (salario_base / 30) * dias

            auxilio = 0
            if salario_base < (SALARIO_MINIMO * 2):
                auxilio = AUX_TRANSPORTE

            bruto = salario_proporcional + auxilio
            descuento = bruto * DESCUENTO
            neto = bruto - descuento

            print(f"""
Empleado: {emp['nombre']}
Salario base: {salario_base}
Días trabajados: {dias}
Auxilio: {auxilio}
Descuento (8%): {descuento}
TOTAL A PAGAR: {neto}
----------------------------
""")

        except KeyError:
            print("Error en los datos del empleado")