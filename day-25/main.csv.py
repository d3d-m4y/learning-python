import csv

with open("files\\weather_data.csv") as file:
    data = csv.reader(file)
    temps = []

    for row in data:
        if row[1] != "temp":
            temps.append(int(row[1]))

    print(temps)
