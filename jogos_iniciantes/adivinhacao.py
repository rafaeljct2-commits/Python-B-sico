import random

numero_secreto = random.randint(1, 10)

print("=== Jogo da Adivinhação ===")

while True:
    palpite = int(input("Digite um número de 1 a 10: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Tente novamente!")
