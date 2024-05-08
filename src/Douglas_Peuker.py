from matplotlib import pyplot as plt
import numpy as np
from cluster import convert_list_to_linestring
from distance import manhattan
from preprocess import load_track, save_track
import tqdm

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
        # d = manhattan(line[i], line[0]) + manhattan(line[i], line[end])
        d = np.linalg.norm(np.cross(np.array(line[i]) - np.array(line[0]), np.array(line[0]) - np.array(line[end])))/np.linalg.norm(np.array(line[end]) - np.array(line[0]))
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

def process():
    # data\track16.pickle
    track = load_track('H:\\bike\\data\\track16.pickle')

    track = track[:1741]
    # 提取最长的 10 条轨迹
    # track = sorted(track, key=lambda x: len(x), reverse=True)[:20]
    n = 0.0015
    new_track = []
    for i in tqdm.tqdm(range(len(track))):
        new_track.append(douglas_peuker(track[i], n))
    # save_track(new_track, 'H:\\bike\\data\\track16_sim.pickle')

    new_track = convert_list_to_linestring(new_track)
    # 以图层的方式 绘制在地图上
    fig, ax = plt.subplots(figsize=(10, 10))
    new_track.plot(ax=ax, color='gray')
    plt.show()


def tmp():
    # test step line
    line = [[121.413, 31.359], [121.414, 31.359], [121.414, 31.36], [121.415, 31.36], [121.416, 31.36], [121.416, 31.361], [121.417, 31.361], [121.418, 31.361], [121.418, 31.362], [121.419, 31.362], [121.42, 31.362], [121.42, 31.363], [121.421, 31.363], [121.421, 31.362], [121.422, 31.362], [121.422, 31.361], [121.422, 31.36], [121.422, 31.359], [121.423, 31.359], [121.423, 31.358], [121.424, 31.358], [121.424, 31.359], [121.425, 31.359], [121.426, 31.359], [121.427, 31.359], [121.427, 31.36], [121.428, 31.36], [121.429, 31.36], [121.43, 31.36], [121.43, 31.361], [121.431, 31.361], [121.432, 31.361], [121.433, 31.361], [121.433, 31.36], [121.433, 31.359], [121.433, 31.358], [121.433, 31.357], [121.433, 31.356], [121.432, 31.356]]

    res = douglas_peuker(line, 0.0015)

    # # 两个子图 一列两行
    # fig, axs = plt.subplots(2, 1)
    # x, y = zip(*line)
    # axs[0].plot(x, y, 'r-')
    # x, y = zip(*res)
    # axs[1].plot(x, y, 'g-')
    # # label
    # axs[0].set_title('Original Line')
    # axs[1].set_title('Douglas-Peuker Simplification')
    # # Legend  阈值标注 
    # axs[0].legend(['Original Line'])
    # axs[1].legend(['Douglas-Peuker Simplification (epsilon=0.015)'])
    # # x, y label
    # axs[0].set_xlabel('Longitude')
    # axs[0].set_ylabel('Latitude')
    # axs[1].set_xlabel('Longitude')
    # axs[1].set_ylabel('Latitude')

    # # 设置 X 轴显示精度
    # axs[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '%.3f' % x))
    # axs[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '%.3f' % x))

    # 叠加在一张图上
    # plt.plot(line[:, 0], line[:, 1], 'o-', label='Original')
    # plt.plot(res[:, 0], res[:, 1], 'o-', label='Simplified')
    # plt.legend()

    # plot
    line = np.array(line)
    res = np.array(res)

    # plot
    plt.plot(line[:, 0], line[:, 1], 'o-', label='Original')
    plt.plot(res[:, 0], res[:, 1], 'o-', label='Simplified')

    # label
    plt.title('Douglas-Peuker Simplification (epsilon=0.0015)')
    # Legend
    plt.legend()
    # x, y label
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    # 设置 X 轴显示精度
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '%.3f' % x))
    # 设置 Y 轴显示精度
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '%.3f' % y))


    # layout
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    tmp()
    # process()