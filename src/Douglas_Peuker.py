from matplotlib import pyplot as plt
from typing import List
def manhattan(p1: List[float], p2: List[float]) -> float:
    return sum([abs(p1[i]-p2[i]) for i in range(len(p1))])

def douglas_peuker(line, n):
    """
    Douglas-Peuker algorithm
    :param line: List[List[float]]
    :param n: float
    :return: List[List[float]]
    """
    if len(line) <= 2:
        return line
    # Find the point with the maximum distance
    dmax = 0
    index = 0
    end = len(line) - 1
    for i in range(1, end):
        d = manhattan(line[i], line[0]) + manhattan(line[i], line[end])
        if d > dmax:
            index = i
            dmax = d
    # If the maximum distance is greater than epsilon, recursively simplify
    res = []
    if dmax > n:
        # Recursive simplification
        res1 = douglas_peuker(line[:index + 1], n)
        res2 = douglas_peuker(line[index:], n)
        res = res1[:-1] + res2
    else:
        res = [line[0], line[-1]]
    return res

# test step line
line = [[121.413, 31.359], [121.414, 31.359], [121.414, 31.36], [121.415, 31.36], [121.416, 31.36], [121.416, 31.361], [121.417, 31.361], [121.418, 31.361], [121.418, 31.362], [121.419, 31.362], [121.42, 31.362], [121.42, 31.363], [121.421, 31.363], [121.421, 31.362], [121.422, 31.362], [121.422, 31.361], [121.422, 31.36], [121.422, 31.359], [121.423, 31.359], [121.423, 31.358], [121.424, 31.358], [121.424, 31.359], [121.425, 31.359], [121.426, 31.359], [121.427, 31.359], [121.427, 31.36], [121.428, 31.36], [121.429, 31.36], [121.43, 31.36], [121.43, 31.361], [121.431, 31.361], [121.432, 31.361], [121.433, 31.361], [121.433, 31.36], [121.433, 31.359], [121.433, 31.358], [121.433, 31.357], [121.433, 31.356], [121.432, 31.356]]

res = douglas_peuker(line, 0.01)
# plot in different color
x, y = zip(*line)
plt.plot(x, y, 'r-')
x, y = zip(*res)
plt.plot(x, y, 'g-')
plt.show()
