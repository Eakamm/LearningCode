# import this
import math
import random

print(math.pi)
# age = 18
str2 = "18"
myDouble = 2.11

# 强制类型转化
# age = int(str2)
# print(age)
# type(age)

# 字符串拼接需要将int主动转为字符串
# string = "it is "+str(age)+" hh"

# 格式化输入输出
# print(string+"age:%d" % age)

# 求字符串长度
# print(len(string)/2)

# 类型
# print(type(len(string)))

# 返回小于等于该值的最大整数
# floorTest = math.floor(myDouble)
# 返回大于等于该值的最小整数
# floorTest = math.ceil(myDouble)
# print(floorTest)
# print(type(floorTest))

# 成绩判断


def select(score):
    try:
        score = int(score)
        return True
    except ValueError:
        return False


# score = input()


# if (select(score)):
#     score = float(score)
#     if score >= 90:
#         print("A")
#     elif score > 70:
#         print("B")
#     elif score >= 60:
#         print("C")
#     else:
#         print("D")
# else:
#     print("成绩格式错误")


# 剪刀石头布
# selects = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
# people = input("请输入（0：石头，1：剪刀，2，布）：")
# if select(people):
#     people = int(people)
# else:
#     pass

# ai = random.randint(0, 2)
# print(people+ai)
# print(selects[people][ai])
# if selects[people][ai] == 0:
#     print("平局")
# elif selects[people][ai] == 1:
#     print("赢了")
# elif selects[people][ai] == -1:
#     print("输了")
# else:
#     print("错误")

# 求偶数和
# sum = 0
# for i in range(1, 101):
#     sum += i if i % 2 == 0 else 0
# print(sum)

# 99乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(str(j)+"*"+str(i)+"="+str(i*j)+"\t", end=" ")
#     print()
