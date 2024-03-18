import random
import time
from config import *
import requests


params = {
    'city': '',
    'experience': '',
    'payType': '',
    'partTime': '',
    'degree': '',
    'industry': '',
    'scale': '',
    'salary': '',
    'jobType': '1902',
    'encryptExpectId': '414ad8fe5d55766133N_29-_ElBZ',
    'mixExpectType': '',
    'page': '1',
    'pageSize': '15',
}

for i in range(10):
    params["page"] = str(i+1)
    response = requests.get(
        'https://www.zhipin.com/wapi/zpgeek/pc/recommend/job/list.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response.text)
    time.sleep(1 + random.random() * 2)
    break

# 地点，工资，描述，要求，工作名称

