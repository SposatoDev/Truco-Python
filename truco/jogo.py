from truco import baralho
from truco.baralho import Baralho
from truco.jogador import Jogador

class Jogo:

    def __init__(self):

        self.baralho = Baralho()

        self.jogador1 = Jogador("Kauã")
        self.jogador2 = Jogador("Computador")

    def iniciar(self):

        self.baralho.criar()
        self.baralho.embaralhar()
        self.distribuir_carta()

    def distribuir_carta(self):

        for i in range(3):

            carta_jogador1 = self.baralho.retirar_carta()
            self.jogador1.receber_cartas(carta_jogador1)

            carta_jogador2 = self.baralho.retirar_carta()
            self.jogador2.receber_cartas(carta_jogador2)



