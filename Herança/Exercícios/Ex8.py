class Bebida:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo


class Suco (Bebida):
    def __init__(self, nome, tipo, doce):
        super().__init__(nome, tipo)
        self.doce = doce


class Cerveja (Bebida):
    def __init__(self, nome, tipo, doce):
        super().__init__(nome, tipo)
        self.doce = doce

cervejinha =Cerveja("Skol", "alcoólica", "não")
print(cervejinha.doce)