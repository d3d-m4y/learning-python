import pandas

data = pandas.read_csv(
    "files\\2018_central_park_squirrel_census-squirrel_data.csv")

squirrel_color_data = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [0, 0, 0]
}

for fur_color in data["Primary Fur Color"]:
    if fur_color == "Gray":
        squirrel_color_data["Count"][0] += 1
    elif fur_color == "Black":
        squirrel_color_data["Count"][1] += 1
    elif fur_color == "Cinnamon":
        squirrel_color_data["Count"][2] += 1
    else:
        pass

# instead of using a for loop you could just run the len() method 
# on the squirrel_color_data

squirrel_color_data_frame = pandas.DataFrame(squirrel_color_data)
print(squirrel_color_data_frame)

squirrel_color_data_frame.to_csv("squirrel_count.csv")
