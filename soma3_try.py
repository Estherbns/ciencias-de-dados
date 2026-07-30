class NumeroImparError(Exception): #Cria a classe NumeroImparError que herda todas as caracteristicas de Exception
    """Exceção específica para números ímpares"""
    pass # como a classe não precisa de implementação adicional porque já herda tudo que precisa da classe Exception. O pass é um placeholder que indica "nada aqui"

def ler_pares_numeros():
    """
    Função que lê 3 pares de números inteiros, validando se são pares.
    Trata exceções para números ímpares e entradas não numéricas.
    """
    pares_encontrados = []
    
    for i in range(3):
        print(f"\n--- Par {i+1} de 3 ---")
        
        while True:  # Loop para garantir que o usuário digite um número par válido
            try:
                # Solicita o primeiro número do par
                num1_input = input(f"Digite o 1º número do {i+1}º par: ")
                num1 = int(num1_input)  # Pode lançar ValueError
                
                # Verifica se o número é ímpar
                if num1 % 2 != 0:
                    raise NumeroImparError(f"Erro: {num1} é ímpar. Apenas números pares são aceitos!")
                    #Comando raise serve para propositalmente invocar um except
                # Solicita o segundo número do par
                num2_input = input(f"Digite o 2º número do {i+1}º par: ")
                num2 = int(num2_input)  # Pode lançar ValueError
                
                # Verifica se o segundo número é ímpar
                if num2 % 2 != 0:
                    raise NumeroImparError(f"Erro: {num2} é ímpar. Apenas números pares são aceitos!")
                
                # Se chegou aqui, ambos os números são pares
                pares_encontrados.append((num1, num2))
                print(f"✓ Par {i+1} aceito: ({num1}, {num2})")
                break  # Sai do loop while para o próximo par
                
            except ValueError as e:
                print(f"Erro de valor: Você digitou algo que não é um número inteiro!")
                print(f"Detalhe: {e}")
                print("Por favor, digite apenas números inteiros.\n")
                
            except NumeroImparError as e:
                print(e)
                print("Por favor, digite apenas números pares.\n")
    
    print("\n" + "="*40)
    print("Todos os 3 pares foram lidos com sucesso!")

# Exemplo de uso
if __name__ == "__main__": #__name__ quando o codigo é executado direto do arquivo, ele tera o valor "__main__"
    #se ele for executado em outro arquivo ou codigo via import, ele tera o valor de __"nome do arquivo"__
    resultados = ler_pares_numeros()
    print(f"\nDados finais: {resultados}")


#