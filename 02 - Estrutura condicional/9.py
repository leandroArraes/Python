"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""
num = []
for n in range(1,4):
    num.append(int(input(f"{n}° valor: ")))
num = sorted(num)
a1 = len(num)-1

for a in range(3):
    print(num[a1])
    a1 = a1-1