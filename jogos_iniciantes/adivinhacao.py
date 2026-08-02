import random

numero_secreto = random.randint(1, 10)

tentativas = 3

while tentativas > 0:
    palpite = int(input("Digite um número: "))

    if palpite == numero_secreto:
        print("Acertou!")
        break

    tentativas -= 1
    print("Tentativas restantes:", tentativas)
