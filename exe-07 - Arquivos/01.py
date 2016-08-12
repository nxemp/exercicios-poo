def cont(arq):
	k = 0
	with open(arq, 'r') as arq:
		for i in arq:
			k +=  1
	return k

def cont_ca(arq):
	k = 0
	with open(arq, 'r') as arq:
		for line in arq:
			for car in line:
				k += 1
	return k

print(cont('tec.txt'))
print(cont_ca('tec.txt'))
