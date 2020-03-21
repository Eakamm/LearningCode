'''
@Author: your name
@Date: 2020-02-20 16:55:30
@LastEditTime: 2020-02-20 18:24:29
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\PythonBase\test.py
'''
# 温度转化
# n = input().upper()

# l = len(n)
# m = n[:l - 1]
# if '.' in m:
#     m = float(m)
# else:
#     m = int(m)

# if 'F' in n:
#     c = (m - 32) / 1.8
#     print('%.2f' % c + 'C')
# elif 'C' in n:
#     f = m * 1.8 + 32
#     print('%.2f' % f + 'F')
# else:
#     print('输入格式错误')

# 数字转化

# strs = input()

# data = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
# strs2 = ''
# for c in strs:
#     strs2 += data[int(c)]

# print(strs2)

# 数值运算

strs = input()
# list = strs.split(' ')
strs = strs.replace(' ', '')
data = ['+', '-', '*', '/']
count = 3
while count >= 0:
    if strs.find(data[count]) != -1:
        op_index = strs.find(data[count], 2)
        break
    else:
        count -= 1
left = float(strs[:op_index])
right = float(strs[op_index + 1:])
op = 0
if count == 0:
    op = left + right
elif count == 1:
    op = left - right
elif count == 2:
    op = left * right
elif count == 3:
    op = left / right
print('%.2f' % op)
