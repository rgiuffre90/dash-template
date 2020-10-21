# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd
# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Goal'), 
        dcc.Slider(
            id='goal', 
            min=0, 
            max=20000, 
            step=100, 
            value=2000, 
            marks={n: str(n) for n in range(0,20000,5000)}, 
            className='mb-5'
        ), 
 
        dcc.Markdown('#### Backers'), 
        dcc.Slider(
            id='backers', 
            min=1, 
            max=20000, 
            step=100, 
            value=2000, 
            marks={n: str(n) for n in range(1,20000,2000)}, 
            className='mb-5' 
        ),

        dcc.Markdown('#### Currency'), 
        dcc.Dropdown(
            id='currency', 
            options = [
                {'label': 'USD', 'value': 'USD'}, 
                {'label': 'GBP', 'value': 'GBP'}, 
                {'label': 'EUR', 'value': 'EUR'}, 
                {'label': 'CAD', 'value': 'CAD'}, 
                {'label': 'AUD', 'value': 'AUD'}, 
                {'label': 'SEK', 'value': 'SEK'}, 
                {'label': 'MXN', 'value': 'MXN'}, 
                {'label': 'NZD', 'value': 'NZD'}, 
                {'label': 'DKK', 'value': 'DKK'}, 
                {'label': 'CHF', 'value': 'CHF'},
                {'label': 'NOK', 'value': 'NOK'}, 
                {'label': 'HKD', 'value': 'HKD'}, 
                {'label': 'SGD', 'value': 'SGD'}, 
                {'label': 'JPY', 'value': 'JPY'}  
            ], 
            value = 'USD', 
            className='mb-5' 
        ), 
        
        dcc.Markdown('#### Main Category'), 
        dcc.Dropdown(
            id='main_category', 
            options = [
                {'label': 'Publishing', 'value': 1}, 
                {'label': 'Film & Video', 'value': 2}, 
                {'label': 'Music', 'value': 3}, 
                {'label': 'Food', 'value': 4}, 
                {'label': 'Desgin', 'value': 5}, 
                {'label': 'Crafts', 'value': 6}, 
                {'label': 'Games', 'value': 7}, 
                {'label': 'Comics', 'value': 8}, 
                {'label': 'Fashion', 'value': 9}, 
                {'label': 'Theatre', 'value': 10},
                {'label': 'Art', 'value': 11}, 
                {'label': 'Photography', 'value': 12}, 
                {'label': 'Technology', 'value': 13}, 
                {'label': 'Dance', 'value': 14}, 
                {'label': 'Journalism', 'value': 15}, 
            ], 
            value = 1, 
            className='mb-5' 
        ), 

        dcc.Markdown('#### Length of Campaign (Days)'), 
        dcc.Slider(
            id='length_of_campaign', 
            min=0, 
            max=100, 
            step=1, 
            value=10, 
            marks={n: str(n) for n in range(0,100,10)}, 
            className='mb-5' 
        ), 
        dcc.Markdown('#### Name Sentiment (Postive or Negative)'), 
        dcc.Slider(
            id='sentiments', 
            min=0, 
            max=1, 
            step=.1, 
            value=0, 
            marks={n: str(n) for n in range(0,1)}, 
            className='mb-5' 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Kickstarter Success', className='mb-5'), 
        html.Div(id='state', className='lead')
    ]
)

@app.callback(
    Output('state', 'children'),
    [Input('backers', 'value'), Input('goal', 'value'),
    Input('currency', 'value'), Input('main_category', 'value'),
    Input('length_of_campaign', 'value'), Input('sentiments', 'value')],
)
def predict( goal, backers,  currency, main_category, length_of_campaign, sentiments):
    df = pd.DataFrame(
        columns=['goal', 'backers', 'currency',
                'main_category', 'length_of_campaign',
                'sentiments'], 
        data=[[goal, backers, currency, main_category, length_of_campaign, sentiments]]
    )
    y_pred = pipeline.predict(df)[0]
    
    def result(y_pred):
        if y_pred == '1':
            return 'Successful Campaign'
        else:
            return 'Failed Campaign'

    return result(y_pred)

layout = dbc.Row([column1, column2])

#backers
#goal
#legnth_of_campaign
#main_category
#sentiments
#currency
