import random
import time

import requests
from config import *

listSecurityId = [
    "4wJO8sDqOWAta-819FDMllyT25RL3YC6QyYrnr-h8GqprJGiVCnC-s9oG3HdHA6YznI-DK68stOGyOJKeKAgVGHr-HkUkt4MDh2bJ9ew7KdyiTAaXKjbpXNv"
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
    print("向boss发送：", response.json()['zpData']['greeting'])
    # 避免发送过快
    time.sleep(1 + random.random() * 1)
