import matplotlib.pyplot as plt
import pandas as pd

class_map= {
    0: 'Transportation',
    1: 'Sports and Leisure',
    2: 'Company',
    3: 'Business Residence',
    4: 'Science and Education Culture',
    5: 'Shopping',
    6: 'Scenic Spots',
    7: 'Catering'
}


# 样例数据
data = [3, 6, 3, 5, 5, 0, 5, 5, 7, 4, 5, 1, 7]

def draw_pie(data,title):
    # 统计类别数量
    counts = [data.count(i) for i in range(8)]
    labels = [class_map[i] for i in range(8)]
    # 自定义颜色 使用渐变色带
    colors = ['#FF6347', '#FFA07A', '#FFD700', '#ADFF2F', '#00FF7F', '#00FFFF', '#1E90FF', '#9370DB']

    # 找到最大值的索引
    max_index = counts.index(max(counts))

    # 绘制圆环图
    plt.figure(figsize=(8, 8))

    # 突出显示最大值
    explode = [0] * 8
    explode[max_index] = 0.1

    plt.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3, edgecolor='w'), explode=explode)

    plt.axis('equal')  # 使饼图保持圆形
    plt.title(title, fontsize=16, fontweight='bold')
    # legend 图例
    plt.legend(labels, loc='upper right', fontsize=12, title='Class', title_fontsize='14')
    
    plt.show()

if __name__ == '__main__':

    YEAR = '2020'
    # src\simple\class\tmp\class16.csv
    # 读取数据
    data = pd.read_csv('src\simple\class\\tmp\class20.csv')
    data = data['class'].values.tolist()
    draw_pie(data, YEAR + ' Destination Distribution')