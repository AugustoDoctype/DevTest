import random


def jogar(jogador):
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)

    print("Computador escolheu:", computador)

    if jogador == computador:
        return "Empate"

    if jogador == "pedra" and computador == "tesoura":
        return "Você venceu"

    if jogador == "papel" and computador == "pedra":
        return "Você venceu"

    if jogador == "tesoura" and computador == "papel":
        return "Você venceu"

    return "Computador venceu"