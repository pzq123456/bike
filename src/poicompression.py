import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import tqdm
import pickle

def dbscan(data, eps, min_samples):
    # 根据 类别划分数据
    class_data = {}
    for i in range(len(data)):
        if data[i][-1] not in class_data:
            class_data[data[i][-1]] = []
        class_data[data[i][-1]].append(data[i])
    # 聚类
    labels = np.zeros(len(data))
    for key in tqdm.tqdm(class_data.keys()):
        class_data[key] = np.array(class_data[key])
        db = DBSCAN(eps=eps, min_samples=min_samples).fit(class_data[key][:, :-1])
        labels[class_data[key][:, -1].astype(int)] = db.labels_
    return labels

# def center_point(data, labels):
#     # 计算聚类中心 并将保留类别标签
#     center_points = []
#     for i in range(len(np.unique(labels))):
#         class_data = data[labels == i]
#         center_point = np.mean(class_data, axis=0)
#         center_points.append(center_point)
#     center_points = np.array(center_points)
#     return center_points

# def poi_compression(data, eps, min_samples):
#     """
#     对POI数据进行压缩
#     :param data: POI数据
#     :param eps: DBSCAN算法参数
#     :param min_samples: DBSCAN算法参数
#     :return: 压缩后的POI数据
#     """
#     labels = dbscan(data, eps, min_samples)
#     center_points = center_point(data, labels)
#     return center_points

# if __name__ == "__main__":

#     data = pd.read_csv("H:/bike/poi18_code.csv")
#     data = np.array(data)
#     # 只取前1000个数据
#     data = data[:1000]

#     eps = 0.01    
#     min_samples = 5
#     center_points = poi_compression(data, eps, min_samples)
#     print(center_points)
