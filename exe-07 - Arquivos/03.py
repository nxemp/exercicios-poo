def cript(msg):
	s = ''
	for ch in msg:
		s += chr(ord(ch) + 30000)
	return s


def descript(msg):
	s = ''
	for ch in msg:
		s += chr(ord(ch) - 30000)
	return s


def escrever_mensagem(nome, msg):
	ar = open(nome, 'w', encoding='utf-8')
	ar.write(cript(msg))
	ar.close()

def ler_mensagem(nome):
	ar = open(nome, 'r', encoding='utf-8')
	text = ar.read()
	ar.close()

	ar = open('text_descrip.txt', 'w', encoding='utf-8')
	ar.write(descript(text))
	ar.close()
#escrever_mensagem('testando.txt', 'wallysson de lima silva')
#ler_mensagem('testando.txt')
