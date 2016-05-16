nota = 0

for aluno in range(1, 5):
    t_nota = 1
    while t_nota <= 3:
        nota += int(input('Aluno {0}, nota {1}: ' .format(aluno, t_nota)))
        t_nota += 1


print('Média entre as quato notas finais: %g' % (nota / 4))
