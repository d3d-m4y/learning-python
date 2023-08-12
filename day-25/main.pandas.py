import pandas

data = pandas.read_csv("files\\weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

# get data from columns
print(data['condition'])
print(data.condition)

# get data from rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

c_monday = data.temp[0]
f_friday = c_monday * (9/5) + 32
print(f_friday)

# create a dataframe from scratch
another_data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

more_data = pandas.DataFrame(another_data_dict)
print(more_data)

more_data.to_csv("more_data.csv")