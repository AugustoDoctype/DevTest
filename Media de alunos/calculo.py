def calcular_media(notas):
    if len(notas) == 0:
        return 0

    media = sum(notas) / len(notas)

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"