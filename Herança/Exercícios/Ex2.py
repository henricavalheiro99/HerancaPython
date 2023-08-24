class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("som")


class Cachorro (Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print("AuAu")


class Gato (Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print("Miau")


class Vaca(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print("Muuuu")


Nicolas = Cachorro("Nicolas")
Nicolas.fazer_som()
