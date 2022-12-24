num = 1
votos = [ ]
while num != 0:
	num = int(input('Numero: '))
	if num > 0 and num <= 23:
		votos.append(num)
	elif num > 6:
		print('\n ==== Valor Invalido ====\n')

print(f'\nTotal de votos: {len(votos)}\n')
 
total=[ ]
pct=100/len(votos)
melhor = 0

for a in set(votos):
	x = votos.count(a)
	total.append(x)
	if x > melhor:
		melhor = a
		print()
	print(f'Sistema: {a}  teve --> {x} Votos = --> {pct*x} % dos votos ')

print('\nSistema mais Votado -->',melhor)