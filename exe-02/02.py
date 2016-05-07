velocidade = int(input('Digite a velocidade: '))

if velocidade > 110:
    print('Você foi multado! ')
    print('Valor da multa: R$ %.2f' % ((velocidade - 110) * 5))

else:
    print('Você não foi multado!')
