import polars as pl
import time

df = pl.DataFrame({
    "nome": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda"],
    "idade": [25, 32, 19, 41, 28],
    "cidade": ["SP", "RJ", "SP", "BH", "RJ"],
    "salario": [5000, 7200, 3800, 9200, 6100]
})

print("=" * 50)
print("DATAFRAME ORIGINAL:")
print("=" * 50)
print(df)
print("\n")

# 2. USANDO .lazy() - CRIA O PLANO DE EXECUÇÃO
print("=" * 50)
print("PASSO 1: CRIANDO O PLANO COM .lazy()")
print("=" * 50)

plano_lazy = (df
    .lazy()  # <-- Entra no modo preguiçoso
    .filter(pl.col("idade") > 20)  # Filtra maiores de 20 anos
    .group_by("cidade")  # Agrupa por cidade
    .agg([
        pl.col("salario").mean().alias("salario_medio"),
        pl.col("nome").count().alias("quantidade")
    ])
    .sort("salario_medio", descending=True)  # Ordena do maior salário
)

print("✅ Plano criado, mas NENHUM dado foi processado ainda!")
print(f"Tipo do objeto: {type(plano_lazy)}")
print("\n")

# 3. USANDO .explain() - MOSTRA O PLANO OTIMIZADO (SEM EXECUTAR)
print("=" * 50)
print("PASSO 2: ANALISANDO O PLANO COM .explain()")
print("=" * 50)

plano_otimizado = plano_lazy.explain()
print("📋 Plano de execução otimizado (ainda não executado):")
print("-" * 40)
print(plano_otimizado)
print("-" * 40)
print("\n")

# 4. USANDO .collect() - EXECUTA O PLANO E TRAZ OS DADOS
print("=" * 50)
print("PASSO 3: EXECUTANDO COM .collect()")
print("=" * 50)

resultado = plano_lazy.collect()  # <-- Agora sim executa!

print("✅ Plano executado! Dados processados e prontos:")
print("-" * 40)
print(resultado)
print("-" * 40)
print(f"Tipo do resultado: {type(resultado)}")
print("\n")

# 5. DEMONSTRANDO A DIFERENÇA NA PRÁTICA
print("=" * 50)
print("COMPARAÇÃO: .lazy() vs .collect()")
print("=" * 50)

# Sem .lazy() - executa imediatamente
print("🔹 Sem .lazy():")
inicio = time.time()
resultado_direto = (df
    .filter(pl.col("idade") > 20)
    .group_by("cidade")
    .agg([
        pl.col("salario").mean().alias("salario_medio"),
        pl.col("nome").count().alias("quantidade")
    ])
    .sort("salario_medio", descending=True)
)
print(resultado_direto)
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.4f} segundos")
print("\n")

# Com .lazy() - executa apenas no .collect()
print("🔹 Com .lazy():")
inicio = time.time()
resultado_lazy = (df
    .lazy()
    .filter(pl.col("idade") > 20)
    .group_by("cidade")
    .agg([
        pl.col("salario").mean().alias("salario_medio"),
        pl.col("nome").count().alias("quantidade")
    ])
    .sort("salario_medio", descending=True)
    .collect()  # <-- executa aqui
)
fim = time.time()
print(resultado_lazy)
print(f"Tempo de execução: {fim - inicio:.4f} segundos")
print("\n")

# 6. BÔNUS: MOSTRANDO O TEMPO DE EXECUÇÃO
print("=" * 50)
print("BÔNUS: ENTENDENDO A OTIMIZAÇÃO")
print("=" * 50)

# Criando um dataframe maior para ver a diferença
df_grande = pl.DataFrame({
    "col_a": range(1000000),
    "col_b": range(1000000),
    "col_c": range(1000000)
})

print("🔍 Com .lazy(), o Polars só processa o necessário:")
plano_otimizado_2 = (df_grande
    .lazy()
    .select([  # Só seleciona uma coluna
        pl.col("col_a")
    ])
    .filter(pl.col("col_a") > 500000)
    .explain()  # Veja como ele otimiza
)

print("Plano sem otimização (mostra todas as colunas):")
print("(O Polars vai fazer 'Projection Pushdown' para eliminar col_b e col_c)")
print("-" * 40)
print(plano_otimizado_2[:500] + "...")  # Mostra só o início
print("-" * 40)


	