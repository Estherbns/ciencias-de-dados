
opcao = int(input("digite o numero do mês: "))

match opcao:
    case 1:
        print(" janeiro")    
    case 2:
        print(" fevereiro")
    case 3:
        print("março")
    case 4:
        print(" Abril")    
    case 5:
        print(" Maio")
    case 6:
        print("Junho")
    case 7:
        print(" Julho")    
    case 8:
        print(" Agosto")
    case 9:
        print("Setembro")
    case 10:
        print(" Outubro")    
    case 11:
        print(" Novembro")
    case 12:
        print("Dezembro")
    case _:    # comendo de excessão ( equivalente o else).
        print("dgite novamene")