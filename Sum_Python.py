# Crear una cadena
nombre = "Luisa"

# Acceder a caracteres de la cadena
primer_caracter = nombre[0]
print(primer_caracter)  # Output: "L"

# Obtener la longitud de la cadena
longitud = len(nombre)
print(longitud)  # Output: 5

# Concatenar cadenas
apellido = "López"
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Output: "Luisa López"

# Convertir a mayúsculas o minúsculas
nombre_mayusculas = nombre.upper()
print(nombre_mayusculas)  # Output: "LUISA"

nombre_minusculas = nombre.lower()
print(nombre_minusculas)  # Output: "luisa"
