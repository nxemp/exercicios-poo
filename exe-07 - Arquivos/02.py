from 01 import cont

import random

def sortear_palavra(nome_arquivo):
	with open(nome_arquivo) as t:
		text = t.read()
	return random.choice(text.split())

print(sortear_palavra('tec.txt'))

