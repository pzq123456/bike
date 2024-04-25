from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.collections import PolyCollection


# 读取数据
# UID,ST
# 759,2016/8/1 0:23
# 1440,2016/8/1 0:25
# 5463,2016/8/1 0:26
# 4666,2016/8/1 0:32
# 2193,2016/8/1 0:33
# 5114,2016/8/1 0:35

weekDayName = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hourName = ["0:00-1:00", "1:00-2:00", "2:00-3:00", "3:00-4:00", 
            "4:00-5:00", "5:00-6:00", "6:00-7:00", "7:00-8:00", 
            "8:00-9:00", "9:00-10:00", "10:00-11:00", "11:00-12:00", 
            "12:00-13:00", "13:00-14:00", "14:00-15:00", "15:00-16:00", 
            "16:00-17:00", "17:00-18:00", "18:00-19:00","19:00-20:00", 
            "20:00-21:00", "21:00-22:00", "22:00-23:00", "23:00-24:00"]
hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
         20, 21, 22, 23]
frequency = [] # 7 * 24

# 首先读取数据
data = pd.read_csv('src/simple/cdf20.csv')


data['ST'] = pd.to_datetime(data['ST'])
# 添加星期几
data['weekday'] = data['ST'].dt.weekday
# 添加小时
data['hour'] = data['ST'].dt.hour

# 首先按照 weekday 分组，对于每一个 weekday 再按照 hour 分组统计数量
grouped = data.groupby(['weekday', 'hour']).size().reset_index(name='count')

# 生成 7 * 24 的矩阵
for i in range(7):
    frequency.append([0] * 24)

for index, row in grouped.iterrows():
    frequency[row['weekday']][row['hour']] = row['count']


ax = plt.figure().add_subplot(projection='3d')

def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]


ax = plt.figure().add_subplot(projection='3d')

# x = np.linspace(0., 10., 31)
# lambdas = range(1, 9)

# # verts[i] is a list of (x, y) pairs defining polygon i.
# gamma = np.vectorize(math.gamma)
# verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
#          for l in lambdas]
# facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))

# poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
# ax.add_collection3d(poly, zs=lambdas, zdir='y')

# ax.set(xlim=(0, 10), ylim=(1, 9), zlim=(0, 0.35),
#        xlabel='x', ylabel=r'$\lambda$', zlabel='probability')

# plt.show()

verts = []
for i in range(7):
    verts.append(polygon_under_graph(hours, frequency[i]))

# 每一个面的颜色 weekday 为一个颜色
facecolors = plt.cm.viridis(np.linspace(0, 1, 7))

poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=range(7), zdir='y')

ax.set(xlim=(0, 23),
       ylim=(0, 7), 
       zlim=(0, 500),
         xlabel='hour', ylabel='weekday', zlabel='frequency')

# 减少 x 轴的标签并旋转
ax.set_xticks(hours[::2])
ax.set_xticklabels(hourName[::2], rotation=45)
# 调整 xlabel 的位置
ax.xaxis.set_label_coords(0.5, -0.1)

# add weekday names
ax.set_yticks(range(7))
ax.set_yticklabels(weekDayName)

# 图例
plt.colorbar(poly, ax=ax, orientation='vertical')
plt.title('3D plot of frequency')

plt.show()

