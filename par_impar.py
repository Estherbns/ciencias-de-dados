def par_ou_impar(numero): 
   if numero % 2 == 0: 
       return "par" 
   else: 
       return "ímpar" 
 
# Programa principal .
num = int(input("Digite um número: ")) 
print(f"O número {num} é {par_ou_impar(num)}")

