tabuleiro = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " "
]

while True:
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---------")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---------")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])

    posicao = int(input("Escolha uma posição (0 a 8): "))

    if tabuleiro[posicao] == " ":
        tabuleiro[posicao] = "X"
    else:
        print("Posição ocupada!")
