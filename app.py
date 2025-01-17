######### Import your libraries #######
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly as py
import plotly.graph_objs as go


###### Define your variables #####
tabtitle = 'foootbalbalball!'
color1='#92A5E8'
color2='#8E44AD'
color3='#FFC300'
#sourceurl = 'https://www.kaggle.com/c/titanic'
githublink = 'https://github.com/pratikadyalkar/304-titanic-dropdown'


###### Import a dataframe #######
df = pd.read_csv('assets/football.csv')
#df['Female']=df['Sex'].map({'male':0, 'female':1})
#df['Cabin Class'] = df['Pclass'].map({1:'first', 2: 'second', 3:'third'})
labels=['Most home goals', 'Most away goals', 'Top 10 city hosting tournaments', 'Top 10 countries hosting tournaments']
values=[{'groupby':'home_team','column':'home_score', 'function':'sum()'},
       {'groupby':'away_team','column':'away_score', 'function':'sum()'},
       {'groupby':'city','column':'tournament', 'function':'count()'},
       {'groupby':'country','column':'tournament', 'function':'count()'}]
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
        placeholder="Select a filter",
    ),
    html.Br(),
    dcc.Graph(id='display-value'),
    html.P('''The dataset contains football tournament data. It includes data ranging from date 1872-11-30 to 2018-07-10.
    102 different tournaments are hosted by 265 countries in 1874 cities across the globe over the period of time. '''),
    html.Br(),
    html.A('Code on Github', href=githublink),
    #html.Br(),
    #html.A("Data Source", href=sourceurl)
])


######### Interactive callbacks go here #########
@app.callback(Output('display-value', 'figure'),
              [Input('dropdown', 'value')])
def display_value(continuous_var):
    print(continuous_var)
    dicj = values[continuous_var]
    grouped_mean=eval('df.groupby("{0}").{2}.sort_values(by="{1}", ascending=False).head(10)'.format(dicj['groupby'],dicj['column'],dicj['function']))
    results=pd.DataFrame(grouped_mean).reset_index()
    # # Create a grouped bar chart
    mydata1 = go.Bar(
        x=results[dicj['groupby']],
        y=results[dicj['column']],
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
        xaxis = dict(title = dicj['groupby']), # x-axis label
        yaxis = dict(title = dicj['column']), # y-axis label

    )
    fig = go.Figure(data=mydata1, layout=mylayout)
    return fig



######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
