palavra_secreta = "python"

palpite = input("Digite uma letra: ").lower()

if palpite in palavra_secreta:
    print("Acertou!")
else:
    print("Errou!")
