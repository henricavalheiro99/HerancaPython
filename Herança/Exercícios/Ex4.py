class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Livro (Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class Eletronico (Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.autor = voltagem


livrinho = Livro("One Piece", 20, "Eichiro Oda")
print(livrinho.nome)

