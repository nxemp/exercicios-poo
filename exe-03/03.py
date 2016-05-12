valor = 50000
meses = 0
while meses < 48:
    valor += valor * 0.18
    meses += 1
print('Valor final: R$ %.2f' % valor)
