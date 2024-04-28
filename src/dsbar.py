import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# 加载数据 CSV
DS = pd.read_csv('src\\simple\\track\\DS20.csv')['DS']

YEAR = 2020

# 去除异常值 大于 20000
# DS = DS[DS < 10000]


# # 绘制直方图
# fig, ax1 = plt.subplots()
# n, bins, patches = ax1.hist(DS, alpha=0.5, label='Distance', bins=20)

# # 设置刻度单位
# ax1.tick_params(bottom=True, top=False, left=True, right=False, labelleft=True, labelright=False)
# ax1.set_xlabel("Distance")
# ax1.set_ylabel("Frequency")
# ax1.set_title("Distance Distribution in {}".format(YEAR))

# # 显示图例
# fig.legend()
# plt.show()


# 拟合正态分布
mu, sigma = stats.norm.fit(DS)

# 绘制直方图
fig, ax1 = plt.subplots()
n, bins, patches = ax1.hist(DS, alpha=0.5, label='Distance', bins=20)

# 设置刻度单位
ax1.tick_params(bottom=True, top=False, left=True, right=False, labelleft=True, labelright=False)
ax1.set_xlabel("Distance")
ax1.set_ylabel("Frequency")
ax1.set_title("Distance Distribution in {}".format(YEAR))

# 调整刻度范围使直方图可见
ax1.set_xlim(min(DS), max(DS))

# 添加网格线
ax1.grid(True)

# 绘制拟合曲线
ax2 = ax1.twinx()  # 共享 x 轴
x = np.linspace(min(DS), max(DS), 1000)
y = stats.norm.pdf(x, mu, sigma)
ax2.plot(x, y, label='Fit: $\mu$ = {:.2f}, $\sigma$ = {:.2f}'.format(mu, sigma))

# 设置右侧及顶部坐标轴
ax2.tick_params(bottom=False, top=True, left=False, right=True, labelleft=False, labelright=True)
ax2.set_ylabel("Probability Density")

# 调整刻度范围使曲线可见
ax2.set_ylim(0, max(y) * 1.1)

# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.show()