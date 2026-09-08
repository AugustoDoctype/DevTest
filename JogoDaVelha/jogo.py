def avaliar_jogo_da_velha(tabuleiro: list) -> str:
    """Avalia o status de um tabuleiro de Jogo da Velha."""
    
    # Validação de segurança para garantir o formato correto
    if len(tabuleiro) != 3 or any(len(linha) != 3 for linha in tabuleiro):
        raise ValueError("O tabuleiro deve ser uma matriz 3x3 exata.")

    # 1. Checar vitórias nas linhas e colunas
    for i in range(3):
        # Checa a linha 'i'
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] is not None:
            return f"Vitória de {tabuleiro[i][0]}"
        # Checa a coluna 'i'
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] is not None:
            return f"Vitória de {tabuleiro[0][i]}"

    # 2. Checar vitórias nas duas diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] is not None:
        return f"Vitória de {tabuleiro[0][0]}"
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] is not None:
        return f"Vitória de {tabuleiro[0][2]}"

    # 3. Verificar se ainda há espaços vazios (Em andamento)
    tem_espaco = any(celula is None for linha in tabuleiro for celula in linha)
    if tem_espaco:
        return "Em andamento"
    
    # 4. Se não há vitória e não há espaço, é empate
    return "Empate"

if __name__ == "__main__":
    # criar um tabuleiro de exemplo (uma vitória do X na diagonal)
    meu_tabuleiro = [
        ["X", "O", None],
        [None, "X", "O"],
        [None, None, "X"]
    ]
    
    resultado = avaliar_jogo_da_velha(meu_tabuleiro)
    
    # Imprime o resultado na tela
    print("O status do jogo é:", resultado)