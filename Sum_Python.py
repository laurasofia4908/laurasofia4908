animales = ["perro", "gato", "pato", "pingüino", "pulpo", "puma", "paloma", "pájaro", "pez"]

animales_con_p = [animal for animal in animales if animal.startswith("p")]

print("Animales que comienzan con la letra P:")
for animal in animales_con_p:
    print(animal)
