class Retangulo():
    def __init__(self, comprimento, largura):
        self.setComprimento(comprimento)
        self.setLargura(largura)

    def setComprimento(self, comprimento):
        self.comprimento = comprimento
    def setLargura(self, largura):
        self.largura = largura
    def getComprimento(self):
        return self.comprimento
    def getLargura(self):
        return self.largura
    def area(self):
        return self.largura * self.comprimento
    def perimetro(self):
        return (2* self.comprimento) + (2 * self.largura)

comp = float(input('informe o valor do comprimento: '))
larg = float(input('informe o valor da largura: '))

r= Retangulo(comp,larg)
print("A área é:",r.area())
print("o Primeiro é:", r.perimetro())