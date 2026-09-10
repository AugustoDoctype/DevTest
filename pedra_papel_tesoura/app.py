from jogo import jogar


print("=== Pedra, Papel ou Tesoura ===")

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

resultado = jogar(jogador)

print(resultado)