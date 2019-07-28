import httplib2

h = httplib2.Http(".cache")
for i in range(30, 4656):
    resp, content = h.request("http://202.120.40.8:30741/rating/add/itemid/"+str(i), "POST",
                              headers={"Authorization": "Bearer 176786e5-3ed3-4a7e-8b84-058a0de17996",
                                       "Content-Type": "application/json"})
