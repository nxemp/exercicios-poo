altura = float(input('Digite sua altura (em centimetros): '))
sexo = input('Digite seu sexo (f ou m): ')


if sexo == 'f':
    peso = altura - 100 - ((altura - 150) / 2)
else:
    peso = altura - 100 - ((altura - 150) / 2)

print('Seu pesso ideal é: %.2f kg' % peso)
