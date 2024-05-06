# https://github.com/GISerWang/Spatio-temporal-Clustering
# TRACLUS 算法
# pip install geopandas
# pip --proxy 127.0.0.1:7890 install geopandas
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point,LineString
import numpy as np
import pickle

from traclus import traclus, smooth_trajectory

# utils
def convert_list_to_linestring(lst):
    lines = [LineString(i) for i in lst]
    s = gpd.GeoSeries(lines, crs="EPSG:4326")
    return s

# 读取不定长的轨迹数据
def load_track(path):
    with open(path,'rb') as f:
        data = pickle.load(f)
    return data

def tmp(): 
    # read and show the data
    shape = gpd.read_file('H:\\bike\\supermap\\boundary\\boundary.shp')

    # data\track16.pickle
    track = load_track('H:\\bike\\data\\track16.pickle')
    # 打印长度
    # print(len(track))
    # 提取前十条轨迹
    track = track[:1000]

    # 转化为 GeoDataFrame
    track = convert_list_to_linestring(track)
    # 以图层的方式 绘制在地图上
    fig, ax = plt.subplots(figsize=(10, 10))
    shape.boundary.plot(ax=ax)
    track.plot(ax=ax, color='red')

    plt.show()

# Your Trajectory Data
track = load_track('H:\\bike\\data\\track16.pickle')

track = track[:10]
# 对每一个元素进行转换 numpy.array 
track = [np.array(i) for i in track]

trajectories = track

# Run the TRACLUS Algorithm
partitions, segments, dist_matrix, clusters, cluster_assignments, representative_trajectories = traclus(trajectories)

# 去掉空的轨迹
representative_trajectories = [i for i in representative_trajectories if len(i) > 0]

# Smooth the Representative Trajectories
smoothed_representative_trajectories = [smooth_trajectory(trajectory, window_size=21) for trajectory in representative_trajectories]

# Plot the Results
fig, ax = plt.subplots(figsize=(10, 10))
for trajectory in trajectories:
    ax.plot(trajectory[:, 0], trajectory[:, 1], color='gray', alpha=0.5)
for trajectory in smoothed_representative_trajectories:
    ax.plot(trajectory[:, 0], trajectory[:, 1], color='red')
plt.show()




