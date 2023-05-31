recetas = {}

def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes (separados por comas): ").split(",")
    instrucciones = input("Ingrese las instrucciones: ")
    recetas[nombre] = {"ingredientes": ingredientes, "instrucciones": instrucciones}
    print("Receta agregada con éxito.")

def mostrar_recetas():
    if len(recetas) == 0:
        print("No hay recetas disponibles.")
    else:
        for nombre, receta in recetas.items():
            print("\nNombre: ", nombre)
            print("Ingredientes: ", ", ".join(receta["ingredientes"]))
            print("Instrucciones: ", receta["instrucciones"])

while True:
    print("\n--- MENÚ ---")
    print("1. Pizza")
    print("2. Mostrar recetas")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1"pizza
        agregar_receta()
    elif opcion == "2":
        mostrar_recetas()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
