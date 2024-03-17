import random
import time

import requests

cookies = {
    'lastCity': '101250600',
    # '__zp_seo_uuid__': '47f7ac22-0c56-4b21-8ac5-857ceb389706',
    # '__g': '-',
    # '__l': 'r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fchengshi%2Fc101250600%2F&s=1&g=&s=3&friend_source=0',
    # 'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a': '1710406376,1710654480',
    # 'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a': '1710654480',
    # 'wd_guid': '383b7fc3-3f0a-48de-8834-4da09421573b',
    # 'historyState': 'state',
    # '_bl_uid': 'R9ldptLpvUX33ti9FvRzqO6r4g5m',
    # 'gdxidpyhxdE': 'kQ%2Bolpj5zzIX5%2By%2BvgwrIAp8xX%2FY0f9ya64%2FrDWb5jJDNWjBgnLkDzDS5UTN3ewHVIETC86Eu%5CAL%5CGqlaeDbC8ha121tUYsyXk0e76Qoe00cf%2BBcLG6M%2BVOAbvSzg7rp48xX7q5LaK%5CR%2FS6eSf4Agp%2FriGKkmLQAA1EXwIBBpQAN4rmH%3A1710655419194',
    'wt2': 'DlypN27EnyHNIebfhI5G3yhLj6S4-oeQQoOp1YOpITlF72Fllq8hJuVTxlqQcclb54SwmPrNjjmlwvUTDtI06cA~~',
    # 'wbg': '0',
    # 'zp_at': 'QetdgPYsfWsdWhQL3D4Z8DeIrQCu85YS46qS8Xi_5yg~',
    # '__c': '1710654480',
    # '__a': '19622815.1710406376.1710406376.1710654480.4.2.3.4',
    # 'geek_zp_token': 'V1RN0jGeD9215iVtRuzh0eLC6w5TvWxyw~',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://www.zhipin.com/web/geek/job-recommend?ka=open_joblist',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'token': 'ZGBhMov55hIlGcgs',
    # 'traceId': 'EC997741-DFAB-4BBE-A81F-9E430DB58CD1',
    # 'zp_token': 'V1RN0jGeD9215iVtRuzh0eLC6w5TvWxyw~',
}

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

