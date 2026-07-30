def calculadora(num1, num2, operador): 
   if operador == '+': 
       return num1 + num2 
   elif operador == '-': 
       return num1 - num2 
   elif operador == '*': 
       return num1 * num2 
   elif operador == '/': 
       if num2 != 0: 
           return num1 / num2 
       else: 
           return "Erro: divisão por zero" 
   else: 
       return "Operador inválido" 
 
# Testando a função 
print(f"10 / 2 = {calculadora(10, 2, '/')}") 
print(f"5 + 3 = {calculadora(5, 3, '+')}") 
print(f"8 * 4 = {calculadora(8, 4, '*')}") 
print(f"15 - 7 = {calculadora(15, 7, '-')}") 
print(f"10 / 0 = {calculadora(10, 0, '/')}") 
print(f"10 % 2 = {calculadora(10, 2, '%')}")
#