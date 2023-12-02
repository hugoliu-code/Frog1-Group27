import earthquakes


print(earthquakes.get_earthquake()[1])

for x in earthquakes.get_earthquake():
    print((x["impact"])["magnitude"], (x["location"])["depth"])