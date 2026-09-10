def test_aluno_aprovado():
    notas = [8, 7, 9]

    resultado = calcular_media(notas)

    assert resultado == "Aprovado"


def test_aluno_recuperacao():
    notas = [5, 6, 4]

    resultado = calcular_media(notas)

    assert resultado == "Recuperação"


def test_aluno_reprovado():
    notas = [3, 4, 2]

    resultado = calcular_media(notas)

    assert resultado == "Reprovado"


def test_sem_notas():
    notas = []

    resultado = calcular_media(notas)

    assert resultado == 0