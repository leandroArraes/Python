'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada'''
lista1= [0+a for a in range(1,11)]
lista2= [10+a for a in range(1,11)]
lista3 = [21+a for a in range(1,11)]
lista4=[ ]

for a in range(0,10):
	lista4.append(lista1[a])
	lista4.append(lista2[a])
	lista4.append(lista3[a])

print(lista1)
print(lista2)	
print(lista3)
print()
print(lista4)
