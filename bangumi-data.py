# !/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
# author: pleiadesian
import json
from urllib.parse import urlencode
import httplib2

users = []

for i in range(177, 10000):
    for uid in range(100*(i-1), 100*i-1):
        h = httplib2.Http(".cache")
        resp, content = h.request("http://mirror.api.bgm.rin.cat/user/"+str(uid) +
                                  "/collections/book?app_id=bgm11135d144bf87cda7", "GET")
        resp1, content1 = h.request("http://mirror.api.bgm.rin.cat/user/"+str(uid) +
                                    "/collections/anime?app_id=bgm11135d144bf87cda7", "GET")
        resp2, content2 = h.request("http://mirror.api.bgm.rin.cat/user/"+str(uid) +
                                    "/collections/music?app_id=bgm11135d144bf87cda7", "GET")
        resp3, content3 = h.request("http://mirror.api.bgm.rin.cat/user/"+str(uid) +
                                    "/collections/game?app_id=bgm11135d144bf87cda7", "GET")
        resp4, content4 = h.request("http://mirror.api.bgm.rin.cat/user/"+str(uid) +
                                    "/collections/real?app_id=bgm11135d144bf87cda7", "GET")
        user_info = dict()
        user_info["uid"] = uid
        if resp.status == 200:
            user_info["book"] = json.loads(content)
        if resp1.status == 200:
            user_info["anime"] = json.loads(content1)
        if resp2.status == 200:
            user_info["music"] = json.loads(content2)
        if resp3.status == 200:
            user_info["game"] = json.loads(content3)
        if resp4.status == 200:
            user_info["real"] = json.loads(content4)
        if "book" in user_info and "anime" in user_info and "music" in user_info and "game" in user_info and\
                "real" in user_info and user_info["book"] is None and user_info["anime"] is None and\
                user_info["music"] is None and user_info["game"] is None and user_info["real"] is None:
            continue
        users.append(user_info)
        print(str(uid)+"\n")
    json.dump(users, open('./bangumi5.json', 'w'), ensure_ascii=False, indent=1)
