names = ['gg', 'ggg', 'ddd']

# print(names[-1])

# 添加
# names.append('hhhh')

# names.insert(1, 'bbb')

# print("添加：" + str(names))

# 删除
# del names[0]

# name = names.pop()
# print(name)
# name = names.pop(1)
# print(name)
# names.remove('bbb')

# print(names)

# 排序
# names = ['gg', 'ggg', 'ddd', 'dsssss', 'ass']
# names.sort()
# print(names)
# names.sort(reverse=True)
# print(names)

# sorted(names)
# print(names)
# sorted(names, reverse=True)
# print(names)

# 倒着输出，永久改变数据
# names.reverse()
# print(names)
# names.reverse()
# print(names)

# 替换值
# print(names)
# names[1:3] = ['C', 'D']
# print(names)

name = "liuzhihao"
for n in range(len(name)):
    print(name[-1-n], end="")
print(name[:])
# print(name.split.reverse())
