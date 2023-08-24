class Forma:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


class retangulo (Forma):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)

    def areaRetangulo (self):
        area = self.largura * self.altura
        return area


class triangulo (Forma):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)

    def areaTriangulo (self):
        area = self.largura * self.altura / 2
        return area


retangulinho = triangulo(10, 15)
print(retangulinho.areaTriangulo())