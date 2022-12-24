'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa'''

lista = []
for i in range(1,11):
	lista.append(i)

for i in range(len(lista)-1,-1,-1):
	print(lista[i])