'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''

idade= []
altura = [ ]

for a in range(3):
	print(f'==== {a+1}° Pessoa ====')
	for i in range(1):
		idade.append(int(input('Idade: ')))
		altura.append(float(input('Altura: ')))
		print()
print(idade)
print(altura)
print()
for a in range(len(idade)-1,-1,-1):
	print(idade[a] , end='  ',)
print()
for i in range(len(altura)-1,-1,-1):
	print(altura[i], end='  ')
	