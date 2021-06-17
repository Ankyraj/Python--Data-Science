import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

orders = pd.read_csv('RawData_246F28274A7C_MAY_21.txt', delimiter='\t')

j = 0
s = 'abcdefghi'
for i in orders.columns:
    orders.rename(columns = {i: s[j]}, inplace = True)
    j += 1

print(orders.head())

app.layout = html.Div([
    dcc.Graph(id = 'scatter_chart',
              figure={
                  'data': [
                      go.Scatter(
                          x = orders.c,
                          y = orders.h,
                          mode = 'markers'
                      )
                  ],
                  'layout': go.Layout(
                      title = 'Scatterplot of RawData',
                      xaxis = {'title': 'X-axis'},
                      yaxis = {'title': 'Y-axis'}
                  )
              })
])

if __name__ == '__main__':
    app.run_server(debug=True)