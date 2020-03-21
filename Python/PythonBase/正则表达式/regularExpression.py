'''
@Author: your name
@Date: 2020-02-18 20:22:41
@LastEditTime: 2020-02-18 20:22:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\PythonBase\正则表达式\regularExpression.py
'''

import re

str = 'Python'
# match
print('-------------match()-----------')
matchObj = re.match(r'[p]\S+', str)
if matchObj:
    print(matchObj.group())
else:
    print('没有匹配到！')

matchObj = re.match(r'[P]\S+', str)
print(matchObj.group())

print('-------------search()-----------')