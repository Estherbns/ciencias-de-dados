import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame
dados = {
    'Aluno': ['Ana', 'Carlos', 'Mariana', 'Pedro', 'Julia'],
    'Matemática': [8.5, 7.0, 9.5, 6.5, 9.0],
    'Português': [9.0, 6.5, 8.0, 7.5, 8.5],
    'Ciências': [7.5, 8.0, 9.0, 7.0, 9.5]
}
df = pd.DataFrame(dados)

# Criando o gráfico de barras agrupadas
# .plot() é um método do DataFrame que permite criar gráficos diretamente a partir dos dados contidos nele.
#set_index() é usado para definir a coluna 'Aluno' como índice do DataFrame, o que facilita a plotagem das notas por aluno.
df.set_index('Aluno').plot(kind='bar', # kind decide o tipo de gráfico 
                           figsize=(12, 6), # figsize define o tamanho da figura
                           title='Notas dos Alunos por Disciplina', # title define o título do gráfico
                           xlabel='Aluno', # xlabel define o rótulo do eixo x
                           ylabel='Nota', # ylabel define o rótulo do eixo y
                           rot=0,  # Rotação das labels
                           colormap='viridis', # colormap define o mapa de cores
                           edgecolor='black') # edgecolor define a cor da borda das barras


plt.legend(title='Disciplina', loc='upper right') #.legend() adiciona uma legenda ao gráfico, title define o título da legenda e loc define a posição da legenda no gráfico.
plt.grid(axis='y', alpha=0.3) # .grid() adiciona uma grade ao gráfico, axis define o eixo em que a grade será aplicada (neste caso, apenas no eixo y) e alpha define a transparência da grade.
plt.show() #.show() exibe o gráfico na tela