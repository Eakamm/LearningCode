'''
@Author: your name
@Date: 2020-01-16 16:31:07
@LastEditTime : 2020-01-16 20:34:34
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \PythonPersonal\小项目\数据可视化\test.py
'''
import matplotlib.pyplot as plt

squals = [1, 4, 9, 16, 25]
# 标题
plt.title('test')
# x,y轴的名称和字体大小
plt.xlabel('value', fontsize=24)
plt.ylabel('square of value', fontsize=14)
plt.plot(squals)
plt.show()
