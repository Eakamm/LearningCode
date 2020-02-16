import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.baidu.com")
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')

#
print(soup.find_all('p'))
print(soup.find_all(id = 'lh'))
