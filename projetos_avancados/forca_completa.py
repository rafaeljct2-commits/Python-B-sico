import random

palavras = [
    "python",
    "computador",
    "programacao",
    "github",
    "pygame",
    "algoritmo",
    "desenvolvedor"
]

palavra = random.choice(palavras)

letras_acertadas = []
tentativas = 6

print("=== JOGO DA FORCA ===")

while tentativas > 0:

    exibicao = ""

    for letra in palavra:
        if letra in letras_acertadas:
            exibicao += letra + " "
        else:
            exibicao += "_ "

    print("\nPalavra:", exibicao)

    if "_" not in exibicao:
        print("\n🎉 Parabéns! Você venceu!")
        break

    chute = input("Digite uma letra: ").lower()

    if chute in palavra:

        if chute not in letras_acertadas:
            letras_acertadas.append(chute)

        print("✅ Letra correta!")

    else:
        tentativas -= 1
        print("❌ Letra incorreta!")
        print("Tentativas restantes:", tentativas)

if tentativas == 0:
    print("\n💀 Game Over!")
    print("A palavra era:", palavra)
