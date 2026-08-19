import polars as pl
import pandas as pd

arquivo1 = r"C:\Users\esther.naveira\Documents\trab-final\BASE DE ATUALIZAÇÃO - MÊS DE REFERÊNCIA AGOSTO 2026.csv"
df = pl.read_csv(arquivo1, separator=';')

arquivo2 = r"C:\Users\esther.naveira\Documents\trab-final\BASE DE ATUALIZAÇÃO - MÊS DE REFERÊNCIA JULHO 2026.csv"
df2 = pl.read_csv(arquivo2, separator=';')
#print(df2)
df_concatenado = pl.concat([df, df2])
df_concatenado.write_parquet(r"C:\Users\esther.naveira\Documents\trab-final\BASE DE ATUALIZAÇÃO - juntos 2026.parquet")
df_concatenado = pl.scan_parquet(r"C:\Users\esther.naveira\Documents\trab-final\BASE DE ATUALIZAÇÃO - juntos 2026.parquet")

#print(df_concatenado)

# estatísticas
# Calcular Q1 (percentil 25%) e Q3 (percentil 75%)

q1 = df_concatenado.collect()["Roubos de Veículos"].quantile(0.25)
q3 = df_concatenado.collect()["Roubos de Veículos"].quantile(0.75)


# Criar a coluna flag com a lógica do boxplot
df = df_concatenado.collect().with_columns( # .with_columns é para criar ou alterar colunas no polars
    pl.when(pl.col("Roubos de Veículos") < q1)
    .then(pl.lit("menos"))
    .when(pl.col("Roubos de Veículos") > q3)
    .then(pl.lit("mais"))
    .otherwise(pl.lit("medio"))
    .alias("flag")
)

#----
df.write_parquet(r"C:\Users\esther.naveira\Documents\trab-final\BASE DE ATUALIZAÇÃO - juntos 2026.parquet")
print(df)

