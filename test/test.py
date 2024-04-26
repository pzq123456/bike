# 计算每一个小时 占当天总数的比例
# frequency = frequency / frequency.sum(axis=1)[:, None]

# 测试 计算每一个小时 占当天总数的比例 是否正确
import numpy as np

frequency = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(frequency)
print(frequency.sum(axis=1))
print(frequency.sum(axis=1)[:, None])
print(frequency / frequency.sum(axis=1)[:, None])
