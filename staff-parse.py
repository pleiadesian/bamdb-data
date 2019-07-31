# !/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
# author: pleiadesian
import json
from urllib.parse import urlencode
import httplib2


newlines = []
with open("./bangumi-staff5.sql") as sqlfile:
    lines = sqlfile.readlines()
    for line in lines:
        line = line.replace("author=", "author=\"")
        line = line.replace(" where", "\" where")
        line = line.replace("\n", ";\n")
        newlines.append(line)
open('./bamdb-staff5.sql', 'w').writelines(newlines)
