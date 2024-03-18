# 把数据变成指定格式，然后转换成为一个csv格式，交给gpt，然后让它把这些数据变成简历的描述
import csv
import json

ans = []

listTxt = open("data/list.txt", encoding="utf-8").read()


def detail(securityId):
    with open("data/json/" + securityId + ".json", "r", encoding="utf-8") as f:
        data = f.read()
    data = json.loads(data)
    return data


typeBase = {
    "标题": "",
    "类别": "",
    "薪资": "",
    "职责": "",
    "地址": "",
    "地区": "",
    "工作时间": "",
    "学历": "",
    "职位描述": [],
    "id": ""
}

for arrStr in listTxt.split("\n"):
    if not arrStr:
        continue
    arrItem = json.loads(arrStr)
    for father in arrItem:
        baseList = {
            "标题": "",
            "类别": "",
            "薪资": "",
            "职责": "",
            "地址": "",
            "地区": "",
            "工作时间": "",
            "学历": "",
            "职位描述": [],
            "id": ""
        }
        raw = detail(father["securityId"])
        item = raw["zpData"]["jobInfo"]
        baseList["id"] = raw["zpData"]["securityId"]
        baseList["标题"] = item["jobName"]
        baseList["类别"] = item["positionName"]
        baseList["薪资"] = item["salaryDesc"]
        baseList["职责"] = item["postDescription"]
        baseList["地址"] = item["address"]
        baseList["地区"] = item["locationName"]
        baseList["工作时间"] = item["experienceName"]
        baseList["学历"] = item["degreeName"]
        baseList["职位描述"] = item["showSkills"]
        print(baseList)
        ans.append(baseList)

with open("data/ans.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(ans, ensure_ascii=False))

print("总数：", len(ans))

# 把ans整合成为csv
with open("data/ans.json", "r", encoding="utf-8") as f:
    ans = json.loads(f.read())

# 不新增
fileCsv = open("data/ans.csv", "w", encoding="utf-8", newline="")
fileWriter = csv.writer(fileCsv)

fileWriter.writerow(typeBase.keys())
for item in ans:
    fileWriter.writerow(item.values())

fileCsv.close()
