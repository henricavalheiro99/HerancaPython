class Instrumento:
    def __init__(self, nome):
        self.nome = nome

    def tocando(self):
        print("som")

class Violino (Instrumento):
    def __init__(self, nome):
        super().__init__(nome)

    def tocando(self):
        print("Violino tocando")


class Piano (Instrumento):
    def __init__(self, nome):
        super().__init__(nome)

    def tocando(self):
        print("Piano tocando")


class Flauta(Instrumento):
    def __init__(self, nome):
        super().__init__(nome)

    def tocando(self):
        print("Flauta tocando")


flauta = Flauta("flautinha")
flauta.tocando()


