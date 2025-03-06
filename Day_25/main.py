import pandas
# data = pandas.read_csv("002 weather-data.csv")
# # print(data["temp"])
# # data_dic = data.to_dict()
# # print(data_dic)
# # temp_list = data["temp"].to_list()
# # average = data["temp"].mean()
# # max_value = data["temp"].max()
# # print(max_value)
# day = data[data.day == "Monday"]
# conversion = day.temp
# print((conversion * (9/5)) + 32)
#
data = pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
fur_color = data["Primary Fur Color"].to_list()
num_gray = 0
num_cinnamon = 0
num_black = 0
for color in fur_color:
    if color == "Gray":
        num_gray += 1
    elif color == "Cinnamon":
        num_cinnamon += 1
    elif color == "Black":
        num_black += 1
count_dict = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count" : [num_gray,num_cinnamon,num_black]
}
new_data = pandas.DataFrame(count_dict)
new_data.to_csv("squirrel_color_count.csv")