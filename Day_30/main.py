fruits = ["Apple", "Pear", "Orange"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)
x_posts = [
    {"likes": 21, "comments": 2},
    {"likes": 13, "comments": 8, "shares": 3},
    {"comments": 4, "shares": 2},
    {"comments": 1, "shares": 1},
    {"likes": 19, "comments": 3}
]

total_likes = 0

for post in x_posts:
    try:
        total_likes += post["likes"]
    except KeyError:
        total_likes += 0
print(total_likes)
