from distance import manhattan,haversine,encode,decode,geohash_approximate_distance

# 生成轨迹点
trajectory_points = [
    [121.412,31.359],
    [121.413,31.359],
    [121.414,31.359],
    [121.414,31.360],
    [121.415,31.360],
    [121.416,31.360],
    [121.416,31.361],
    [121.417,31.361],
    [121.418,31.361],
    [121.418,31.362],
    [121.419,31.362],
    [121.420,31.362],
    [121.420,31.363],
    [121.421,31.362],
    [121.421,31.363],
    [121.422,31.359],
    [121.422,31.360],
    [121.422,31.361],
    [121.422,31.362],
    [121.423,31.358],
    [121.423,31.359],
    [121.424,31.358],
    [121.424,31.359],
    [121.425,31.359],
    [121.426,31.359],
    [121.427,31.359],
    [121.427,31.360],
    [121.428,31.360],
    [121.429,31.360],
    [121.430,31.360],
    [121.430,31.361],
    [121.431,31.361],
    [121.432,31.356],
    [121.432,31.361],
    [121.433,31.356],
    [121.433,31.357],
    [121.433,31.358],
    [121.433,31.359],
    [121.433,31.360],
    [121.433,31.361]
]


start_point =  [121.413,31.358]
end_point = [121.432,31.356]

# 将起点和终点加入轨迹点
trajectory_points.append(start_point)
trajectory_points.append(end_point)

# geoHash set
trajectory_points = set([encode(t[1],t[0]) for t in trajectory_points])

trajectory = []
trajectory.append(encode(start_point[1],start_point[0]))

while len(trajectory_points) > 0:
    distance = float('inf')
    nearest_point = None
    for point in trajectory_points:
        if manhattan(decode(trajectory[-1]),decode(point)) < distance:
            distance = manhattan(decode(trajectory[-1]),decode(point))
            nearest_point = point
    trajectory.append(nearest_point)
    trajectory_points.remove(nearest_point)
    if nearest_point == encode(end_point[1],end_point[0]):
        print('找到终点')
        break

trajectory = [decode(t) for t in trajectory]
# 将 元组 转换为 列表
trajectory = [list(t) for t in trajectory]
print(trajectory)
