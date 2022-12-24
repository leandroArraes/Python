class ContaCorrente:
		def __init__(self,conta,nome):
			self.conta = conta
			self.nome = nome
			self.saldo = 0
	
		def setNome(self,nome):
			self.nome = nome
			print(f'Você Alterou o nome para {nome}')
	
		def deposito(self,valor):
			self.saldo = self.saldo + valor
		
		def sacar(self,saque):
			self.saldo = self.saldo - saque
			print(f'Você sacou R$: {saque}')
		
		def getSaldo(self):
			return self.saldo

cc= ContaCorrente(1234,'leo')
print(vars(cc))

cc.setNome('Leandro')

cc.deposito(1000)
print(vars(cc))

cc.sacar(5)
print(vars(cc))

print(f'saldo R$: {cc.getSaldo()}')