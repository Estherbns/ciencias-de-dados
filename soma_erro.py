try:
    def calcular( num1, num2):        
        resultado = num1 + num2
        return resultado  
      
    resultado1 = calcular(int(input('digite o primeiro numero: ')), int(input('digite o segundo numero: ')))
    print(f'O resultado da soma é: {resultado1}')
except: # pode colocar mais de um except.
    print("erro")
else: # é referente ao except, abaixo seria o codigo a ser executado, ja que não há erro
    print("calculo sucesso ")

finally:
    print("fim do calculo")
