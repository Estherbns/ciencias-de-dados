import pandas as pd
import polars as pl
import time

inicio = time.time()
df1 = pl.scan_csv('202601_NovoBolsaFamilia_utf8.csv')
df2 = pl.scan_csv('202602_NovoBolsaFamilia_utf8.csv')

resultado = pl.concat([df1, df2], rechunk=True).collect()
resultado.write_parquet('bolsa_familia12_limpo.parquet')

fim = time.time()

print(f"tempo de execução do Polars:{fim - inicio: .6f} segundos")  