from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import cv2

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

def boolean2int(data):
    data = data.astype(np.uint8)
    return data


def intersection(raster1, raster2):
    data1, geotransform, projection = read_single_band_image(raster1)
    data2, geotransform, projection = read_single_band_image(raster2)
    # 默认进行二值化处理
    data1[data1 != 0] = 1
    data2[data2 != 0] = 1
    # 计算两个栅格数据的交集
    intersection = np.logical_and(data1, data2)
    # 返回包含了交集的栅格数据
    intersection = boolean2int(intersection)
    return intersection

# 计算道路对通勤轨迹的覆盖率
def coverage(raster1, raster2):
    '''
    raster1: 通勤轨迹栅格数据
    raster2: 道路栅格数据
    '''
    data1, geotransform, projection = read_single_band_image(raster1)
    data2, geotransform, projection = read_single_band_image(raster2)
    # 二值化
    data1[data1 != 0] = 1
    data2[data2 != 0] = 1
    # 计算两个栅格数据的交集
    intersection = np.logical_and(data1, data2)
    # 计算道路对通勤轨迹的覆盖率
    coverage = np.sum(intersection) / np.sum(data1)
    return coverage

def coverage_(data1, data2):
    # 二值化
    data1[data1 != 0] = 1
    data2[data2 != 0] = 1
    # 计算两个栅格数据的交集
    intersection = np.logical_and(data1, data2)
    # 计算道路对通勤轨迹的覆盖率
    coverage = np.sum(intersection) / np.sum(data1)
    return coverage


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
def binaryzation(data):
    data[data != 0] = 1
    return data

custom_kernel = np.array([
    [0, 1, 0], 
    [1, 1, 1],
    [0, 1, 0]], np.uint8)

# 腐蚀操作
def erode(data, kernel=custom_kernel):
    data = cv2.erode(data, kernel, iterations=1)
    return data
# 膨胀操作
def dilate(data, kernel=custom_kernel):
    data = cv2.dilate(data, kernel, iterations=1)
    return data

# 开运算
def open(data, kernel=custom_kernel):
    data = cv2.morphologyEx(data, cv2.MORPH_OPEN, kernel)
    return data

# 闭运算
def close(data, kernel=custom_kernel):
    data = cv2.morphologyEx(data, cv2.MORPH_CLOSE, kernel)
    return data

# 顶帽运算
def tophat(data, kernel=custom_kernel):
    data = cv2.morphologyEx(data, cv2.MORPH_TOPHAT, kernel)
    return data

# 黑帽运算
def blackhat(data, kernel=custom_kernel):
    data = cv2.morphologyEx(data, cv2.MORPH_BLACKHAT, kernel)
    return data

# 梯度运算
def gradient(data):
    kernel = np.ones((3, 3), np.uint8)
    data = cv2.morphologyEx(data, cv2.MORPH_GRADIENT, kernel)
    return data

# 去除点状噪声
def remove_noise(data, size=3):
    data = cv2.medianBlur(data, size) 
    return data

def helper(data, mykernel):
    data = close(data)
    data = erode(data, mykernel)
    return data

def save_single_band_image(image_path, data, geotransform, projection):
    # 创建一个 driver
    driver = gdal.GetDriverByName('GTiff')
    # 创建一个输出影像
    dataset = driver.Create(image_path, data.shape[1], data.shape[0], 1, gdal.GDT_Float32)
    # 设置仿射变换参数
    dataset.SetGeoTransform(geotransform)
    # 设置投影信息
    dataset.SetProjection(projection)
    # 写入数据
    dataset.GetRasterBand(1).WriteArray(data)
    # 释放资源
    dataset = None

# 绘制轨迹数据 需要绘制颜色条带 并对数据作夸张处理
def draw_track():
    data, geotransform, projection = read_single_band_image('H:\\bike\qgis\轨迹.tif')
    # 设置拉伸函数
    data = np.power(data, 0.5)
    # 获取数据的最大值和最小值
    min_value = np.min(data)
    max_value = np.max(data)
    # 设置数据的最大值和最小值
    vmin = min_value
    vmax = max_value
    # 根据最大值最小值划分 3 个层级 并提取每一个层级的数据 空位 0
    data1 = np.where(data < (max_value - min_value) / 3, data, 0)
    data2 = np.where(np.logical_and(data >= (max_value - min_value) / 3, data < 2 * (max_value - min_value) / 3), data, 0)
    data3 = np.where(data >= 2 * (max_value - min_value) / 3, data, 0)

    # 绘制轨迹数据
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    # 绘制第一个层级的数据
    ax = axs[0]
    # 对 data1 做腐蚀
    data1 = close(data1)
    im = ax.imshow(data1, cmap='hot', vmin=vmin, vmax=vmax)
    ax.set_title('{:.2f} < desity < {:.2f}'.format(min_value, (max_value - min_value) / 3))
    ax.axis('off')
    # 绘制第二个层级的数据
    ax = axs[1]
    im = ax.imshow(data2, cmap='hot', vmin=vmin, vmax=vmax)
    ax.set_title('{:.2f} < desity < {:.2f}'.format((max_value - min_value) / 3, 2 * (max_value - min_value) / 3))
    ax.axis('off')
    # 绘制第三个层级的数据
    ax = axs[2]
    # 对data3 做膨胀操作
    data3 = dilate(data3)
    data3 = remove_noise(data3)
    # 对data3 做开运算
    data3 = open(data3)
    # 对data3 做闭运算
    data3 = close(data3)
    # 保存三个层级的数据为 tif 文件 同样的投影和仿射变换参数
    save_single_band_image('H:\\bike\qgis\轨迹1.tif', data1, geotransform, projection)
    save_single_band_image('H:\\bike\qgis\轨迹2.tif', data2, geotransform, projection)
    save_single_band_image('H:\\bike\qgis\轨迹3.tif', data3, geotransform, projection)
    im = ax.imshow(data3, cmap='hot', vmin=vmin, vmax=vmax)
    ax.set_title('{:.2f} < desity < {:.2f}'.format(2 * (max_value - min_value) / 3, max_value))
    ax.axis('off')
    # 添加颜色条带
    fig.colorbar(im, ax=axs.ravel().tolist(), shrink=0.6)
    plt.show()

def coverage():
 # draw_track()
    image_paths = ['H:\\bike\qgis\轨迹.tif', 'H:\\bike\qgis\主路.tif', 'H:\\bike\qgis\次主路.tif', 'H:\\bike\qgis\支路.tif']
    names = ['track ∩ primary_road', 'track ∩ secondary_road', 'track ∩ tertiary_road']

    mykernel = np.array([
        [0,1],
        [0,1]
    ], np.uint8)

    intersection_data = []

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    for i in range(3):
        diff_data = intersection(image_paths[0], image_paths[i + 1])

        # 闭运算
        diff_data = erode(diff_data, mykernel)

        diff_data = dilate(diff_data, mykernel)
        diff_data = dilate(diff_data, mykernel)
        diff_data = close(diff_data, mykernel)
        # 去除噪声


        intersection_data.append(diff_data)

    # 计算轨迹与主路、次主路、支路的覆盖率
    # coverages = [coverage(image_paths[0], image_paths[i + 1]) for i in range(3)]
    coverages = [coverage_(binaryzation(read_single_band_image(image_paths[0])[0])
                           , helper(binaryzation(read_single_band_image(image_paths[i + 1])[0]), mykernel)) for i in range(3)]

    # 向 name 中添加覆盖率
    for i in range(3):
        names[i] += ' ' + "{:.2%}".format(coverages[i]) + " coverage"

    # 为每个子图设置标题
    for i in range(3):
        ax = axs[i]
        ax.imshow(intersection_data[i], cmap='gray')
        ax.set_title(names[i])
        ax.axis('off')

    plt.show()


def jaccard(data1,data2):
    # read data
    data1, geotransform, projection = read_single_band_image(data1)
    data2, geotransform, projection = read_single_band_image(data2)
    data1 = binaryzation(data1)
    data2 = binaryzation(data2)
    intersection = np.logical_and(data1, data2)
    union = np.logical_or(data1, data2)
    jaccard = np.sum(intersection) / np.sum(union)
    return jaccard

def jaccard_(data1, data2):
    data1 = binaryzation(data1)
    data2 = binaryzation(data2)
    intersection = np.logical_and(data1, data2)
    union = np.logical_or(data1, data2)
    jaccard = np.sum(intersection) / np.sum(union)
    return jaccard

def jaccard_main():
    image_paths = ['H:\\bike\qgis\轨迹.tif', 'H:\\bike\qgis\主路.tif', 'H:\\bike\qgis\次主路.tif', 'H:\\bike\qgis\支路.tif']
    jaccards = []
    for i in range(3):
        jaccard_ = jaccard(image_paths[0], image_paths[i + 1])
        jaccards.append(jaccard_)
    print(jaccards)

def length(data):
    # 读取数据
    data, geotransform, projection = read_single_band_image(data)
    # 二值化
    data = binaryzation(data)
    # 计算长度
    length = np.sum(data)
    return length

def length_(data):
    # 二值化
    data = binaryzation(data)
    # 计算长度
    length = np.sum(data)
    return length




if __name__ == '__main__':
    # 计算轨迹与各级别道路的length
    image_paths = ['H:\\bike\qgis\轨迹.tif', 'H:\\bike\qgis\主路.tif', 'H:\\bike\qgis\次主路.tif', 'H:\\bike\qgis\支路.tif']
    lengths = []
    # 首先腐各级别道路数据
    mykernel = np.array([
        [0,1],
        [0,1]
    ], np.uint8)
    for i in range(3):
        mylength= length_(helper(binaryzation(read_single_band_image(image_paths[i + 1])[0]), mykernel))
        lengths.append(mylength)
    print(lengths)



   

# pip --proxy 127.0.0.1:7890 install --upgrade opencv-python