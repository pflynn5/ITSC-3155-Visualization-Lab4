import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Preparing data
data = [
    go.Scatter(x=df['average_max_temp'],
               y=df['average_min_temp'],
               text=df['month'],
               mode='markers',
               marker=dict(size=(df['average_max_temp']), color=(df['average_max_temp']), showscale=True))
]

# Preparing layout
layout = go.Layout(title='Average Maximum and Minimum Temperatures For Each Month (2014-15)',
                   xaxis_title="Max Temp", yaxis_title="Min Temp", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')