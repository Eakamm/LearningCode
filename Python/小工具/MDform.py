'''
@Author: your name
@Date: 2020-02-18 12:32:10
@LastEditTime: 2020-02-18 13:56:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\小工具\MDform.py
'''
import re

pattern = re.compile(r'(\t|\n)+')
with open('小工具/form.text', 'r') as f:
    # for line in f.readlines:
    #     print(line)
    lines = f.readlines()
    data = []
    # print(lines)
    for line in lines:
        line = pattern.sub('|', line)
        print(line)
