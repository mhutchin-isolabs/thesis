# %%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import tikzplotlib

base_path = "/home/mhutchin/GoogleDrive/University - Postgraduate/Theses/Final/"

plt.style.use(base_path + "code/thesis.mplstyle")

plt.figure(figsize=(1, 1))

plt.gca().axis("off")

X, Y = np.meshgrid(*([np.linspace(-2, 2, 100)] * 2))

Z = np.exp(-1 / 2 * (X**2 + Y**2)) * 1 / np.sqrt(2 * np.pi)

cmap = matplotlib.cm.get_cmap("Blues")

levels = 6
colors = [(0.0, 0.0, 0.0, 0.0)] + [cmap(i / (levels - 1)) for i in range(levels)]

plt.contourf(X, Y, Z, levels=6, colors=colors, vmax=1, vmin=0, extend="neither")

plt.tight_layout()

plt.savefig(
    base_path + "figures/diagrams/simple_distribution.pdf",
    bbox_inches="tight",
    pad_inches=0,
)
# tikzplotlib.save("../../figures/tex/simple_distribution.tex")
# %%
