"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input("informe uma letra: ").upper()
if letra == "A" or  letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f'"{letra}" é vogal')
elif letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9" or letra == "0":
    print(f'"{letra}" é numero')
else:
    print(f'"{letra}" é consoante')