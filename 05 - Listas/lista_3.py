'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

lista= [ ]
for i in range(4):
	lista.append(int(input('Nota: ')))

media = sum(lista)/len(lista)
print(f'\nA media é: {media}')