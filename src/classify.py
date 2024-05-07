# from tree import create_geohash_tree, greedy_search
# from distance import geohash_approximate_distance
import pandas as pd
import tqdm
import pickle

def load_geohash_tree(path):
    with open(path, 'rb') as f:
        geohash_tree = pickle.load(f)
    return geohash_tree

def classify_geohash(poipath, tracpath, respath):
    # class,lon,lat,geohash
    # 0,121.180367,31.161415,wtw1m8bb7hyc
    # 读取数据
    df = pd.read_csv(poipath)
    tf = pd.read_csv(tracpath)
    # 将 tf 中的 geohash 字段替换为 poi 中的 geohash 对应的类别
    # 从 df 中检索出 geohash 对应的类别
    # tf['class'] = tf['nearest'].apply(lambda x: df[df['geohash'] == x]['class'].values[0])
    # tqdm 是一个进度条库，可以在循环中使用
    for i in tqdm.tqdm(range(len(tf))):
        # 取出每一行的 geohash
        geohash = tf.loc[i, 'nearest']
        tf.loc[i, 'class'] = df[df['geohash'] == geohash]['class'].values[0]
    # 保存结果
    tf.to_csv(respath, index=False)





# if __name__ == '__main__':

    # 1. 
    # # 读取数据
    # df = pd.read_csv('src/simple/class/poi_geohash.csv')
    # geohashes = df['geohash'].tolist()
    # # 创建geohash树
    # geohash_tree = create_geohash_tree(geohashes)
    # # 保存geohash树
    # with open('src/simple/class/geohash_tree.pkl', 'wb') as f:
    #     pickle.dump(geohash_tree, f)

    # 2.
    # geohash_tree = load_geohash_tree('src/simple/class/tmp/geohash_tree.pkl')
    # # src\simple\class\tra16.csv
    # # 读取数据
    # df = pd.read_csv('src/simple/class/tra20.csv')
    # # 提取geohash
    # geohashes = df['geohash'].tolist()
    # # 保存结果
    # results = []
    # for geohash in tqdm.tqdm(geohashes):
    #     result = greedy_search(geohash, geohash_tree)
    #     results.append(result.pop() if result else None)

    # # 保存为单独的 csv 文件 仅包含 result 列名为 nearest
    # result_df = pd.DataFrame({'nearest': results})
    # result_df.to_csv('src/simple/class/tmp/res20.csv', index=False)

    # 3.
    # poipath = 'src\simple\class\poi_geohash.csv'
    # tracpath = 'src\simple\class\\tmp\\res20.csv'
    # respath = 'src\simple\class\\tmp\\class20.csv'
    # classify_geohash(poipath, tracpath, respath)






