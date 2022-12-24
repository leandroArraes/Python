"""Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez
"""
nota_1 = int(input("Nota 1: "))
nota_2 = int(input("Nota 2: "))
media = (nota_1 + nota_2)/2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print('Aprovado')
elif media <= 7:
    print('Reprovado')







