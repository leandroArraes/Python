class Carro:
	def __init__(self):
		self.kmLitro = 15
		self.tanque = 10
		
	def dirigir(self,distancia):
		consumo = distancia/self.kmLitro
		self.tanque -= consumo
		return consumo
	
	def obterGasolina(self):
		return self.tanque
	def addGasolina(self,litros):
		self.tanque += litros

a = Carro()
print(f'Consumo do carro: {a.kmLitro} km/litro')
print(f'Nivel do Tanque: {a.tanque} Litros\n')
b = float(input('Dirigir Quantos km: '))
c = a.dirigir(b)
print(f'Dirigir a Distancia de {b} km consumiu %1.1f litros '%c)
print('Tanque: %1.2f Litros'%a.tanque)
a.addGasolina(40)
print(vars(a))
			
		