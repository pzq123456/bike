from matplotlib import pyplot as plt
from distance import manhattan

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

res = douglas_peuker(line, 0.015)

# 两个子图 一列两行
fig, axs = plt.subplots(2, 1)
x, y = zip(*line)
axs[0].plot(x, y, 'r-')
x, y = zip(*res)
axs[1].plot(x, y, 'g-')
# label
axs[0].set_title('Original Line')
axs[1].set_title('Douglas-Peuker Simplification')
# Legend  阈值标注 
axs[0].legend(['Original Line'])
axs[1].legend(['Douglas-Peuker Simplification (epsilon=0.015)'])
# x, y label
axs[0].set_xlabel('Longitude')
axs[0].set_ylabel('Latitude')
axs[1].set_xlabel('Longitude')
axs[1].set_ylabel('Latitude')

# 设置 X 轴显示精度
axs[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '%.3f' % x))
axs[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '%.3f' % x))

# layout
plt.tight_layout()
plt.show()

