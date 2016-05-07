altura = float(input('Digite sua altura (em centimetros): '))
sexo = input('Digite seu sexo (f ou m): ')

if sexo == 'f':
    k = 2
else:
    k = 4

print('Seu pesso ideal é: %.2f kg' % (altura - 100 - ((altura - 150) / k)))
