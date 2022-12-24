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
        self._tamanho = 0

    def insere_no_inicio(self, novo_dado):
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        self._tamanho = self._tamanho + 1


    def Busca(self,valor):
         # retorna uma tupla (anterior,corrente)
        if not self.cabeca:
            return 'Lista vazia'
        corrente = self.cabeca
        anterior = None
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        if corrente:
            return corrente.dado
        else:
            anterior.proximo = None
            return None

    def BuscaAprimorada(self, valor):
        # retorna uma tupla (anterior,corrente)
        if not self.cabeca:
            return 'Lista vazia'
        corrente = self.cabeca
        anterior = None
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        if corrente:
            return anterior, corrente
        else:
            anterior.proximo = None
            return None

    def Remover(self, valor):
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

    def Buscar_e_remover(self, valor):
        busca = self.BuscaAprimorada(valor)
        if busca[0] == None:
            self.cabeca = self.cabeca.proximo
        elif busca:
            busca[0].proximo = busca[1].proximo
            self._tamanho = self._tamanho - 1

    def __len__(self):
        # Retorna o tamanho da Lista
        return self._tamanho

    def __getitem__(self, index):
        pointer = self.cabeca
        for i in range(index):
            if pointer:
                pointer = pointer.proximo
            else:
                return False
                #raise IndexError('list index out of renge')
        if pointer:
            return pointer.dado
        else:
            # return False
            None
        #raise ImportError('list index out of range')

    def __setitem__(self, index, elem):
        pointer = self.cabeca
        for i in range(index):
            if pointer:
                pointer = pointer.proximo
            else:
                raise IndexError('list index out of renge')
        if pointer:
            pointer.dado = elem
        else:
            raise ImportError('list index out of range')

    def index(self, elem):
        # Retorna o Indicie do Elemento na lista
        pointer = self.cabeca
        i = 0
        while (pointer):
            if pointer.dado == elem:
                return i
            pointer = pointer.proximo
            i = i + 1
        raise ValueError(f'{elem} is not in list')

    
def __repr__(self) -> str:
    return "[" + str(self.cabeca) + "]"
