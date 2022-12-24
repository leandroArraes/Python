'''A multiplicação de dois números inteiros pode ser feita através de somas sucessivas.
Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros. '''

def Multip_Rec(a,b):
	if a == 0 or b == 0:
		return 0
	if b == 1:
		return a
	return a + Multip_Rec(a, b - 1)

print(Multip_Rec(8,10))