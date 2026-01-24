import pandas

data = pandas.read_csv("central_park_squirrel_census.csv")
gray_squirrel_num = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_num = len(data[data["Primary Fur Color"] == "Black"])
red_squirrel_num = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrel_num)
print(black_squirrel_num)
print(red_squirrel_num)
