import scrapy


class SelectCss(scrapy.Spider):
    name = 'CssDemo'

    def start_requests(self):
        urls = {
            'http://lab.scrapyd.cn'
        }

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.css('title'))
