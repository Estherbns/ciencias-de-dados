import numpy as np #

#dados_vendas = np.array([3, 7, 8, 10, 14, 18, 21, 25])
#dados_vendas = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
dados_vendas = np.array([2, 4, 6, 8, 10, 12, 15, 18, 22, 30])

print(dados_vendas)

media_vendas = np.mean(dados_vendas)
# Calculando a Mediana (robusta a extremos)
mediana_vendas = np.median(dados_vendas)

Distancia = (media_vendas - mediana_vendas) / mediana_vendas
print(media_vendas)
print(mediana_vendas)
print(Distancia)