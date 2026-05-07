# %%

import matplotlib.pyplot as plt
import numpy as np

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas = [42, 58, 73, 61, 89, 95]
meta = [60, 60, 70, 70, 80, 90]

fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor("#0f0f1a")
ax.set_facecolor("#0f0f1a")

x = np.arange(len(meses))
bars = ax.bar(x, vendas, width=0.5, color="#7c3aed", alpha=0.85, zorder=3)
ax.plot(x, meta, color="#f59e0b", linewidth=2, linestyle="--", marker="o",
        markersize=6, label="Meta", zorder=4)

for bar, val in zip(bars, vendas):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
            str(val), ha="center", va="bottom", color="white", fontsize=10, fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(meses, color="#a1a1aa", fontsize=11)
ax.set_yticks(range(0, 110, 20))
ax.set_yticklabels(range(0, 110, 20), color="#a1a1aa", fontsize=10)
ax.yaxis.grid(True, color="#2d2d44", linestyle="-", linewidth=0.8, zorder=0)
ax.set_axisbelow(True)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title("Desempenho de Vendas 2026", color="white", fontsize=15, fontweight="bold", pad=18)
ax.legend(facecolor="#1a1a2e", edgecolor="none", labelcolor="white", fontsize=10)

plt.tight_layout()
plt.show()


# %%
