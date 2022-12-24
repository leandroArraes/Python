peso_Limite = 50
peso = float(input("Digite a quantidade de kgs de peixe que JoÃ£o trouxe: "))
if peso > peso_Limite:
    excesso = peso - peso_Limite
    multa = excesso * 4.00
    print ("Multa foi de " + str(multa) + " reais")
