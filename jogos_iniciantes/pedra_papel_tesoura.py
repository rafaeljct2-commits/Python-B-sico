import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)

print("Computador escolheu:", computador)

if jogador == computador:
    print("Empate!")
elif (
    (jogador == "pedra" and computador == "tesoura") or
    (jogador == "papel" and computador == "pedra") or
    (jogador == "tesoura" and computador == "papel")
):
    print("Você ganhou!")
else:
    print("Você perdeu!")
