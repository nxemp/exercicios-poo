'''Faça um programa que peça três números e verifique se esses númerospodem formar um triângulo, ou seja, se cada lado é menor que
a soma dosoutros dois lados. Seu programa deve imprimir apenas verdadeiro (True) oufalso (False)'''

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

print(l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1)
