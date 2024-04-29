import numpy as np
from distance import haversine
import pickle
import tqdm


class Node:
    def __init__(self, data, dimension=None, parent=None):
        self.data = data
        self.dimension = dimension
        self.left = None
        self.right = None
        self.parent = parent

    def __str__(self):
        return str(self.data)


def distance(a, b):
    # haversine(a,b)
    return haversine(a,b)
    # This function calculates the Euclidean distance between two points.
    # You can replace this function with your custom distance metric.
    # dis = 0
    # for i in range(len(a)):
    #     dis += (a[i] - b[i]) ** 2
    # return np.sqrt(dis)


def construct(data, node, dimension=0):
    if len(data) == 0:
        return None

    if len(data) == 1:
        node.data = data[0]
        node.dimension = dimension
        return node

    # Select the median value of the current dimension as the pivot
    median_index = np.median(data, axis=0)[dimension]

    # Partition the data into two subsets based on the pivot
    left_data = [point for point in data if point[dimension] <= median_index]
    right_data = [point for point in data if point[dimension] > median_index]

    # Construct the left and right subtrees
    node.left = construct(left_data, node=Node(None, dimension=(dimension + 1) % len(data[0])), dimension=(dimension + 1) % len(data[0]))
    node.right = construct(right_data, node=Node(None, dimension=(dimension + 1) % len(data[0])), dimension=(dimension + 1) % len(data[0]))

    # Set the node's data and dimension
    node.data = data[np.argmax(data, axis=0)[dimension]]
    node.dimension = dimension

    return node


def nearest_neighbors(root, query_point, k=1, distance=distance):
    # Initialize the nearest neighbors
    nearest_neighbors = []

    # Define a function to recursively search for the nearest neighbors
    def search(node):
        if node is None:
            return

        # Calculate the distance between the query point and the current node
        d = distance(query_point, node.data)

        # If the current node is closer to the query point than the farthest nearest neighbor,
        # update the nearest neighbors
        if len(nearest_neighbors) < k:
            nearest_neighbors.append((node, d))
            nearest_neighbors.sort(key=lambda x: x[1], reverse=True)
        elif d < nearest_neighbors[0][1]:
            nearest_neighbors[0] = (node, d)
            nearest_neighbors.sort(key=lambda x: x[1], reverse=True)

        # Choose the next branch to visit
        next_branch = None
        opposite_branch = None
        if query_point[node.dimension] < node.data[node.dimension]:
            next_branch = node.left
            opposite_branch = node.right
        else:
            next_branch = node.right
            opposite_branch = node.left

        # Recursively search the next branch
        search(next_branch)

        # If the hypersphere crosses the splitting plane, there may be nearest neighbors on the opposite side
        if len(nearest_neighbors) < k or abs(query_point[node.dimension] - node.data[node.dimension]) < nearest_neighbors[0][1]:
            search(opposite_branch)

    # Start the recursive search
    search(root)

    # Return the k nearest neighbors
    nearest_neighbors = [x[0].data for x in nearest_neighbors]

    return nearest_neighbors


if __name__ == "__main__":
    # Generate some sample data
    data = [[20, 30], [20, 20], [9, 6], [4, 7], [8, 1], [7, 2], [6, 3]]
    point = [2, 3]

    # 打印距离
    for d in data:
        print("point:",d,"distance:",distance(d,point))

    # Construct the kd-tree
    root = construct(data, node=Node(None))

    # Query for the nearest neighbors of a point
    query_point = np.array(point)
    nearest_neighbors = nearest_neighbors(root, query_point, k=1)

    print("Query Point:", query_point)
    print("Nearest Neighbors:", nearest_neighbors)
