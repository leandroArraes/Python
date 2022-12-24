"""Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

saque = int(input('Valor do Saque R$: '))

numero = saque
# Extraindo a unidade
unidade = numero % 10

    # Eliminando a unidade de nosso número
numero = (numero - unidade)/10

    # Extraindo a dezena
dezena = numero % 10

    # Eliminando a dezena do número original, fica a centena
numero = (numero - dezena)/10
centena = numero

    # Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)

if (saque >=10) and (saque<=600):
    if centena > 0:
        print(f'{centena} notas de R$: 100,00')
    if 5 < dezena <= 9:
        print('1 nota  de R$:  50,00')
        dezena = dezena - 5
    if dezena < 5:
        print(f'{dezena} notas de R$:  10,00')

    if unidade >= 5:
        print('1 nota de R$:    5,00')
        unidade = unidade - 5
    if unidade < 5:
        print(f'{unidade} notas de R$:   1,00')
else:
    print('valor invalido')