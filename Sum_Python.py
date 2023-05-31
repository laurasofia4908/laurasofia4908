class Receta:
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pasos = pasos

    def imprimir_receta(self):
        print("Receta: {}".format(self.nombre))
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            print("- {}".format(ingrediente))
        print("Pasos:")
        for i, paso in enumerate(self.pasos, 1):
            print("{}. {}".format(i, paso))

receta_pizza = Receta("Pizza", ["Masa de pizza", "Salsa de tomate", "Queso", "Pepperoni"], 
                      ["Precalienta el horno a 200 grados Celsius.",
                       "Extiende la masa de pizza sobre una bandeja para horno.",
                       "Unta la salsa de tomate sobre la masa.",
                       "Espolvorea el queso y distribuye el pepperoni sobre la pizza.",
                       "Hornea durante 15-20 minutos o hasta que la masa esté dorada y el queso derretido."])

receta_pizza.imprimir_receta()
