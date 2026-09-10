from adivinhacao import sortear_numero, verificar_palpite


print("=== Jogo de Adivinhação ===")

palpite = int(input("Digite um número de 1 a 10: "))

numero = sortear_numero()

print("O número sorteado foi:", numero)
print(verificar_palpite(palpite, numero))