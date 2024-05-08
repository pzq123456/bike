import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString
from preprocess import load_track
from traclus import traclus, smooth_trajectory

# utils
def convert_list_to_linestring(list):
    lines = [LineString(i) for i in list]
    s = gpd.GeoSeries(lines, crs="EPSG:4326")
    return s

def tmp(): 
    # read and show the data
    shape = gpd.read_file('H:\\bike\\supermap\\boundary\\boundary.shp')

    # data\track16.pickle data\track16_simplified.pickle
    track = load_track('H:\\bike\\data\\track16_sim.pickle')
    # 提取 10 条轨迹
    track = track[:50]
    track = [np.array(i) for i in track]
    partitions, segments, dist_matrix, clusters, cluster_assignments, representative_trajectories = traclus(track)

    # 去空
    representative_trajectories = [i for i in representative_trajectories if i is not None]

    # 转化为 GeoDataFrame
    representative_trajectories = convert_list_to_linestring(representative_trajectories)

    # 转化为 GeoDataFrame
    track = convert_list_to_linestring(track)
    # 以图层的方式 绘制在地图上
    fig, ax = plt.subplots(figsize=(10, 10))
    shape.boundary.plot(ax=ax)
    track.plot(ax=ax, color='gray')
    representative_trajectories.plot(ax=ax, color='red')

    plt.show()

if __name__ == '__main__':
    tmp()








