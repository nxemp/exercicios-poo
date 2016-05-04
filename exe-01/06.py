'''
Leia duas datas no formato dd/mm/aaaa sendo data1 < data2 e imprima a
quantidade de anos entre as duas datas
'''
ano1 = ano2 = int()

while ano1 > ano2 or ano1 == ano2:
    data1 = input('Primeira data (dd/mm/aaaa): ')
    data2 = input('Segunda data (dd/mm/aaaa): ')
    ano1, ano2 = int(data1[6:]), int(data2[6:])


print('Diferença entre os anos:', ano2 - ano1)
