# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, DateTime, Float
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Book(Base):
    # 表名
    __tablename__ = "copy_book"

    id = Column(Integer, primary_key=True)
    # day = Column(String)
    # count = Column(Integer)
    image_url = Column(String)
    title = Column(String)
    rate = Column(String)
    original_name = Column(String)
    translator = Column(String)
    author = Column(String)
    publisher = Column(String)
    publish_time = Column(String)
    descripe = Column(String)
    original_price = Column(Float)
    # now_price= Column(float)
    ISBN = Column(String)
    # type = Column(String)
    # clicks = Column(Integer)
    dou_ban_url = Column(String)
    jd_url = Column(String)
    CommitNumbers = Column(Integer)


class JingdongPipeline(object):

    def __init__(self):
        # 二进制方法打开文件
        # self.f = open('DouBanNewBook.json', 'wb')
        # self.exporter = JsonItemExporter(self.f, ensure_ascii=False, encoding='utf-8')
        # self.exporter.start_exporting()

        # pymysql数据库配置
        # self.db = pymysql.Connect(
        #     host="localhost",
        #     port="3306",
        #     user="root",
        #     password="1996111Lzh.",
        #     db="ry",
        #     chaarset="utf-8"
        # )

        # sqlalchemy连接数据库
        self.engine = create_engine("mysql+pymysql://root:1996111Lzh.@localhost:3306/ry")
        # # 把当前的引擎绑定给这个会话
        # Session = sessionmaker(bind=engine)
        # # 创建Session实例
        # self.session = Session()

        # chrome_opt = Options()  # 创建参数设置对象.
        # chrome_opt.add_argument('--headless')  # 无界面化.
        # chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
        # chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.
        #
        # # 创建Chrome对象并传入设置信息.
        # self.driver = webdriver.Chrome()

    def open_spider(self, spilder):

        print('爬虫开始了')
        pass

    def process_item(self, item, spider):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        # self.exporter.export_item(item)
        book = Book(
                    image_url=item['image_url'],
                    title=item['title'],
                    rate=item['rate'],
                    original_name=item['original_name'],
                    author=item['author'],
                    publisher=item['publisher'],
                    publish_time=item['publish_time'],
                    original_price=item['original_price'],
                    descripe=item['descripe'],
                    ISBN=item['ISBN'],
                    dou_ban_url=item['dou_ban_url'],
                    translator=item['translator'],
                    jd_url=item['jd_url'],
                    CommitNumbers=item['CommitNumbers']
                    )
        # 添加一条数据
        # self.session.add(book)
        # self.session.commit()

        book2 = session.query(Book).filter_by(ISBN=book.ISBN).first()

        if book2:
            pass
        else:
            session.add(book)
            session.commit()
        session.close()
        return item

    def close_spider(self, spider):
        print('爬虫结束了了')

        # 关闭session
        # session.close()

        # self.exporter.finish_exporting()
        # self.f.close()
