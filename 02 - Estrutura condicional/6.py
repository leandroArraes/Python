"""Faça um Programa que leia três números e mostre o maior deles.
"""
num = 0
for n in range(1,4):
    n = int(input(f'valor {n}: '))
    if n > num:
        num = n
print(num)

