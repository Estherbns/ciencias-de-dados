import polars as pl
import pandas as pd

arquivo1 = r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\202601_NovoBolsaFamilia_utf8.csv"
df = pl.read_csv(arquivo1, separator=';')
arquivo2 = r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\202603_NovoBolsaFamilia_utf8.csv"
df2 = pl.read_csv(arquivo2, separator=';')
df_concatenado = pl.concat([df, df2])
df_concatenado.write_csv(r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\202601_202603_NovoBolsaFamilia_juntos_utf8.csv")
#print(df_concatenado)

# estatísticas
df_concatenado = df_concatenado.with_columns(pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64))
# Calcular Q1 (percentil 25%) e Q3 (percentil 75%)
#q1 = df.collect()["VALOR PARCELA"].quantile(0.25)  - não aceitou o collect em casa
q1 = df_concatenado["VALOR PARCELA"].quantile(0.25)
q3 = df_concatenado["VALOR PARCELA"].quantile(0.75)

# Criar a coluna flag com a lógica do boxplot
df = df_concatenado.with_columns( # .with_columns é para criar ou alterar colunas no polars
    pl.when(pl.col("VALOR PARCELA") < q1)
    .then(pl.lit("menos"))
    .when(pl.col("VALOR PARCELA") > q3)
    .then(pl.lit("mais"))
    .otherwise(pl.lit("medio"))
    .alias("flag")
)

df.write_parquet(r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\202601_202603_NovoBolsaFamilia_com_flag_utf8.parquet")

print(df)
