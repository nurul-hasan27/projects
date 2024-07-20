# # with open("./weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
# #
# #
# # import csv
# # with open("./weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperature = []
# #     for row in data:
# #         print(row)
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
# #
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# data_series = data["temp"]
#
# # data frames conversions
# data_dict = data.to_dict()
# print(data_dict)
#
# # series conversions
# data_list = data_series.tolist()
# print(data_list)
# avg = data_series.mean()
# print(avg)
#
# # Get data in columns
# data_col1 = data["condition"]
# data_col2 = data.condition
# print(data_col1)
# print(data_col2)
#
# # Get data in row
# data_row = data[data.condition == "Sunny"]
# print(data_row)
#
#
# max_temp = data.temp.max()
# which_col = data[data.temp == max_temp]
# print(which_col)
#
# # Get intersection of row and column
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# print(monday_temp)
# only_temp = monday_temp[0]
# print(only_temp)


# ========== squirrel census ==========
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)


# data_color = data["Primary Fur Color"].tolist()
# # print(data_color)
# count_gray = 0
# count_black = 0
# count_red = 0
# for color in data_color:
#     if color == "Gray":
#         count_gray += 1
#     if color == "Cinnamon":
#         count_red += 1
#     if color == "Black":
#         count_black += 1

count_gray = len(data[data["Primary Fur Color"] == "Gray"])
count_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_black = len(data[data["Primary Fur Color"] == "Black"])

# print(count_gray, count_black, count_red)
data_dict = {
    "fur color": ["gray", "red", "black"],
    "count": [count_gray, count_red, count_black]
}

color_data = pandas.DataFrame(data_dict)
print(color_data)
color_data.to_csv("./color_data.csv")
