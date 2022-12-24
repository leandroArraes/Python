'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0'''

media = [ ]
nota=0

for i in range(0,10):
	print(f'Notas do {i+1}° Aluno')
	for a in range(0,4):
		valor = float(input(f' {a+1}° Nota: '))
		nota += valor
	print()
	media.append(nota/4)
	nota = 0

print(f'Media dos Alunos: {media}')