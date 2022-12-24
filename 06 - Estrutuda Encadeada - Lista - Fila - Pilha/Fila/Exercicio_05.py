import Class_Exercicio_05
import string

''' 
    5.  No seu sistema operacional ao abrir o “gerenciador de tarefas” 
        você pode exibir os processos que estão em execução,
        veja como isso é apresentado no windows:
        você já parou pra pensar como é possível executar todos esses aplicativos em apenas um processador?
        Isso existe graças a uma funcionalidade chamada de tempo compartilhado (“time-shared”). 
        Essa funcionalidade mantém uma sequência de processos em uma fila, esperando para serem executados. 
        Modifique a fila dinâmica que você implementou anteriormente para armazenar as informações desses processos.

'''

painelDeControle = Class_Exercicio_05.Queue()
#.insert()
painelDeControle.push(1)
painelDeControle.push(2)
painelDeControle.push(3)
print(painelDeControle.index(1))

a = Class_Exercicio_05.Queue()
cont = 1

# Incluir novos processos na fila de processo;
for b in range(1000,9000,1000):
    a.insert(b,('Processo ' + str(b)),1,2 + cont)
    cont+=1

# Matar o processo com o maior tempo de espera;
print(a)
a[5]['Wait'] = 900
print(a[5])
print()
a.MatarMaiorTempoEspera()
print(a)

#Executar um processo (remover da fila)
a.RemoverDafila(7000)
print(a)
a.RemoverDafila(8000)
print(a)