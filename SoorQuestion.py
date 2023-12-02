import earthquakes
import pandas as pd
import matplotlib.pyplot as plt

earthquake_data = earthquakes.get_earthquake()

data_list = []

for x in earthquake_data:
    data = (x["impact"]["magnitude"], x["location"]["depth"])
    data_list.append(data)

data_frame = pd.DataFrame(data_list, columns=["Magnitude", "Depth"])

correlation = data_frame["Magnitude"].corr(data_frame["Depth"])
print(correlation)

plt.scatter(data_frame["Depth"], data_frame["Magnitude"])
plt.title(f"Scatter Plot - Correlation: {correlation:.2f}")
plt.xlabel("Depth (km)")
plt.ylabel("Magnitude (Richter Scale)")
plt.show()
