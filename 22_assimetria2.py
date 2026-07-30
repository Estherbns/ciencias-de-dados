import pandas as pd #
from scipy.stats import skew
import numpy as np

df = pd.read_csv('vendas_dataorganized.csv')
#print(df)

assimetria_coluna = df["vendas_diarias"].skew()  # Calcula o coeficiente de assimetria da coluna "Salario"
print(assimetria_coluna)

mediana_vendas = np.median(df["vendas_diarias"])

media_venda = df['vendas_diarias'].mean ()
var_popu = df['vendas_diarias'].var(ddof=0) # variancia populacional
var_amostral = df['vendas_diarias'].var(ddof=1) # variancia amostral
desvio_popu_venda = df['vendas_diarias'].std(ddof=0) # desvio padrão populacional
desvio_amost_venda = df['vendas_diarias'].std(ddof=1) # desvio padrão amotral

assimetria = df['vendas_diarias'].skew() # necessita da biblioteca scipy chamada via from scipy.stats import skew 
#print(assimetria)
 
valor_curtose = df['vendas_diarias'].kurtosis() #curtose. tendencia ou não de ter valores extremos
distancia = var_amostral / (media_venda ** 2) 
distancia_perc = distancia *100
print(distancia)
print(distancia_perc)

print(f"distancia : {distancia_perc:2f}") # vai aparecer em percentual por causa do :2f






