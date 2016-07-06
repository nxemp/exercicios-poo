import random


def sortear_palavra():
    palavras = ['carro', 'gato', 'casa', 'caderno']
    return palavras[random.randint(0, 3)]


def gerar_palavra():
    return ['_'] * len(gerada)


def modificar_forca(letra, sortada):
    pos = 0
    for ch in gerada:
        if ch == letra:
            forca[pos] = letra
        pos += 1
    return forca


gerada = sortear_palavra()
forca = gerar_palavra()
print (forca)


def main():
    tentativas = 6
    i = 0
    while i < tentativas:
        letra = input('Digite uma letra: ')
        print(modificar_forca(letra, gerada))
        escolha = input('Qual a palavra?: ')
        if escolha == gerada:
            print ('Parabéns, você acertou!!!')
            break
        else:
            print ('A palavra não é essa. Tente novamente!!!')

        i += 1


if __name__ == '__main__':
    main()
