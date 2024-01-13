# %%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import tikzplotlib

cm = 1 / 2.54  # centimeters in inches
base_path = "/home/mhutchin/GoogleDrive/University - Postgraduate/Theses/Final/"

plt.style.use(base_path + "code/thesis.mplstyle")

plt.figure(figsize=(12 * cm, 3 * cm))

plt.gca().axis("off")
plt.gca().set_position([0, 0, 1, 1])

n = 40
minx = -0.2
maxx = 0.4
alpha = 0.6

i = np.arange(n)
xi = (1 / (i + 1)) ** alpha * (((i + 1) % 2) - 0.5) * 2

Ni = i[np.logical_not(np.logical_and(xi < maxx, xi > minx))][-1]


plt.scatter(i + 1, xi, s=4)

plt.plot([0, n], [0, 0], c="gray", lw=0.5),
plt.plot([0, 0], [-1, 1], c="k")
plt.plot([Ni, Ni], [-1, 0.7], c="gray", linestyle=":")

plt.fill_between(
    [0, n], maxx, minx, color="tab:blue", alpha=0.5, zorder=-1, edgecolor=None
)
plt.fill_between(
    [Ni + 0.15, Ni + 0.8],
    0.86,
    0.99,
    color="tab:blue",
    alpha=0.5,
    zorder=-1,
    edgecolor=None,
)
# plt.fill_between([Ni, n], maxx, 1, color="gray", alpha=0.5, zorder=-2, edgecolor=None)
# plt.fill_between([Ni, n], -1, minx, color="gray", alpha=0.5, zorder=-2, edgecolor=None)

plt.text(-2, 0, "$x$")
plt.text(Ni - 0.8, 0.9, "$N_{}$")


# plt.tight_layout()
# plt.axis('tight')

plt.savefig(
    base_path + "figures/diagrams/neighbourhood.pdf",
    # bbox_inches="tight",
    pad_inches=0,
)
# tikzplotlib.save(
#     "../../figures/tex/neighbourhood.tex",
#     standalone=True,
#     axis_width=str(12 * cm),
#     axis_height=str(3 * cm),
# )

# # %%

# %%
