from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

chrome_opt = Options()      # 创建参数设置对象.
chrome_opt.add_argument('--headless')   # 无界面化.
chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.

# 创建Chrome对象并传入设置信息.
driver = webdriver.Chrome(options=chrome_opt)

# 操作这个对象.
driver.get('https://book.douban.com/link2/?lowest=10110&pre=0&vendor=jingdong&srcpage=subject&price=12800&pos=1&url=https%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIGZRprFQEVBVMSWRcyVlgNRQQlW1dCFFlQCxxKQgFHRE5XDVULR0UVARUFUxJZFx1LQglGa2VxcH8ecCNDZ2xfM3kYZnxTeh4aGUMOHjdSHlwTBRsEUitbEQMWA2UrWxQyRGlVGloUAxMAVR9bJQMiB1ESXB0HEQ9cGlkXByIHXR9rzIKl0feJgouIx4%252FCK2slASI3ZRtrFTJNQwhGaxcDEwVX&cntvendor=3&srcsubj=34978161&type=bkbuy&subject=34978161')     # get方式访问百度.
print(driver.current_url)
url = driver.current_url
match_obj = re.match(r'[a-zA-z]+://[^\s]*[?]', url)
print(match_obj.group()[:-1])
time.sleep(2)
driver.quit()
