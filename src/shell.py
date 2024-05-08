import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

def extract_skeleton(points):
    '''
    提取点集的骨架(首先求解凸包，然后找到凸包的最长向量，将所有点投影到该向量上，最大投影和最小投影即为骨架的起点和终点)
    '''
    # 使用ConvexHull求解凸包
    hull = ConvexHull(points)

    # 提取凸包顶点
    hull_points = points[hull.vertices]
    # 计算凸包的中心
    center = np.mean(hull_points, axis=0)
    # 计算凸包的中心到各个顶点的向量
    vectors = hull_points - center
    # 计算各个向量的模
    norms = np.linalg.norm(vectors, axis=1)
    # 找到最长的向量
    longest_vector = vectors[np.argmax(norms)]
    # 计算最长向量的单位向量
    longest_vector = longest_vector / np.linalg.norm(longest_vector)

    # 据此方向，将所有点投影到一维空间
    projections = np.dot(vectors, longest_vector)
    # 找到最大投影和最小投影
    min_projection = np.min(projections)
    max_projection = np.max(projections)
    # 将其作为中心线的起点和终点
    start_point = center + min_projection * longest_vector
    end_point = center + max_projection * longest_vector
    return [start_point, end_point], hull_points

if __name__ == '__main__':
    # 模拟生成一些点 呈条状分布
    np.random.seed(0)
    data = np.random.rand(100, 2)
    data[:, 1] = data[:, 1] * 0.1 + data[:, 0] * 0.8


    # 提取轴线
    centerline,hull_points = extract_skeleton(data)

    # 绘制结果
    plt.figure(figsize=(6, 6))
    plt.plot(data[:, 0], data[:, 1], 'o', label='Points')
    plt.plot(hull_points[:, 0], hull_points[:, 1], 'r--', lw=2, label='Convex Hull')
    plt.plot(np.array(centerline)[:, 0], np.array(centerline)[:, 1], 'g-', lw=2, label='Centerline')
    plt.legend()
    plt.show()
