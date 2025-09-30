import os
import nltk

# Ensure NLTK data is downloaded and accessible on Render
nltk_data_path = '/opt/render/nltk_data'
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

nltk.data.path.append(nltk_data_path)
nltk.download('punkt', download_dir=nltk_data_path)

import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import random


# Load the dataset
data = pd.read_csv("chatbot_dataset.csv")

# Preprocess the data
nltk.download('punkt')   #punkt tokenizer
data['Question'] = data['Question'].apply(lambda x: ' '.join(nltk.word_tokenize(x.lower()))) #Normalized data 

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data['Question'], data['Answer'], test_size=0.2, random_state=42)

# Create a model pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

def get_response(question):
    question = ' '.join(nltk.word_tokenize(question.lower()))
    answer = model.predict([question])[0]
    return answer

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("💬 My ChatterBox", style={
        'textAlign': 'center',
        'color': 'white',
        'backgroundColor': "#00030D",
        'padding': '15px',
        'borderRadius': '10px'
    }),

    # Chat window
    html.Div(id='chat-window', style={
        'border': '2px solid #2980b9',
        'borderRadius': '15px',
        'padding': '15px',
        'height': '400px',
        'overflowY': 'scroll',
        'backgroundColor': '#f0f8ff',  # light blue background
        'marginBottom': '15px',
        'boxShadow': '0px 4px 8px rgba(0,0,0,0.2)'
    }),

    # Input area
    html.Div([
        dcc.Input(
            id='user-input',
            type='text',
            placeholder='Type your message...',
            style={
                'flex': '1',
                'padding': '12px',
                'borderRadius': '20px',
                'border': '1px solid #ccc',
                'fontSize': '16px'
            }
        ),
        html.Button('➤ Send', id='submit-button', n_clicks=0, style={
            'marginLeft': '10px',
            'padding': '12px 20px',
            'borderRadius': '20px',
            'border': 'none',
            'backgroundColor': '#3498db',
            'color': 'white',
            'cursor': 'pointer',
            'fontWeight': 'bold',
            'fontSize': '16px'
        })
    ], style={'display': 'flex', 'justifyContent': 'center'})
], style={
    'maxWidth': '700px',
    'margin': 'auto',
    'fontFamily': 'Arial, sans-serif',
    'backgroundColor': "#8974D8", # Main dark background
    'minHeight': '100vh',
    'padding': '20px'})


chat_history = []

@app.callback(
    Output('chat-window', 'children'),
    Input('submit-button', 'n_clicks'),
    [dash.dependencies.State('user-input', 'value')]
)
def update_output(n_clicks, user_input):
    if n_clicks > 0 and user_input:
        response = get_response(user_input)

        # User bubble (green, aligned right)
        chat_history.append(html.Div(user_input, style={
            'textAlign': 'right',
            'margin': '10px',
            'padding': '10px 15px',
            'backgroundColor': '#2ecc71',
            'color': 'white',
            'borderRadius': '15px',
            'display': 'inline-block',
            'maxWidth': '70%'
        }))

        # Bot bubble (blue, aligned left)
        chat_history.append(html.Div(response, style={
            'textAlign': 'left',
            'margin': '10px',
            'padding': '10px 15px',
            'backgroundColor': '#3498db',
            'color': 'white',
            'borderRadius': '15px',
            'display': 'inline-block',
            'maxWidth': '70%'
        }))

    return chat_history


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

