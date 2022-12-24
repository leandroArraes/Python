class ContaInvestimento:
		def __init__(self,saldo,tJuros : float):
			self.saldo = saldo
			self.taxaDeJuros = tJuros
			
		def setSaldo(self,sado):
			self.saldo=saldo
			
		def setTjuros(self,valor):
			self.taxaDeJuros = valor
		
		def addJuros(self,valor):
			a = (self.saldo + (self.saldo* self.taxaDeJuros))
			b = a + (a*valor)
			self.saldo= a+b

conta1= ContaInvestimento(1000,0.10)
conta1.addJuros(0.01)
conta1.addJuros(0.01)
conta1.addJuros(0.01)
conta1.addJuros(0.01)
conta1.addJuros(0.01)

print('%1.2f'%conta1.saldo)
		
		