print('''Digite:
\t + - Adição
\t - - Subtração
\t x - Multiplicação
\t / - Divisão
\t Qualquer outro valor para sair''')

while True:
    opcao = input('Digite a opcao: ')
    if opcao == '+':
        tabuada = 1
        while tabuada <= 10:
            num = 1
            while num <= 10:
                print('{} {} {} = {}' .format(
                    tabuada, opcao, num, tabuada + num))
                num += 1
            tabuada += 1
    elif opcao == '-':
        tabuada = 1
        while tabuada <= 10:
            num = 1
            while num <= 10:
                print('{} {} {} = {}' .format(
                    tabuada, opcao, num, tabuada - num))
                num += 1
            tabuada += 1
    elif opcao == 'x' or opcao == '*':
        tabuada = 1
        while tabuada <= 10:
            num = 1
            while num <= 10:
                print('{} {} {} = {}' .format(
                    tabuada, opcao, num, tabuada * num))
                num += 1
            tabuada += 1
    elif opcao == '/':
        tabuada = 1
        while tabuada <= 10:
            num = 1
            while num <= 10:
                print('{} {} {} = {}' .format(
                    tabuada, opcao, num, tabuada / num))
                num += 1
            tabuada += 1
    else:
        break
