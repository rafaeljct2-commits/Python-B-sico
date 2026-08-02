import random

numero_secreto = random.randint(1, 10)

print("=== Jogo da Adivinhação ===")

palpite = int(input("Digite um número de 1 a 10: "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Você errou!")
    print("O número era:", numero_secreto)
