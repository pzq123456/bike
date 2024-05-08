import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import MultiPoint
import geopandas as gpd
import pandas as pd
from sklearn.cluster import OPTICS
# read and show the data
# shape = gpd.read_file('H:\\bike\\supermap\\boundary\\boundary.shp')

def convert_list_to_MultiPoint(list):
    points = [MultiPoint(i) for i in list]
    s = gpd.GeoSeries(points, crs="EPSG:4326")
    return s

# Generate sample data
#  src\simple\class\tra16.csv
data = pd.read_csv('H:\\bike\\src\\simple\\class\\tra16.csv')


# data 只取前两列
data = data.iloc[:, :2]

# 只取前 1000 条数据
data = data[:300]

# 转化为 numpy
data = data.to_numpy()

# 训练模型
clustering = OPTICS(min_samples=50).fit(data)

# 可视化
fig, ax = plt.subplots(figsize=(10, 10))
colors = ['g.', 'r.', 'b.', 'y.', 'c.']
for i in range(len(data)):
    ax.plot(data[i][0], data[i][1], colors[clustering.labels_[i]], markersize=10)

plt.show()
