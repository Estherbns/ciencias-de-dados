Tcomodo = int(input("1 - Sala | 2 - Cozinha | 3 - Quarto: "))
Plampada = float(input("digite a potencia da lampada (em Watts): "))
LComodo = float(input("Digite a largura do comodo: "))
Ccomodo = float(input("Digite o comprimento do comodo: "))
area = LComodo * Ccomodo


match Tcomodo: #
    case 1:
        Wmetro = 7
        Cfinal = (area * Wmetro) / Plampada
        print(F"A quantidade necessaria de lampadas é {Cfinal}")
    case 2:
        Wmetro = 10
        Cfinal = (area * Wmetro) / Plampada
        print(F"A quantidade necessaria de lampadas é {Cfinal}")
    case 3:
        Wmetro = 7
        Cfinal = (area * Wmetro) / Plampada
        print(F"A quantidade necessaria de lampadas é {Cfinal}")
    