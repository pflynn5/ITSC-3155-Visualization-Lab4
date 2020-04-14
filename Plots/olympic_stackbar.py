import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv("../Datasets/Olympic2016Rio.csv")

# Remove empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Create sum of number of cases grouped by Country Column
new_df = df.groupby(['NOC']).agg(
    {'Gold': 'sum', 'Silver': 'sum', 'Bronze': 'sum'}).reset_index()

# Sort values and select first 20 values
new_df = new_df.sort_values(by=['Gold'], ascending=[False]).head(20).reset_index()

# Preparing data
trace1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold', marker={'color': '#FFD700'})
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Gold, Silver, and Bronze Medals by Top 20 Countries in 2016 Olympics', xaxis_title="Country",
                   yaxis_title="Medals Won", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')