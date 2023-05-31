class Palabras:
    def __init__(self):
        self.palabras = ["taza", "tigre", "tomate", "tren", "televisión", "tarjeta", "teléfono", "tiempo", "tesoro"]

    def palabras_con_letra(self, letra):
        return [palabra for palabra in self.palabras if palabra.startswith(letra)]


letra = input("Ingresa una letra: ")

objeto_palabras = Palabras()
palabras_con_letra_t = objeto_palabras.palabras_con_letra(letra)

print("Palabras que comienzan con la letra", letra + ":")
for palabra in palabras_con_letra_t:
    print(palabra)
