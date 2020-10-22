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
        
            ## Time to kickstart your dream?

            Out of the half-million launched campaigns, a third are successful, [according to Kickstarter](https://www.kickstarter.com/help/stats). Our app, Kickstart Or Stop, analyzes hundreds of thousands of campaigns from 2018 to answer the question: What makes a successful campaign? 
            

            Using the interactive quiz, you can find out whether your hypothetical kickstarter campaign would be successful -- or how your current campaign stacks up! However, we advise to use Kickstart Or Stop in tandem with other consulting resources before making a decision about launching a campaign. 

            (Graphic courtesy of [amateurphotographer.co.uk](https://www.amateurphotographer.co.uk/latest/articles/the-kickstarter-photo-projects-that-never-delivered-45430))

            """
        ),
        dcc.Link(dbc.Button("Let's get started!", color='success'), href='/predictions')
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