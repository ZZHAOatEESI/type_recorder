import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask
from flask_cors import CORS
import pandas as pd
import numpy as np
import os
import time

app = dash.Dash()
server = app.server

app.layout = html.Div([
    html.H1(
        children='Type_recorder',
        style={
            'textAlign': 'center',
            'fontSize':'30px'
        }
    ),

    html.Div(children='''
        Content to type:
        ''',id ='message',
             className = 'row',
        style = dict(fontSize='15px', textAlign='center')),
    html.Iframe(id = 'iframe-msg',srcDoc='The quick brown fox jumps over the lazy dog',width = 450,style=dict(textAlign='center')),
    
    html.Label('Please type the content here:'),
    dcc.Input(id = 'user_input', value='', type='text', className = 'seven columns'),
          
    html.Div(id='typing_indictor', children = '', style = dict(fontSize='15px', textAlign='center', display='none')),
          
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
],style = {'textAlign':'center'})

@app.callback(Output(component_id="typing_indictor", component_property="children"),
              [Input('user_input', 'value')],
              [State('typing_indictor', 'children')])
def start_timer(typing_flag, flag):
    ## call backend function and return description of the nearest hydrant
    if typing_flag and flag == '':
        start = str(time.time())
    else:
        start = flag
    return start

@app.callback(Output("iframe-msg", "srcDoc"),
              [Input('submit-button', 'n_clicks')],
              [State('user_input', 'value'),
               State('typing_indictor', 'children')
               ])
def update_message(click, user_input, start):
    ## call backend function and return description of the nearest hydrant
    txt_to_type = 'The quick brown fox jumps over the lazy dog'
    print(user_input)
    print(time.time() - float(start))
    return txt_to_type

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "//fonts.googleapis.com/css?family=Dosis:Medium",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/62f0eb4f1fadbefea64b2404493079bf848974e8/dash-uber-ride-demo.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]


for css in external_css:
    app.css.append_css({"external_url": css})

if __name__ == '__main__':
    app.run_server(debug=True)
