import random

palavras = ['java', 'cplusplus', 'pascal', 'python', 'csharp',
            'delphi', 'ruby', 'sql', 'visual basic', ]

palavra = random.choice(palavras)
#print(palavra)
t = len(palavra)
dica = ['_'] * t

tentativas = 0
while tentativas <= 6:
    letra = input('Letra: ')
    if letra in palavra:
        for i in range(len(palavra) - 1):
            if palavra[i] == letra:
                dica[i] = letra
        print(dica)
    else:
        print('Letra não existe na palavra!')

    test = input('Qual a palavra? ')
    if test == palavra:
        print('Parabéns, você acertou!!!')
        break
    else:
        print('A palavra não é essa. Tente novamente!!!')
    tentativas += 1