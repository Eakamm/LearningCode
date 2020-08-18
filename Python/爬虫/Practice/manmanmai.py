#!coding=utf-8
import requests
import json
import datetime
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings()

def raw(text):  # 转化URL字符串

    escape_dict = {
        '/': '%252F',
        '?': '%253F',
        '=': '%253D',
        ':': '%253A',
        '&': '%26',

    }
    new_string = ''
    for char in text:
        try:
            new_string += escape_dict[char]
        except KeyError:
            new_string += char
    return new_string


def mmm(item):
    item = raw(item)
    url = 'https://apapia.manmanbuy.com/ChromeWidgetServices/WidgetServices.ashx'
    s = requests.session()
    headers = {
        'Host': 'apapia.manmanbuy.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Proxy-Connection': 'close',
        'Cookie': 'ASP.NET_SessionId=uwhkmhd023ce0yx22jag2e0o; jjkcpnew111=cp46144734_1171363291_2017/11/25',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 mmbWebBrowse',
        'Content-Length': '457',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
    }
    postdata = 'c_devid=2C5039AF-99D0-4800-BC36-DEB3654D202C&username=&qs=true&c_engver=1.2.35&c_devtoken=&c_devmodel=iPhone%20SE&c_contype=wifi&' \
               't=1537348981671&c_win=w_320_h_568&p_url={}&' \
               'c_ostype=ios&jsoncallback=%3F&c_ctrl=w_search_trend0_f_content&methodName=getBiJiaInfo_wxsmall&c_devtype=phone&' \
               'jgzspic=no&c_operator=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&c_appver=2.9.0&bj=false&c_dp=2&c_osver=10.3.3'.format(
        item)
    s.headers.update(headers)
    req = s.get(url=url, data=postdata, verify=False).text

    # print(req)
    try:
        js = json.loads(req)
        title = js['single']['title']  ##名称
    except Exception as e:
        print(e)
        # exit(mmm(item))
    ###数据清洗
    pic = js['single']['smallpic']  ##图片
    jiagequshi = js['single']['jiagequshi']  ##价格趋势
    lowerPrice = js['single']['lowerPrice']  ##最低价格
    lowerDate = js['single']['lowerDate']  ##最低价格日期
    lowerDate = re.search('[1-9]\d{0,9}', lowerDate).group(0)
    # print(lowerDate)
    lowerDate = time.strftime("%Y-%m-%d", time.localtime(int(lowerDate)))
    itemurl = js['single']['url']  ##商品链接
    qushi = js['single']['qushi']  ##趋势
    changPriceRemark = js['single']['changPriceRemark']  ##趋势变动
    date_list = []  ##日期
    price_list = []  ##价格
    ##日期转换
    datalist=jiagequshi.replace('[Date.UTC(','').replace(')','').replace(']','').split(',')
    for i in range(0, len(datalist), 5):

        if i != 0:
            day = int(datalist[i + 2])
            if int(datalist[i + 1]) == 12:
                mon = 1
                year = int(datalist[i]) + 1
            else:
                mon = int(datalist[i + 1]) + 1
                year = int(datalist[i])
            date = datetime.date(year=year, month=mon, day=day)
            date = date - datetime.timedelta(days=1)
            price = float(datalist[i + 3])
            date_list.append(date)
            price_list.append(price)

        day = int(datalist[i + 2])
        if int(datalist[i + 1]) == 12:
            mon = 1
            year = int(datalist[i]) + 1
        else:
            mon = int(datalist[i + 1]) + 1
            year = int(datalist[i])

        date = datetime.date(year=year, month=mon, day=day)
        price = float(datalist[i + 3])
        date_list.append(date)
        price_list.append(price)

    data = {'date_日期': date_list, 'price_价格': price_list}
    df = pd.DataFrame(data)
    # df.loc[:, "title_名称"] = title
    # df.loc[:, "pic_图片"] = pic
    # df.loc[:, "lowerPrice_最低价格"] = lowerPrice
    # df.loc[:, "lowerDate_最低价格日期"] = lowerDate
    # df.loc[:, "itemurl_商品链接"] = itemurl
    # df.loc[:, "qushi_趋势"] = qushi
    # df.loc[:, "changPriceRemark_趋势变动"] = changPriceRemark

    df.to_csv('out.csv', index=False, mode='a', encoding="GB18030")  ##保存数据
    print(df)
    # return df


if __name__ == '__main__':
    # 无界面运行
    chrome_opt = Options()  # 创建参数设置对象.
    chrome_opt.add_argument('--headless')  # 无界面化.
    chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
    chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.

    # # 创建Chrome对象并传入设置信息.
    driver = webdriver.Chrome(options=chrome_opt)

    driver.get('https://book.douban.com/link2/?lowest=1380&pre=0&vendor=dangdang&srcpage=subject&price=1930&pos=1&url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s4913064%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D25137790&cntvendor=4&srcsubj=4913064&type=bkbuy&subject=4913064')
    url = driver.current_url
    match_obj = re.match(r'[a-zA-z]+://[^\s]*[?]', url)
    jd_url = match_obj.group(0)[:-1]
    # item = 'https://re.jd.com/cps/item/12637833.html'  ##京东、淘宝、天猫等电商平台数据都可以获取
    mmm(jd_url)

    driver.quit()
