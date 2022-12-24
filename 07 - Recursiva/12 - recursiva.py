''' Faça uma função recursiva que receba um número inteiro
positivo N e imprima todos os números naturais de 0 até N em ordem crescente. '''

def imprimir(n):
    if n == 1:
        return 1
    else:
        return imprimir(n-1)

print(imprimir(10))