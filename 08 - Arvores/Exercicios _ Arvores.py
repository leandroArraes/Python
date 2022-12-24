class NodoArvore:

    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return f'{self.esquerda and self.esquerda.chave} <- {self.chave} -> {self.direita and self.direita.chave}'


def em_ordem(raiz):
    if not raiz:
        return

    em_ordem(raiz.esquerda)
    print(raiz.chave)
    em_ordem(raiz.direita)


def insere(raiz, nodo):
    if raiz is None:
        raiz = nodo
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)


def busca(raiz, chave):
    if raiz is None:
        return None

    if raiz.chave == chave:
        return raiz

    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    return busca(raiz.esquerda, chave)



# 1. Encontre o menor elemento em uma BST.
def findMenor(raiz):
    if raiz.esquerda is None:
        return raiz.chave

    return findMaior(raiz.esquerda)

# 2. Encontre o maior elemento em uma BST.
def findMaior(raiz):
    if raiz.direita is None:
        return raiz.chave

    return findMaior(raiz.direita)

# 3. Verifique se duas árvores binárias são idênticas.
def check(raiz, raiz1):
    if raiz is None:
        return True

    if raiz.chave != raiz1.chave:
        return False

    if raiz.chave < chave:
        return check(raiz.direita, raiz1.direita)

    return check(raiz.esquerda, raiz1.esquerda)

# 4. Calcule a altura de uma BST.
def alturaD(raiz, steps=0):
    if raiz.direita is None:
        return steps

    return alturaD(raiz.direita, (steps+1))

def alturaE(raiz, steps=0):
    if raiz.direita is None:
        return steps

    return alturaE(raiz.direita, (steps+1))


# 5. Verifique se uma árvore binária é balanceada.
def checkTree():
    extremoE = alturaE(raiz)
    extremoD = alturaD(raiz)
    if extremoE == extremoD:
        return f"A arvore é balanceada, simetrica, e sua altura é {extremoE}"
    elif (extremoE - extremoD < -1) or (extremoE - extremoD > 1):
        return f"A arvore não é balanceada e sua altura max é {max(extremoE, extremoD)}"
    else:
        return f"A arvore é balanceada e sua altura é {max(extremoE, extremoD)}"


raiz = NodoArvore(40)

for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

raiz1 = NodoArvore(40)

for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    insere(raiz1, nodo)


if check(raiz, raiz1):
    print("OK, são identicas")
