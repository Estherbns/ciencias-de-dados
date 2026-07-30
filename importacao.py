import pandas as pd

df = pd.read_excel("Vendas_empresas.xlsx")

df.to_csv("Vendas_empresas.csv", index=False) # Salvar como CSV