
print("1 - cadastrar | 2 - listar | 3 - sair")
opcao = int(input(""))
#
match opcao:
    case 1:
        print(" escolheu cadastrar")    
    case 2:
        print(" escolheu listar")
    case 3:
        print("escolheu sair")
    case _:    # comendo de excessão ( equivalente o else)
        print("commando errado")