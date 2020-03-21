import requests
from bs4 import BeautifulSoup
import bs4
import re
import json


def get_html(url, page):
    try:
        user_agent = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'cookie': '__jdu=1011833842; shshshfpb=lDIayCxebqXuWeDz6d3u9fQ%3D%3D; shshshfpa=lDIayCxebqXuWeDz6d3u9fQ%3D%3D; unpl=V2_ZzNtbUoFQEYmD0RTfh1bDWJUQFwSVRNFcQAUVn8RXQE0ABRbclRCFnQUR1dnGV8UZwIZX0tcQBNFCEdkex1dAWMzIm1BV3McRQhHVHsQXgduBhFtclBzFXYJRFR9EFQ1voOli%2bDFmov%2f3c7DSx5ZAmEEG15FZ0IldDgUOqOv6t3Csg6J6NiWneJFRlV7GVUHZQoXXnJWcxY%3d; mt_xid=V2_52007VwMTUl1RUFgWTBpsUGJRFVcJC1FGHBkYWBliVxAHQVEGCBxVSVoFNApCAl9QVFkXeRpdBmYfE1FBWFFLH0gSXgxsARFiX2hRahtKH1wAYDMSVlw%3D; PCSYCityID=CN_150000_0_0; TrackID=16ssN_36ImQ3yGKAMO7qpr5PMr1NQFB5tlzcjh2aKOhBEp8pbRaqS849hFEITtIYRa5b7ATS2WWpWPfJCt3Tl0SyxfOws6WQzhUvZFvmNPD4; pinId=QHSQegFCzNp-eKPli7afpLV9-x-f3wj7; pin=jd_586a87176323c; unick=%E4%BB%BF%E4%BD%9B%E6%98%AF%E4%B8%80%E6%9D%A1%E5%92%B8%E9%B1%BC%E5%95%8A; _tp=vQ6Dme8BFfoKS7rjjsz5MOP0wC5OBKmvS%2BRf3sDJuek%3D; _pst=jd_586a87176323c; user-key=dd6ab02e-3221-4e51-bbe5-c27934d181e7; cn=64; __jdv=122270672|baidu|-|organic|not set|1582167255164; areaId=11; ipLoc-djd=11-799-32653-0; shshshfp=97011bb11899ecd1ae9c3fd141042c8e; shshshsID=42959e5163a64b830a7f8eb6d8298084_1_1582380059389; __jda=122270672.1011833842.1569738280.1582167255.1582380056.12; __jdc=122270672; listck=95c3b270a64dc10b5af0cd06f3a2b442; _gcl_au=1.1.1435555317.1582380079; 3AB9D23F7A4B3C9B=IWVEEG3DKGO6LOSSIZ7N2Y77RVNDRBGQEUQW7VZAFH3O5G6HV77SHPIXLWB3RFIYRT2WQMQDJ4EMZOBA6F2JZVDCV4; __jdb=122270672.6.1011833842|12.1582380056'
        }
        if page > 1:
            url += '&page='+str(page)
        r = requests.get(
            url,
            headers=user_agent)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('连接失败！')


def analysis_html(content, data):
    soup = BeautifulSoup(content, 'html.parser')
    tag = soup.find_all('li', 'gl-item')
    for t in tag:
        phone = {}
        phone['Id'] = t.div.attrs['data-sku']
        phone['name'] = t.find_all('div', 'p-name')[0].a.em.string
        data.append(phone)
        # print(type(t))
    # item = tag[0]
    # data.append(book)


def store_data(data):
    try:
        with open('DouBanNewBook.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
    except FileNotFoundError:
        print('文件写入失败！')


def main():
    data = []
    url = 'https://list.jd.com/list.html?cat=9987,653,655'
    page = 1
    content = get_html(url, page)
    # print(content)
    analysis_html(content, data)
    print(data)
    # store_data(data)


main()
