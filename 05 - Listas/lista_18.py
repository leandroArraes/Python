'''Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?'''


num = 1
votos = [ ]
while num != 0:
	num = int(input('Numero: '))
	if num > 0 and num <= 23:
		votos.append(num)
	elif num >23:
		print('\n ==== Valor Invalido ====\n')

print(f'\nTotal de votos: {len(votos)}\n')
 
total=[ ]
pct=100/len(votos)
melhor = 0

for a in set(votos):
	x = votos.count(a)
	total.append(x)
	if x > melhor:
		melhor = a
		print()
	print(f'Jogador: {a}  teve --> {x} Votos = --> {pct*x} % dos votos ')

print('\nMelhor Jogador -->',melhor)

total= len(votos)	
	