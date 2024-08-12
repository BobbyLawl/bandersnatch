''' The visualizations.py file generates a chart with visual data
relating to the bandersnatch monsters file '''
import os
from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd
import altair as alt

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB
DB_URL = os.getenv('DB_URL')
client = MongoClient(DB_URL)
db = client['mongodbVSCodePlaygroundDB']
monsters_collection = db['monsters']

# Load data into a Pandas DataFrame
df = pd.DataFrame(list(monsters_collection.find()))

# Convert ObjectId values to strings
df['_id'] = df['_id'].astype(str)

# Ensure df is a pandas DataFrame (double check)
assert isinstance(df, pd.DataFrame), "df is not a pandas DataFrame"


# Define the chart function
def chart(df: pd.DataFrame, x: str, y: str, target: str) -> alt.Chart:
    '''Check if columns exist in the DataFrame'''
    assert x in df.columns, f"x column '{x}' does not exist in the DataFrame"
    assert target in df.columns, f"target column '{target}' does not exist in the DataFrame"

    # Define properties and configuration
    properties = {
        'width': 3200,
        'height': 1400,
        'background': '#333',
        'padding': {'left': 50, 'top': 50, 'right': 50, 'bottom': 50}
    }

    # Create the chart
    graph = alt.Chart(df, title="Monster Names").mark_bar().encode(
        x=alt.X(x, axis=alt.Axis(title=x)),
        y=alt.Y(value=1),  # Use a constant value for y-axis
        color=target,
        tooltip=alt.Tooltip(df.columns.to_list())
    ).properties(**properties)

    return graph

# Example usage:
graph = chart(df, 'Name', 'Value', 'Name')
print(graph.to_json())
