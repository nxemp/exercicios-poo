minutos = int(input('Digite a quantidade de minutos: '))

# assumindo que o usuario não entre com valor negativo
if minutos < 200:
    valor = 0.2
elif minutos > 200 and minutos < 400:
    valor = 0.18
else:
    valor = 0.15

print('Você pagará R$ %.2f' % (minutos * valor))
