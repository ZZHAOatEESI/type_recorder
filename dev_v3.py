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
            'fontSize':'30px',
            'color': 'blue'
        }
    ),
                       
    html.Div(children='''
        Content to type:
        ''',id ='message',
             className = 'row',
        style = dict(fontSize='15px', textAlign='center', color='red')),
    html.Iframe(id = 'iframe-msg',srcDoc='The quick brown fox jumps over the lazy dog',width = 450,style=dict(textAlign='center')),
    
    html.Label('Please type the content here:', style = {'color': 'green'}),
    dcc.Input(id = 'user_input', value='', type='text', className = 'seven columns'),
          
    html.Div(id='typing_indictor', children = '', style = dict(fontSize='15px', textAlign='center', display='none')),
          
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
],style = {'textAlign':'center'})

@app.callback(Output(component_id="typing_indictor", component_property="children"),
              [Input('user_input', 'value')])
def start_timer(typing_flag):
    global start
    ## call backend function and record the time when user start to type
    if typing_flag and start == 0:
        start = time.time()
    return str(start)

@app.callback(Output('user_input', 'value'),
              [Input('submit-button', 'n_clicks')])
def empty_input_box(click):
    return ''

@app.callback(Output("iframe-msg", "srcDoc"),
              [Input('submit-button', 'n_clicks')],
              [State('user_input', 'value')])
def update_message(click, user_input):
    ## call backend function and compute the typing duration
    global start
    global test_idx
    global test_case_size
    typing_time = time.time() - start
    if test_idx == 0:
        recorder[test_idx] = {}
    elif test_idx < test_case_size + 1:
        recorder[test_idx] = {'duration': typing_time, 'user input': user_input, 'reference content': contest_dict[test_idx-1]}
    else:
        pass
    if test_idx < test_case_size:
        txt_to_type = contest_dict[test_idx]
    elif test_idx == test_case_size:
        del recorder[0]
        records = pd.DataFrame.from_dict(recorder, orient='index')
        records.to_csv('records.csv')
        txt_to_type  = ':::::::: Type Recording is Done! Thanks For your Help ::::::::'
    else:
        txt_to_type  = ':::::::: Type Recording is Done! Thanks For your Help ::::::::'
    
    test_idx += 1
    start = 0
    return txt_to_type

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "//fonts.googleapis.com/css?family=Dosis:Medium",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/62f0eb4f1fadbefea64b2404493079bf848974e8/dash-uber-ride-demo.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]


for css in external_css:
    app.css.append_css({"external_url": css})

if __name__ == '__main__':
    global start, test_idx, test_case_size
    test_idx = 0
    start = 0
    recorder = {}
    contest_dict = {0: 'The quick brown fox jumps over the lazy dog',
                    1: 'Talk is cheap, show me the code',
                    2: 'Manners maketh man',
                    3: 'You are going to need a pair of shoes to go with your suit.',
                    4: 'An Oxford is any formal shoe with open lacing.',
                    5: 'This additional decorative piece is called broguing.',
                    6: 'Oxfords, not brogues'
                    }
    test_case_size = len(contest_dict.keys())
    app.run_server(debug=True)
