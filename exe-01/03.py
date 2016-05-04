'''
 Escreva um programa que pergunte o nome e o sobrenome de uma pessoa, aquantidade de dias que ela quer alugar um veículo e calcule o
 preço apagar. Considere que o aluguel é R$ 60.00 por dia. Imprima a saída deacordo com o exemplo abaixo usando formatação de string.
'''

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
aluguel = int(input('Dias de aluguel: '))

print('Sr.(a) %s, você deve pagar R$ %.2f pelo aluguel por %d dias.'
      % (sobrenome, aluguel * 60, aluguel))
