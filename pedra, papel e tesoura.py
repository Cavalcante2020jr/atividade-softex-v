import random

opcoes = ['pedra', 'papel', 'tesoura']

usuario = input("Escolha: pedra, papel ou tesoura: ").lower()

if usuario not in opcoes:
    print("Escolha inválida. Por favor, digite pedra, papel ou tesoura.")
else:
    computador = random.choice(opcoes)

    print(f"\nVocê escolheu: {usuario}")
    print(f"O computador escolheu: {computador}")

    if usuario == computador:
        resultado = "Empate!"
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "tesoura" and computador == "papel") or \
         (usuario == "papel" and computador == "pedra"):
        resultado = "Você venceu!"
    else:
        resultado = "O computador venceu!"

    # Exibe o resultado
    print(f"\nResultado: {resultado}")
