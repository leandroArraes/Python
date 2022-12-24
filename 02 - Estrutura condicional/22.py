"""Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão)."""
valor = int(input('informe um valor: '))
if valor % 2:
    print(f'{valor} é impar')
else:
    print(f'{valor} é par')