class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.cartas = []
        self.pontos = 0

    def receber_cartas(self, carta):
        self.cartas.append(carta)

    def jogar_carta(self, indice):
        if indice < 0 or indice >= len(self.cartas):
            raise IndexError("Índice de carta inválido.")

        return self.cartas.pop(indice)
