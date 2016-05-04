'''
Faça um programa que calcule o pagamento semanal de um trabalhadordadas a quantidade de horas trabalhadas e o valor pago por cada hora.
Caso o trabalhador ultrapasse as 40 horas semanais, deve ser pago 1.5vezes o valor por hora para cada hora extra trabalhada. Exiba a 
saída comaté 10 dígitos, sendo desses duas casas decimais
'''

hora = int(input('Números de horas trabalhadas: '))
valor = float(input('Valor ganho por hora: '))

extra = 0
total = hora * valor

if hora > 40:
    extra = hora - 40
    total = (hora - extra) * valor + extra * valor * 1.5

print('Total a ser pago: R$ %10.2f' % total)
