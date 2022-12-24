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


    def __len__(self):
        #retorna o tamanho da lista
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()


