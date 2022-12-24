class VirtualPet:
	def __init__(self,nome):
		
		self.nome = nome
		self.comida  = 50
		self.saude = 75
		self.idade  = 0.1
		self.humor = int((self.comida+self.saude)/2)
		self.vida = self.comida > 1
		 

		
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

	def Alimentar(self):
		if self.comida <= 90:
			self.comida += 10
		else:
			self.saude = 100

		if self.saude <= 95:
			self.saude += 5
		else:
			self.saude = 100

	def getHumor(self):
		return f'  - Humor:   {self.humor}/100'

	def brincar(self):
		if self.humor <= 75:
			self.humor += 15
		else:
			self.humor = 100
		if self.saude <=75:
			self.saude  += 15
		else:
			self.saude = 100
		if self.comida >= 20:
			self.comida -= 20
		else:
			self.comida = 0


def AlimentarTodos():
	for a in range(len(fazenda)):
		fazenda[a].Alimentar()
	print('\n','-'*22)
	print('Todos Animais Alimentados\n')
	for a in range(len(fazenda)):
		print(fazenda[a].getNome())
	Manu()

def PetAdd():
	n= int(input('Quantos Animais quer Adicinar a sua Fazenda: '))
	for a in range(n):
		addPet(fazenda)
	Menu()
	

def addPet(lista):
	nome = str(input("  - Nome do Pet: "))
	pet = VirtualPet(nome)
	lista.append(pet)
	#return print(f'  - {nome} Adicionado a fazenda \n')

def reAddPet():
	chave = "S"
	while chave == "S":
		chave = input("\n  - Deseja Adicionar Animal a sua fazenda [S/N]: ").upper()
		if chave == "S":
			addPet(fazenda)
		else:
			chave = "N"
			Menu()

def verFazenda():
	remover()
	total = len(fazenda)
	#print('='*20)
	print(' Animais da Fazenda')
	print('=' * 20)
	if total == 0:
		print('\n  --> Fazenda sem animais\n')
		PetAdd()
	else: 
		for a in range(total):
			print(f'{a+1} - {fazenda[a].nome}')
		verPet()


def verPet():
	num = int(input('Digite o n° do animal que deseja ver: '))
	num -=1
	if num < len(fazenda):
		print('\n')
		print('='*20)
		print('  *** Seu Pet ***\n')
		print(f'  - Nome: {fazenda[num].getNome()}')
		print(f'  - Idade: {fazenda[num].getIdade()}')
		print(f'  - Saude: {fazenda[num].getSaude()}/100')
		print(f'  - Comida: {fazenda[num].getComida()}/100')
		print(f'{fazenda[num].getHumor()}')
		interaPet()
		return (n == num)
		
		
def interaPet():
	print('-'*20)
	print('      Interagir')
	print('-'*20)
	print('1 | Alimentar\n2 | Brincar \n3 | Ver outro\n4 | Menu Principal')
	interacao = int(input('Digite a opção: ')) 
	if interacao == 1:
		 fazenda[n].Alimentar()
		 print(f'  - Comida: {fazenda[n].getComida()}/100')
		 interaPet()
	elif interacao == 2:
		fazenda[n].brincar()
		print('\n  --> Brincando...\n')
		interaPet()
	elif interacao == 3:
		verFazenda()
		verPet()
	else:
		Menu()



def Menu():
	print('=' * 22)
	print(' Painel Do Fazendeiro ')
	print('=' * 22)
	print('1 | Ver Animais'
		  '\n2 | Adicionar Animais'
		  '\n3 | Alimentar Animal')
	print('-' * 22)
	resposta = int(input("Informe a opção: "))
	print('-' * 22,'\n')
	if resposta == 1:
		verFazenda()
	elif resposta == 2:
		PetAdd()
	elif resposta == 3:
		AlimentarTodos()       

def remover():
    for a in range(len(fazenda)):
        if fazenda[a].comida < 1 :
            print('\n','-'*22)
            print(f'   !!! {fazenda[a].getNome()} Morreu !!! ')
            print('-'*22,'\n')
            fazenda.pop(a)
            break  
 

                  
n = 0
fazenda= []

Menu()






