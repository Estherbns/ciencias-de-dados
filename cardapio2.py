# Dicionário representando o cardápio do restaurante (Prato: Preço)
"""cardapio = {
    "Hambúrguer Artesanal": 32.50,
    "Batata Frita com Cheddar": 18.00,
    "Refrigerante Lata": 7.50,
    "Suco Natural": 9.00,
    "Pizza Margherita": 45.00,
    "nhoque ao sugo": 60.00
}


def exibir_menu():
    print("====== CARDÁPIO ======")
    # Percorre o dicionário exibindo cada item e seu respectivo valor
    for indice, (prato, preco) in enumerate(cardapio.items(), 1):
        print(f"{indice} - {prato:<25} | R$ {preco:.2f}")
    print("======================")

exibir_menu ()"""


# OU


# Etapa 1: Recepção do Cliente (slide 12)
def mostrar_cardapio():
    cardapio = {
        "sushi": 25.0,
        "sashimi": 30.0,
        "tempura": 20.0,
        "yakisoba": 28.0,
        "missoshiro": 10.0
    }
    print("\n--- Cardápio do Restaurante Tanoshimi ---")
    for item, preco in cardapio.items():
        print(f"{item}: R$ {preco:.2f}")
    return cardapio

mostrar_cardapio()
