import numpy as np
import random

# 获取numpy版本
# print(np.version.version)

# numpy的数组
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([random.random() for i in range(10)])  # 小数
# print(b)
# print(type(b))

# 读取数据
# filename = 'PythonModule/file/sitka_weather_2014.csv'

# a = np.loadtxt(filename)
# print(a[:10])

# 索引

x = np.arange(20)

print(x[0:4])
# 分为4行5列
x.shape = (4, 5)
# 数组切片不会复制内部数组数据，只会生成原始数据的新视图。这与列表或元组切片不同
# 多维数组用单个
print(x[:2])

print(x[1:3, 1:3])
