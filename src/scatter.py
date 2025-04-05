import plotly.express as px
import pandas as pd

# Load the dataset

filepath = '/workspaces/data-engineering-demo/data/2019.csv'
df = pd.read_csv(filepath)

# Ensure required columns exists 
required_cols = ["Score", "GDP per capita", "Country or region"]
if not all(col in df.columns for col in required_cols):
    raise ValueError("Missing required columns (or typo)")

# Create scatter plot
fig = px.scatter(
    df,
    x="Score",
    y="GDP per capita",
    color="Country or region",
    hover_name="Country or region",
    title="Happiness Score vs. GDP per Capita"
)

# Display the plot
fig.show()