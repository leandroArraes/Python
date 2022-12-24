class Quadrado:
	def __init__(self,lado):
		self.lado = lado
		self.area  = lado*lado
		
	def setLado(self,lado):
		self.lado = lado
	
	def getLado(self):
		return self.lado
	
	def getArea(self):
		return self.area

q = Quadrado(10)
print(vars(q))

#altera o valor do lado
q.setLado(15)
print(vars(q))
#mostra o valor do lado
print(q.getLado())

#mostra area do quadrado
print(q.getArea())
