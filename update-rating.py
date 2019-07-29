import httplib2
import json

h = httplib2.Http(".cache")
for i in range(18227, 50180):
    resp1, content1 = h.request("http://202.120.40.8:30741/item/id/" + str(i), "GET")
    if json.loads(content1)["itemname"] == "":
        continue
    resp, content = h.request("http://202.120.40.8:30741/rating/add/itemid/"+str(i), "POST",
                              headers={"Authorization": "Bearer 1f2e047c-03b5-4c5f-a637-293f2dca9f20",
                                       "Content-Type": "application/json"})
