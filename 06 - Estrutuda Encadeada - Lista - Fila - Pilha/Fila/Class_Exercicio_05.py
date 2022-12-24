import string

class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

    def __repr__ (self):
        pass

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push (self,elem):
        # insere um elemento na fila
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def pop(self):
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem

        raise IndexError("the queou is empty")

    def peek(self):
        # Retorna o topo sem remover
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("the queou is empty")

    def reverse(self):
        r = ""
        size = self._size - 1
        while size >= 0:
            pointer = self.first
            for i in range(0,size):
                pointer = pointer.next
            r = r + str(pointer.data) + " "
            size = size - 1

        if pointer:
            return r
            # pointer.data
        else:
            # return False
            None
        # raise ImportError('list index out of range')

    def MatarMaiorTempoEspera(self):
        # retorna o maior)
        if not self.first:
            return 'Lista vazia'
        corrente = self.first
        anterior = None
        maior = 0
        apagar = None
        cont = 0
        while corrente:
            if corrente.data['Wait'] > maior:
                maior = corrente.data['Wait']
                apagar = corrente
                anterior = corrente
                corrente = corrente.next
                cont+=1
            else:
                corrente = corrente.next
                #cont += 1
        pointer = self.first
        last = None
        for a in range(cont-1):
            last = pointer
            pointer = pointer.next
        last.next = pointer.next

    def RemoverDafila(self,elem):
        pointer = self.first
        last = None
        while pointer and pointer.data['ID'] != elem:
            last = pointer
            pointer = pointer.next
        if pointer:
            last.next = pointer.next


#   Funções do Exercicio 05

    def insert(self,id,nome,priority,wait):
        elem = {
            'ID': id,
            'Nome':nome,
            'Priority':priority,
            'Wait':wait
           }
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def __getitem__(self, index):
        pointer = self.first
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                return False
                # raise IndexError('list index out of renge')
        if pointer:
            return pointer.data
        else:
            # return False
            None
        # raise ImportError('list index out of range')

    def index(self, elem):
        # Retorna o Indicie do Elemento na lista
        pointer = self.first
        i = 0
        while (pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError(f'{elem} is not in list')


    def __len__(self):
        #retorna o tamanho da lista
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + "\n "
                pointer = pointer.next
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()


