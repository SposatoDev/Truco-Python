from truco.jogo import Jogo

def main():
    jogo = Jogo()

    print("Iniciando jogo...")
    jogo.iniciar()

    escolha = 0

    while escolha != 3:
        print("Escolha uma opção: ")
        print("[ 1 ] Ver suas cartas")
        print("[ 2 ] Truco")
        print("[ 3 ] Sair")




if __name__ == "__main__":
    main()