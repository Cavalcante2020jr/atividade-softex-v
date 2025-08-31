cardapio = {
    1: {"nome": "Feijoada", "preco": 25.00},
    2: {"nome": "Pizza", "preco": 15.00},
    3: {"nome": "Cerveja", "preco": 8.00}
}

print("=== Cardápio ===")
for codigo, item in cardapio.items():
    print(f"{codigo} - {item['nome']} - R${item['preco']:.2f}")

try:
    escolha = int(input("\nDigite o código do item desejado: "))
    if escolha in cardapio:
        item_escolhido = cardapio[escolha]
        print(f"\nVocê escolheu: {item_escolhido['nome']} - R${item_escolhido['preco']:.2f}")
    else:
        print("\nOpção inválida.")
except ValueError:
    print("\nEntrada inválida. Por favor, digite um número.")
