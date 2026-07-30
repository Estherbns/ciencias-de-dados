import pandas as pd #
from scipy.stats import skew

df = pd.read_csv('Vendas_empresas.csv')

assimetria_coluna = df["Salario"].skew()  # Calcula o coeficiente de assimetria da coluna "Salario"
print(assimetria_coluna)
#print(df)

assimetria = df[["Vendas_Mes", "Horas_Extras"]].skew() # qdo for + de uma coluna coloque dois []
#print(assimetria)
 
 #curtose. tendencia ou não de ter valores extremos
valor_curtose = df['Salario'].kurtosis()
print(valor_curtose)