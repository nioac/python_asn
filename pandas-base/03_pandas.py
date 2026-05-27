# %%

import pandas as pd
dados = {
    "idades":  [27,30,35,42,28,50,35,36,36],
    "nome": ["Ana", "Barbara", "Cida", "Dona", "Teo", "Bela", None, "Lara", "Nah"],
}

dados

# %%


df = pd.DataFrame(dados)
df  

# %%

df.describe()

# %%

df.sort_values("idades")

# %%

df.sort_values("idades", ascending=False)

# %%

