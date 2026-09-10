from adivinhacao import verificar_palpite


def test_palpite_certo():
    resultado = verificar_palpite(5, 5)

    assert resultado == "Você acertou!"


def test_palpite_errado():
    resultado = verificar_palpite(5, 3)

    assert resultado == "Você errou!"