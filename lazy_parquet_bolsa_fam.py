import pandas as pd
import polars as pl
import time



#df = pl.scan_csv(r"c:\Users\esther.naveira\Documents\bolsa_familia\202601_NovoBolsaFamilia_utf8.csv" , separator=";")

#df.collect().write_parquet(r"c:\Users\esther.naveira\Documents\bolsa_familia\202601_NovoBolsaFamilia_utf8_lazy.parquet" )

df = pl.scan_parquet(r"c:\Users\esther.naveira\Documents\bolsa_familia\202601_NovoBolsaFamilia_utf8_lazy.parquet")

agregascao = (df.lazy()
              .group_by("MÊS REFERÊNCIA")
              .agg([
                  pl.col("VALOR PARCELA").count().alias("quantidade"),])   
              )

agregaExecuta = agregascao.collect()

print(agregaExecuta)