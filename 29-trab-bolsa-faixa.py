import polars as pl


df = pl.read_csv(r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\202601_NovoBolsaFamilia_utf8.csv", separator=';')
df.write_parquet(r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\Trab__NovoBolsaFamilia_utf8_lazy.parquet" )
df = pl.scan_parquet(r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\Trab__NovoBolsaFamilia_utf8_lazy.parquet")
#print(df.collect().columns)


df = df.collect()
df = df.with_columns(pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64))

df_com_classificacao = df.with_columns(
    pl.when(pl.col("VALOR PARCELA") < 200)
    .then(pl.lit("Baixo"))
    .when((pl.col("VALOR PARCELA") >= 200) & (pl.col("VALOR PARCELA") <= 400))
    .then(pl.lit("Médio"))
    .otherwise(pl.lit("Alto"))
    .alias("Classificação")
)
#print(df_com_classificacao)
agregascao = (df_com_classificacao.lazy()
    .group_by("UF")
    .agg([        
        pl.col("Classificação").filter(pl.col("Classificação") == "Baixo").count().alias("Qtd Baixo"),
        pl.col("Classificação").filter(pl.col("Classificação") == "Médio").count().alias("Qtd Médio"),
        pl.col("Classificação").filter(pl.col("Classificação") == "Alto").count().alias("Qtd Alto"),
    ])
)

agregaExecuta = agregascao.collect()
print(agregaExecuta)

