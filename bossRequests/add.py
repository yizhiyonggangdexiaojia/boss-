import requests
from config import *

data = {
    'sessionId': '',
}

response = requests.post(
    'https://www.zhipin.com/wapi/zpgeek/friend/add.json?securityId=U710MIQzRwxLn-m1IjajhAoE29W1OKIkhKxpNofde1FkR3iAGCSWqyQ3rPC3asi02Djpo0Eer_wPYUUAaHrfMHTQlFj6DAZeezF-SWyaaKHsXLVRthUBSb4JOofM4YBy6QNELc3PdoSG4CrjLtXu2B9_mw2TYdveqeWJZtWl3e77asbrMULY1LcryaQBcw~~&jobId=0f260c2f33e952411XN73dS9EVFZ&lid=731bdb1f-bb25-41ce-bf13-b9c85ba281e6.f1:common.eyJzZXNzaW9uSWQiOiIzNzY3NmY5Ni1kZTQ2LTRiNjEtOGQ2MS02NWMzMjQ1NTY3ZmMiLCJyY2RCelR5cGUiOiJmMV9ncmNkIn0.1',
    cookies=cookies,
    headers=headers,
    data=data,
)
