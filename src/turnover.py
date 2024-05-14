import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def plot_userFreq(path, year):
    '''
    UID,ST
    1,2020-01-01 00:00:00
    1,2020-01-01 01:00:00
    2,2020-01-01 00:00:00
    ...
    统计每个用户的骑行频率，绘制频率的直方图
    '''
    # 读取数据
    df = pd.read_csv(path)
    df['ST'] = pd.to_datetime(df['ST'])
    df = df.sort_values(by=['UID', 'ST'])

    # 统计每个用户的骑行频率
    user_freq = df.groupby('UID').size()

    # 截取 频率小于20的数据
    user_freq = user_freq[user_freq <= 20]

    # 绘制直方图 归一化
    plt.hist(user_freq, bins=20, range=(1, 10), edgecolor='black', density=True)

    # x 轴分割 20 个点
    plt.xticks(np.arange(1, 11, 1))

    plt.xlabel('Frequency')
    plt.ylabel('Number of Users')
    plt.title('{} User Frequency'.format(year))
    plt.grid(True)
    plt.show()

# 绘制两年的用户骑行频率 饼图
def plot_userFreq_pie(paths, names):
    '''
    paths: 数据文件路径
    names: 数据文件对应的年份
    '''
    # 读取数据
    df1 = pd.read_csv(paths[0])
    df1['ST'] = pd.to_datetime(df1['ST'])
    df1 = df1.sort_values(by=['UID', 'ST'])
    user_freq1 = df1.groupby('UID').size()

    df2 = pd.read_csv(paths[1])
    df2['ST'] = pd.to_datetime(df2['ST'])
    df2 = df2.sort_values(by=['UID', 'ST'])
    user_freq2 = df2.groupby('UID').size()

    # 绘制饼图
    fig, axs = plt.subplots(1, 2)
    axs[0].pie(user_freq1.value_counts(), labels=user_freq1.value_counts().index, autopct='%1.1f%%')
    axs[0].set_title(names[0])
    axs[1].pie(user_freq2.value_counts(), labels=user_freq2.value_counts().index, autopct='%1.1f%%')
    axs[1].set_title(names[1])

    plt.show()

# 计算日单车周转率并绘制为折线图
def turnover_rate(paths,years):
    '''
    df: 数据
    UID,ST,BID
    759,2016/8/1 0:23,79699
    1440,2016/8/1 0:25,33279
    5463,2016/8/1 0:26,3060
    '''
    # 读取数据
    df1 = pd.read_csv(paths[0])
    df1['ST'] = pd.to_datetime(df1['ST'])
    df1 = df1.sort_values(by=['UID', 'ST'])

    df2 = pd.read_csv(paths[1])
    df2['ST'] = pd.to_datetime(df2['ST'])
    df2 = df2.sort_values(by=['UID', 'ST'])
    
    # # 1. 计算每天的单车数
    bike_num1 = df1.groupby(df1['ST'].dt.date)['BID'].nunique()

    bike_num2 = df2.groupby(df2['ST'].dt.date)['BID'].nunique()


    # # 2. 计算每天的单车使用次数
    bike_freq1 = df1.groupby(df1['ST'].dt.date).size()
    bike_freq2 = df2.groupby(df2['ST'].dt.date).size()

    # 3. 计算日单车周转率
    turnover_rate1 = bike_freq1 / bike_num1
    turnover_rate2 = bike_freq2 / bike_num2

    # 增加一个日期索引 去除年份
    turnover_rate1.index = [str(date)[5:] for date in turnover_rate1.index]
    turnover_rate2.index = [str(date)[5:] for date in turnover_rate2.index]

    # 线性回归
    slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(range(len(turnover_rate1)), turnover_rate1)
    slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(range(len(turnover_rate2)), turnover_rate2)
    # 调大字体
    plt.rcParams.update({'font.size': 15})
    # 绘制折线图 并添加线性回归线 在 legend 表示直线方程
    plt.plot(turnover_rate1, label='{}: y={:.4f}x+{:.4f}, r={:.4f}'.format(years[0], slope1, intercept1, r_value1))
    plt.plot(turnover_rate2, label='{}: y={:.4f}x+{:.4f}, r={:.4f}'.format(years[1], slope2, intercept2, r_value2))

    # 绘制线性回归线
    plt.plot(range(len(turnover_rate1)), slope1 * range(len(turnover_rate1)) + intercept1,color = 'gray',linestyle='--')
    plt.plot(range(len(turnover_rate2)), slope2 * range(len(turnover_rate2)) + intercept2,color = 'gray',linestyle='--')

    plt.xlabel('Date')
    plt.ylabel('Turnover Rate')

    plt.xticks(range(len(turnover_rate1)), turnover_rate1.index, rotation=45)

    plt.title('Daily Turnover Rate')
    plt.legend()

    plt.show()

def turnover_rate_week(paths,years):
    '''
    df: 数据
    UID,ST,BID
    759,2016/8/1 0:23,79699
    1440,2016/8/1 0:25,33279
    5463,2016/8/1 0:26,3060
    '''
    # 读取数据
    df1 = pd.read_csv(paths[0])
    df1['ST'] = pd.to_datetime(df1['ST'])
    df1 = df1.sort_values(by=['UID', 'ST'])

    df2 = pd.read_csv(paths[1])
    df2['ST'] = pd.to_datetime(df2['ST'])
    df2 = df2.sort_values(by=['UID', 'ST'])

    # 计算一周七个工作日的单车周转率 

    # 1. 计算每周的单车数
    bike_num1 = df1.groupby(df1['ST'].dt.weekday)['BID'].nunique()
    bike_num2 = df2.groupby(df2['ST'].dt.weekday)['BID'].nunique()

    # 2. 计算每周的单车使用次数
    bike_freq1 = df1.groupby(df1['ST'].dt.weekday).size()
    bike_freq2 = df2.groupby(df2['ST'].dt.weekday).size()

    # 3. 计算日单车周转率
    turnover_rate1 = bike_freq1 / bike_num1
    turnover_rate2 = bike_freq2 / bike_num2

    # 线性回归
    slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(range(len(turnover_rate1)), turnover_rate1)
    slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(range(len(turnover_rate2)), turnover_rate2)
    # 调大字体
    plt.rcParams.update({'font.size': 15})
    # 绘制折线图 并添加线性回归线 在 legend 表示直线方程
    plt.plot(turnover_rate1, label='{}: y={:.4f}x+{:.4f}, r={:.4f}'.format(years[0], slope1, intercept1, r_value1))
    plt.plot(turnover_rate2, label='{}: y={:.4f}x+{:.4f}, r={:.4f}'.format(years[1], slope2, intercept2, r_value2))

    # 绘制线性回归线
    plt.plot(range(len(turnover_rate1)), slope1 * range(len(turnover_rate1)) + intercept1,color = 'gray',linestyle='--')
    plt.plot(range(len(turnover_rate2)), slope2 * range(len(turnover_rate2)) + intercept2,color = 'gray',linestyle='--')

    plt.xlabel('Week')
    plt.ylabel('Turnover Rate')

    notation = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    plt.xticks(range(len(turnover_rate1)), notation)
    

    plt.title('Weekly Turnover Rate')
    plt.legend()

    plt.show()






if __name__ == '__main__':

    names = ['2016', '2020']
    paths = ['src/simple/cdf16.csv','src/simple/cdf20.csv']

    # plot_userFreq('src/simple/cdf16.csv', '2016')
    # plot_userFreq('src/simple/cdf20.csv', '2020')
    # plot_userFreq_pie(paths, names)

    # turnover_rate(paths, names)
    turnover_rate_week(paths, names)
