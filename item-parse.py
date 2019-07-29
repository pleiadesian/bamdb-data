# !/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
# author: pleiadesian
import json
from urllib.parse import urlencode
import httplib2

output = []
data = json.load(open("./bangumi-item.json", 'r'))
for item_in in data:
    item_out = dict()  # {"itemname": "", "pubTime": "", "chapterNum": 0, "mainAuthor": "", "type": 2}
    item_out["itemname"] = item_in["title"]
    item_out["pubTime"] = "2009-07-01T00:00:00.000+0000"
    item_out["chapterNum"] = 10
    item_out["mainAuthor"] = "暂无"
    if item_in["type"] == "Book":
        item_out["type"] = 0
    elif item_in["type"] == "Anime":
        item_out["type"] = 2
    elif item_in["type"] == "Music":
        item_out["type"] = 4
    elif item_in["type"] == "Game":
        item_out["type"] = 5
    elif item_in["type"] == "Real":
        item_out["type"] = 3
    else:
        item_out["type"] = 6
    output.append(item_out)
    req = json.dumps(item_out).encode('utf-8')
    h = httplib2.Http(".cache")
    resp, content = h.request("http://202.120.40.8:30741/item/add",
                              "POST", body=req,
                              headers={"Authorization": "Bearer efd8fe7f-a5b3-48a3-b57d-21507b028167",
                                       "Content-Type": "application/json"})
    print(content)
json.dump(output, open('./item-output.json', 'w'), ensure_ascii=False, indent=1)
