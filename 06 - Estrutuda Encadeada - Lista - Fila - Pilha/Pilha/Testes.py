import Pilha
import Funcoes

pilha = Pilha.Pilha()
for a in range(1,6):
    pilha.inserir(a)

print('-'*140)
print('01 | Escrever uma função que receba como parâmetro uma pilha.',
        'A função deve retornar o maior elemento da pilha.')

print(f'\n    --> {pilha}\n')
print(f'        --> Retorna o Maior da Pilha --> {pilha.Maior()}\n')
print('-'*140)

# 02
print('02 | Utilizando uma pilha resolver o exercício a seguir:',
        'Dada uma sequência contendo N (N >0) números reais, imprimila na ordem inversa.')

d= pilha.inverta()
print(f'\n    --> {pilha}\n')
print(f'\n    --> Invertendo a ordem')
print(f'       --> {d}\n')

# 03
print('-'*140)
print('03 | Escreva uma função que receba como parâmetro duas pilhas e',
        'verifique de elas são iguais.\n',
        '  Duas pilhas são iguais se possuem os mesmos elementos, na',
        ' mesma ordem.')
c= pilha
print('\n     Teste 1')
Funcoes.Comparar(pilha,d)
print('\n     Teste 02')
Funcoes.Comparar(pilha,c)

#04

print('-'*140)
print('04 | Construa um programa utilizando uma pilha que resolva o',
'seguinte problema:\n',
'    • Armazene as placas dos carros (apenas os números) que estão\n',
'      estacionados numa rua sem saída estreita.\n',
'    • Dado uma placa verifique se o carro está estacionado na rua.\n',
'    • Caso esteja, informe a sequência de carros que deverá ser retirada',
',para que o carro em questão consiga sair.\n')

estacionamento = Pilha.Pilha()
for a in range(1000,5000,1000):
    estacionamento.inserir(a)
    

print(f'       Estacionemnto -->  {estacionamento}')
print(f'       Encontrar Placa: 2000\n')
Funcoes.RemoverVeiculo(estacionamento,1000)

# 05
print('\n05 | Implemente uma função chamada TPilha, que receba um',
        'vetor de inteiros com 15 elementos. Para cada um deles, como segue:\n',
        '  • Se o número for par, insira-o na pilha;\n',
        '  • Se o número lido for ímpar, retire um número da pilha;\n',
        '  • Ao final, esvazie a pilha imprimindo os elementos.\n')

'''p2 = Pilha.Pilha()
Funcoes.InserirVetor(p2)
print(p2)
Funcoes.Removertodas(p2)
print(p2)'''

#06

print('\n06 | Escreva uma função chamada TPilha2 que recebe como',
        'parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um:\n',
        '   • se positivo, inserir na pilha P;\n',
        '   • se negativo, inserir na pilha N;\n',
        '   • se zero, retirar um elemento de cada pilha.\n')

p = Pilha.Pilha()
n = Pilha.Pilha()
Funcoes.TPilha2(p,n)
print(f'{p}\n{n}')