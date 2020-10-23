# 导入模块
# import ToImport
# 导入特定函数
# from ToImport import make_pizza

# 导入特定函数
# make_pizza(16, 'pepperoni')
# # 函数模块导入
# ToImport.make_pizza(16, 'pepperoni')
# ToImport.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 关键字参数
# def get_formatted_name(first_name, last_name, middle_name):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# 使用关键字可以不在乎参数的位置
# musician = get_formatted_name(
#     first_name='jimi', last_name='hendrix', middle_name='joke')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# 形参默认值（默认值必须放到参数列表最后）
# def sum(a, b=5):
#     return a+b
# print(sum(1))
# print(sum(1, 2))


# 练习一
# def count(a, b, c):
#     return a + b - c
# print(count(1, 2, 3))


# 使用任意数量的关键字实参
# def getProfile(name, sex, **others):
#     profile = {}
#     profile['name'] = name
#     profile['sex'] = sex
#     for key, value in others.items():
#         profile[key] = value
#     return profile


# print(getProfile('刘志豪', '男', county='china', habbit='game'))

# 可以返回多个值(返回的类型是一个元组)
# def count(a, b, c):
#     return a + b, b - c
# print(count(1, 2, 3))
