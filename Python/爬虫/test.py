"""
@Author: your name
@Date: 2020-01-30 10:53:39
@LastEditTime : 2020-01-31 12:00:12
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Python/爬虫/test.py
"""
import requests

# r = requests.get(" https://www.mi.com")
# r = requests.get(" https://www.github.com")
# r = requests.get("https://www.baidu.com")
# r.encoding = "utf-8"
# print(r.encoding)
# print(r.headers['Content-Type'])
# print(r.headers)
# print(r.text)

try:
    r = requests.get(" https://www.github.com")
except requests.ConnectionError:
    print("连接错误")
