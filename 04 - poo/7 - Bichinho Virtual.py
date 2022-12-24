class VirtualPet:
	def __init__(self,nome,comida,saude,idade):
		
		self.nome = nome
		self.comida  = comida					
		self.saude = saude
		self.idade  = idade
		
	def setNome(self,nome):
		self.nome = nome
		
	def setComida(self,comida : int):
		self.comida = comida
		
	def setSaude(self,saude : int):
		self.saude = saude
		
	def setIdade(self,idade):
		self.idade = idade
	
	def getNome(self):
		return self.nome
	def getComida(self):
		return self.comida
	def getSaude(self):
		return self.saude
	def getIdade(self):
		return self.idade
		
		
	def getHumor(self):
		humor = (self.comida+self.saude)/2
		if humor <= 40:
			return print('Humor: Irritado')
		elif humor >= 70:
			return print('Humor: Feliz')
		

	
		
gato= VirtualPet('lua',5,30,1)
print(vars(gato))
gato.setComida(80)
gato.setSaude(80)
gato.setNome('sol')
gato.getHumor()
print(vars(gato))
	