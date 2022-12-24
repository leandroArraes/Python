import ListaEncadeada
import FunExt

# criando e inserido intem na lista
lista = ListaEncadeada.ListaEncadeada()
FunExt.inserirListaDuplicada(lista)
print('Lista -> ',lista)
print()
#--------------------------------------

# 01 Remover atraves da função Busca
lista.insere_no_inicio(10)
print(f'--> Inserindo o Numero 10 na Lista \n    --> {lista}')


a = lista.Buscar_e_remover(10)
print(f'\n--> Removendo o Numero 10 da Lista Atraves da Busca \n   --> {lista}')
# ---------------------------------------

# 02  Remover os duplicicidades
b = FunExt.Remover_duplicados(lista)
print(f'\n--> Removendo as Duplicicidades \n   --> {lista}')

# 03 Defina as funções inserção, remoção e busca como métodos da Classe Lista. (Vide apostila)
lista.insere_no_inicio(15)
c = lista.Busca(2)
print(f'\n--> Busca do {c}')
lista.Remover(2)
print(f'--> Removendo o 2 da lista \n   --> {lista}')