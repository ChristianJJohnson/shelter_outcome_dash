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
row1 = dbc.Row(
    [
        dcc.Markdown(
            """
                According to some studies there are about 70 million stray animals in the United States alone. Solving
                 this issue can improve not only the lives of the stray animals but goes a long way in making the
                 communities they frequent better as well. One often overlooked problem that homeless animals cause is
                 the strain on ecosystems as a whole. When a non-native species overtakes an area, it can negatively
                 impact delicate ecosystems through pollution and the spreading of disease. Stray animals usually aren’t 
                 vaccinated, leading to the transmission of rabies and other life-threatening diseases to other animal
                 populations. Internal parasites can also be passed along through the feces of an infected animal,
                 threatening native wildlife when the fecal matter contaminates food and water sources.
            """
        ),

        html.Img(src='../assets/aac.jpg', width="275", height="200", ),

        dcc.Markdown(
            """
                Shelters play a huge role in meeting the problems head on by providing necessary food, water, shelter
                and standard veterinary care for animals in need. They work year round to find pets loving and sustainable
                homes. Austin, Texas is the largest No Kill community in the nation, and home to the Austin Animal Center.
                They provide shelter to more than 16,000 animals each year and animal protection and pet resource services
                to all of Austin and Travis County. As part of the City of Austin Open Data Initiative, the Austin Animal
                Center makes available its collected dataset that contains statistics and outcomes of animals entering the
                Austin Animal Services system. My data is sourced from their most recent release at the time of writing
                (March 7, 2020). While my model is strictly for educational purposes I hope it may offer some value in
                helping better understand what type of animals find homes, since as we gain understanding we can concentrate
                efforts more effectively on the animals that are the highest risk for negative outcomes such as being harder
                to find homes alongside Euthanasias and death.
            """
        ),
    ],
)

row2 = dbc.Row(
    [
        dcc.Markdown(
            '''
                Going into this dataset my general assumptions were:
                that puppy and kittens would be much more likely to be adopted than their older counterparts
                breeds would play a large role in whether an animal is adopted
                Notorious breeds would be less likely to be adopted due to stereotypes
                Older animals would have a harder time finding homes and may be euthaized more often
            '''
        ),
        html.H5('Going into this dataset my general assumptions were:'),
        html.Li(
            children=[
                'That puppy and kittens would be much more likely to be adopted than their older.',
                'Breeds would play a large role in whether an animal is adopted.',
                'Notorious breeds would be less likely to be adopted due to stereotypes.',
                'Older animals would have a harder time finding homes and may be euthanized more often.'
            ],

        )
    ]
)

row3 = dbc.Row(
    [
        dcc.Markdown(
            '''
                For this visual I looked at bulldogs and retriever breeds of dogs what I found was:
                total number of bulldog breeds in the dataset is 11,282 while retrievers account for 11,107 so relatively close number
                Bulldogs are more than two times more likely to be euthanized than retrievers
                Bulldogs are about 31% less likely to be adopted over retrievers
                The data seems to support the notion that notorious breeds are less likely good outcomes
            '''
        ),
        html.Img(src='../assets/plot2.png', width="700", height="450")
    ]
)

row4 = dbc.Row(
    [
        html.H5('For my next visualization I wanted to game more insight about how the different outcomes was effected by age.\n'),
        html.H6('\nWhat I found was that all outcomes seem to be sqewed to younger animals'),
        html.H6('\nAge seem to play a role in how each out come turned outs'),

        html.Img(src='../assets/plot3.png', width="750", height="450")
    ]
)

layout = dbc.Row([row1, row2, row3, row4])