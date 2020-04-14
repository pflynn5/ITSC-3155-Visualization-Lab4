import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Olympic2016Rio.csv')

app = dash.Dash()

# Barchart
barchart_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
barchart_df = df1.groupby(['NOC'])['Gold'].sum().reset_index()
barchart_df = barchart_df.sort_values(by=['Gold'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df['NOC'], y=barchart_df['Gold'])]

# Stack bar chart
stackbarchart_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
stackbarchart_df = stackbarchart_df.groupby(['NOC']).agg(
    {'Gold': 'sum', 'Silver': 'sum', 'Bronze': 'sum'}).reset_index()
stackbarchart_df = stackbarchart_df.sort_values(by=['Gold'], ascending=[False]).head(20).reset_index()
trace1 = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Gold'], name='Gold', marker={'color': '#FFD700'})
data_stackbarchart = [trace1, trace2, trace3]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Olympic Games 2016- Medals by Country', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the number of gold medals won by the top 20 countries.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Gold Medals Won',
                                      xaxis={'title': 'Countries'}, yaxis={'title': 'Number of medals won'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represent the number of gold, silver, and bronze medals won by the top 20 countries.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Medals won in the top 20 countries',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Medals won'},
                                      barmode='stack')
              }
              ),
])


if __name__ == '__main__':
    app.run_server()