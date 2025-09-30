# 💬 My ChatterBox: Data Science & ML Chatbot

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.13-blue?logo=plotly&logoColor=white)](https://dash.plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🚀 Project Overview

**My ChatterBox** is a sleek, web-based chatbot built with **Python**, **Dash**, and **machine learning**. It answers questions about **Data Science**, **Machine Learning**, and related tools like Python, Pandas, SQL, and algorithms.  

It uses **Multinomial Naive Bayes** with **TF-IDF vectorization** to map user queries to structured answers from a **custom knowledge base**.

✨ **Key Idea:** Train the bot on a dataset of Q&A pairs to provide instant responses in a visually appealing chat interface.

---

## 🛠 Features

- 📝 **Custom Knowledge Base** – Trainable dataset (`chatbot_dataset.csv`) with FAQs.  
- 🧠 **NLP Backend** – Uses `nltk` for tokenization and `TfidfVectorizer` for feature extraction.  
- 🌙 **Dark Mode UI** – Modern, responsive interface built with Dash.  
- 💬 **Interactive Chat** – Real-time messages with styled chat bubbles.  
- ⚡ **Lightweight & Extendable** – Easily add new Q&A pairs to expand intelligence.

---

## 🌈 UI Preview

### Chat in Action
![Chatbot GIF](https://media.giphy.com/media/l0HlNaQ6gWfllcjDO/giphy.gif)  
*Example of user asking a question and bot responding.*

### Dark Mode & Chat Styling
![Dark Mode Screenshot](https://via.placeholder.com/600x300.png?text=Chatbot+Dark+Mode+Screenshot)  
*Clean UI with scrollable chat bubbles.*

> 💡 Tip: Replace the above placeholder image/GIF with your actual screenshots or GIFs.

---

## 🛠 Technology Stack

| Component            | Technology      | Role                                                      |
|----------------------|----------------|-----------------------------------------------------------|
| Backend/Core Logic    | Python         | ML model training and data preprocessing                 |
| Web Framework         | Dash           | Builds the interactive web interface                     |
| Machine Learning      | scikit-learn   | Multinomial Naive Bayes classifier                        |
| NLP Preprocessing     | NLTK           | Tokenization & text normalization                         |
| Data Storage          | Pandas         | Loads and manages the dataset                              |

---

## ⚡ Setup & Installation

### Prerequisites
- Python 3.7+ installed

### 1️⃣ Clone the Repository
```bash
git clone <repository_url>
cd my-chatterbox
```

### 2️⃣ Install Dependencies
```bash
pip install pandas scikit-learn dash nltk
```

### 3️⃣ Download NLTK Data
```python
import nltk
nltk.download('punkt')
```

### 4️⃣ Project Structure
```
my-chatterbox/
├── dark_mode_chatbot.py       # Main application script
├── chatbot_dataset.csv        # Q&A dataset
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

### 5️⃣ Run the Application
```bash
python dark_mode_chatbot.py
```
Open [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in your browser to start chatting.

---

## 📚 Training Data (`chatbot_dataset.csv`)

| Question                   | Answer                                                                 |
|-----------------------------|------------------------------------------------------------------------|
| What is SQL?               | SQL (Structured Query Language) is used to manage data in relational databases. |
| What does a Data Scientist do? | Designs and implements statistical models, analyzes data, and provides actionable insights. |

> 💡 Tip: Add more question-answer pairs to improve performance.

---

## 🤝 Contributing
Contributions are welcome! You can:

- Add more Q&A pairs to the dataset  
- Improve UI/UX design  
- Suggest features or optimizations  

Open an issue or submit a pull request.

---

## 📄 License
MIT License © 2025 **Ayush**

---

## ⭐ Acknowledgements
- Built with [Dash](https://dash.plotly.com/) and [Scikit-learn](https://scikit-learn.org/)  
- Tokenization with [NLTK](https://www.nltk.org/)  
- Inspired by interactive AI chatbots and educational projects  

> Made with ❤️ by **Ayush**

