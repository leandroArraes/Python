'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem'''

lista = [ ]
valor = 0
cont = 0
while valor >= 0:
	valor = int(input('valor: '))
	if valor > 0:
		lista.append(valor)
	cont += 1
cont-=1
print(f'Valores Lidos \n{lista}')
for i in range(cont-1,-1,-1):
	print(lista[i],end=(' '))
print(end=('\n'))
print(f'Soma dos Valores {sum(lista)}')
media = sum(lista)/len(lista)
print('Media dos Valores %1.1f'%media)

for i in lista:
	if i > media:
		print(f'Valores acima da media --> {i} ')

for i in lista:
	if i < 7:
		print(f'Valor abaixo de 7 -- > {i}')

print('=== Fimmm ===')
	