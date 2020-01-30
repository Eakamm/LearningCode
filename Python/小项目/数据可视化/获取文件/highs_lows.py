'''
@Author: your name
@Date: 2020-01-16 21:01:24
@LastEditTime : 2020-01-21 13:18:40
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \PythonPersonal\小项目\数据可视化\获取文件\highs_lows.py
'''
import csv
from datetime import datetime

from matplotlib import pyplot as plt


def show_row(header_row):
    # enumerate()获取索引及其值
    for index, title in enumerate(header_row):
        print(str(index) + "  " + title)


def get_file_data(filename, highs, lows, dates):
    with open(filename) as f:
        reader = csv.reader(f)
        # 获取头，光标就到了下一行，就可以获取数据了
        header_row = next(reader)
        show_row(header_row)
        for row in reader:
            # 当数据缺失的时候，有时后会报错
            # ValueError: invalid literal for int() with base 10: ''
            try:
                high = int(row[1])
                low = int(row[3])
                date = row[0]
            except ValueError:
                pass
            else:
                lows.append(low)
                highs.append(high)
                dates.append(datetime.strptime(date, '%Y-%m-%d'))


# Get dates, high, and low temperatures from file.
# 最高气温
highs = []
# 日期
dates = []
# 最低气温
lows = []
filename = 'Python\PythonPersonal\小项目\数据可视化\获取文件\sitka_weather_2014.csv'
get_file_data(filename, highs, lows, dates)
fig = plt.figure(dpi=128, figsize=(10, 6))
# 设置数据
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 样式
plt.title('High Templept')
plt.ylabel('Temperature (F)', fontsize=14)
plt.xlabel('', fontsize=10)
# 绘制斜的日期
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

#     dates, highs, lows = [], [], []
#     for row in reader:
#         try:
#             current_date = datetime.strptime(row[0], "%Y-%m-%d")
#             high = int(row[1])
#             low = int(row[3])
#         except ValueError:
#             print(current_date, 'missing data')
#         else:
#             dates.append(current_date)
#             highs.append(high)
#             lows.append(low)

# # Plot data.
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red', alpha=0.5)
# plt.plot(dates, lows, c='blue', alpha=0.5)
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# # Format plot.
# title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
# plt.title(title, fontsize=20)
# plt.xlabel('', fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)

# plt.show()
