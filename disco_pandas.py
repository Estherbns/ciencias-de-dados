import pandas as pd

df = pd.read_csv('ClassicDisco.csv')
pd.options.display.min_rows = 40
pd.options.display.max_rows = 60

total = df[['Artist','Track' ]].value_counts() # total de cada artista.
print(total)

#df[["Artist","Track"]].to_csv("df_artista2.csv", index = False) #criando arquivo csv - E qdo for + de uma coluna, coloca [[ ]], duas vezes
#df["Artist"].to_csv("df_artista.csv", index = False)

#print(df.to_string()) # imprime o arquivo todo

#print(df['Artist']) # puxa só uma coluna  
