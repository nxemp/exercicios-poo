quest = int(input('Número de questões (1 ≤ N ≤ 80): '))
gabarito = list()


for tmp in range(quest):
	gabarito.append(input('Gabarito, questão %d: ' % (tmp+1)))

acertos = 0
for tmp in range(quest):
	resposta = input('Digite a resposta %d: ' % (tmp+1))
	if resposta == gabarito[tmp]:
		acertos += 1

print('Você acertou %d questões.' % acertos)
