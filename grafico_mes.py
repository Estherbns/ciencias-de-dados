import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Vendas_mês.csv')
#print(df)

#criar grafico de linha
df.plot(x= 'Mês', y = ['Vendas_Produto_A', 'Vendas_Produto_B', 'Vendas_Produto_C'], title='Vendas por mês')
plt.show()