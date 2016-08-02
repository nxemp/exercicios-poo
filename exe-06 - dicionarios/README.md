##Exercícios – Dicionários em Python

#### 1. Faça um programa que crie uma agenda de contatos a partir de um dicionário vazio (agenda = {}). Os dados de cada contato (nome, email, telefone e aniversário) devem ser armazenados como pares no dicionário agenda. A chave de cada contato é o seu email. As demais informações devem ser associadas à chave como uma lista.

Exemplo da estrutura de dados da agenda:
``` python
{ bruno.gurgel@ifrn.edu.br : ['Bruno Gomes', '84988889999', '16/01/1982'],
lucia.pereira@ifrn.edu.br : ['Lúcia de Fátima', '8498929282222', '02/04/1979'] }
```

#### 2. Continuando a questão anterior, implemente as funções pedidas a seguir. Use a função adicionar para realizar a inclusão de 4 (quatro) contatos na agenda. Use as demais funções posteriormente para modificar os dados de um contato, apagar um contato e imprimir as informações de um contato dado o seu e-mail. 
	a) adicionar (agenda, email, dados) – adiciona um novo contato, caso ele não exista na agenda. 
	b) existe (agenda, email) – verifica se um contato já existe na agenda. Devolve True em caso positivo e False caso contrário. 
	c) modificar (agenda, email, dados) – modifica os dados de um contato que já existe na agenda.
	d) apagar (agenda, email) – apaga o contato, caso ele exista na agenda.
	e) imprimir (agenda, email) – imprime os dados de um contato.