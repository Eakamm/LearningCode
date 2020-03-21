import json

import scrapy


class Demo(scrapy.Spider):
    name = "demo"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.company_list = []
        self.details_list = []

    def start_requests(self):
        # 需要爬取的页面
        urls = [
            'http://74.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:MK0201&fields=f2,f12,f14,f15,f16,f17,f18,f20',
            'https://www.laohu8.com/proxy/stock/stock_info/detail/'
        ]

        for url in urls:
            print(url)
            if 'laohu' in url:
                print(self.company_list)
                for i in self.company_list:
                    print(i)
                    yield scrapy.Request(url=url+i, callback=self.parse)
            else:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if 'push2' in response.request.url:
            lists = json.loads(response.text)['data']['diff']
            for company in lists:
                self.company_list.append(company['f12'])
        else:
            print(response.text)

