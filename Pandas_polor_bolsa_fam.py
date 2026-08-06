import pandas as pd
import polars as pl
import time

inicio = time.time()
df1 = pd.read_csv('202601_NovoBolsaFamilia.csv', encoding='latin1')
df2 = pd.read_csv('202602_NovoBolsaFamilia.csv', encoding='latin1')

resultado = pd.concat([df1, df2], ignore_index= True)
fim = time.time()

print(f"tempo de execução do Pandas:{fim - inicio: .6f}")  