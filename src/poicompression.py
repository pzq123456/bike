import numpy as np
from sklearn.cluster import KMeans

def interest_point_clustering(data, k):
    """
    基于兴趣点的空间点数据集抽稀

    参数：
        data: 输入数据，形状为 (n, p)，其中 n 是数据点的数量，p 是特征的维度。
        k: 每个子数据集的簇数量。

    返回：
        抽稀后的数据，形状为 (m, p)。
    """
    # 数据预处理

    # 类别划分
    categories = np.unique(data[:, -1])
    clustered_data = []

    for category in categories:
        # 分层聚类
        category_data = data[data[:, -1] == category]
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(category_data[:, :-1])
        cluster_centers = kmeans.cluster_centers_
        cluster_labels = kmeans.labels_

        # 将每个簇的重心作为代表点
        clustered_data.append(np.hstack([cluster_centers, category_data[:, -1].reshape(-1, 1)]))

    # 合并结果
    clustered_data = np.vstack(clustered_data)
    return clustered_data

# 示例用法
data = np.array([
    [1, 2, 1],
    [3, 4, 1],
    [5, 6, 2],
    [7, 8, 2],
    [9, 10, 1],
])
k = 2
clustered_data = interest_point_clustering(data, k)
print(clustered_data)

import numpy as np
from sklearn.neighbors import KernelDensity

def density_based_center_selection(data, k):
    """
    基于密度选择K均值聚类初始聚类重心

    参数：
        data: 输入数据，形状为 (n, p)，其中 n 是数据点的数量，p 是特征的维度。
        k: 簇数量。

    返回：
        初始聚类重心，形状为 (k, p)。
    """
    # 计算数据点的密度
    kde = KernelDensity(kernel='gaussian', bandwidth=0.5)
    kde.fit(data)
    densities = kde.evaluate(data)

    # 划分密度等级
    density_levels = np.unique(densities)
    num_centers_per_level = np.ceil(k * densities / np.sum(densities))

    # 按密度等级选择初始聚类重心
    centers = []
    for i, density_level in enumerate(density_levels):
        data_level = data[densities == density_level]
        num_centers = num_centers_per_level[i]
        centers_level = np.random.choice(data_level, num_centers, replace=False)
        centers.append(centers_level)

    # 合并结果
    centers = np.vstack(centers)
    return centers

# 示例用法
data = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
    [1, 3],
    [2, 4],
    [3, 5],
    [4, 6],
    [5, 7],
])
k = 4
centers = density_based_center_selection(data, k)
print(centers)
