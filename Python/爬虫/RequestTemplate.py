"""
@Author: your name
@Date: 2020-01-31 12:02:21
@LastEditTime : 2020-02-07 11:05:34
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Python/爬虫/RequestTemplate.py
"""
import requests

try:
    r = requests.get(" https://www.mi.com")
except requests.ConnectionError:
    print("连接错误")
else:
    print(r.text)
