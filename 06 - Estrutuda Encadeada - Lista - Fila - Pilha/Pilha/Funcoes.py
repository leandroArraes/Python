
import Pilha

def Comparar(pilha1,pilha2): 

    parametro_1 = pilha1.topo
    parametro_2 = pilha2.topo
    while parametro_1 and parametro_2:
        if parametro_1.dado == parametro_2.dado:
            parametro_1 = parametro_1.anterior
            parametro_2 = parametro_2.anterior
        else:
            return print(f'\n       --> Pilha I  = {pilha1}\n       --> Pilha II = {pilha2}\n            -->  Pilha I e Pilha II São Diferentes !')
        return print(f'\n       --> Pilha I  -> {pilha1}\n       --> Pilha II -> {pilha2}\n             -->  Pilha I e Pilha II São Identicas !\n')

def RemoverVeiculo(lista,chave):

    pointer = lista.Busca(chave)
    corrente = lista.topo
    if pointer:
        while corrente and corrente.dado != pointer:
            print(f'       Remover primeiro --> {corrente.dado}')
            corrente = corrente.anterior
    else:
        return print(f'       Veiculo {pointer} não Econtrado')

def InserirVetor(pilha):
    while pilha.topo is None:
        if pilha.topo == None:
            novo = int(input('    --> Valor: '))
            if novo % 2 == 0:
                pilha.inserir(novo)
            else:
                print('      • Não é possivel Inserir um Numero Impar')
                print('      • Lista Vazia - Não é possivel remover\n')
    for a in range(5):
        novo = int(input(f'    --> valor: '))
        if novo % 2 == 0:
            pilha.inserir(novo)
        else:
            if pilha:
                a = pilha.topo.dado
                print(f'          --> {pilha}')
                pilha.remover()
                print(f'          --> Digitou um Numero Impar Removendo o {a} da Pilha\n          --> {pilha}')

            else:
                print('Pilha Vazaia')

def Removertodas(pilha):
    corrente = pilha.topo
    while pilha:
        print(pilha)
        pilha.remover()
        if corrente.anterior:
            corrente = corrente.anterior
        else:
            return

def TPilha2(pilhaP,pilhaN):
    for a in range(10):
        novo = int(input((' Novo valor: ')))
        if novo > 0:
            pilhaP.inserir(novo)
        elif novo < 0:
            pilhaN.inserir(novo)
        else:
            pilhaP.remover()
            pilhaN.remover()

