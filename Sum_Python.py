# Diccionario de recetas
recetas = {
    "panqueques": {
        "ingredientes": ["harina", "azúcar", "leche", "huevos"],
        "pasos": ["Mezclar los ingredientes secos en un tazón.", "Agregar la leche y los huevos.", "Mezclar bien hasta obtener una masa suave.", "Calentar una sartén y verter la masa.", "Cocinar por ambos lados hasta que estén dorados."]
    },
    "ensalada": {
        "ingredientes": ["lechuga", "tomate", "cebolla", "pepino"],
        "pasos": ["Lavar y cortar los ingredientes.", "Mezclar todo en un tazón.", "Aliñar con aceite, vinagre, sal y pimienta al gusto."]
    },
    "pasta": {
        "ingredientes": ["pasta", "salsa de tomate", "cebolla", "ajo"],
        "pasos": ["Cocinar la pasta según las instrucciones del paquete.", "En una sartén, sofreír la cebolla y el ajo.", "Agregar la salsa de tomate y cocinar a fuego lento.", "Escurrir la pasta y mezclar con la salsa.", "Servir caliente."]
    }
}

# Función para mostrar una receta
def mostrar_receta(nombre):
    receta = recetas.get(nombre)
    if receta:
        print("Receta de", nombre.capitalize())
        print("Ingredientes:")
        for ingrediente in receta["ingredientes"]:
            print("- ", ingrediente)
        print("Pasos:")
        for paso in receta["pasos"]:
            print("- ", paso)
    else:
        print("No se encontró la receta", nombre)

# Ejemplo de uso
mostrar_receta("panqueques")
