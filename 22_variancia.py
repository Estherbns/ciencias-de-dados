import pandas as pd #
import numpy as np
# Dados fornecidos
dados = {
'vendas': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
'custo': [5, 8, 12, 18, 22, 28, 32, 38, 42, 48]
 }
df = pd.DataFrame(dados)
arr = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

#********* boxplot
# Calculando os Quartis (usando os dados de 'vendas' ou 'arr')
q1 = np.percentile(df['vendas'], 25)  # ou np.percentile(arr, 25)
q2 = np.percentile(df['vendas'], 50)  # Mediana
q3 = np.percentile(df['vendas'], 75)

# Encontrando o IQR
iqr = q3 - q1

# Limite superior
limite_superior = q3 + 1.5 * iqr

# Exibindo os resultados
print(f"Q1: {q1}")
print(f"Q2 (Mediana): {q2}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite Superior: {limite_superior}")

#********** fim boxplot

# varancia -var 
var_popul_venda = df['vendas'].var(ddof=0)
print(var_popul_venda)

var_amost_venda = df['vendas'].var(ddof=1)
print(var_amost_venda)

var_poul_arr = np.var(arr)
print("*********")
print(var_poul_arr)

var_amost_arr = np.var(arr, ddof=1)
print(var_amost_arr)

print("*********")
# desvio padrão
des_p_popu_venda = df['vendas'].std(ddof=0)
des_p_amost_venda = df['vendas'].std(ddof=1)

# coeficiente de variação
CV_venda = (df['vendas'].std() / df['vendas'].mean()) *100

print(des_p_popu_venda)
print(des_p_amost_venda)
print(CV_venda)

media = df['vendas'].mean()
distancia = (var_popul_venda / (media ** 2)) * 100

print(media)
print(distancia)


