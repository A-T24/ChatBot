import os
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# --------------------------
# NLTK Setup for Render
# --------------------------
nltk_data_dir = os.path.join(os.path.dirname(_file_), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)

# Download necessary NLTK packages
nltk.download('punkt',download_dir=nltk_data_dir )
nltk.download('punkt_tab', download_dir=nltk_data_dir)  # Fix for newer NLTK versions
# Add directory to NLTK search path
nltk.data.path.append(nltk_data_dir)

# --------------------------
# Load dataset
# --------------------------
data = pd.read_csv("chatbot_dataset.csv")
# Preprocess: lowercase + tokenize + remove extra spaces
data['Question'] = data['Question'].apply(lambda x: ' '.join(nltk.word_tokenize(str(x).lower())).strip())

# --------------------------
# Train model
# --------------------------
X_train, X_test, y_train, y_test = train_test_split(
    data['Question'], data['Answer'], test_size=0.2, random_state=42
)
model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2), min_df=2), MultinomialNB())
model.fit(X_train, y_train)

def get_response(question):
    question = ' '.join(nltk.word_tokenize(str(question).lower())).strip()
    try:
        pred = model.predict([question])[0]
        return pred
    except:
        return "Sorry, I couldn't understand that."

# --------------------------
# Dash App
# --------------------------
app = dash.Dash(_name_)
chat_history = []

app.layout = html.Div([
    html.H1("💬 My ChatterBox", style={
        'textAlign': 'center',
        'color': 'white',
        'backgroundColor': "#00030D",
        'padding': '15px',
        'borderRadius': '10px'
    }),
    html.Div(id='chat-window', style={
        'border': '2px solid #2980b9',
        'borderRadius': '15px',
        'padding': '15px',
        'height': '400px',
        'overflowY': 'scroll',
        'backgroundColor': '#f0f8ff',
        'marginBottom': '15px',
        'boxShadow': '0px 4px 8px rgba(0,0,0,0.2)'
    }),
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
    'backgroundColor': "#8974D8",
    'minHeight': '100vh',
    'padding': '20px'
})

@app.callback(
    Output('chat-window', 'children'),
    Input('submit-button', 'n_clicks'),
    [dash.dependencies.State('user-input', 'value')]
)
def update_output(n_clicks, user_input):
    if n_clicks > 0 and user_input:
        response = get_response(user_input)

        # User bubble
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

        # Bot bubble
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

# --------------------------
# Run server
# --------------------------
# Run the app
if _name_ == '_main_':
    port = int(os.environ.get('PORT', 8050))
    app.run(host='0.0.0.0', port=port)