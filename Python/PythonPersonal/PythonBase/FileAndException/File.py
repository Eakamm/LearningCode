'''
@Author: your name
@Date: 2020-01-11 17:27:56
@LastEditTime : 2020-01-15 00:03:10
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit:
@FilePath: \PythonPersonal\PythonBase\FileAndException\File.py
'''
# 打开文件读取返回字符串
# with open('PythonBase/FileAndException/Need_File/pi_digits.txt') as file_object:
#     lines = file_object.read()
#     print(lines.rstrip())

# 打开文件按行读取
# with open('PythonBase/FileAndException/Need_File/pi_million_digits.txt') as file_object:
#     lines = file_object.readlines()
# content = ""
# my_birthday = input("Your Birthday:")
# for line in lines:
#     content += line
# if my_birthday in content:
#     print("yes")
# else:
#     print("no")

# I love programming.
# I love creating new games.
# I also love finding meaning in large datasets.
# I love creating apps that can run in a browser.
# with open('PythonBase/FileAndException/Need_File/programming.txt', 'w') as write_file:
#     write_file.write('I love programming.I\'m '+my_birthday)

# 异常
# try:
#   with open('PythonBase/FileAndException/Need_File/45.txt') as ani:
#     text = ani.read()
# except FileNotFoundError:
#   print('文件没有找到！')
# else:
#   words = text.split(' ');
#   length = len(words)
#   print("文章长度为："+str(length))

# 作业 10-6
# while 1:
#   try:
#       a = int(input('请输入数字a：'))
#       b = int(input('请输入数字b：'))
#   except ValueError:
#       print('请输入数字！')
#   else:
#       print(a+b)
#
#      break

# 作业 10-10

# file_name = "PythonBase/FileAndException/Need_File/45.txt"
# with open(file_name) as file_object:
#   text = file_object.read()
#   print(text.lower().count('the'))

# Json
# import json

# names = ['小王','小李','老王','老李']
# file_name = 'PythonBase/FileAndException/Need_File/names.txt'

# with open(file_name,'w') as json_write:
#   json.dump(names,json_write)

# with open(file_name) as json_read:
#   names2 = json.load(json_read)
#   print(names2)

# 作业 10-12
# import json

# file_name = 'PythonBase/FileAndException/Need_File/FavouriteNumbers.json'

# def get_user_number():
#   try:
#     with open(file_name) as target:
#       numbers = json.load(target)
#   except FileNotFoundError:
#     return None
#   else:
#     return numbers

# def get_favourite_number(n):
#   numbers = get_user_number()
#   if numbers and n in numbers:
#     print('I know yourfavorite number! It\'s .'+n)
#   else:
#     print('Please you must input your favourite Number！')
#     save_favourite_number(input("Your number:"))

# def save_favourite_number(n):
#   numbers = get_user_number()
#   if not numbers:
#     numbers = []
#   else:
# #   将numbers字符串转为Python对象
#     numbers = json.loads(numbers)
# # 向对象中添加数据
#   numbers.append(n)
#   with open(file_name,'w') as target:
# #   json.dumps(numbers)将Python对象转为json字符串。因为.dump只支持字符串
#     json.dump(json.dumps(numbers),target)

# while 1:
#   number = input('Enter your favorite number：')
#   if number == 'q':
#     break
#   get_favourite_number(number)

# import json

# numbers = ['1','2','3']

# numbers = json.dumps(numbers)
# print(type(numbers))
# print(numbers)
# numbers = json.loads(numbers)
# print(type(numbers))
# print(numbers)

# 异常
import unittest
from sums import sums
from survey import AnonymousSurvey


class SumTestCase(unittest.TestCase):
    def setUp(self):
        question = 'what?'
        self.mysurvey = AnonymousSurvey(question)
        self.responses = ['a', 'b', 'c']

    def test_sum(self):
        result = sums(1, 2)
        self.assertEqual(str(result), '3')

    def test_store_single(self):
        self.mysurvey.store_response(self.responses[0])
        self.assertIn(self.mysurvey.responses[0], self.responses)

    def test_store_three(self):
        for response in self.responses:
            self.mysurvey.store_response(response)
        for response in self.mysurvey.responses:
            self.assertIn(response, self.responses)


unittest.main()

# setup()
