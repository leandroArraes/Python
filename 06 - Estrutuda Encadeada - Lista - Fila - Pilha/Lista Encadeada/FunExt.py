import ListaEncadeada


def inserirListaDuplicada(lista):
    for a in range(1, 4):
        lista.insere_no_inicio(a)
    for a in range(1, 4):
        lista.insere_no_inicio(a)

#Essa está retornando quando ocorrencias do  primeiro termo em uma lista
def ocorrencia(lista):
    chave = lista.cabeca
    proximo = lista.cabeca
    dupli = ListaEncadeada.ListaEncadeada()
    while chave:
        if chave.dado == proximo.dado:
            dupli.insere_no_inicio(proximo.dado)
        chave = chave.proximo
    return dupli

# remove só as primeiras duplciados 
def Remover_duplicados(lista):
    corrente = lista.cabeca
    while corrente:
        anterior = corrente
        if anterior.dado != corrente.proximo:
            corrente.proximo = corrente.proximo.proximo
        corrente = corrente.proximo
    return lista


