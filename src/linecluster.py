import numpy as np
from sklearn.cluster import OPTICS
import matplotlib.pyplot as plt
from preprocess import load_track

def custom_distance(l1, l2):
    # Euclidean distance between the start points of the lines
    return np.linalg.norm(l1[0] - l2[0])

def get_distance_matrix(lines):
    """
    Get the distance matrix for a list of lines
    :param lines: list
    :return: np.ndarray
    """
    n = len(lines)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = custom_distance(lines[i], lines[j])
    return dist_matrix

def optics_line_clustering(lines, min_cluster_size=3, eps=0.5):
    """
    Perform OPTICS clustering on a list of lines
    :param lines: list
    :param min_cluster_size: int
    :param eps: float
    :return: list
    """
    dist_matrix = get_distance_matrix(lines)
    clustering = OPTICS(min_samples=min_cluster_size, metric='precomputed', eps=eps).fit(dist_matrix)
    labels = clustering.labels_
    clusters = []
    for label in np.unique(labels):
        cluster = [lines[i] for i in range(len(lines)) if labels[i] == label]
        clusters.append(cluster)
    return clusters


lines = load_track('H:\\bike\\data\\track16_sim.pickle')
lines = lines[:10]
lines = [np.array(line) for line in lines]

clusters = optics_line_clustering(lines)

for i, cluster in enumerate(clusters):
    for line in cluster:
        plt.plot(line[:, 0], line[:, 1], label=f'Cluster {i}')
plt.legend()
plt.show()