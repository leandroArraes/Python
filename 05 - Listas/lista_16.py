'''Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.'''

semana = 200
pVenda = 0.09
lista = [ ]

aux=0
lim= int(input('Quantas Vendas ? '))
while aux <= lim:
	venda = int(input('Total em vendas R$: '))
	total= semana + (venda*pVenda)
	lista.append(total)
	aux+=1
print()	

cont = 0
m=0
print(lista)
print()

for x in range(200,1000,100):
	for b in lista:
		if ((b >= x ) and (b <= (x+99)) ) :
			cont+=1
	if cont > 0:
		print(f'Entre {x} e {x+99} --> {cont}')	
	cont=0
	
for c in lista:
		if c > 999:
			m+=1
print('Maior que 999 -->',m)