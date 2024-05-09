from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

# 读取单波段影像
def read_single_band_image(image_path):
    # 读取影像
    dataset = gdal.Open(image_path)
    # 获取影像的宽和高
    width = dataset.RasterXSize
    height = dataset.RasterYSize
    # 获取影像的波段数
    band_count = dataset.RasterCount
    # 获取影像的仿射变换参数
    geotransform = dataset.GetGeoTransform()
    # 获取影像的投影信息
    projection = dataset.GetProjection()
    # 读取影像的第一个波段
    band = dataset.GetRasterBand(1)
    # 读取第一个波段的数据
    data = band.ReadAsArray(0, 0, width, height)
    # 释放资源
    dataset = None
    return data, geotransform, projection

def draw():
    image_paths = ['H:\\bike\qgis\轨迹.tif', 'H:\\bike\qgis\主路.tif', 'H:\\bike\qgis\次主路.tif', 'H:\\bike\qgis\支路.tif']
    # names = ['轨迹', '主路']
    names = ['track', 'primary_road', 'secondary_road', 'tertiary_road']

    datas = []

    for i in range(len(image_paths)):
        data, geotransform, projection = read_single_band_image(image_paths[i])
        datas.append(data)

    # 多子图显示 根据 path 的数量 分两行显示 紧凑显示
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    # 为每个子图设置标题
    for i in range(len(datas)):
        ax = axs[int(i / 2), i % 2]
        ax.imshow(datas[i], cmap='hot')
        ax.set_title(names[i])
        ax.axis('off')
    plt.show()

def diff(raster1, raster2):
    data1, geotransform, projection = read_single_band_image(raster1)
    data2, geotransform, projection = read_single_band_image(raster2)
    # 默认进行二值化处理
    data1[data1 != 0] = 1
    data2[data2 != 0] = 1
    # 计算两个栅格数据的差异
    diff = data1 - data2
    diff[diff != 0] = 1
    # 返回包含了差异的栅格数据
    return diff

def intersection(raster1, raster2):
    data1, geotransform, projection = read_single_band_image(raster1)
    data2, geotransform, projection = read_single_band_image(raster2)
    # 默认进行二值化处理
    data1[data1 != 0] = 1
    data2[data2 != 0] = 1
    # 计算两个栅格数据的交集
    intersection = np.logical_and(data1, data2)
    return intersection

# IoU 计算
def iou(raster1, raster2):
    data1, geotransform, projection = read_single_band_image(raster1)
    data2, geotransform, projection = read_single_band_image(raster2)
    # 计算两个栅格数据的交集
    intersection = np.logical_and(data1, data2)
    # 计算两个栅格数据的并集
    union = np.logical_or(data1, data2)
    # 计算 IoU
    iou = np.sum(intersection) / np.sum(union)
    return iou

# 二值化 默认将所有非零值设置为 1
def binaryzation(raster):
    data, geotransform, projection = read_single_band_image(raster)
    data[data != 0] = 1
    return data

if __name__ == '__main__':
    image_paths = ['H:\\bike\qgis\轨迹.tif', 'H:\\bike\qgis\主路.tif', 'H:\\bike\qgis\次主路.tif', 'H:\\bike\qgis\支路.tif']
    names = ['track ∩ primary_road', 'track ∩ secondary_road', 'track ∩ tertiary_road']
    # 计算轨迹与主路、次主路、支路的 IoU
    IoU = []
    for i in range(3):
        iou_value = iou(image_paths[0], image_paths[i + 1])
        IoU.append(iou_value)
    # 计算轨迹与主路、次主路、支路的差异 子图显示 标注 IoU
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    for i in range(3):
        diff_data = intersection(image_paths[0], image_paths[i + 1])
        ax = axs[i]
        ax.imshow(diff_data, cmap='hot')
        ax.set_title(names[i])
        ax.axis('off')
        # legend show IoU
        ax.text(0, 0, 'IoU: %.2f' % IoU[i], color='white', fontsize=10)

    # add bar of the color
    plt.show()


    
        