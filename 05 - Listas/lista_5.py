'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''

lista = [ ]
par = [ ]
impar= [ ]
for a in range(1,21):
	lista.append(a)
	if a % 2  == 0:
		par.append(a)
	else:
		impar.append(a)
print(lista)
print(f'Par: {par}')
print(f'Impar: {impar}')