from jogo import jogar


def test_jogar():
    resultado = jogar("pedra")

    assert resultado in ["Empate", "Você venceu", "Computador venceu"]