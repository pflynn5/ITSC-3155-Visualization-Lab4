import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Line Chart
line_df = df1
line_df['date'] = pd.to_datetime(line_df['date'])
data_linechart = [go.Scatter(x=line_df['date'], y=line_df['actual_max_temp'], mode='lines', name='Max Temperature')]

# Multi Line Chart
multiline_df = df1
multiline_df['date'] = pd.to_datetime(multiline_df['date'])
trace1 = go.Scatter(x=multiline_df['date'], y=multiline_df['actual_min_temp'], mode='lines', name='Min Temp')
trace2 = go.Scatter(x=multiline_df['date'], y=multiline_df['actual_max_temp'], mode='lines', name='Max Temp')
trace3 = go.Scatter(x=multiline_df['date'], y=multiline_df['actual_mean_temp'], mode='lines', name='Average Temp')
data_multiline = [trace1,trace2,trace3]

# Bubble chart
bubble_df = df1
data_bubblechart = [
    go.Scatter(x=bubble_df['average_max_temp'],
               y=bubble_df['average_min_temp'],
               text=bubble_df['month'],
               mode='markers',
               marker=dict(size=(bubble_df['average_max_temp']), color=(bubble_df['average_max_temp']), showscale=True))
]

# Heatmap
data_heatmap = [go.Heatmap(x=df1['day'],
                  y=df1['month'],
                  z=df1['record_max_temp'].values.tolist(),
                  colorscale='Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Temperature Highs and Lows July 2014-June 2015', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the maximum temperature in the given period.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Max temperature July 2014 to June 2015',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Temperature'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represent the maximum, minimum, and average temperature in the given period.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Max, Min, and Average Temperatures July 2014 to June 2015',
                      xaxis={'title': 'Month'}, yaxis={'title': 'Temperature'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    html.Div(
        'This bubble chart represents the average maximum and minimum temperatures in the given period.'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='Average Max and Min Temperature July 2014 to June 2015.',
                                      xaxis={'title': 'Average Max Temp'}, yaxis={'title': 'Average Min Temp'},
                                      hovermode='closest')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represents the record high temperatures in each day of the week and week of month.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Record Max Temperatures by Day and Month July 2014 to June 2015',
                                      xaxis={'title': 'Day of Week'}, yaxis={'title': 'Month'})
              }
              )
])


if __name__ == '__main__':
    app.run_server()