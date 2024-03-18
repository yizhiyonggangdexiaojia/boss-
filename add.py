import random
import time

import requests
from config import *


# 存放gpt为你筛选的id
listSecurityId = [
    ""
]

params = {
    'securityId': '',
    'jobId': 'b8a6f6603ad49b711XF92dy6FVZX',
    'lid': '2u1SeMQAIII.search.3',
}

data = {
    'sessionId': '',
}

for securityId in listSecurityId:
    params['securityId'] = securityId
    response = requests.post(
        'https://www.zhipin.com/wapi/zpgeek/friend/add.json',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print("向boss发送：", response.json()['zpData'])
    # 避免发送过快
    time.sleep(1 + random.random() * 1)
