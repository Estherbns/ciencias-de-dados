import polars as pl


df = pl.scan_csv("delegacias_rj_powerbi_sem_flag.csv")

# Calcular Q1 (percentil 25%) e Q3 (percentil 75%)
q1 = df.collect()["roubo_veiculo"].quantile(0.25)
q3 = df.collect()["roubo_veiculo"].quantile(0.75)

# Criar a coluna flag com a lógica do boxplot
df = df.collect().with_columns( # .with_columns é para criar ou alterar colunas no polars
    pl.when(pl.col("roubo_veiculo") < q1)
    .then(pl.lit("menos"))
    .when(pl.col("roubo_veiculo") > q3)
    .then(pl.lit("mais"))
    .otherwise(pl.lit("medio"))
    .alias("flag")
)

df.write_csv("delegacias_rj_powerbi_com_novo_flag.csv")

print(df)
