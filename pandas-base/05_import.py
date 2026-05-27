# %%

import pandas as pd


df = pd.read_csv(r"C:\Users\paulo\Documents\TeoPython\Pandas_2025\data\transacoes.csv", sep=";")


df


# %% 

df.shape

# %%

df.info(memory_usage="deep")

# %%

df.dtypes

# %%

df["QtdePontos"].dtypes

# %%

columns = ['IdTransacao', 'IdCliente']

df[columns]

# %%

df.iloc[0:2]

# %%

df.loc[0:2]

# %%

nomes_novos = {
    "IdTransacao": "ID Transação",
    "IdCliente": "ID Cliente",
    "ValorCompra": "Valor Compra",
    "QtdePontos": "Quantidade Pontos"
}

df_new = df.rename(columns=nomes_novos)

# %%

df_new

# %%

ordem_colunas = [
    "ID Cliente",
    "ID Transação",
    "Valor Compra",
    "Quantidade Pontos" 
]   

df_new.T


# %%


df['Nova Coluna'] = df['Quantidade Pontos'] * 2
df


# %%

df['Coluna_1'] = float("1")
df

# %%

df.to_csv(r"C:\Users\paulo\Documents\TeoPython\Pandas_2025\data\transacoes_1.csv", index=False, sep=";")

# %%


import sys

sys.path

# %% Exercícios

DATA = r"C:\Users\paulo\Documents\TeoPython\Pandas_2025\data"

df_clientes   = pd.read_csv(f"{DATA}/clientes.csv",   sep=";")
df_transacoes = pd.read_csv(f"{DATA}/transacoes.csv", sep=";")
df_produtos   = pd.read_csv(f"{DATA}/produtos.csv",   sep=";")

# %% 1 - Quantas linhas há no arquivo clientes.csv?

df_clientes.shape[0]

# %% 2 - Quantas colunas do tipo int há no arquivo transacoes.csv?

df_transacoes.select_dtypes(include="int64").shape[1]

# %% 3 - Quantas colunas do tipo object há no arquivo produtos.csv?

df_produtos.select_dtypes(include="object").shape[1]

# %% 4 - Qual o id do cliente no índice 4 no arquivo clientes.csv?

df_clientes.iloc[4]["idCliente"]

# %% 5 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar)?

df_clientes.iloc[9]["qtdePontos"]