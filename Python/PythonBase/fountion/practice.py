import math

# 素数
# status = True

# for i in range(100, 201):
#     status = True
#     for j in range(2, int(math.sqrt(i))):
#         if (i % j == 0):
#             status = False
#             break
#     if (status):
#         print(i, end=",")


# 闰年判断
def isYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 200 != 0:
        return True
    else:
        return False


year = input()
if isYear(int(year)):
    print("是闰年")
else:
    print("不是闰年")
