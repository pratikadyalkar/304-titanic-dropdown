######### Import your libraries #######
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly as py
import plotly.graph_objs as go


###### Define your variables #####
tabtitle = 'Titanic!'
color1='#92A5E8'
color2='#8E44AD'
color3='#FFC300'
sourceurl = 'https://www.kaggle.com/c/titanic'
githublink = 'https://github.com/plotly-dash-apps/304-titanic-dropdown'


###### Import a dataframe #######
df = pd.read_csv('assets/football.csv')
#df['Female']=df['Sex'].map({'male':0, 'female':1})
#df['Cabin Class'] = df['Pclass'].map({1:'first', 2: 'second', 3:'third'})
labels=['Most home goals']#, 'Most away goals', 'Top 10 city hosting tournaments', 'Top 10 countries hosting tournaments']
values=[{'groubyby':'home_team','column':'home_score', 'function':'sum()'}]
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H3(id='display-value'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': j} for i,j in zip(labels,values)],
        value=values[0]
    ),
    html.Br(),
    #dcc.Graph(id='display-value'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
])

@app.callback(Output('output', 'children'), Input('dropdown', 'value'))
def display_output(value):
    return f'You have selected "{value}"'

######### Interactive callbacks go here #########
@app.callback(Output('display-value', 'figure'),
              [Input('dropdown', 'value')])
def display_value(continuous_var):
    # print(continuous_var)
    # grouped_mean=df.groupby(['Cabin Class', 'Embarked'])[continuous_var].mean()
    # results=pd.DataFrame(grouped_mean)
    # # Create a grouped bar chart
    # mydata1 = go.Bar(
    #     x=results.loc['first'].index,
    #     y=results.loc['first'][continuous_var],
    #     name='First Class',
    #     marker=dict(color=color1)
    # )
    # mydata2 = go.Bar(
    #     x=results.loc['second'].index,
    #     y=results.loc['second'][continuous_var],
    #     name='Second Class',
    #     marker=dict(color=color2)
    # )
    # mydata3 = go.Bar(
    #     x=results.loc['third'].index,
    #     y=results.loc['third'][continuous_var],
    #     name='Third Class',
    #     marker=dict(color=color3)
    # )

#     mylayout = go.Layout(
#         title= continuous_var,
#         xaxis = dict(title = 'Port of Embarkation'), # x-axis label
#         yaxis = dict(title = 'lol'), # y-axis label

#     )
#     fig = go.Figure(layout=mylayout)
#     return fig

    return f'You have selected "{value}"'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
