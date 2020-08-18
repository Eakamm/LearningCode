import json
from bs4 import BeautifulSoup
import bs4
import re
from selenium import webdriver
import scrapy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, DateTime, Float
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class BookType(Base):
    # 表名
    __tablename__ = "book_type"

    id = Column(Integer, primary_key=True)
    type = Column(String)


class TypeList(scrapy.Spider):
    name = 'typeList'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
        # sqlalchemy连接数据库
        engine = create_engine("mysql+pymysql://root:1996111Lzh.@localhost:3306/ry")
        # # 把当前的引擎绑定给这个会话
        Session = sessionmaker(bind=engine)
        # 创建Session实例
        self.session = Session()

    def start_requests(self):
        urls = [
            "https://book.douban.com/tag/?view=cloud"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        tag = soup.find('table', 'tagCol')
        for item in tag.find_all('td'):
            bookType = BookType(type=item.a.string)
            # 添加一条数据
            self.session.add(bookType)
            print('爬虫结束了了')
        # 提交事务
        self.session.commit()
        # 关闭session
        self.session.close()
