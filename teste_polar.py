import pandas as pd
import polars as pl
import time

inicio = time.time()

dfPolars = pl.DataFrame(
    {
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Carol", "Dan", "Eve"],
        "department": ["Sales", "Sales", "HR", "HR", "IT"],
        "salary": [50000, 55000, 48000, 62000, 70000],
        "active": [True, True, False, True, True],
    }
)

dfPolars.write_csv('dfPolar22.csv')

fim = time.time()
print(f"tempo de execução do polars:{fim - inicio: .6f}")  

inicio = time.time()
dfPandas = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Carol", "Dan", "Eve"],
        "department": ["Sales", "Sales", "HR", "HR", "IT"],
        "salary": [50000, 55000, 48000, 62000, 70000],
        "active": [True, True, False, True, True],
    }
)

dfPandas.to_csv('dfPandas22.csv')

fim = time.time()
print(f"tempo de execução do Pandas:{fim - inicio: .6f}")  