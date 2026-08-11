import pandas as pd
import polars as pl
import time

df = pl.scan_csv(r"c:\Users\esther.naveira\Documents\bolsa_familia\202601_NovoBolsaFamilia_utf8.csv")

inicio = time.time()
print(df.collect().columns)
fim = time.time()
print(f"Tempo de execução: {fim - inicio: .4f} segundos")

inicio = time.time()
colunas = (df
           .lazy()
           .collect_schema()
           .names()
)
print(colunas)
fim = time.time()
print(f"Tempo de execução: {fim - inicio: .4f} segundos")


