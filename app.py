import pandas as pd
from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

app = JupyterDash(__name__)

df=pd.read_csv("https://raw.githubusercontent.com/srinathkr07/IPL-Data-Analysis/master/matches.csv")

df=df.fillna(0)

win=px.bar(df,x="winner",title="Best Team Based on Winning count")
pom=px.bar(df,y="player_of_match",title="Best Player")
run=px.bar(df,x="winner",y="win_by_runs",title="Best Team based on high marginal win by run")
wic=px.bar(df,x="winner",y="win_by_wickets",title="Best team based win by wicket")
lvet=px.bar(df,y='venue',color='winner',title='Luckiest Venue for Each Team',barmode='relative')
wpwt= px.bar(df,x='toss_winner',y='winner',color="winner",title='Winning probability by Winning Toss')

app.layout = html.Div(children=[
   html.H1(children='Analysis of IPL dataset',style={'textalign':'center'}),
 
   html.Div(children='''
       Basic Analysis of an IPL Dataset
   ''',style={'textAlign':'center'}),
 
   dcc.Graph(
       id='example-graph',
       figure=win
   ),
   dcc.Graph(
       id='example-graph-2',
       figure=pom
   ),
   dcc.Graph(
       id='example-graph-3',
       figure=run
   ),
   dcc.Graph(
       id='example-graph-4',
       figure=wic
   ),
   dcc.Graph(
       id='example-graph-5',
       figure=lvet
   ),
   dcc.Graph(
       id='example-graph-6',
       figure=wpwt
   )
])
if __name__ == '__main__':
   app.run_server(debug=True)
