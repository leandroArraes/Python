"""Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
num_menor = 0
num_maior = 0
for n in range(1,4):
    n = float(input(f'produto {n} R$: '))
    if n > num_maior:
        num_maior = n
    elif n < num_maior:
        num_menor = n
print(f'menor valor é R$: {num_menor}')