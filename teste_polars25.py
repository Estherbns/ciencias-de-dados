import pandas as pd
import polars as pl
import time

inicio = time.time()
dfPolars = pl.scan_csv('dfPolars22.csv')


fim = time.time()
print(f"tempo de execução do polars:{fim - inicio: .6f}")  

inicio = time.time()
dfPandas = pd.read_csv('dfPandas22.csv')

fim = time.time()
print(f"tempo de execução do Pandas:{fim - inicio: .6f}")  