'''Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192. '''
lista=[ ]
num = 762021192
ultimo = num % 10
resto = num//10

cont =0
 
while resto  != 0:
	ultimo = num % 10
	print(ultimo)
	num = num//10
	
	
def verifica(num,cont,aux):
    if num==0:
        return cont
    
    else:
        if aux==(num//10):
            cont += 1
            num=num//10
            return verifica(num,cont,aux)
        else:            
            num=num//10
            return verifica(num,cont,aux)
    print('numero',aux,'encontrado',c,'vezes')

cont=0    
num=int(input('digite um numero: '))
aux=int(input('digite o numero que procura: '))
verifica(num,c,aux)
print('encontrei',aux,cont,'vezes.')
	
	
	



