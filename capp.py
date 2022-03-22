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
labels=['Most home goals', 'Most away goals', 'Top 10 city hosting tournaments', 'Top 10 countries hosting tournaments']
values=[{'groubyby':'home_team','column':'home_score', 'function':'sum()'},
       {'groubyby':'away_team','column':'away_score', 'function':'sum()'},
       {'groubyby':'city','column':'tournament', 'function':'count()'},
       {'groubyby':'country','column':'tournament', 'function':'count()'}]
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H3('Football Tournaments around the world'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': j, 'value': i} for i,j in enumerate(labels)],
        value=values[0],
        placeholder="Select a filter",
    ),
    html.Br(),
    dcc.Graph(id='display-value'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl)
])


######### Interactive callbacks go here #########
@app.callback(Output('display-value', 'figure'),
              [Input('dropdown', 'value')])
def display_value(continuous_var):
    print(continuous_var)
    dicj = values[continuous_var]
    grouped_mean=eval('df.groupby("{0}").{2}.sort_values(by="{1}", ascending=False).head(10)'.format(dicj['groubyby'],dicj['column'],dicj['function']))
    results=pd.DataFrame(grouped_mean)
    # # Create a grouped bar chart
    mydata1 = go.Bar(
        x=results[dicj['column']],
        y=results[dicj['groupby']],
    )
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

    mylayout = go.Layout(
        title= labels[continuous_var],
        xaxis = dict(title = 'Port of Embarkation'), # x-axis label
        yaxis = dict(title = 'lol'), # y-axis label

    )
    fig = go.Figure(layout=mylayout)
    return fig



######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
