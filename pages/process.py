# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights and Methodology
            
            The dataset that the model is based on, Mickaël Mouillé’s [“Kickstarter Project”](https://www.kaggle.com/kemical/kickstarter-projects), contains information about kickstarter campaigns recorded in 2016 and 2018. Our model only evaluates data from 2016. 

            In order to access the dataset, we chose to download the specific csv for 2018 campaigns (Mouillé also includes a csv for 2016 campaign data).  Another method to accessing the csv would be to pull the csv through an API, which acts as a bridge between a database like Kaggle and a personal computer. (Information on installing and using the specific API for accessing the Kaggle database is available [here](https://github.com/Kaggle/kaggle-api/blob/master/setup.py).)

            In the original dataset, Mouillé organized campaigns to have one of five outcomes: failed, canceled, successful, suspended and live. Because we built a model that predicts whether a kickstarter campaign would be a success, we created a new column that would change the structure of the ‘outcome’ column.  Now, the model is predicting a boolean -- whether the campaign was ‘successful’ or a ‘failure.’

            A boolean question is one that requires a ‘yes/no’, ‘true/false’ answer. Because our model is supposed to answer the question “Will my kickstarter campaign be successful?” our model requires a target that is black and white. If we, the data scientists, were asking “How successful will my kickstarter campaign be?” then our model would be able to make a prediction based off of multiple types of outcomes, not just a boolean.

            But, what about the three outlying outcome categories?

            Canceled campaigns are campaigns that have ended before the set deadline without meeting its monetary goal. By using the value counts method, we found that, out of almost 39,000 canceled campaigns, around a third did not garner any money. Other common canceled campaign donation amounts range between $1 and $50USD. As a result, we inferred that these campaigns were canceled due to inability to reach their goal, and categorized them as ‘failure.’
            Suspended campaigns are campaigns that are not temporarily live, but not canceled. Because of the ambiguity of these types of campaigns, as well as the reasons for why a campaign would be suspended, we decided to omit the all suspended campaigns from the ‘outcomes’ column. 

            Live campaigns are campaigns that are currently accepting donations and have not yet reached their deadline. Because we don’t know the results of a campaign until it either reaches its goal, its deadline or is cancelled, we also omitted this status. 

            If there was data available on 2019 campaigns, then we would be able to categorize 2018 live campaigns as ‘successful’ or a ‘failure’ -- or not, if they were suspended.

            We also added a column that states the length of a campaign (from launch date to deadline), in order to improve the model’s accuracy. Similar to how a scene in a book is clearer if there are descriptions, adding columns to a data set can help improve a model’s accuracy.

            To prevent leakage — when a specific aspect of the dataset gives away the answer before making a prediction — we removed information about the number of contributors to each campaign (in the dataset, contributors are referred to as “backers”). Without knowing the number of backers, the model must depend on other information, such as the amount of money pledged, to make a prediction.

            After defining which columns to use to make predictions with -- ‘main_category’, ‘deadline’, ‘launched’, ‘goal’, ‘usd_pledged_real’, ‘usd_goal_real’ and ‘outcome’ -- we then split the dataset 80/20. This technique is called a ‘train-test split.’ 80 percent of the dataset will be passed through the model; the remaining 20 percent will remain untouched, and act as a comparison tool to see how accurate our model is. 

            Then we established a baseline accuracy. Like a signpost, baseline accuracy scores indicate how effective the model is. As the model is fitted and iterated, new accuracy scores will be generated and compared to the baseline.

            Logistic regression models take a non-numerical category of data, like names, and predict which category a piece of data belongs to. In regards to my dataset, the logistic model takes descriptive data, such as the amount of money pledged and length of campaign, to decide whether a campaign would be a success or a failure. 

            Before modeling, we could predict whether a kickstarter campaign would be successful with 41 percent accuracy. After fitting our data to a logistic regression model, we could predict with 60 percent accuracy. 

            While the model increased our model's accuracy considerably, there is still room for improvement. One way to improve the model would be to increase the number of columns used to predict. The more specific and desciptive the dataset is, the more accurately the audience can predict whether their kickstarter campaign idea is worth launching.

            """
        ),

    ],
)

column2 = dbc.Col(
    [
        #dcc.Graph(figure=fig),
        html.Img(src='assets/Screenshot 2020-10-21 222150.png', className='img-fluid')
    ]
)

column3 = dbc.Col(
    [
        #dcc.Graph(figure=fig),
        html.Img(src='assets/Screenshot 2020-10-21 222814.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2, column3])
