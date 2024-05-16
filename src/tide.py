import numpy as np
from osgeo import gdal, osr
import matplotlib.pyplot as plt
import pandas as pd
import tqdm
from shapely import geometry
# kmeans
from sklearn.cluster import KMeans
import geopandas as gpd

EXTENT = [121.297, 121.629, 31.077, 31.416]
# 121.2969999999999970,31.0770000000000017
# 121.6290000000000049,31.4160000000000004

# bike16.csv
# ID,BID,UID,ST,SX,SY,ET,EX,EY,EC,DS,DU
# 1,79699,759,2016/8/1 0:23,121.52,31.309,2016/8/1 0:32,121.525,31.316,3,867.65,9
# 2,33279,1440,2016/8/1 0:25,121.505,31.294,2016/8/1 0:40,121.517,31.309,6,2967.41,15
def read_data(filename):
    df = pd.read_csv(filename)
    # only keep the columns we need: SX, SY, EX, EY, ST, ET
    df = df[['SX', 'SY', 'EX', 'EY', 'ST', 'ET']]
    # convert ST and ET to datetime objects
    df['ST'] = pd.to_datetime(df['ST'])
    df['ET'] = pd.to_datetime(df['ET'])
    return df

def init_grid(extent, size, time_windows):
    # time_windows = [[7, 10], [17, 20]]
    # make mutiple grids for each time window
    grid = np.zeros((len(time_windows), int((extent[3] - extent[2]) / size), int((extent[1] - extent[0]) / size), 2), dtype=np.int32)
    return grid

# test if the grid is initialized correctly
def test_init_grid():
    grid = init_grid(EXTENT, 0.001, [[7, 10], [17, 20]])
    print(grid.shape)
    print(grid[0].shape)
    print(grid[0][0].shape)
    print(grid[0][0][0].shape)

def get_grid_index(lat, lon, extent, size):
    lat_index = int((lat - extent[2]) / size)
    lon_index = int((lon - extent[0]) / size)
    return lat_index, lon_index

def get_time_index(timestamp, time_windows):
    hour = timestamp.hour
    for i, window in enumerate(time_windows):
        if window[0] <= hour < window[1]:
            return i
    return None

def update_grid(data, grid, extent, size, time_windows):
    borrow_grid = np.zeros((grid.shape[0], grid.shape[1], grid.shape[2], 2), dtype=np.int32)
    return_grid = np.zeros((grid.shape[0], grid.shape[1], grid.shape[2], 2), dtype=np.int32)
    for i in tqdm.tqdm(range(data.shape[0])):
        borrow_lat, borrow_lon = data.iloc[i]['SY'], data.iloc[i]['SX']
        return_lat, return_lon = data.iloc[i]['EY'], data.iloc[i]['EX']
        borrow_time_index = get_time_index(data.iloc[i]['ST'], time_windows)
        return_time_index = get_time_index(data.iloc[i]['ET'], time_windows)
        if borrow_time_index is not None:
            borrow_lat_index, borrow_lon_index = get_grid_index(borrow_lat, borrow_lon, extent, size)
            borrow_grid[borrow_time_index, borrow_lat_index, borrow_lon_index, 0] += 1
        if return_time_index is not None:
            return_lat_index, return_lon_index = get_grid_index(return_lat, return_lon, extent, size)
            return_grid[return_time_index, return_lat_index, return_lon_index, 1] += 1
    return borrow_grid, return_grid
    

def calculate_tidal_index(borrow_grid, return_grid):
    # 计算方法：借车次数 - 还车次数 / 借车次数 + 还车次数
    tidal_index = np.zeros((borrow_grid.shape[0], borrow_grid.shape[1], borrow_grid.shape[2]), dtype=np.float32)
    for i in range(borrow_grid.shape[0]):
        for j in range(borrow_grid.shape[1]):
            for k in range(borrow_grid.shape[2]):
                borrow = borrow_grid[i, j, k, 0]
                return_ = return_grid[i, j, k, 1]
                if borrow + return_ == 0:
                    tidal_index[i, j, k] = 0
                else:
                    tidal_index[i, j, k] = (borrow - return_) / (borrow + return_)
    return tidal_index

def save_tiff(data, filename, extent, size):
    # debug：首先需要将逆序排列行 GeoTIFF 用的是屏幕坐标系，所以需要将数据逆序排列
    data = np.flipud(data)
    driver = gdal.GetDriverByName('GTiff')
    rows, cols = data.shape
    dataset = driver.Create(filename, cols, rows, 1, gdal.GDT_Float32)
    dataset.SetGeoTransform((extent[0], size, 0, extent[3], 0, -size))
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    dataset.SetProjection(srs.ExportToWkt())
    dataset.GetRasterBand(1).WriteArray(data)
    dataset.FlushCache()

# 提取结果数据中不为0的数据为点集数据 并保存为shp文件
def save_shp(data, extent, size,path):
    # 同时需要保存经纬度信息 和 值信息 选择栅格中点作为经纬度信息
    # 保存为点集数据
    rows, cols = data.shape
    points = []
    values = []
    for i in tqdm.tqdm(range(rows)):
        for j in range(cols):
            if data[i,j] != 0:
                lat = extent[2] + i * size
                lon = extent[0] + j * size
                points.append([lon, lat])
                values.append(data[i,j])
    gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([p[0] for p in points], [p[1] for p in points]))
    # 设置坐标系 
    gdf.crs = 'EPSG:4326'
    gdf['value'] = values
    gdf.to_file(path)

# 将边界转化为 shp文件

def save_boundary(extent, path):
    # 保存为shp文件
    # 构造边界多边形
    # 构造为一个矩形

    boundary = geometry.Polygon([[extent[0], extent[2]], [extent[1], extent[2]], [extent[1], extent[3]], [extent[0], extent[3]]])
    # 转化为geopandas的数据格式
    boundary = gpd.GeoDataFrame(geometry=[boundary])
    boundary.crs = 'EPSG:4326'
    boundary.to_file(path)

def test():
# EXTENT = [121.297, 121.629, 31.077, 31.416] 

    pointLT = [121.296, 31.415]
    valueLT = 1
    pointRB = [121.627, 31.077]
    valueRB = -1

    pointlist = [pointLT, pointRB]
    valuelist = [valueLT, valueRB]

    # 生成栅格数据
    grid = init_grid(EXTENT, 0.001, [[7, 10]])
    # 计算栅格索引 将测试点放入栅格中
    for i in range(len(pointlist)):
        lat_index, lon_index = get_grid_index(pointlist[i][1], pointlist[i][0], EXTENT, 0.001)
        print('lat_index', lat_index)
        print('lon_index', lon_index)
        grid[0, lat_index, lon_index, 0] = valuelist[i]

    # 保存为 tiff
    save_tiff(grid[0,:,:,0], 'H:\\bike\qgis\TEST.tiff', EXTENT, 0.001)



if __name__ == "__main__":
    test()

    # filename = 'data/bike16.csv'
    # data = read_data(filename)
    # # 只取前100条数据
    # data = data.head(1741)

    # grid = init_grid(EXTENT, 0.001, [[7, 10], [17, 20]])
    # borrow_grid, return_grid = update_grid(data, grid, EXTENT, 0.001, [[7, 10], [17, 20]])
    # tidal_index = calculate_tidal_index(borrow_grid, return_grid)
    # # save shp
    # save_shp(tidal_index[0], EXTENT, 0.001, 'H:\\bike\qgis\潮汐数据\morning20.shp')
    # save_shp(tidal_index[1], EXTENT, 0.001, 'H:\\bike\qgis\潮汐数据\evening20.shp')

    # # save H:\bike\qgis
    # save_tiff(tidal_index[0], 'H:\\bike\qgis\morning20.tiff', EXTENT, 0.001)
    # save_tiff(tidal_index[1], 'H:\\bike\qgis\evening20.tiff', EXTENT, 0.001)
    # print('done')
