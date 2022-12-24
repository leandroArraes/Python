'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )'''

temp= [ ]
print('Temperarura de Cada Mês do ano: ')
for a in range(1,5):
	temp.append(float(input(f'{a}° Mes: ')))
	
tm= sum(temp)/len(temp)

print(f'\nTemperatura Media: {tm}°C\n')
print('Meses Com temperatura a Cima da Media:')
cont = 0
for i in temp:
	if i < tm:
		print(f' {cont+1}° Mês do ano  --> {temp[cont]}°c')
	cont+=1



#	if i > tm:
#		print(f'{temp[i]}°C ---  Mês{cont}')
#	cont+=1