'''
Solicite o preço de uma mercadoria e o percentual de desconto.Exiba opreço 
final a pagar após o desconto.
'''

preco = float(input('Valor da mercadoria: '))
desconto = float(input('Percentual de desconto da mercadoria: '))

desconto /= 100

print('Preço final: R$ %.2f' % (preco - preco * desconto))