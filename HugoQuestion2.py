import pandas as pd

# Read the DataFrame from the pickle file
earthquake_df = pd.read_pickle('earthquake_data.pkl')
airline_df = pd.read_pickle('airline_data.pkl')
print(earthquake_df)
