class Pessoa():
    def __init__(self,nome, idade,peso, altura):
        self.setNome(nome)
        self.setIdade(idade)
        self.setPeso(peso)
        self.setAltura(altura)

    def setNome(self,nome):
        self.nome = nome
    def setIdade(self,idade):
        self.idade = idade
    def setPeso(self,peso):
        self.peso = peso
    def setAltura(self,altura):
        self.altura = altura

    def envelhecer (self,anos):
        self.idade += anos
        if (self.idade < 21):
            self.crescer(0.5)
    def crescer(self,altura):
        self.altura += altura
    def engordar(self,peso):
        self.peso += peso
    def emagrecer(self,peso):
        self.peso -= peso

p = Pessoa('leo',31,80,172)
print(vars(p))
p.engordar(5)
print(vars(p))
p.emagrecer(12)
print(vars(p))
p.envelhecer(1)
print(vars(p))

