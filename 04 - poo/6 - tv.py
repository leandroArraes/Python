def menu(tv):
			n = 0
			while n != 4:
				print(
				'*******************\n'
				'  Controle Remoto\n'
				'-------------------\n'
				'\n1) Mudar canal\n'
				'2) Aumentar Volume\n'
				'3) Dimunuir Volume\n'
				'4) Desligar\n'
				'-------------------')
				n = int(input('Digite a Opção: '))
				
				if n == 1:
					tv.setCanal()
				elif n == 2:
					tv.volumeUp()
				elif n == 3:
					tv.volumeDown()
				elif n== 4 :
					print('\n --->     Desligando Tv')
				else:
					print('\n --->   Opção Invalida\n ')
class Tv:
	def __init__(self):
		self.canal = None
		self.volume = 3
	
	def setCanal(self):
		
		canal = int(input('Digite o Canal: '))
		if canal > 0 and canal < 11:
			self.canal = canal
			print(f'\n ---> Assistindo canal {self.canal}/10\n')
			
		else:
			return print(f'\n--------------------\n'
			 f'Canal {canal} é invalido !!!\n')

	def volumeUp(self):
		if self.volume <= 9:
			self.volume = self.volume + 1
			return print(f'\n --->    Volume em {self.volume}/10\n')
		else:
			return print('\n ---> Volume máximo 100/100\n')
			
	def  volumeDown(self):
		if self.volume >1:
			self.volume = self.volume -1
			return print(f'\n --->  Volume em {self.volume}/10\n')
		else:
			return print('\n  --> Volume: Mudo\n')

controle = Tv()
menu(controle)