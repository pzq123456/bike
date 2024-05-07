import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import LineString
from preprocess import load_track

# utils
def convert_list_to_linestring(lst):
    lines = [LineString(i) for i in lst]
    s = gpd.GeoSeries(lines, crs="EPSG:4326")
    return s

def tmp(): 
    # read and show the data
    shape = gpd.read_file('H:\\bike\\supermap\\boundary\\boundary.shp')

    # data\track16.pickle data\track16_simplified.pickle
    track = load_track('H:\\bike\\data\\track16_simplified.pickle')
    # 打印长度
    # print(len(track))
    # 提取前十条轨迹
    # track = track[:1741]

    # 转化为 GeoDataFrame
    track = convert_list_to_linestring(track)
    # 以图层的方式 绘制在地图上
    fig, ax = plt.subplots(figsize=(10, 10))
    shape.boundary.plot(ax=ax)
    track.plot(ax=ax, color='red')

    plt.show()

if __name__ == '__main__':
    tmp()









