from distance import manhattan,haversine,encode,decode
import pickle
# import numpy as np
import pandas as pd
import tqdm

# 封装
def generate_trajectory_points(start_point,end_point,trajectory_points):
    # 将起点和终点加入轨迹点
    trajectory_points.append(start_point)
    trajectory_points.append(end_point)
    # 去重
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
            # print('找到终点')
            break

    trajectory = [decode(t) for t in trajectory]
    # 将 元组 转换为 列表
    trajectory = [list(t) for t in trajectory]
    return trajectory

# 计算轨迹长度
def trajectory_length(trajectory):
    '''
    使用haversine公式计算轨迹长度
    '''
    length = 0
    for i in range(len(trajectory)-1):
        length += haversine(trajectory[i],trajectory[i+1])
    return length

# 业务代码

def extract(path):
    '''
    ID,BID,UID,ST,WD,SX,SY,ET,DU,EX,EY,track
    1,79699,759,2016/8/1 0:23,星期一,121.52,31.309,2016/8/1 0:32,9,121.525,31.316,"121.520,31.309#121.521,31.309#121.522,31.309#121.524,31.309"
    仅提取对轨迹排序有用的字段
    '''
    data = pd.read_csv(path)
    Olist = data[['SX','SY']]
    Dlist = data[['EX','EY']]
    track = data['track'].apply(lambda x: [list(map(float,point.split(','))) for point in x.split('#')])
    return Olist,Dlist,track

def preprocess(Olist,Dlist,track):
    # 重排序
    Olist = Olist.values
    Dlist = Dlist.values
    track = track.values
    new_track = []
    # tqdm.tqdm() 显示进度条

    # for i in range(len(track)):
    #     new_track.append(generate_trajectory_points(Olist[i],Dlist[i],track[i]))

    for i in tqdm.tqdm(range(len(track))):
        new_track.append(generate_trajectory_points(Olist[i],Dlist[i],track[i]))

    # 不使用 np.array() 转换为 numpy 数组
    return new_track

# 保存不定长的轨迹数据
def save_track(data,path):
    # 若无文件，则创建文件
    with open(path,'wb') as f:
        pickle.dump(data,f)

# 读取不定长的轨迹数据
def load_track(path):
    with open(path,'rb') as f:
        data = pickle.load(f)
    return data

class_map = {
    '交通设施服务': 0,
    '体育休闲服务': 1,
    '公司企业': 2,
    '商务住宅': 3,
    '科教文化服务': 4,
    '购物服务': 5,
    '风景名胜': 6,
    '餐饮服务': 7
}

# 数据预处理 对 poi 及轨迹分类
# 首先加载 poi 数据 将字符串类别转换为数字编码 并将经纬度转换为 GeoHash 编码
def preprocess_poi_data(path,save_path):
    #     class,lon,lat
    # 交通设施服务,121.180367,31.161415
    poi_data = pd.read_csv(path)
    poi_data['class'] = poi_data['class'].apply(lambda x: class_map[x])
    poi_data['geohash'] = poi_data.apply(
        lambda row: encode(row['lat'], row['lon']), axis=1
    )
    poi_data.to_csv(save_path, index=False)

# 预处理 轨迹终点数据
# ID,EX,EY
# 1,121.525,31.316
# 2,121.517,31.309
def preprocess_trajectory_data(path,save_path):
    # 加载轨迹点数据
    trajectory_data = pd.read_csv(path)
    # 对轨迹点数据进行 GeoHash 编码
    trajectory_data['geohash'] = trajectory_data.apply(
        lambda row: encode(row['EY'], row['EX']), axis=1
    )
    trajectory_data.to_csv(save_path, index=False)

# test
if __name__ == '__main__':
    path = 'data\\bike16.csv'
    Olist,Dlist,track = extract(path)

    new_track = preprocess(Olist,Dlist,track)
    save_track(new_track,'src\\simple\\track\\track16.pickle')

    # 计算轨迹长度 组织成 DataFrame 并保存为 csv 文件
    print('计算轨迹长度并保存为csv文件')
    length = [trajectory_length(t) for t in tqdm.tqdm(new_track)]
    # length = [trajectory_length(t) for t in new_track]
    length = pd.DataFrame(length,columns=['length'])
    length.to_csv('src\\simple\\track\\length16.csv',index=False)

    # # load data
    # new_track = load_track('src\\simple\\track\\track.pickle')
    # print(new_track[0])