import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

# Create app
app = dash.Dash(__name__)
server = app.server

# Define layout
app.layout = html.Div(children=[
    html.H1(children='Gapminder Data'),

    html.Div(children='''
        A simple scatter plot of life expectancy vs GDP per capita.
    '''),

    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=px.scatter(df, x="gdpPercap", y="lifeExp", log_x=True, size="pop", color="continent",
                           hover_name="country", animation_frame="year", height=600)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
