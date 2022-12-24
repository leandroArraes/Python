'''Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321'''


def inverter(num):
	n =''	
	for i in range(len(num)-1,-1,-1):
		a = num[i]
		n += a
	return n

n = input('inverter valor: ')
m = inverter(n)
print('Valor inverso de %s  é %s'%(n,m))
	