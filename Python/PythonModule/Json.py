'''
@Author: your name
@Date: 2020-02-17 10:31:01
@LastEditTime: 2020-02-17 10:31:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\PythonModule\Json.py
'''
import json

data = [{
    'title': '小行星掉在下午',
    'rate': '8.0',
    'author': '沈大成',
    'detail': '沈大成短篇小说集，一个异质而又有其自身逻辑的世界。'
}, {
    'title': '卢浮地宫',
    'rate': '8.9',
    'author': '[法]马克-安托万·马修',
    'detail': '一位名字古怪的鉴定专家受聘来到神秘的“完结博物馆”，从事一份严肃的不定期工作：统计数不胜数的藏品，丈量无穷无尽的走廊。'
}]

str = json.dumps(data)

py = json.loads(str)

with open('PythonModule/file/test.json', 'w', encoding='utf-8') as f:
    # json的默认写入中文是以ascii的形式，所以在写入的时候指定ensure_ascii=False
    json.dump(data, f, ensure_ascii=False)

# print(str)
