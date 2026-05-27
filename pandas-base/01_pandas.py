# %%

import pandas as pd

# %%

idade = [27, 30, 25, 28, 32, 29, 31, 26, 24, 33]

# %%

media = sum(idade) / len(idade)

# %%

total = 0
for i in idade:
    total += i (- media) ** 2

variancia = total / (len(idade) - 1)

# %%

idade_series = pd.Series(idade)
idade_series

# %%

idade_series.describe()

# %%

idade_series.mean()

# %%

idade_series.var()

# %%

idade_series.std()

# %%

idade_series.median()

# %%

idade_series.quantile(0.25)

# %%

idade_series.index

# %%

len(idade_series)

# %%

idade_series.shape[0]

# %%

idade_series.name
