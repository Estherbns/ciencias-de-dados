def soma_lista(numeros): 
   total = 0 
   for numero in numeros: 
       total = total + numero 
   return total 
 
# Testando a função .
lista_teste = [3, 7, 2, 5] 
resultado = soma_lista(lista_teste) 
print(f"A soma dos elementos de {lista_teste} é {resultado}")

