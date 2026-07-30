import pandas as pd
#Puxar o arquivo ClassicDisco.csv para um dataframe no pandas.
df = pd.read_csv("ClassicDisco.csv")
#Escolher tres colunas e classificalas estatiticamente e algoritmicamente
#Criar um novo csv contento somente a coluna cujo nome seja Sua Classificação
#df["Track"].to_csv("TrackQualitativaString.csv", index=False)

# Mostrar todas as linhas (sem cortar) para todo o resto do codigo
#pd.set_option('display.max_rows', None)
# mostrar todas as linhas (sem cortar) apenas para o bloco de codigo
""" with pd.option_context('display.max_rows', None):
    print(df.value_counts("Artist")) """

#Metodo para verificar a media da Coluna(Serie) Popularity De somente linhas aonde o valor da coluna Artist é Voyage
#Ou seja a media aritmetica so puxara linhas que possuem o valor Voyage Tambem
Voyage = df[df['Artist'] == 'Voyage']['Popularity'].mean()
print(Voyage)
#Verificar a media aritmetica da coluna(serie) Popularity
print(df["Popularity"].mean())
