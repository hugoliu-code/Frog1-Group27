import pandas as pd
import matplotlib.pyplot as plt

loaded_df = pd.read_pickle('earthquake_data.pkl')

data_frame = loaded_df[["magnitude", "depth"]]

correlation = data_frame["magnitude"].corr(data_frame["depth"])
print(correlation)

plt.scatter(data_frame["depth"], data_frame["magnitude"])
plt.title(f"Scatter Plot - Correlation: {correlation:.2f}")
plt.xlabel("Depth (km)")
plt.ylabel("Magnitude (Richter Scale)")
plt.show()
