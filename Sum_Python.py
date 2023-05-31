palabras = ["lápiz", "león", "luna", "libro", "largo", "luz", "lindo", "leche", "lugar"]

letra = input("Ingresa una letra: ")

palabras_con_letra = [palabra for palabra in palabras if palabra.startswith(letra)]

print("Palabras que comienzan con la letra", letra + ":")

for palabra in palabras_con_letra:
    print(palabra)
