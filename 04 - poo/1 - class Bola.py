class Bola:
	def __init__(self,cor, circuferencia,material):
		
		self.cor = cor 
		self.circuferencia = circuferencia
		self.material = material
		
	def setTrocarCor (self,cor):
		self.cor = cor 
	
	def setCircuferencia (self,circuferencia):
		self.circuferencia = circuferencia
	
	def setMaterial(self,material):
		self.material = matetial
	
	def getCor (self):
		return self.cor
		
	def getCircuferencia(self):
		return self.circuferencia
	
	def getMaterial(self):
		return self.material
	
b = Bola('azul',20,'coro')
print(vars(b))

b.setTrocarCor('branca')
print(vars(b))