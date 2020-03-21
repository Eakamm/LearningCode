import re

str = 'Python Good'

c = re.compile(r'[o]\S+')
# 找到所有匹配的字符串
list = c.findall(str)
print(list)
# 限制匹配长度
list = c.findall(str, 0, 8)
print(list)

# 找到所有匹配的字符串,返回一个迭代器
iter = c.finditer(str)
print(type(iter))
for i in iter:
    print(i.group(), end=',')

