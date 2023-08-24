class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class aluno (pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula


Miguel = aluno("Miguel", 16, "matriculado")
print(Miguel.matricula)