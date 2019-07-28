# !/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
# author: pleiadesian
import json
from urllib.parse import urlencode
import httplib2

output = []
data = json.load(open("./response.json", 'r'))
item_data = data["items"]
for item_in in item_data:
    item_out = dict()  # {"itemname": "", "pubTime": "", "chapterNum": 0, "mainAuthor": "", "type": 2}
    if "titleTranslate" in item_in and "zh-Hans" in item_in["titleTranslate"]:
        item_out["itemname"] = item_in["titleTranslate"]["zh-Hans"][0]
    else:
        item_out["itemname"] = item_in["title"]
    if int(item_in["begin"][0:3]) >= 1970:
        item_out["pubTime"] = item_in["begin"]
    item_out["chapterNum"] = 10
    item_out["mainAuthor"] = "暂无"
    if item_in["type"] == "tv":
        item_out["type"] = 2
    else:
        item_out["type"] = 1
    output.append(item_out)
    req = json.dumps(item_out).encode('utf-8')
    h = httplib2.Http(".cache")
    resp, content = h.request("http://202.120.40.8:30741/item/add",
                              "POST", body=req,
                              headers={"Authorization": "Bearer 176786e5-3ed3-4a7e-8b84-058a0de17996",
                                       "Content-Type": "application/json"})
    print(resp)
json.dump(output, open('./output.json', 'w'), ensure_ascii=False, indent=1)
