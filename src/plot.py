import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statis import compute_cdf,compute_pdf



# 封装为函数
def cdf(path):
    '''
    数据格式：
    UID,ST
    1,2020-01-01 00:00:00
    1,2020-01-01 01:00:00
    2,2020-01-01 00:00:00
    ...
    函数效果：
    读取数据文件，计算每个 UID 的时间间隔，绘制时间间隔的 CDF 图
    '''
    # 读取数据
    df = pd.read_csv(path)
    df['ST'] = pd.to_datetime(df['ST'])
    df = df.sort_values(by=['UID', 'ST'])
    df['TimeDiff'] = df.groupby('UID')['ST'].diff().dt.total_seconds() / 3600

    # 使用 compute_cdf 函数计算 CDF
    sorted_data, cdf = compute_cdf(df['TimeDiff'])
    return sorted_data,cdf

    # # 绘制 CDF 图
    # plt.plot(sorted_data, cdf)
    # plt.xlabel('Time Interval (hours)')
    # plt.ylabel('CDF')
    # plt.title('CDF of Time Interval')
    # plt.grid(True)
    # plt.show()

def plot_cdf(cdfs,names,styles):
    '''
    函数效果：
    绘制多个 CDF 图
    '''
    for i in range(len(cdfs)):
        plt.plot(cdfs[i][0], cdfs[i][1], label=names[i], linestyle=styles[i])
    plt.xlabel('Time Interval (hours)')
    plt.ylabel('CDF')
    plt.title('CDF of Time Interval')
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_pdf(path):
    '''
    数据格式：
    UID,ST
    1,2020-01-01 00:00:00
    1,2020-01-01 01:00:00
    2,2020-01-01 00:00:00
    ...
    函数效果：
    读取数据文件，计算每个 UID 的时间间隔，绘制时间间隔的 PDF 图
    '''
    # 读取数据
    df = pd.read_csv(path)
    df['ST'] = pd.to_datetime(df['ST'])
    df = df.sort_values(by=['UID', 'ST'])
    df['TimeDiff'] = df.groupby('UID')['ST'].diff().dt.total_seconds() / 3600

    # 使用 compute_pdf 函数计算 PDF
    sorted_data, pdf = compute_pdf(df['TimeDiff'])

    # 绘制 PDF 图
    plt.plot(sorted_data, pdf)
    plt.xlabel('Time Interval (hours)')
    plt.ylabel('PDF')
    plt.title('PDF of Time Interval')
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    # plot_cdf('src\simple\cdf20.csv')
    # 绘制 2016 年和 2020 年的 CDF 图
    cdfs = []
    names = ['2016', '2020']
    styles = ['-', '--']
    cdfs.append(cdf('src\simple\cdf16.csv'))
    cdfs.append(cdf('src\simple\cdf20.csv'))
    # 保存 cdfs 文件为 npy 文件
    np.save('cdfs.npy', cdfs)

    plot_cdf(cdfs, names, styles)