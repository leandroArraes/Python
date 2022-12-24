class Macaco:
	def __init__(self):
		self.nome = None
		self.bucho = []
	
	def setNome(self,nome):
		self.nome = nome
		
	def come(self,alimento):
		self.bucho.append(alimento)
		return print('Estomago',self.bucho)
	
	def getNome(self):
		return self.nome
	
	def getBucho(self):
		return self.bucho

bilico= Macaco()
bilico.setNome('zé')
bilico.come('morango')
print(vars(bilico))

zeze=Macaco()
zeze.setNome('zezé')
zeze.come(bilico.getNome())
print(vars(zeze))