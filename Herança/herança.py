class Carro:
    def __init__(self, nome, cor, marca):
        self.nome = nome
        self.cor = cor
        self.marca = marca

    def ligar(self):
        print("Ligando", self.nome)


class Carro2:
    def __init__(self, ano):
        self.ano = ano

    def Farol (self):
        print("Acendendo as luzes")

    def Acelerar (self):

        print("Acelerando....")


class CarroCitroen (Carro, Carro2):
    def __init__(self, nome, cor, portas, ano):
        Carro.__init__(self, nome, cor, "Citroen")
        Carro2.__init__(self, ano)
        self.portas = portas


    def ligar(self):
        print("Citroen tá ligano aí pae")


Car = CarroCitroen("Cactus", "Azul", 2, 2022)
print(Car.nome)

