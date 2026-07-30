import random #

def gerar_dados(qtd, min_val, max_val):
    return [random.randint(min_val, max_val) for i in range(qtd)]
    

print("Gerando 10 numeros aleatorios entre 1 e 100:")
dados = gerar_dados(100, 1, 1000000)
print(dados,"\n")
print("Soma de 100 numeros aleatorios: ") 
resultado = 0
for i in dados:
    resultado = resultado + i
print(resultado)
