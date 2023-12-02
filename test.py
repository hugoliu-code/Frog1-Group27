import pandas as pd

# Read the DataFrame from the pickle file
loaded_df = pd.read_pickle('earthquake_data.pkl')

# Display the loaded DataFrame
print(loaded_df)