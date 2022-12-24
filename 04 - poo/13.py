class Funcionario:
	def __init__(self,nome ,salario):
		self.nome = nome
		self.salario = salario
	
	def getNome(self):
		return self.nome
	def getSalario(self):
		return self.salario

nome = input('Nome: ')
salario = float(input('Salario R$: '))
pessoa = Funcionario(nome,salario)

print(f'\nFuncionario: {pessoa.getNome()}\nSalario R$: {pessoa.getSalario()}')
