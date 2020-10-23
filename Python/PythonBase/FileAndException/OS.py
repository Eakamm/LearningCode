import os

path = "PythonBase/FileAndException/test"
# 移除该路径的文件
# os.remove(path+"/test.txt")

# 创建目录
# os.mkdir(path)
# 删除目录
os.rmdir(path)

# 获取当前工作目录
# retval = os.getcwd()
# print(retval)

# 更改工作目录
# os.chdir("PythonBase/FileAndException")
# print(os.getcwd())

# 获取该目录下的所有文件和目录，返回值为list
# if len(os.listdir(path)) != 0:
#     print(os.listdir(path))
# else:
# 递归删除该路径下的所有文件
print(os.removedirs(path))
