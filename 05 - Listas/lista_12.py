'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.'''

idade = [10+a for a in range(1,11)]
altura= [1.3,1.4,1.5,1.4,1.3,1.5,1.7,1.65,1.72,1.78]
alturaMedia= sum(altura)/len(altura)

print(idade)
print(altura)
print(alturaMedia)

cont=0
for i in range(0,9):
	if idade[i] > 13 and altura[i] < alturaMedia:
		cont+=1
print(cont)