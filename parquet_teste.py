import polars as pl

df = pl.scan_csv('202601_NovoBolsaFamilia_utf8.csv')

df.collect().write_parquet('202601_NovoBolsaFamilia_utf8_limpo.parquet')