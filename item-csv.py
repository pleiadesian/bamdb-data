import json

data = json.load(open("./bangumi-item.json", 'r'))
items = []
ratings = []

line = ["itemname", "chapter_num", "main_author", "imgurl", "type"]
items.append(",".join(line)+"\n")
rating_line = ["avg_score", "item_id", "rank", "score_1", "score_2", "score_3", "score_4", "score_5", "score_6",
               "score_7", "score_8", "score_9", "score_10", "tot_score_num", "type"]
ratings.append(",".join(rating_line)+"\n")
item_id = 50186
chara = ","
count = 0
for item_in in data:
    line = list()
    line.append("\""+item_in["title"]+"\"")
    # line.append("090701")
    line.append(str(10))
    line.append("\"暂无\"")
    line.append("\""+item_in["imgurl"]+"\"")
    item_type = 0
    if item_in["type"] == "Book":
        item_type = 0
    elif item_in["type"] == "Anime":
        item_type = 2
    elif item_in["type"] == "Music":
        item_type = 4
    elif item_in["type"] == "Game":
        item_type = 5
    elif item_in["type"] == "Real":
        item_type = 3
    else:
        item_type = 6
    line.append(str(item_type))
    line_str = chara.join(line)
    line_str = line_str + "\n"
    items.append(line_str)
    score = list()
    score.append(0)
    score_sum = 0
    for i in range(1, 11):
        score.append(int(item_in["score_details"][str(i)]))
        score_sum += score[i] * i
    avg_score = 0.0
    if int(item_in["score_details"]["total"]) != 0:
        avg_score = score_sum / int(item_in["score_details"]["total"])

    rating_line = list()
    rating_line.append(str(avg_score))
    rating_line.append(str(item_id))
    rating_line.append(str(0))
    for i in range(1, 11):
        rating_line.append(str(score[i]))

    rating_line.append(item_in["score_details"]["total"])
    rating_line.append(str(item_type))
    rating_str = chara.join(rating_line)
    rating_str = rating_str + "\n"
    ratings.append(rating_str)
    item_id += 1
    count += 1
    print(count)
    if count == 111622:
        open("./bangumi-item1.csv", "w").writelines(items)
        open("./bangumi-rating1.csv", "w").writelines(ratings)
        items.clear()
        items.append(",".join(line) + "\n")
        ratings.clear()
        ratings.append(",".join(rating_line) + "\n")
        count = 0
    if count == 111622:
        open("./bangumi-item2.csv", "w").writelines(items)
        open("./bangumi-rating2.csv", "w").writelines(ratings)
        items.clear()
        items.append(",".join(line) + "\n")
        ratings.clear()
        ratings.append(",".join(rating_line) + "\n")
        count = 0
open("./bangumi-item3.csv", "w").writelines(items)
open("./bangumi-rating3.csv", "w").writelines(ratings)