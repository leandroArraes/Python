class BombaCombustivel:
	def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
		self.tipoCombustivel = tipoCombustivel
		self.valorLitro = valorLitro
		self.quantidadeCombustivel = quantidadeCombustivel
		
	def abastecerPorValor(self,valor):
		return valor/ self.valorLitro
	def abastecerPorLitro(self,litro):
		return litro*self.valorLitro
	def setValorLitro(self,valor):
				self.valorLitro = valor
	def setTipoCombistivel(self,tipo):
				self.tipoCombustivel = tipo
				
	def setQuantidadeCombustivel(self,qt):
				self.quantidadeCombustivel = qt
				
posto1 = BombaCombustivel('gas',5.0,100)

posto1.valorLitro = 5

print(vars(posto1))
print(posto1.abastecerPorValor(50))
print(posto1.abastecerPorLitro(5))

