'''7) Crie um programa em C que receba um vetor de números reais com 100 elementos. Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor. '''


def inverter(lista):
    if not lista: # lista vazia, retorna ela mesma
        return lista
    return lista[-1:] + inverter(lista[:-1])

lista = []
cont = 1 
while cont <= 100:
	lista.append(cont)
	cont+=1
print(lista)
print()
print(inverter(lista))