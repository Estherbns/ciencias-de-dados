
import polars as pl
#import time

df = pl.read_csv(r"c:\Users\esther.naveira\Documents\bolsa_familia\202601_NovoBolsaFamilia_utf8.csv", separator=';')
df.write_parquet(r"c:\Users\esther.naveira\Documents\bolsa_familia\Trab__NovoBolsaFamilia_utf8_lazy.parquet" )
df = pl.scan_parquet(r"c:\Users\esther.naveira\Documents\bolsa_familia\Trab__NovoBolsaFamilia_utf8_lazy.parquet")
print(df.collect().columns)
#print(df['UF'] == 'SP')

df = df.collect()
df = df.with_columns(pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64))
filtro = (pl.col('UF') == 'RJ') & (pl.col('VALOR PARCELA') > 200)


estatisticas = (df.filter(filtro).select(
        pl.col('VALOR PARCELA').mean().alias('valor_medio'),
        pl.col('VALOR PARCELA').min().alias('valor_minimo'),
        pl.col('VALOR PARCELA').max().alias('valor_maximo'),
        pl.col('NOME FAVORECIDO').count().alias('total_beneficiarios')))
print(estatisticas)