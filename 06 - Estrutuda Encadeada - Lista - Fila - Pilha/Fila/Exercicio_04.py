import Class

# 4. Escreva uma função que inverta a ordem dos elementos da fila.  Por exemplo:
# [1] [4] [5] [2] → [2] [5] [4] [1]

fila = Class.Queue()

for a in range(1,5):
    print(f'Inserindo -> {a}')
    fila.push(a)

aux = fila.reverse()
print(f'\nFila       ->  {fila}')
print(f'Invertendo ->  {aux}')

