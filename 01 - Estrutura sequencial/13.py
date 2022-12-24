altura = float(input('informe a altura: '))
sexo = input('informe seu Sexo [F/M]').upper()
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f'seu peso ideal é {peso_ideal}')
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f'seu peso ideal é {peso_ideal}')
else:
    print("opção invalida")
