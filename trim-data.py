# !/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
# author: pleiadesian
import json
import re

with open("./a.sql") as f:
    line = f.readline()
    relation_set = []
    tag_set = []
    item_set = []
    while line:
        line = f.readline()
        if line.split(' ')[0] == 'INSERT' and line.split(' ')[2] == '`relation`':
            relation_compile = re.compile(r'[(](.*?)[)]', re.S)
            relations = re.findall(relation_compile, line)
            for relation_line in relations:
                columns = relation_line.split(',')
                relation_data = dict()
                relation_data["type"] = columns[1][1:-1]
                relation_data["source"] = columns[2]
                relation_data["target"] = columns[3]
                relation_set.append(relation_data)
        if line.split(' ')[0] == 'INSERT' and line.split(' ')[2] == '`tag`':
            tag_compile = re.compile(r'[(](.*?)[)]', re.S)
            tags = re.findall(tag_compile, line)
            for tag_line in tags:
                columns = tag_line.split(',')
                if len(columns) < 3:
                    continue
                tag_data = dict()
                tag_data["itemId"] = columns[0]
                tag_data["content"] = columns[1][1:-1]
                if '肉' in tag_data["content"] or '里' in tag_data['content'] or '奶' in tag_data['content'] or\
                        '乳' in tag_data['content'] or '色' in tag_data['content'] or '淫' in tag_data['content'] or\
                        '奸' in tag_data['content'] or '裸' in tag_data['content'] or '妹' in tag_data['content'] or\
                        '妻' in tag_data['content'] or '胸' in tag_data['content']:
                    continue
                tag_data["count"] = columns[2]
                tag_set.append(tag_data)
        if line.split(' ')[0] == 'INSERT' and line.split(' ')[2] == '`subject`':
            item_compile = re.compile(r'[(](.*?)[)]', re.S)
            items = re.findall(item_compile, line)
            for item_line in items:
                # problems in info columns
                columns = item_line.split(',')
                item_data = dict()
                item_data["itemId"] = columns[0]
                item_data["title"] = columns[4][1:-1]
                item_data["imgurl"] = columns[2][1:-1]
                item_data["type"] = columns[3][1:-1]
                item_data["info"] = dict()
                info = json.loads(columns[6][-1:1])
                item_data["info"] = info
                item_data["score_details"] = dict()
                for i in range(1, 10):
                    item_data["score_details"][str(i)] = json.loads(columns[7])[str(i)]
                item_data["score_details"]["total"] = columns[7]["total"]
                item_data["avgScore"] = columns[8][1:-1]
                item_data["wishes"] = columns[9]
                item_data["done"] = columns[10]
                item_data["doings"] = columns[11]
                item_data["on_hold"] = columns[12]
                item_data["dropped"] = columns[13]
                item_set.append(item_data)
    json.dump(relation_set, open('./bamgumi-relation.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(tag_set, open('./bamgumi-tag.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(item_set, open('./bamgumi-item.json', 'w'), ensure_ascii=False, indent=1)
