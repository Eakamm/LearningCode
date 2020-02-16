'''
@Author: your name
@Date: 2020-02-07 12:00:48
@LastEditTime : 2020-02-11 11:11:43
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\爬虫\GetBaidu.py
'''
import requests

# ky = {'User-Agent': 'Mozilla/5.0'}
# path = 'test.html'
# try:
#     r = requests.get('https://www.amazon.cn/dp/B01N32HKQA', headers=ky)
#     r.encoding = 'utf-8'
# except requests.ConnectionError:
#     print('连接错误')
# else:
#     print(r.encoding)
#     print(r.request.headers)
#     # print(r.text)
#     try:
#         with open(path, 'w', encoding='utf-8') as f:
#             f.write(r.text)
#     except FileNotFoundError:
#         print('文件未找到')
ky = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.baidu.com/s'
key = {'wd': '奇异小队'}

r = requests.get(url, params=key, headers=ky)
r.encoding = 'utf-8'
r.status_code
print(r.text)
