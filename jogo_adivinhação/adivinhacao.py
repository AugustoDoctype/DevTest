import random


def sortear_numero():
    return random.randint(1, 10)


def verificar_palpite(palpite, numero):
    if palpite == numero:
        return "Você acertou!"

    return "Você errou!"