import ClassArvore

raiz = ClassArvore.NodoArvore(3)
for a in range(20):
    raiz.esquerda = ClassArvore.NodoArvore(a)
    raiz.direita = ClassArvore.NodoArvore(a+1)
