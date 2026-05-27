# %%

import pandas as pd

# %% 


import os
os.getcwd()

# %%

df = pd.read_csv(r"C:\Users\paulo\Documents\TeoPython\Pandas_2025\data\clientes.csv", sep=";")


# %%


df.shape

# %%

df

# %% 


df.head(2)

# %%

df_10 = df.head(10).copy()
df_10

# %%

df_10.to_csv(r"C:\Users\paulo\Documents\TeoPython\Pandas_2025\data\clientes_10.csv", index=False, sep=";")


# %%

