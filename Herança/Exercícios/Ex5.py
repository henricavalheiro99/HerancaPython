class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro (veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = cor

class Moto (veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = cor

carrinho = Carro("Skooda", "Octavia", 2018, "prata")
print(carrinho.cor)