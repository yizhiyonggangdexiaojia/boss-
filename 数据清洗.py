# 把数据变成指定格式，然后转换成为一个csv格式，交给gpt，然后让它把这些数据变成简历的描述
import json

ans = []

listTxt = open("data/list.txt", encoding="utf-8").read()

for itemStr in listTxt.split("\n"):
    item = json.dumps(itemStr)
    print(item)

