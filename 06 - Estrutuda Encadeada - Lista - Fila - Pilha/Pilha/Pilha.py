class NodoPilha:
    '''Esta Classe representa um nodo de uma lista encadeada'''

    def __init__(self, dado = 0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):  # repr transforma a saida em string
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha:
    
    def __init__(self):
        self.topo = None
        self._tamanho = 0
        
    
    def inserir(self,novo_dado):
        #insere na Base
        novo_nodo = NodoPilha(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo
        
    def Busca(self,valor):
         # retorna uma tupla (anterior,corrente)
        if not self.topo:
            return 'Lista vazia'
        corrente = self.topo
        anterior = None
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.anterior
        if corrente:
            return corrente.dado
        else:
            anterior.anterior = None
            return None

    def remover(self):
        #assert self.topo, "impossivel remover lista vazia"
        if not self.topo:
            return None
        self.topo = self.topo.anterior

    def Maior(self):
        corrente = self.topo
        anterior = None
        maior = 0
        while corrente:
            if corrente.dado > maior:
                maior = corrente.dado
            anterior = corrente
            corrente = corrente.anterior
        return maior

    
        if not self.topo.anterior:
            return
        else:
            print(self.topo)
            self.inverter(self.topo.anterior)

    def index(self, elem):
        # Retorna o Indicie do Elemento na lista
        pointer = self.topo
        i = 0
        while (pointer):
            if pointer.dado == elem:
                return i
            pointer = pointer.anterior
            i = i + 1
        raise ValueError(f'{elem} is not in list')

    def __getitem__(self, index):
        pointer = self.topo
        for i in range(index):
            if pointer:
                pointer = pointer.anterior
            else:
                raise IndexError('list index out of renge')
        if pointer:
            return pointer.dado
        else:
            raise ImportError('list index out of range')

    def inverta(self):
        corrente = self.topo
        cont = 0
        aux = Pilha()
        while corrente:
            cont+=1
            corrente = corrente.anterior
        for a in range(cont):
            aux.inserir(self[a])
        return aux

    def __repr__(self) -> str:
        return "[" + str(self.topo) + "]"


 