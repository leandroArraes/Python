def MB(valor):
	m= (valor/1024)/1024
	n = '%1.2f'%m
	return float(n)

def discTotal():
	v= sum(relatorio.values())
	return MB(v)

def porcent (valor):
	p = 100/discTotal()
	tt= valor*p
	return valor*p
		
def esp(nom,d):
	a = len(nom)
	n = d - a
	s = ' '
	return nom + s*n

def espNr(nom,d):
	a = len(nom)
	n = d - a
	s = ' '
	return s*n + nom
	


relatorio = {
'alexandre':   456123789,
'anderson': 1245698456,
'antonio'   :    123456456,
'carlos'      :       91257581,
'cesar'       :            987458,
'rosemary':     789456125}

cont=1
b= len(relatorio)
print('--'*25)
print('Nr   Nome       Espaço Utilizado    % de uso')
print('--'*25)



for nome in relatorio:
	nom = esp(nome,12)
	tam = MB(relatorio[nome])
	x = str(tam)
	p = f'{porcent(tam):,.2f}'
	
	print(f'{cont} - {nom} {espNr(x,8)} MB         {espNr(p,5)} %')
	cont+=1

print(f'\nEspaço total ocupado: {discTotal()} MB')
media= discTotal()/len(relatorio.keys())
print(f'Espaço médio ocupado:  {media:,.2f} MB')
	
