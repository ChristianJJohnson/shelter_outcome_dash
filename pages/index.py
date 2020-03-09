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
                There is a huge population of homeless pets, particularly cats and dogs in the United States. 
                Cruelty and neglect aside, this is perhaps the biggest issue in the companion animal world that can 
                actually be solved.
                
                Furiends - is a interactive prediction model that trys to predict the outcome of cats and dogs in a shelter
                
                My goal with Furiends is to accurately predict the outcome of cats and dogs in a shelter. So that it may
                give new insights to better understand what may cause an animal to find homes verses a negative outcome
                such euthanasia.
            """
        ),
        dcc.Link(dbc.Button('Go to App', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='../assets/cat_with_dog.jpg', width="650", height="400")
    ]
)

layout = dbc.Row([column1, column2])