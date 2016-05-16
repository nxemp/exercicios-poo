print('Ímpares de 3 até um limite superior (>=3)')
numero = int(input('Digite o limite: '))
i = 3
k = 0
while i <= numero:
    print(i)
    k += i
    i += 2

print('Soma dos números: {0}' .format(k))
