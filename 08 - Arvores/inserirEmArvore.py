import ClassArvore

def insere(raiz, nodo):
#Insere um nodo em uma árvore binária de pesquisa.'
# Nodo deve ser inserido na raiz.
if raiz is None:
    raiz = nodo
# Nodo deve ser inserido na subárvore direita.
elif raiz.chave < nodo.chave:
    if raiz.direita is None: 
        raiz.direita nodo
else:
insere (raiz.direita, nodo)
# Nodo deve ser inserido na subárvore esquerda.
else:
if raiz.esquerda is None:
raiz.esquerda nodo
else:
insere(raiz.esquerda, nodo)