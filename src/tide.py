import numpy as np
from osgeo import gdal, osr
import datetime

# 定义空间范围和格网大小
min_lon, max_lon = 116.0, 117.0
min_lat, max_lat = 39.0, 40.0
grid_size = 0.001

# 计算格网行列数
lat_grid_count = int((max_lat - min_lat) / grid_size)
lon_grid_count = int((max_lon - min_lon) / grid_size)

# 初始化借车和还车计数栅格
borrow_grid = np.zeros((lat_grid_count, lon_grid_count, 2), dtype=np.int32)
return_grid = np.zeros((lat_grid_count, lon_grid_count, 2), dtype=np.int32)

# 示例数据记录
data = [
    {'SX': 116.1, 'SY': 39.1, 'start_time': datetime.datetime(2024, 5, 15, 8, 30),
     'EX': 116.2, 'EY': 39.2, 'end_time': datetime.datetime(2024, 5, 15, 9, 0)},
    # 添加更多数据
]

# 计算网格索引函数
def get_grid_index(lat, lon, min_lat, min_lon, grid_size):
    lat_index = int((lat - min_lat) / grid_size)
    lon_index = int((lon - min_lon) / grid_size)
    return lat_index, lon_index

# 计算时间索引函数
def get_time_index(timestamp):
    hour = timestamp.hour
    if 7 <= hour < 10:
        return 0  # 早高峰
    elif 17 <= hour < 20:
        return 1  # 晚高峰
    return None  # 非高峰期

# 遍历轨迹数据，更新借车和还车计数
for record in data:
    borrow_time_index = get_time_index(record['start_time'])
    return_time_index = get_time_index(record['end_time'])
    if borrow_time_index is not None:
        lat_index, lon_index = get_grid_index(record['SY'], record['SX'], min_lat, min_lon, grid_size)
        borrow_grid[lat_index][lon_index][borrow_time_index] += 1
    if return_time_index is not None:
        lat_index, lon_index = get_grid_index(record['EY'], record['EX'], min_lat, min_lon, grid_size)
        return_grid[lat_index][lon_index][return_time_index] += 1

# 计算潮汐指数栅格
tidal_index_grid = np.zeros_like(borrow_grid, dtype=np.float32)

for i in range(lat_grid_count):
    for j in range(lon_grid_count):
        for k in range(2):  # 0: 早高峰, 1: 晚高峰
            borrow_count = borrow_grid[i][j][k]
            return_count = return_grid[i][j][k]
            if borrow_count + return_count > 0:
                tidal_index = (borrow_count - return_count) / (borrow_count + return_count)
                tidal_index_grid[i][j][k] = tidal_index

# GDAL创建TIFF文件函数
def save_tiff(data, filename, min_lon, min_lat, grid_size):
    driver = gdal.GetDriverByName('GTiff')
    rows, cols = data.shape
    dataset = driver.Create(filename, cols, rows, 1, gdal.GDT_Float32)
    
    # 设置地理变换参数（左上角坐标和分辨率）
    geotransform = (min_lon, grid_size, 0, max_lat, 0, -grid_size)
    dataset.SetGeoTransform(geotransform)
    
    # 设置投影信息（WGS84坐标系）
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    dataset.SetProjection(srs.ExportToWkt())
    
    # 写入数据
    dataset.GetRasterBand(1).WriteArray(data)
    dataset.FlushCache()

# 保存潮汐指数栅格为TIFF文件
save_tiff(tidal_index_grid[:, :, 0], 'morning_peak_tidal_index.tiff', min_lon, min_lat, grid_size)
save_tiff(tidal_index_grid[:, :, 1], 'evening_peak_tidal_index.tiff', min_lon, min_lat, grid_size)

print("TIFF文件已生成")
