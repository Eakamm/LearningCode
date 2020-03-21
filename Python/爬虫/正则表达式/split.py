'''
@Author: your name
@Date: 2020-02-17 09:44:39
@LastEditTime: 2020-02-21 10:34:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\爬虫\正则表达式\split.py
'''
import re

Obj = re.split('[/]',
               '                       [中] 沈大成 / 理想国 | 广西师范大学出版社 / 2020-1')

str = re.search(r'\S+[\s]\S+', Obj[0])
print(str)
