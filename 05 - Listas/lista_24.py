'''Faça um programa que simule um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados em um vetor .
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios,
simulando os lançamentos dos dados.'''

import random
numero = random.randint(1,6)
vetor = [ ]
cont = 0
while cont < 101 :
	vetor.append(int(random.randint(1,6)))
	cont+=1

print(vetor)

aux = {}
c=0
for a in set(vetor):
	c=0
	for b in range(len(vetor)):
		if a == vetor[b]:
			c+=1
	aux[a]=c
print(aux)
for a in aux:
	print(f'Numero {a}  Caiu --> {aux[a]} Vezes')
