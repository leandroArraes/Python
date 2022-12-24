'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''

lista = [ 'abcdefghij']
vogal= ['aeiou']
cont = 0

for i in range(len(lista[0])):
	c = lista[0][i]
	for a in range(len(vogal[0])):
		v = vogal[0][a]
		if c == v:
			cont+=1
totalConsoantes = len(lista[0])-cont			
print(f'Total de consoantes é: {totalConsoantes}')