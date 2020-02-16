import requests

ky = {'User-Agent': 'Mozilla/5.0'}
# 图片存储的位置
path = 'test.jpg'
url = 'https://imgs.ali213.net/oday/uploadfile/2017/06/08/201706089250952.jpg'
key = {'wd': '奇异小队'}

r = requests.get(url, headers=ky)
print(r.status_code)
try:
    # 打开图片文件，以二进制写入
    with open(path, 'wb') as f:
        f.write(r.content)
except FileNotFoundError:
    print('文件未找到！')
