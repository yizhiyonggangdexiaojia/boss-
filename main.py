import random
import time
import json
from config import *

import requests
import queue

# 获取encryptId
with open("bossRequests/data/encryptExpectId.json", "r", encoding="utf-8") as f:
    encryptExpectId = json.loads(f.read())

listTxtFile = open("data/list.txt", "w", encoding="utf-8")

encryptId = encryptExpectId["zpData"]["expectList"][0]["encryptId"]
securityIdQueue = queue.Queue()


def getDetail(securityId):
    time.sleep(0.7 + random.random() * 0.5)
    params = {
        'securityId': securityId,
        'lid': '2XMHfiFUWfz.search.2',
    }
    response = requests.get('https://www.zhipin.com/wapi/zpgeek/job/detail.json', params=params,
                            cookies=cookies, headers=headers)
    with open("data/json/" + securityId+".json", "w", encoding="utf-8") as file:
        file.write(response.text)


def main():
    params = {
        'city': '',
        'experience': '',
        'payType': '',
        'partTime': '',
        'degree': '',
        'industry': '',
        'scale': '',
        'salary': '',
        'jobType': '',
        'encryptExpectId': encryptId,
        'mixExpectType': '',
        'page': '1',
        'pageSize': '15',
    }
    for i in range(50):
        data = []
        params["page"] = str(i + 1)
        response = requests.get(
            'https://www.zhipin.com/wapi/zpgeek/pc/recommend/job/list.json',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        if not response.json()['zpData']['jobList']:
            break
        for item in response.json()['zpData']['jobList']:
            data.append(item)
            print(item)
            securityId = item["securityId"]
            # securityIdQueue.put(securityId)
            getDetail(securityId)
        listTxtFile.write(json.dumps(data))
        listTxtFile.write("\n")
        time.sleep(1 + random.random() * 1)


if __name__ == '__main__':
    main()
