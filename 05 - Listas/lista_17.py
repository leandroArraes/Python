'''17 )  Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos 

e depois informe o nome, os saltos e a média dos saltos.
 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3 '''

salto = [ ]
nome = input('Nome: ')
print()
for a in range(5):
	salto.append(float(input('Distancia: ')))
media= sum(salto)/len(salto)
print()
print('Nome:',nome)

print(
f'\nPrimeiro Salto: {salto[0]} m\n'
f'Segundo  Salto: {salto[1]} m\n'
f'Terceiro Salto: {salto[2]} m \n'
f'Quarto   Salto: {salto[3]} m\n'
f'Quinto   Salto: {salto[4]} m \n '
)

print('Media',media)