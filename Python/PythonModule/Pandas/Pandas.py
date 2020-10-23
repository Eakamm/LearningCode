import pandas as pd
import numpy as np

# x = np.arange(10)
# 分为2行5列
# x.shape = (2, 5)
# print(x)

# numpy数组支持多维数组的多维索引

# print(x[1, 3])

# pandas创建一个一维数组
# s = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])

# 获取索引序列
# print(s.index)

# 根据索引查找数据
# print(s[1])
# s[1] = "e"
# print(s[1])

# 多个索引查找(可以是自定义的字符串索引和默认的)
# s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# 自定义的索引('a', 'b', 'c')
# print(s2[['a', 'b']])
# 第n行(0,1,2)
# print(s2[[1, 2]])
#

# in判断索引是否存在
# print(1 in s)

# pandas读取文件
# filename = 'PythonModule/file/sitka_weather_2014.csv'
# df = pd.read_csv(filename)

# 打印
# print(df)
# 轴
# print("轴：" + str(df.ndim))

# 索引
# print("索引：" + str(df.index))

# 打印前N行
# print(("打印前%d行：\n" + str(df.head(3))) % 3)

# DataFrame信息
# df.info()
# df.describe()

# DataFrame值
# print("值：" + str(df.values))

# 列名
# print("列名：" + str(df.columns))

# 打印某列数据
# df['PrecipitationIn']


# filename = 'PythonModule/file/IMDB-Movie-Data.csv'
# df = pd.read_csv(filename)

# strings = df['Actors']

# # print(strings.mean())
# print(strings.str.findall('Chris Pratt').str)


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

# 打印某一行
# print(frame.loc[1])
# 创建新的一列
# frame['test'] = frame.state == 'Ohio'
# print(frame)
# 获取某一列，根据
# print(frame['test'])
# 删除
# del frame['test']
# 获取
# print(frame.columns)
# print()

# 布尔值DataFrame进行索引，布尔值DataFrame可以是对标量值进行比较产生的
# frame2 = pd.DataFrame(np.arange(20).reshape(4, 5),
#                       index=list('abcd'),
#                       columns=list('abcde'))

# frame2[frame2 < 10] = 0
# print(frame2)
# print(frame2['a'])


# 算术对齐
df = pd.DataFrame(np.arange(6).reshape(2, 3))
df2 = pd.DataFrame(np.arange(6).reshape(2, 3))

df.loc[1, 1] = np.nan
print(df2+df)

# 设定nan的默认值(nan+4 => nan 0+4 => 4)
print(df.add(df2, fill_value=0))
