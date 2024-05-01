import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# 加载数据 CSV
# DS = pd.read_csv('src/simple/track/DS20.csv')['DS']

# 封装
def dsbar(DSpath, YEAR, lengend = True):
    DS = pd.read_csv(DSpath)['DS']
    DS = DS[DS < 12000]
    mu, sigma = stats.norm.fit(DS)
    fig, ax1 = plt.subplots()
    n, bins, patches = ax1.hist(DS, alpha=0.5, edgecolor='black',label='Distance', bins=30)
    ax1.tick_params(bottom=True, top=False, left=True, right=False, labelleft=True, labelright=False)
    ax1.set_xlabel("Distance(m)")
    ax1.set_ylabel("Frequency(Count)")
    ax1.set_title("Distance Distribution in {}".format(YEAR))
    ax1.set_xlim(min(DS), max(DS))
    ax1.grid(True)
    ax2 = ax1.twinx()
    x = np.linspace(min(DS), max(DS), 1000)
    y = stats.norm.pdf(x, mu, sigma)
    ax2.plot(x, y, label='Fit: $\mu$ = {:.2f}, $\sigma$ = {:.2f}'.format(mu, sigma))
    ax2.tick_params(bottom=False, top=True, left=False, right=True, labelleft=False, labelright=True)
    ax2.set_ylabel("Probability Density")
    ax2.set_ylim(0, max(y) * 1.1)
    if lengend:
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    plt.show()






# 骑行时间分布
def dubar(DSpath, YEAR, lengend = True):
    DU = pd.read_csv(DSpath)['DU']
    DU = DU[DU < 200]
    mu, sigma = stats.norm.fit(DU)
    fig, ax1 = plt.subplots()
    n, bins, patches = ax1.hist(DU, alpha=0.5, edgecolor='black',label='Duration', bins=30)
    ax1.tick_params(bottom=True, top=False, left=True, right=False, labelleft=True, labelright=False)
    ax1.set_xlabel("Duration(min)")
    ax1.set_ylabel("Frequency(Count)")
    ax1.set_title("Duration Distribution in {}".format(YEAR))
    ax1.set_xlim(min(DU), max(DU))
    ax1.grid(True)
    ax2 = ax1.twinx()
    x = np.linspace(min(DU), max(DU), 1000)
    y = stats.norm.pdf(x, mu, sigma)
    ax2.plot(x, y, label='Fit: $\mu$ = {:.2f}, $\sigma$ = {:.2f}'.format(mu, sigma))
    ax2.tick_params(bottom=False, top=True, left=False, right=True, labelleft=False, labelright=True)
    ax2.set_ylabel("Probability Density")
    ax2.set_ylim(0, max(y) * 1.1)
    if lengend:
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    plt.show()

# src/simple/DU/DU16.csv
dubar('src/simple/DU/DU20.csv', '2020')
# dsbar('src/simple/track/DS20.csv', '2020')
