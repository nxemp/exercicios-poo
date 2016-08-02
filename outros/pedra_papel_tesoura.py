import random

jogada = ['pedra', 'papel', 'tesoura']
computador, humano , empa = 0, 0, 0

vitoria = ['pedra x tesoura', 'tesoura x papel','papel x pedra']
for i in range(3):
    jog_com = random.choice(jogada)
    print(jog_com)
    jog_hum = input('Digite sua jogada: ').lower()
    find = jog_com + " x " + jog_hum
    print(find)
    if (jog_com + ' x ' + jog_hum) in vitoria:
        computador += 1
        if computador == 2 : break
    elif (jog_hum + ' x ' + jog_com) in vitoria:
        humano += 1
        if humano == 2: break
    else:
        empa += 1

if humano > computador: print('Você ganhou de {} a {}.' .format(humano, computador))
elif computador > humano: print('Computador ganhou  de {} a {}.' .format(computador, humano))
else: print('Você empataram!')