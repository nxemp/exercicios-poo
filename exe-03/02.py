voto = 0
v1 = v2 = v3 = v4 = branco = nulo = 0
while voto != -1:
    voto = int(input(
        'Vote (1 a 4; 5 para voto em branco; \nqualquer outro para nulo; -1 para sair): '))
    if voto == 1:
        v1 += 1
    elif voto == 2:
        v2 += 1
    elif voto == 3:
        v3 += 1
    elif voto == 4:
        v4 += 1
    elif voto == 5:
        branco += 1
    else:
        if voto != -1:
            nulo += 1

print('Total de votos: {0}' .format(v1 + v2 + v3 + v4 + branco + nulo))
print('Cecília Meireles: {0}\nAriano Suassuna: {1}' .format(v1, v2))
print('Machado de Assis: {0} \nGraciliano Ramos: {1}' .format(v3, v4))
print('Votos em branco: {0}\nVotos nulo: {1}' .format(branco, nulo))
