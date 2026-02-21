import pandas as pd
import os

# create a sample dataframe with column name

data = {
    'name':['Aditya','bob','charlie'],
    'age':[21,42,12],
    'city':['New York', 'Los Angeles','chicago']
}
df = pd.DataFrame(data)

# adding a new column in a row
new_row1 = {
    'name':"GF1",
    'age':34,
    'city':"city1"
}
df.loc[len(df.index)] = new_row1

new_row2 = {
    'name':"GF2",
    'age':34,
    'city':"city2"
}
df.loc[len(df.index)] = new_row2


# Ensure the data directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# define the file path
file_path = os.path.join(data_dir,"sample_data.csv")

# safe the data frame to csv file, including column names
df.to_csv(file_path,index = False)

print(f"CSV file saved to {file_path}")