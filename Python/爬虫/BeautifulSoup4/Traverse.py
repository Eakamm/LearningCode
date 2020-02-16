'''
@Author: your name
@Date: 2020-02-11 17:43:24
@LastEditTime : 2020-02-13 16:07:47
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\爬虫\BeautifulSoup4\Traverse.py
'''
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.baidu.com")
r.encoding = "utf-8"

# 选用python的解析器，这里使用的是python的标准库中的解析器
soup = BeautifulSoup(r.text, "html.parser")
# 展示a标签的上一级标签
print(soup.a.parent)
# 找到所有的a标签,以数组的方式返回
all_a = soup.find_all('a')
for item in all_a[:3]:
    print(item)
# 找到a标签中指定id的标签
all_a = soup.find_all('a'，id = '')

# print(all_a[3])
# print(soup.find_all('a'))

print('------------------------------------------')

# 将子节点迭代打印
head_tag = soup.head
# 将tag的子节点以列表返回
print(head_tag.contents)
# item的类型为Tag，`.children`可以将将标签的子节点做成迭代器，进行遍历
print(type(head_tag.children))
for child in head_tag.children:
    if child.string is not None:
        print(child)
        child.string.replace_with("hahaha")
        print(child)
    else:
        print(child)
# print(head_tag.chilren)

print("----------------------------------------")
