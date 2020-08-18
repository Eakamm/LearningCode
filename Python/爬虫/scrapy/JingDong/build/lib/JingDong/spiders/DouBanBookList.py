import json
from bs4 import BeautifulSoup
import bs4
import re
import scrapy


class DouBanBookList(scrapy.Spider):
    name = 'bookList'

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.count = 0
        # 判断是否为京东链接的正则
        self.pattern = re.compile(r'(jingdong)')

    def start_requests(self):
        urls = [
            "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4"
            # "https://book.douban.com/subject/34978161"
        ]

        for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse_details)
            yield scrapy.Request(url=url, callback=self.parse)

    # 书籍列表
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        tag = soup.find_all('ul', 'subject-list')
        item = tag[0]
        for li in item.children:
            # 确保其为bs4.element.Tag标签类型
            if type(li) == bs4.element.Tag:
                try:
                    info = li.find_all('div', 'info')[0]
                    yield scrapy.Request(url=info.h2.a['href'], callback=self.parse_details)
                except IndexError or AttributeError:
                    print('待解决')
        # 翻页
        # 翻几页
        i = 5
        # 起始位置
        count = 20
        while i >= 0:
            next_page = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=" + str(count)
            yield scrapy.Request(url=next_page, callback=self.parse)
            count += 20
            i -= 1
        # self.driver.quit()

    # 书籍详情分析
    def parse_details(self, response):
        book = {
            'image_url': None,
            'title': None,
            'rate': None,
            'original_name': None,
            'translator': None,
            'author': None,
            'publisher': None,
            'publish_time': None,
            'descripe': '',
            'original_price': None,
            'ISBN': None,
            'dou_ban_url': None,
            'jd_url': None
        }
        soup = BeautifulSoup(response.text, 'html.parser')
        # 书籍信息
        details = soup.find('div', 'indent')
        # 购买信息
        buy = soup.find('div', id='buyinfo-printed').ul

        book['title'] = soup.h1.span.string
        book['rate'] = details.find('strong', "ll rating_num").string.strip()
        book['image_url'] = details.find('a', 'nbg')['href']

        # 获取描述
        for string in soup.find('div', 'intro').stripped_strings:
            if string is not None:
                book['descripe'] = book['descripe'] + string
        # 获取豆瓣地址
        book['dou_ban_url'] = response.url

        # 获取京东地址
        for li in buy.find_all('li'):
            if self.pattern.search(li['data-track']):
                book['jd_url'] = li.a['href']
                break


        info = details.find('div', id='info')
        # 找到该div下的所有span标签
        info_tag_lists = info.find_all('span')
        for item in info_tag_lists:
            if item.span is not None:
                if item.span.string.strip() == '作者':
                    book['author'] = item.a.string.strip()
                elif item.span.string.strip() == '译者':
                    book['translator'] = item.a.string.strip()
            else:
                if item.string.strip() == '出版社:':
                    book['publisher'] = item.next_sibling.strip()
                elif item.string.strip() == '原作名:':
                    book['original_name'] = item.next_sibling.strip()
                elif item.string.strip() == '出版年:':
                    book['publish_time'] = item.next_sibling.strip()
                elif item.string.strip() == '定价:':
                    book['original_price'] = float(item.next_sibling.strip()[:-1])
                elif item.string.strip() == 'ISBN:':
                    book['ISBN'] = item.next_sibling.strip()
                elif item.string.strip() == '作者:':
                    book['author'] = info.a.string.strip()
                # elif item.string.strip() == '译者:':
                #     book['translator'] = item.next_sibling.strip()
        yield book




