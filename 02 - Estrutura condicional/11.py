"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

salario= float(input("Salario Atual: "))

if salario <= 280:
    print(f"salario antes do reajuste R$: {salario}")
    print(f'percentual de aumento aplicado 20%')
    print(f'valor do aumento R$: {salario * 0.20}')
    print(f'novo salário, após o aumento R$:{salario + (salario * 0.20)} ')
elif salario > 280 and salario <=700:
    print(f"salario antes do reajuste R$: {salario}")
    print(f'percentual de aumento aplicado 15%')
    print(f'valor do aumento R$: {salario * 0.15}')
    print(f'novo salário, após o aumento R$:{salario + (salario * 0.15)} ')
elif salario > 700 and salario <= 1500:
    print(f"salario antes do reajuste R$: {salario}")
    print(f'percentual de aumento aplicado 10%')
    print(f'valor do aumento R$: {salario * 0.10}')
    print(f'novo salário, após o aumento R$:{salario + (salario * 0.10)} ')
elif salario > 1500:
    print(f"salario antes do reajuste R$: {salario}")
    print(f'percentual de aumento aplicado 5%')
    print(f'valor do aumento R$: {salario * 0.05}')
    print(f'novo salário, após o aumento R$:{salario + (salario * 0.05)} ')


