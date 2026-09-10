def validar_senha(senha):
    if not isinstance(senha, str):
        raise ValueError("A senha deve ser uma string/texto.")

    if len(senha) < 8:
        raise ValueError("A senha deve ter pelo menos 8 caracteres.")

    if not any(char.isdigit() for char in senha):
        raise ValueError("A senha deve conter pelo menos um número.")

    return True
