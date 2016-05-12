num1 = float(input('Número 1: '))
num2 = int(input('Número de vezes: '))
k = 0

for i in range(1, num2 + 1):
    k += num1

print('Multiplicação: %g' % k)
