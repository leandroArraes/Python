'''Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N'''

def nValor(num):
	if num == 0:
		return 0
	else:
		return nValor(num-1)+ num

print(nValor(10))
	