def contagem_regressiva(inicio): 
   for i in range(inicio, 0, -1): 
       print(i) 
   print("FIM!") 
 
# Testando a função .
contagem_regressiva(5) 
 

# Versão alternativa com while, função sera re-declarada com os novos blocos de codigo: 

def contagem_regressiva(inicio): 
   while inicio >= 1: 
       print(inicio) 
       inicio -= 1 
   print("fim!")

contagem_regressiva(7)

