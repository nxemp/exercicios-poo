class PPT():
        def __init__(self):
                self.jogadas = ['pedra x tesoura', 'tesoura X papel', 'papel x pedra']
                self.humano = 0
                self.computador = 0

        def sortear(self):
                import random
                jogada_maquina = random.choice(['pedra', 'papel', 'tesoura'])
                return jogada_maquina
        def confer(self):
                jogada_humano = input('Digite sua jogada: ')
                return jogada_humano
        def check(self):
                for i in range(3):
                        PPT.sortear(self)
                        PPT.confer(self)
                        if (PPT.sortear(self) + ' x ' + PPT.confer(self)) in self.jogadas:
                                print(PPT.sortear(self) + ' x ' + PPT.confer(self))
                                self.computador += 1
                                if self.computador > 1:
                                        break
                        elif (PPT.confer(self) + ' x ' + PPT.sortear(self)) in self.jogadas:
                                print(PPT.confer(self) + ' x ' + PPT.sortear(self))
                                self.humano += 1
                                if self.humano > 1:
                                        break
                        else:
                                print('Jogada maquina: ', PPT.sortear(self))
                                print('Jogada humano: ', PPT.confer(self))
                if self.humano > self.computador:
                        return "Computador perdeu!"
                elif self.computador > self.humano:
                        return "Computador ganhou!"
                else:
                        return "Empate!"


sorte = PPT()
sorte.check()
print(sorte.check())
