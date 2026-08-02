palavra = "python"

while True:
    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        print("Acertou!")
        break
    else:
        print("Errou! Tente novamente.")
