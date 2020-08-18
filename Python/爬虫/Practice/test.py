from bs4 import BeautifulSoup
import bs4
import re
import json

user_agent = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

r = requests.get(
    'https://book.douban.com/subject/1068920/',
    headers=user_agent)
r.raise_for_status()
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
buy = soup.find('div', id='buyinfo-printed').ul

for li in buy.find_all('li'):
    if pattern.search(li['data-track']):
         print(li.a['href'])
         break
