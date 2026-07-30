import pandas as pd
dados = {
'cargos': ["assistente", "auxiliar", "gerente"],
'salários': [2500, 1800, 7500] 
 }

dados_bi = pd.DataFrame(dados)

dados_bi.to_csv("dados_bi.csv", index = False)

print(dados_bi)

#