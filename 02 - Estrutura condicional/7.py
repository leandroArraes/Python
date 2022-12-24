"""Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num_menor = 0
num_maior = 0
for n in range(1,4):
    n = int(input(f'valor {n}: '))
    if n > num_maior:
        num_maior = n
    elif n < num_maior:
        num_menor = n
print(f'Meior é: {num_maior}')
print(f'menor é: {num_menor}')
