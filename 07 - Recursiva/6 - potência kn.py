'''6) Crie um programa em C, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule kn . Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função'''


def potenciakn( k,  n):
	if n == 0:
		return k
	else:
		return k * potenciakn(k, n - 1)

print(potenciakn(2,2))