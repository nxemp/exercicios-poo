agenda = {}

a = int(input('Número de contatos a adicionar: '))

for tmp in range(a):
    email = input('Digite seu email: ')
    agenda[email] = []
    agenda[email].append(input('Seu nome: '))
    agenda[email].append(input('Seu telefone: '))
    agenda[email].append(input('Data de nascimento: '))

for tmp in agenda.keys():
    print(tmp, ':', agenda[tmp])
