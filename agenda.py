def agregar_contacto(agenda, nombre, telefono, email):
    """Agrega un contacto (diccionario) a la agenda."""
    agenda.append({"nombre": nombre, "telefono": telefono, "email": email})


def buscar_contacto(agenda, nombre):
    nombre = nombre.lower()
    return [c for c in agenda if nombre in c["nombre"].lower()]


def eliminar_contacto(agenda, nombre):
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            agenda.remove(contacto)
            return True
    return False


def listar_contactos(agenda):
    """Muestra todos los contactos."""
    if not agenda:
        print("La agenda está vacía.")
        return
    print(f"\n{'#':<4}{'Nombre':<20}{'Teléfono':<15}{'Email'}")
    print("-" * 60)
    for i, c in enumerate(agenda, start=1):
        print(f"{i:<4}{c['nombre']:<20}{c['telefono']:<15}{c['email']}")


def mostrar_menu():
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Listar contactos")
    print("5. Salir")


def main():
    agenda = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            telefono = input("Teléfono: ").strip()
            email = input("Email: ").strip()
            if nombre:
                agregar_contacto(agenda, nombre, telefono, email)
                print(f"Contacto '{nombre}' agregado.")
            else:
                print("El nombre no puede estar vacío.")

        elif opcion == "2":
            texto = input("Nombre a buscar: ").strip()
            resultados = buscar_contacto(agenda, texto)
            if resultados:
                listar_contactos(resultados)
            else:
                print("No se encontraron contactos.")

        elif opcion == "3":
            nombre = input("Nombre exacto del contacto a eliminar: ").strip()
            if eliminar_contacto(agenda, nombre):
                print(f"Contacto '{nombre}' eliminado.")
            else:
                print("No se encontró ese contacto.")

        elif opcion == "4":
            listar_contactos(agenda)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()