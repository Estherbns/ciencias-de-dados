import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Ano': [2019, 2020, 2021, 2022, 2023],
    'Vendas': [150, 200, 250, 300, 350 ]
}

df = pd.DataFrame(dados)

#criar grafico de linha
df.plot(x= 'Ano', y = 'Vendas', title='Vendas por ano')
plt.show()