# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Time to Kickstart your Dream?

            Our model predicts what makes a successful Kickstarter campaign.

            ✅ Tk

            ❌ Tk
            """
        ),
        dcc.Link(dbc.Button('Try it out!', color='success'), href='/predictions')
    ],
    md=4,
)



#gapminder = px.data.gapminder()
#fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        #dcc.Graph(figure=fig),
        html.Img(src='assets/funded-with-kickstarter_0.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])