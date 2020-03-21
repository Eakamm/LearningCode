'''
@Author: your name
@Date: 2020-02-11 11:23:14
@LastEditTime : 2020-02-11 23:46:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\爬虫\BeautifulSoup4\Base.py
'''

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.baidu.com")
r.encoding = "utf-8"

# 选用python的解析器，这里使用的是python的标准库中的解析器
soup = BeautifulSoup(r.text, "html.parser")

# 创建一个a标签的tag对象
tag = soup.a
# 打印第一个a标签的字典内容
print(tag.attrs)

print("tag的类型：")
print(tag.name)

print("soup.a的类型：")
print(type(tag))

print("tag对象的属性：")
print(tag.attrs)

print("soup.a.attrs的类型：")
print(type(tag.attrs))

print("按照字典的方式获取其中的元素：")
print(tag.attrs['class'])
print('获取class属性的值')
print(tag['class'])
print()

# 获取标签的字符串
print("获取a标签的内容:")
print(tag.string)

# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
tag2 = soup.p
print("--------------")
print(tag2)
print(tag2.string)
# 使用.strings迭代获取
for string in tag2.strings:
    print(string)
print("--------------")

tag.string.replace_with("百度一下，你就不知道")
print("替换后的字符串：")
print(tag)

tag.name = "test"
print(tag.name)
# 删除tag的属性
print(tag)
del tag["class"]
print(tag)

# Comment注释

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup2 = BeautifulSoup(markup, "html.parser")
# b标签中的内容为注释，commment的类型被定为bs4.element.Comment
comment = soup2.b.string
print(type(comment))
