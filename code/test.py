# %%
import matplotlib.pyplot as plt

plt.style.use("./thesis.mplstyle")


plt.plot([0, 1], [0, 1])

plt.title(r"Test \fontname\font\ at \the\fontdimen6\font")
plt.xlabel(r"$f(x) + \int $ \fontname\font\ at \the\fontdimen6\font")

plt.tight_layout()

plt.savefig("../images/diagrams/test.pdf", bbox_inches="tight")
# %%
