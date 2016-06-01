quest = int(input('Número de questões: '))
gabarito = list()

for tmp in range(quest):
	gabarito.append(input('Gabarito, questão %d: ' % (tmp+1)))

acertos = 0
for tmp in range(quest):
	