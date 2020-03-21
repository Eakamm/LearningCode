import requests
from bs4 import BeautifulSoup
import bs4
import re
import json


def get_html(url, cookie):
    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }
        if cookie != '':
            headers['Cookie'] = cookie

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except requests.HTTPError:
        print("连接失败！")


def analysis_html(content, data, details_url, cookie):
    company_list = []
    # 获取每个公司信息
    lists = json.loads(content)['data']['diff']
    # 获取股票代码
    for company in lists:
        company_list.append(company['f12'])
    for i in company_list:
        details = get_html(details_url+i, cookie)
        print(details)

    return data


def store_data(data):

    return 1


def main():
    data = []
    # f2最新价，f15最高,f16最低,f17开盘，f12编号,f14名称，f20市值
    list_url = 'http://74.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:MK0201&fields=f2,f12,f14,f15,f16,f17,f18,f20'
    details_url = 'https://www.laohu8.com/proxy/stock/stock_info/detail/'
    cookie = ''
    content = get_html(list_url, cookie)
    print(content)
    cookie = '_ga=GA1.2.1943244652.1577857023; verification="2|1:0|10:1582213537|12:verification|88:ZjYxYTIxMTYwZTk3YWM5YTE2ZmM2NTIwY2M4NTYzMjg4ODAzMzZjN2NmMzRiOGE2OTIwZTRjNjEyM2ZkMjRlOA==|2e6b83e2f962472d59d3d8b6b80e8a60baff88c5f9c4c7b20a2da2523b38c43e"; session_id="2|1:0|10:1582213537|10:session_id|88:NTE0ZTQ1OTVkMTZhZGQ0NDkzYjNiOTQ3NTJjZDJmZDljMmQ1MTNhNzlhOTc2M2MzZmIwNWE0MDAxNmIwYTdiOQ==|2984782b89f8d0b2cd2b268675af819ce5d244cdc5bec6a1bcd5015d6607ba39"; Hm_lvt_aec1ec63a0f76f572b0928df8b4b8211=1582213538; _gid=GA1.2.1310264833.1582540905; ngxid=rBFdQF5V6lkobyh+BSN2Ag==; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2210000000000000001%22%2C%22%24device_id%22%3A%2216f5f9b7d9a46d-0fcbbd0420cae3-6701b35-1327104-16f5f9b7d9c631%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22aladingpc%22%7D%2C%22first_id%22%3A%2216f5f9b7d9a46d-0fcbbd0420cae3-6701b35-1327104-16f5f9b7d9c631%22%7D; JSESSIONID=0261BE4CA1ACDFC022754D1B2D0D50E3'
    analysis_html(content, data, details_url, cookie)

main()
