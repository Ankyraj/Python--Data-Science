import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


orders = pd.read_csv('RawData_246F28274A7C_MAY_21.txt', delimiter='\t')

j = 0
s = 'abcdefghi'
for i in orders.columns:
    orders.rename(columns = {i: s[j]}, inplace = True)
    j += 1

print(orders.head())

app = dash.Dash()
colors = {
    'text': "#ff0000",
    'plot_color': "#838B8B",
    'paper_color': '#00FFFF'
}
app.layout = html.Div([html.H1(children = "Hello Ankit!!!",
                               style={
                                   'textAlign': 'center',
                                   'color': colors['text']
                               }),
                       html.Div(children = "Dash-Plotly",
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                }),
                       dcc.Graph(
                           id = "Samplechart",
                           figure={
                               "data": (
                                   {'x': list(orders.c)[:5], 'y': list(orders.g)[:5], 'type': 'bar', 'name': 'First Chart'},
                                   {'x': list(orders.c)[:5], 'y': list(orders.h)[:5], 'type': 'bar', 'name': 'Second Chart'}
                               ),
                               "layout": {
                                   'plot_bgcolor': colors['plot_color'],
                                   'paper_bgcolor': colors['paper_color'],
                                   'font': {'color': colors['text']},
                                   'title': 'Simple Bar Chart'
                               }
                           }
                       )
                       ])

if __name__ == "__main__":
    app.run_server(debug = True)