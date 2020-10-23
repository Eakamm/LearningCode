import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(20).reshape(4, 5),
                  columns=list('abcde'))

# 求每组数据的最大最小值的差


def f(x): return x.max()-x.min()


# 默认为取出每列
series = df.apply(f)
print(series)

# 取出每行
series = df.apply(f, axis="columns")
print(series)


# 处理所有的元素
# 求平方
def f2(x): return x**2


data_frame = df.applymap(f2)
print(data_frame)

# 处理某一行
data_frame = df.loc[1].map(f2)
print(data_frame)
