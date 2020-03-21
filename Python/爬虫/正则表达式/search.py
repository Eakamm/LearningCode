'''
@Author: your name
@Date: 2020-02-21 10:34:39
@LastEditTime: 2020-02-21 10:39:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\爬虫\正则表达式\search.py
'''

import re

str = 'PythonGood'

# python默认的匹配是贪婪的，会找最长匹配
matchObj = re.search(r'\S.*[o]', str)
print(matchObj.group(0))

# 最小匹配在+，*，？，{m,n}后面加？表示最小匹配
matchObj = re.search(r'\S.*?[o]', str)
print(matchObj.group(0))


