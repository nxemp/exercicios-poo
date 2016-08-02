agenda = {}


def adicionar(agenda: dict, emails: tuple, dados: tuple):
    '''
    email: entre com 4 emails
    dados: entre com quatros listas, contendo os dados dos emails
    recebidos
    '''
    for i in range(len(emails)):
        print(emails[i], dados[i])
        if emails[i] not in agenda:
            k = emails[i]
            agenda[k] = dados[i]
        else:
            print('Não é possivel adicionar', i,',ele já existe')

def existe(agenda, email):
    return email in agenda


def moficar(agenda, email, dados):
    if email in agenda:
        agenda[email] = dados


def apagar(agenda, email):
    if email in agenda:
        del(agenda[email])


def imprimir(agenda, email):
    print

#test
#adicionar(agenda, ('wallyssonlds@gmail.com',), (['wallysson', 17],))
