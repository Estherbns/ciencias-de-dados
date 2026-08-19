import polars as pl


df = pl.read_csv(r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\202601_NovoBolsaFamilia_utf8.csv", separator=';')
df.write_parquet(r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\Trab__NovoBolsaFamilia_utf8_lazy.parquet" )
df = pl.scan_parquet(r"c:\Users\esthe\OneDrive\Documentos\Esther\Apostilas\analise dados-senac\bolsa_familia\Trab__NovoBolsaFamilia_utf8_lazy.parquet")
#print(df.collect().columns)


df = df.collect()
df = df.with_columns(pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64))


agregascao = (df.lazy()
              .group_by("UF")
              .agg([
                  pl.col("VALOR PARCELA").count().alias("Valor Total"),
                  pl.col("VALOR PARCELA").mean().alias("Valor Médio"),
                  pl.col("NOME FAVORECIDO").count().alias("Total Beneficiários"),])   
              )

agregaExecuta = agregascao.collect()
df2 = agregaExecuta
print("-----------novo dataframe----------------")
print(df2)



