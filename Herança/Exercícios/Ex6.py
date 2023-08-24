class Empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


class Filha (Empregado):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

Lara = Filha("Lara", 600, "senai")
print(Lara.setor)