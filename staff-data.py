# !/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
# author: pleiadesian
import json
from urllib.parse import urlencode
import httplib2

staffs = []
output = []
data = json.load(open("./bangumi-item.json", 'r'))
i = 50186
for item_in in data:
    if i < 130000:
        i += 1
        continue
    if i == 140000:
        break
    h = httplib2.Http(".cache")
    resp, content = h.request("http://mirror.api.bgm.rin.cat/subject/"+str(item_in["itemId"]) +
                              "?responseGroup=medium", "GET")
    item_info = dict()
    staff = "暂无"
    if resp.status == 200:
        item_info = json.loads(content)
        item_info["itemId"] = item_in["itemId"]
        if item_info["staff"] is None:
            staff = "暂无"
        else:
            staff = item_info["staff"][0]["name_cn"]
            if staff == "" or staff is None:
                staff = item_info["staff"][0]["name"]
    sql_line = "update bamdb.item set main_author=" + staff + " where id=" + str(i) + "\n"
    staffs.append(sql_line)
    i += 1
    print(i)
open('./bangumi-staff.sql', 'w').writelines(staffs)
