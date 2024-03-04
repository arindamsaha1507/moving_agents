import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

font = {
    'size'   : 16
    }

matplotlib.rc('font', **font)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

data_random = pd.read_csv(
    "random.csv", names=["Movement Scale Factor", "R0", "Standard Deviation"]
)
data_levy = pd.read_csv(
    "levy.csv", names=["Movement Scale Factor", "R0", "Standard Deviation"]
)

data_brownian = pd.read_csv(
    "brownian.csv", names=["Movement Scale Factor", "R0", "Standard Deviation"]
)


ax[0].plot(data_random["Movement Scale Factor"], data_random["R0"], 'x-', label="Random Walk")
# plt.fill_between(
#     data_random["Movement Scale Factor"],
#     data_random["R0"] - data_random["Standard Deviation"],
#     data_random["R0"] + data_random["Standard Deviation"],
#     alpha=0.2,
# )

ax[0].plot(data_levy["Movement Scale Factor"], data_levy["R0"], 'o-', label="Levy Walk")
# plt.fill_between(
#     data_levy["Movement Scale Factor"],
#     data_levy["R0"] - data_levy["Standard Deviation"],
#     data_levy["R0"] + data_levy["Standard Deviation"],
#     alpha=0.2,
# )

ax[0].plot(data_brownian["Movement Scale Factor"], data_brownian["R0"], '+-', label="Brownian Motion")
# plt.fill_between(
#     data_levy["Movement Scale Factor"],
#     data_levy["R0"] - data_levy["Standard Deviation"],
#     data_levy["R0"] + data_levy["Standard Deviation"],
#     alpha=0.2,
# )

ax[0].set_xlabel("Average Speed of Agents (cm step$^{-1}$)")
# plt.ylabel("Basic Reproduction Number")
# plt.legend()
# plt.show()

##################################################################

data_random = pd.read_csv(
    "scale_random.csv", names=["Movement Scale Factor", "R0", "Standard Deviation"]
)
data_levy = pd.read_csv(
    "scale_levy.csv", names=["Movement Scale Factor", "R0", "Standard Deviation"]
)

data_brownian = pd.read_csv(
    "scale_brownian.csv", names=["Movement Scale Factor", "R0", "Standard Deviation"]
)


ax[1].plot(data_random["Movement Scale Factor"], data_random["R0"], 'x-', label="Random Walk")
# plt.fill_between(
#     data_random["Movement Scale Factor"],
#     data_random["R0"] - data_random["Standard Deviation"],
#     data_random["R0"] + data_random["Standard Deviation"],
#     alpha=0.2,
# )

ax[1].plot(data_levy["Movement Scale Factor"], data_levy["R0"], 'o-', label="Levy Walk")
# plt.fill_between(
#     data_levy["Movement Scale Factor"],
#     data_levy["R0"] - data_levy["Standard Deviation"],
#     data_levy["R0"] + data_levy["Standard Deviation"],
#     alpha=0.2,
# )

ax[1].plot(data_brownian["Movement Scale Factor"], data_brownian["R0"], '+-', label="Brownian Motion")
# plt.fill_between(
#     data_levy["Movement Scale Factor"],
#     data_levy["R0"] - data_levy["Standard Deviation"],
#     data_levy["R0"] + data_levy["Standard Deviation"],
#     alpha=0.2,
# )

ax[1].set_xlabel("Density of Agents (m$^{-2}$)")
ax[0].set_ylabel("Average R$_0$")

plt.legend()
plt.tight_layout()
plt.savefig("plot.png")
plt.show()


