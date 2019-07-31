# !/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
# author: pleiadesian
import json
from urllib.parse import urlencode
import httplib2


newlines = []
for i in range(5, 16):
    with open("./bangumi-staff"+str(i)+".sql") as sqlfile:
        lines = sqlfile.readlines()
        for line in lines:
            line = line.replace("author=", "author=\"")
            line = line.replace(" where", "\" where")
            line = line.replace("\n", ";\n")
            newlines.append(line)
open('./bamdb-staff.sql', 'w').writelines(newlines)
