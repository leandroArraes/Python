lista=[1,2,3]
       
def somar( vetor , p= 0 ):
	if p == len(vetor)-1:
		return vetor[p]#retorna o ultimo elemento do vetor 
	else:
	# vetor = [1,2,3]
		return somar(vetor , p+1 ) + vetor[p]
	 #1° retorno ....  vetor , p =1   + 1
	 #2° retorno ....  vetor , p =2   + 2
	 #3° retorno ....  vetor , p =3   + 3
	 

print(somar(lista))