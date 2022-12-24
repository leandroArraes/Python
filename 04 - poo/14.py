import math

class Funcionario:
	def __init__(self,nome ,salario : float):
		self.nome = nome
		self.salario = salario
	
	def getNome(self):
		return self.nome
	def getSalario(self):
		return self.salario
		
	def aumentarSalario(self,valor : float):
		self.salario =  self.salario+ (self.salario * (valor/100))
		

nome = input('Nome: ')
salario = float(input('Salario R$: '))
pessoa = Funcionario(nome,salario)


print(f'\nFuncionario: {pessoa.getNome()}\nSalario R$: {pessoa.getSalario()}\n')

aumento= float(input('Percentual de aumento %'))
pessoa.aumentarSalario(aumento)
print('Salario com Aumento R$:',pessoa.getSalario())
		