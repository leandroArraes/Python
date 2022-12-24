nota = []
for n in range(1,5):
    nota.append(int(input(f'nota {n}: ')))
media = sum(nota)/len(nota)
print(f'A media do aluno é {media}')
