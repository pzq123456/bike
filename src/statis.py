import numpy as np

def compute_cdf(data):
    # 将数据排序
    sorted_data = np.sort(data)
    n = len(sorted_data)
    # 计算每个时间间隔的累积概率
    cdf = np.arange(1, n + 1) / n
    return sorted_data, cdf

def compute_pdf(data):
    # 将数据排序
    sorted_data = np.sort(data)
    n = len(sorted_data)
    # 计算每个时间间隔的概率密度
    pdf = np.ones(n) / n
    return sorted_data, pdf

