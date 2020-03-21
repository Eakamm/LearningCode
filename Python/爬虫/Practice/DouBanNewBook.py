'''
@Author: your name
@Date: 2020-02-16 15:48:37
@LastEditTime: 2020-02-16 15:52:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\爬虫\Practice\ChinaUniversity.py
'''
import requests
from bs4 import BeautifulSoup
import bs4
import re
import json


def get_html(url):
    try:
        user_agent = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        r = requests.get(
            'https://book.douban.com/latest?icn=index-latestbook-all',
            headers=user_agent)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('连接失败！')


def analysis_html(content, data):
    soup = BeautifulSoup(content, 'html.parser')
    tag = soup.find_all('ul', 'cover-col-4 clearfix')
    item = tag[0]
    # 正则表达式，匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
    pattern = re.compile(r'\S+[\s]*\S+')
    for li in item.children:
        book = {}
        # 确保其为bs4.element.Tag标签类型
        if type(li) == bs4.element.Tag:
            # 循环获取每个标签
            for p in li.div.children:
                # 通过名字判断获取p标签
                if p.name == 'p':
                    if p['class'][0] == 'rating':
                        for span in p.strings:
                            matchObj = pattern.search(span)
                            if matchObj is not None:
                                book['rate'] = matchObj.group()
                    elif p['class'][0] == 'color-gray':
                        # 正则表达式，以 / 分割字符串
                        Obj = re.split('[/]', p.string)
                        matchObj = pattern.search(Obj[0])
                        book['author'] = matchObj.group()
                        matchObj = pattern.search(Obj[1])
                        book['publish'] = matchObj.group()
                        matchObj = pattern.search(Obj[2])
                        book['date'] = matchObj.group()
                    elif p['class'][0] == 'detail':
                        matchObj = pattern.search(p.string)
                        book['detail'] = matchObj.group()
                # 通过名字判断获取h2标签
                elif p.name == 'h2':
                    book['title'] = p.a.string
            data.append(book)


def store_data(data):
    try:
        with open('DouBanNewBook.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
    except FileNotFoundError:
        print('文件写入失败！')


def main():
    data = []
    url = 'https://book.douban.com/latest?icn=index-latestbook-all'
    content = get_html(url)
    analysis_html(content, data)
    store_data(data)


main()
