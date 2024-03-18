import requests
from config import *

# 这个有
params = {
    'securityId': 'VCCzhcnDoYlYK-p11H9uez2rgeELL3tbYrGy9p9SlhJtbCxG_SEBSi3W_bKzpSwEvy4j3YwhUtleNBCAVHPkGUuv3g8WK5aSAhMQcxthw4itZbSdscLYk69p6DlgWIK2G-OKaHoaP8JC3Rh1lSv4W4z5aygW5Qrs3hCWapnZJsyRXK_qs12iJ7eWQ5Iu054~',
    'lid': '2XMHfiFUWfz.search.2',
}

response = requests.get('https://www.zhipin.com/wapi/zpgeek/job/detail.json', params=params, cookies=cookies, headers=headers)
print(response.text)
