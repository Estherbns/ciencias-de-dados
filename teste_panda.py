import pandas as pd
import numpy as np

df = pd.read_excel('Vendas_empresas.xlsx')

#print(df.head(5))
#print(df.tail(5))
#print(df.columns)
#print(df.dtypes)
#print(df.shape)
#print(df.describe())
#print(df.loc[0:5,"ID_Funcionario":"Salario"])
#print(df.iloc[0:5,0:5])
#print(df.info())
df2 = df[df["Salario"] > 5000]
df2 = df.query('Salario > 5000 and Idade > 30')
#print(df)
df.loc[df['Salario'] > 5000, 'Cargo'] = df.loc[df['Salario'] > 5000, 'Cargo'].fillna("Pleno")
df2 = df
#df2.drop_duplicates("Cargo") #Comando sem o inplace=true não altera o dataframe, somente para vizualização
#df2.drop_duplicates("Cargo", inplace=True) # Comando alterara o dataframe
df['DobroIdade'] = df['Idade' ] *2
df['Nome'].str.upper().str.strip()
df.rename(columns={'DobroIdade': 'IdadeDobro'}, inplace=True)
print(df) #