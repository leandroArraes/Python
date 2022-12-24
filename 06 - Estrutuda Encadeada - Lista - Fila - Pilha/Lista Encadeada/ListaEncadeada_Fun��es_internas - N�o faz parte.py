#Funções integradas a classe

class NodoLista:
    '''Esta Classe representa um nodo de uma lista encadeada'''

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
        
    def __repr__(self):  # repr transforma a saida em string
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    '''Esta é uma lista representada uma lista encadeada.'''

    def __init__(self):
        self.cabeca = None
        self.tamanho = None
    
    def insere_no_inicio(self, novo_dado):
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        self.tamanho =+ 1
    
    def insere_depois(self, novo_dado):
       # assert nodo_anterior, "Nodo Anterior precisa Existir na lista"
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = self.cabeca.proximo
        self.cabeca.proximo = novo_nodo
    
    def Insere_No_Final(self,novo_dado):
        if self.cabeca:
            #inserção quando a lista já possui elementos
            pointer = self.cabeca
            while (pointer.proximo):
                pointer = pointer.proximo
            pointer.proximo = NodoLista(novo_dado)
        else:
            #primeira inserção
            self.cabeca = NodoLista(novo_dado)

    def Busca(self,valor):
        corrente = self.cabeca
        while corrente and corrente.dado  != valor:
            corrente = corrente.proximo
        if corrente:
            return corrente
        else:
            return None

    def Remover(self,valor):
        if not self.cabeca:
            return 'Lista vazia'
        corrente = self.cabeca
        anterior = None
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        if corrente:
            anterior.proximo = corrente.proximo
        else:
            anterior.proximo = None
            return None
        
    def RemoverPorFun(self,valor):
        if not self.cabeca:
            return 'Lista Vazia'
        self.anterior = None
        corrente = self.Busca(valor)
        if corrente:
            anterior.proximo = corrente.proximo
        else:
            anterior.proximo = None
            return print(f'{valor} não Encontrado')


    def __repr__(self) -> str:
        return "[" + str(self.cabeca) + "]"

lista = ListaEncadeada()

lista.insere_no_inicio(1)
lista.insere_no_inicio(2)
lista.Insere_No_Final(3)

Busca = lista.Busca(0)
print(f'Busca ->',Busca)

print(lista)
lista.RemoverPorFun(2)
print(lista.tamanho)
