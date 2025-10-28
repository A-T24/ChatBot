# 💬 ChatBot

A simple **AI-powered chatbot** built using **Python**, **NLTK**, and **Dash** for a responsive web interface.  
It uses a CSV-based Q&A dataset and text similarity techniques to provide intelligent replies to user queries.

---

## 🚀 Features

- 🧠 **Natural Language Processing** (NLTK + TF-IDF similarity)
- 🌗 **Dark Mode UI** for a modern chatting experience
- 💾 **Customizable Dataset** — easily add your own questions and answers
- ⚙️ **Lightweight Architecture** built on Python and Dash
- 🧩 **Fully Local Execution** — no API keys or cloud services required

---

## 🗂️ Project Structure

ChatBot/
│
├── app.py # Main Dash web app
├── data/
│ └── chatbot_dataset.csv # Question–Answer dataset
├── requirements.txt # Dependencies
├── static/ # (Optional) Static assets: CSS, JS, images
├── templates/ # (Optional) HTML templates
└── README.md


---

## 🧩 Installation

### 1. Clone the repository

git clone https://github.com/A-T24/ChatBot.git
cd ChatBot

2. (Optional) Create a virtual environment

python -m venv venv
# On Linux / macOS
source venv/bin/activate
# On Windows
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

    💡 If NLTK raises missing resource errors:

    import nltk
    nltk.download('punkt')

▶️ Usage

Start the chatbot locally:

python app.py

Then open your browser and visit:
👉 http://127.0.0.1:8050/

You can now chat with the bot in your browser.
🧠 How It Works

    The user sends a message through the Dash interface.

    The chatbot tokenizes input using NLTK.

    A TF-IDF vectorizer transforms text into a numerical representation.

    The app compares the input to known questions using cosine similarity.

    The most similar question’s predefined answer is returned to the user.

🗃️ Dataset

The chatbot reads data from:

data/chatbot_dataset.csv

Each row follows this format:
Question	Answer
Hi	Hello! How can I help you today?
Who are you?	I am a simple chatbot created in Python.

You can easily add your own pairs — just edit the CSV and restart the app.
Be sure to keep the same column names.
🧪 Running Tests

To verify chatbot behavior, you can use pytest:

pytest tests/

Example test (tests/test_basic_response.py):

from app import get_response

def test_greeting():
    reply = get_response("hi")
    assert "hello" in reply.lower()

🛠️ Contributing

Contributions are welcome! 🙌

    Fork this repository

    Create a new branch

git checkout -b improve-readme

Make your changes

Push your branch

    git push origin improve-readme

    Open a Pull Request on GitHub

💅 Code Style

    Follow PEP 8

    Use linters like flake8 or formatters like black

    Add comments/docstrings where needed

📦 Deployment
Deploy on Render or Railway

    Create a new Python web service

    Upload this repo or connect your GitHub fork

    Add the build command:

pip install -r requirements.txt

Run command:

    python app.py

Run with Docker

docker build -t chatbot .
docker run -p 8050:8050 chatbot

🧾 Example Conversation

You: Hi
Bot: Hello! How can I help you today?

You: What can you do?
Bot: I can answer simple questions based on my dataset!

🧱 Future Improvements

    🤖 Add intent recognition for better understanding

    🗣️ Include speech input/output support

    🧮 Integrate transformer-based responses (e.g., DistilBERT)

    🧱 Add database-backed learning system

📄 License

This project is licensed under the MIT License.
See the LICENSE
file for details.

Made with ❤️ by Ayush
