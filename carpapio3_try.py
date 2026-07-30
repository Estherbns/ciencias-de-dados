# Sprint 01 - Código baseado nos slides 3, 7, 10 e 12 (COM TRY/EXCEPT)

# 1. Funções matemáticas da Matriz Operacional (slide 7)
def soma(a, b):
    try:
        return a + b
    except TypeError:
        return 0

def subtracao(a, b):
    try:
        return a - b
    except TypeError:
        return 0

def multiplicacao(a, b):
    try:
        return a * b
    except TypeError:
        return 0

def divisao(a, b):
    try:
        if not isinstance(b, (int, float)):
            raise TypeError("Divisor deve ser número")
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"
    except TypeError as e:
        return f"Erro: {e}"

# 2. Etapa 1: Recepção do Cliente (slide 12)
def mostrar_cardapio():
    try:
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
    except Exception as e:
        print(f"Erro ao carregar cardápio: {e}")
        return {}

# 3. Etapa 2: Consumo (slide 12)
def fazer_pedido(cardapio):
    total_mesa = 0.0
    while True:
        try:
            pedido = input("\nDigite o nome do item (ou 'fim' para encerrar): ").strip().lower()
            
            if pedido == "fim":
                break
            
            if not pedido:
                print("❌ Entrada vazia. Digite um item válido.")
                continue
            
            if pedido in cardapio:
                total_mesa = soma(total_mesa, cardapio[pedido])
                print(f"✔ {pedido} adicionado. Subtotal: R$ {total_mesa:.2f}")
            else:
                print("❌ Item não encontrado. Tente novamente.")
                
        except KeyboardInterrupt:
            print("\n\nPedido cancelado pelo usuário.")
            break
        except EOFError:
            print("\n\nFim de entrada detectado. Encerrando pedido.")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}. Tente novamente.")
    
    return total_mesa

# 4. Etapa 3: Saída - fechar_conta (slide 12)
def fechar_conta(total_sem_taxa):
    try:
        if not isinstance(total_sem_taxa, (int, float)):
            raise TypeError("Total deve ser um número")
        
        if total_sem_taxa < 0:
            raise ValueError("Total não pode ser negativo")
        
        taxa = multiplicacao(total_sem_taxa, 0.10)
        total_com_taxa = soma(total_sem_taxa, taxa)
        
        print("\n--- CONTA FINAL ---")
        print(f"Total consumido: R$ {total_sem_taxa:.2f}")
        print(f"Taxa de serviço (10%): R$ {taxa:.2f}")
        print(f"Total a pagar: R$ {total_com_taxa:.2f}")
        return total_com_taxa
        
    except (TypeError, ValueError) as e:
        print(f"❌ Erro ao calcular conta: {e}")
        return 0.0
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return 0.0

# 5. Execução principal - Integração completa (slide 12)
def main():
    try:
        print("=== Bem-vindo ao Restaurante Tanoshimi ===")
        cardapio = mostrar_cardapio()
        
        if not cardapio:
            print("❌ Cardápio indisponível. Encerrando sistema.")
            return
        
        total_sem_taxa = fazer_pedido(cardapio)
        
        # Garantir que total_sem_taxa seja um número
        try:
            total_sem_taxa = float(total_sem_taxa)
        except (ValueError, TypeError):
            total_sem_taxa = 0.0
        
        if total_sem_taxa > 0:
            fechar_conta(total_sem_taxa)
        else:
            print("Nenhum pedido foi realizado. Até logo!")
            
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário. Até logo!")
    except Exception as e:
        print(f"\n❌ Erro crítico: {e}")
        print("Por favor, reinicie o programa.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
		 	