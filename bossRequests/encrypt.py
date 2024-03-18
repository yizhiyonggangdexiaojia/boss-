import requests
from config import *

response = requests.get('https://www.zhipin.com/wapi/zpgeek/pc/recommend/expect/list.json',
                        cookies=cookies, headers=headers)
print(response.text)
