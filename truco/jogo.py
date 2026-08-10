from unicodedata import category

from truco.baralho import Baralho
from truco.jogador import Jogador
import random

class Jogo:


    def __init__(self):

        self.baralho = Baralho()

        self.jogador1 = Jogador("Kauã")
        self.jogador2 = Jogador("Computador 1")
        self.jogador3 = Jogador("Computador 2")
        self.jogador4 = Jogador("Computador 3")

    def iniciar(self):

        self.baralho.criar()
        self.baralho.embaralhar()
        self.distribuir_carta()

        self.vira = self.baralho.retirar_carta()

        self.iniciar_rodada()

    def distribuir_carta(self):

        for i in range(3):

            carta_jogador1 = self.baralho.retirar_carta()
            self.jogador1.receber_cartas(carta_jogador1)

            carta_jogador2 = self.baralho.retirar_carta()
            self.jogador2.receber_cartas(carta_jogador2)

            carta_jogador3 = self.baralho.retirar_carta()
            self.jogador3.receber_cartas(carta_jogador3)

            carta_jogador4 = self.baralho.retirar_carta()
            self.jogador4.receber_cartas(carta_jogador4)

    def mostrar_cartas(self):

        print(f"\nSuas cartas:")

        for i, carta in enumerate(self.jogador1.cartas):
            print(f"[{i + 1}] {carta}")

    def iniciar_rodada(self):
        print("Rodada 1")
        print(f"Jogada inicial: {self.jogador1.nome}")

        carta_jogador = self.escolher_carta()

        print(f"Você jogou: {carta_jogador}")

        self.computador_jogar(self.jogador2)
        self.computador_jogar(self.jogador3)
        self.computador_jogar(self.jogador4)

    def escolher_carta(self):

        self.mostrar_cartas()

        escolha = int(input("Escolha uma carta: "))

        carta = self.jogador1.cartas[escolha - 1]

        self.jogador1.cartas.remove(carta)

        return carta

    def computador_jogar(self, jogador):

        carta = random.choice(jogador.cartas)

        jogador.cartas.remove(carta)

        print(f"{jogador.nome} jogou {carta}")

        return carta
