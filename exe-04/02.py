cpf = input('Número do cpf: ')

def calcula_d1():
    cont, soma= 10, 0
    for tmp in cpf:
        soma += cont * int(tmp)
        cont -= 1

    rest = soma % 11
    if rest == 0 or rest == 1:
        d1 = 0
    else:
        d1 = 11 - rest

    return str(d1)

cpf_tmp = cpf[1:8] + str(calcula_d1())
def calcula_d2():
    cont, soma = 10, 0
    for tmp in cpf_tmp:
        soma += cont * int(tmp)
        cont -= 1
    rest = soma % 11
    if rest == 0 or rest == 1:
        d2 = 0
    else:
        d2 = 11 - rest
    return str(d2)

print('CPF final: %s' % (cpf + calcula_d1() + calcula_d2()))