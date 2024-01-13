# %%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import tikzplotlib

cm = 1 / 2.54  # centimeters in inches
base_path = "/home/mhutchin/GoogleDrive/University - Postgraduate/Theses/Final/"

plt.style.use(base_path + "code/thesis.mplstyle")

# %%
plt.figure(figsize=(0.2 * cm, 0.2 * cm))

plt.gca().axis("off")
plt.gca().set_position([0, 0, 1, 1])

plt.scatter(0, 0, color="tab:blue", s=20)
plt.savefig(
    base_path + "figures/diagrams/tab_blue_scatter.pdf",
    bbox_inches="tight",
    pad_inches=0,
)

# %%
plt.figure(figsize=(0.2 * cm, 0.2 * cm))

plt.gca().axis("off")
plt.gca().set_position([0, 0, 1, 1])

plt.fill_between([-10, 10], -10, 10, color="tab:blue", alpha=0.5, edgecolor=None)
plt.savefig(
    base_path + "figures/diagrams/tab_blue_fill.pdf",
    bbox_inches="tight",
    pad_inches=0,
)

# %%
