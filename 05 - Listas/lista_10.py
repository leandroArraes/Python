'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''

lista1= [0+a for a in range(1,11)]
lista2= [10+a for a in range(10,20)]
lista3 = []

for a in range(0,10):
	lista3.append(lista1[a])
	lista3.append(lista2[a])
print(lista1)
print(lista2)	
print(lista3)
print(len(lista3))