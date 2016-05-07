preco_produto = float(input('Digite o preço do produto: '))
cond_pagamento = int(input('Digite o código de pagamento: '))

if cond_pagamento == 1:
    preco_produto -= preco_produto * 0.1
elif cond_pagamento == 2:
    preco_produto -= preco_produto * 0.05
elif cond_pagamento == 3:
    preco_produto = preco_produto
elif cond_pagamento == 4:
    preco_produto += preco_produto * 0.1
else:
    print('Código de desconto inválido!')

print('O preço final do produto é: R$ %.2f' % preco_produto)
