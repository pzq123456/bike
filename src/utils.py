import pandas as pd
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

# 读取 data\poi18.csv 将 class 列的字符串类别转换为数字编码
def preprocess_poi_data(path,save_path):
    #     class,lon,lat
    # 交通设施服务,121.180367,31.161415
    poi_data = pd.read_csv(path)
    poi_data['class'] = poi_data['class'].apply(lambda x: class_map[x])
    poi_data.to_csv(save_path, index=False)

if __name__ == '__main__':
    path = 'H:\\bike\data\poi18.csv'
    save_path = 'poi18_code.csv'
    preprocess_poi_data(path,save_path)