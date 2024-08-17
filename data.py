''' The data.py file shows our monsters data'''
import pandas as pd

# Sample data
data = {
    'Name': ['Monster1', 'Monster2', 'Monster3'],
    'Type': ['Fire', 'Water', 'Grass'],
    'HP': [100, 120, 90],
    'Attack': [10, 12, 8]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Define a function to get the data
def get_data():
    ''' the get data funciton returns the df containing all the monsters'''
    return df

# Define a function to process the data (e.g., calculate mean HP)
def process_data():
    ''' The process data function calculates the mean of columns'''
    mean_hp = df['HP'].mean()
    return mean_hp
