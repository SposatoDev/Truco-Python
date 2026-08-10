from truco.baralho import Baralho
from truco.jogador import Jogador


class Rodada:

    def __init__(self, jogadores):

        self.jogadores = jogadores
        self.baralho = Baralho()

        self.manilha = None

        self.cartas_jogadas = []

    def iniciar(self):

        self.baralho.criar()
        self.baralho.embaralhar()
        self.baralho.dis

    def distribuir_cartas(self):

        for jogador in self.jogadores:

            carta = self.baralho.retirar_carta()

            jogador.receber_cartas(carta)

    def definir_manilha(self):
        self.manilha = self.baralho.retirar_carta()
