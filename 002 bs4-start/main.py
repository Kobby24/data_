from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
file_data = response.text

soup = BeautifulSoup(file_data, "lxml")
title = soup.findAll(name="span", class_="titleline")
title_text = []
title_link = []
title_rank = []
for t in title:
    title_text.append(t.find(name="a").getText())
    title_link.append(t.find(name="a").get("href"))

title_ranks = soup.findAll(name="span", class_="score")
for r in title_ranks:
    title_rank.append(r.getText())

split_ = [int(i.split(" ")[0]) for i in title_rank]

max_index = split_.index(max(split_))
print(title_text[max_index])
print(title_link[max_index])

#
# with open("website.html",encoding="utf8") as web_doc:
#     content = web_doc.read()
#
# soup = BeautifulSoup(content,"lxml")
# # for a in soup.find_all('a'):
# #     print(a.get("href"))
#
# heading = soup.find(name="h3",class_="heading")
# print(heading.getText())
#
# a_ = soup.select_one(selector="p a")
# print(a_)
# aa = soup.select(selector=".heading")
# print(aa)
#
#
