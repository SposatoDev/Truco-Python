import random
from truco.carta import Carta

# Classe = Representatividade de um objeto na vida real, no qual há atributos (características) e métodos (ações).
class Baralho:

    # Função para iniciar uma instância do objeto (baralho1 = Baralho()).
    def __init__(self):
        self.cartas = []

    # Métodos:

    def criar(self):

        valores = [
            "4",
            "5",
            "6",
            "7",
            "Rainha",
            "Valete",
            "Rei",
            "Ás",
            "2",
            "3"
        ]

        naipes = [
            "Copas",
            "Ouro",
            "Espadilhas",
            "Paus"
        ]

        for valor in valores:
            for naipe in naipes:
                carta = Carta(valor, naipe)
                self.cartas.append(carta)

    def embaralhar(self):
        random.shuffle(self.cartas)

    def retirar_carta(self):
        if len(self.cartas) == 0:
            raise ValueError("O baralho está vazio.")

        carta = random.choice(self.cartas)
        self.cartas.remove(carta)

        return carta


