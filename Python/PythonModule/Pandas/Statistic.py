# 统计
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20).reshape(4, 5))

# 全部统计
print(df.describe())

# 平均值
print(df.mean())

# 设置为行统计
print(df.mean(axis="columns"))
