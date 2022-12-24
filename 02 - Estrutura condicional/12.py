"""Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

ValorHoras = float(input('valor da sua hora R$:'))
QuantidadeHoras = float(input('Quantidade de Horas trabalhadas:'))

SalarioBruto = ValorHoras*QuantidadeHoras

if SalarioBruto <= 900:
    Imposto = 0
    Percentagem = 'x'
elif SalarioBruto > 900 and SalarioBruto <= 1500:
    Imposto = SalarioBruto*0.05
    Percentagem = '5%'
elif SalarioBruto >1500 and SalarioBruto <=2500:
    Imposto = SalarioBruto*0.1
    Percentagem = '10%'
else:
    Imposto = SalarioBruto*0.2
    Percentagem = '20%'

print('\n*****Folha de Pagamento*****')
print('Salário Bruto \t\tR$',ValorHoras*QuantidadeHoras)
print('(-)IR(',Percentagem,') \t\tR$',Imposto)
INSS = SalarioBruto*0.1
print('(-)INSS(10%) \t\tR$',INSS)
FGTS = SalarioBruto*0.11
print('FGTS(11%) \t\tR$',FGTS)
TotalDesconto = Imposto+INSS
print('Total dos descontos \tR$',TotalDesconto)
SalarioLiquido = SalarioBruto-Imposto-INSS
print('Salário Liquido \tR$',SalarioLiquido)