def solicitar_datos():
    estudiante = {}

    estudiante["nombre"] = input("Nombre del estudiante: ").strip()

    while True:
        try:
            edad = int(input("Edad: "))
            if edad > 0:
                estudiante["edad"] = edad
                break
            print("La edad debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    estudiante["carrera"] = input("Carrera: ").strip()

    while True:
        try:
            promedio = float(input("Promedio (0 a 10): "))
            if 0 <= promedio <= 10:
                estudiante["promedio"] = promedio
                break
            print("El promedio debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    return estudiante


def mostrar_ficha(estudiante):
    print("\n" + "=" * 35)
    print("       FICHA DEL ESTUDIANTE")
    print("=" * 35)
    print(f"Nombre:   {estudiante['nombre']}")
    print(f"Edad:     {estudiante['edad']} años")
    print(f"Carrera:  {estudiante['carrera']}")
    print(f"Promedio: {estudiante['promedio']:.2f}")
    print("=" * 35)


def main():
    estudiante = solicitar_datos()
    mostrar_ficha(estudiante)


if __name__ == "__main__":
    main()