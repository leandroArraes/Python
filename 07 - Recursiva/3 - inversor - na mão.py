'''n = 1234
a = n%10 # Digito extrai o ultimo
b = n//10 # Resto extrai antes do ultimo
c = b%10 # 
d = b//10
ax = 0

print(a)
print(b)
print(c)
print(d)

def inverter(num , resultado = 0):
	if num == 0:
		return resultado
	else:
		ultimo = num % 10 #extrai o ultimo
		sobra = num // 10 
		resultado = resultado * 10 
		return inverter(sobra, resultado) 

print(inverter(123))'''




def inverte(num, aux=0):
    print('num =',num)
    if num < 10:
        return aux + num 
    aux = aux * 10 + (num % 10) * 10 
    
    return inverte(num // 10, aux) , num

print('1° Pegar o resto da divisão por 10')
print('2° dividir pelo inteiro \n')

def inverte(num, aux=0):
    print('num =',num)
    if num < 10:
        print(f'\nnaux = {aux}  num = {num}')
        return (aux + num)
        
    print(f'Entrada: aux = {aux}   num = {num}')
    #-------
    aux = aux * 10 + (num % 10) * 10
    #____0 * 10 + (123%10) = 0 + 3 * 10 =30
    #___30*10 + (12%10) = 300+(2*10)=320
    #----320  (12//10)= 1 >> return 320+1 
    # respota = 321 
    print(f'Saida:   aux = {aux}  num = {num}')
    return inverte(num // 10, aux)
    #               (123//10) = 12 , 30
    #                 123// 10 = 12 ,320
    #                   12 // 10= 1 ,
 
n= 123
print(n)  
print(inverte(n))
		