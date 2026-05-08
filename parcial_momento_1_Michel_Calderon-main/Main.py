empleados = []

def mostrar_menu():
    print("\n SISTEMA DE NÓMINA STARTUP ")
    print("1. Registrar empleado")
    print("2. Calcular nómina")
    print("3. Salir")
    print("****************************************")

# 🔹 Validar nombre (solo letras y espacios)
def validar_nombre(nombre):
    if nombre.replace(" ", "").isalpha():
        return True
    return False

def registrar_empleado():
    print("\n--- REGISTRO DE EMPLEADO ---")

    # 🔹 Validación de nombre
    while True:
        nombre = input("Nombre del empleado: ").strip()

        if validar_nombre(nombre):
            nombre = nombre.lower()
            break
        else:
            print("Error: el nombre solo debe contener letras")

    # 🔹 Validación de salario
    while True:
        try:
            salario_base = float(input("Salario base: "))
            if salario_base <= 0:
                print("Error: el salario debe ser mayor a 0")
            else:
                break
        except ValueError:
            print("Error: ingrese un número válido")

    # 🔹 Validación de días
    while True:
        try:
            dias_trabajados = int(input("Días trabajados (0-30): "))
            if 0 <= dias_trabajados <= 30:
                break
            else:
                print("Error: los días deben estar entre 0 y 30")
        except ValueError:
            print("Error: ingrese un número entero")

    empleado = {
        "nombre": nombre,
        "salario_base": salario_base,
        "dias_trabajados": dias_trabajados
    }

    empleados.append(empleado)
    print("Empleado registrado correctamente ✔")

def main():
    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                registrar_empleado()

            elif opcion == "2":
                import calculos
                calculos.calcular_nomina(empleados)

            elif opcion == "3":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida")

        except Exception as e:
            print("Ocurrió un error inesperado:", e)

if __name__ == "__main__":
    main()


    # Proyecto finalizado por Michel Calderon