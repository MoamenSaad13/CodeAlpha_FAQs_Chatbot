=======
# FAQ Chatbot

A complete FAQ chatbot system built with Flask backend, NLP processing using SpaCy, and a modern web interface.

## Features

- **NLP Processing**: Uses SpaCy for text preprocessing and tokenization
- **Similarity Matching**: Implements cosine similarity with TF-IDF vectorization
- **Modern UI**: Clean, responsive chat interface with typing indicators
- **REST API**: Flask-based backend with CORS support
- **Easy Customization**: Simple JSON-based FAQ management

## Project Structure

```
chatbot_backend/
├── src/
│   ├── main.py                 # Flask application entry point
│   ├── nlp_processor.py        # NLP processing and similarity matching
│   ├── faqs.json              # FAQ data (questions and answers)
│   ├── routes/
│   │   ├── chatbot.py         # Chatbot API endpoints
│   │   └── user.py            # User management (template)
│   ├── models/
│   │   └── user.py            # Database models (template)
│   ├── static/
│   │   └── index.html         # Chat UI frontend
│   └── database/
│       └── app.db             # SQLite database
├── venv/                      # Python virtual environment
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation

1. **Clone or extract the project files**

2. **Navigate to the project directory**
   ```bash
   cd chatbot_backend
   ```

3. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Download SpaCy English model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

1. **Start the Flask server**
   ```bash
   cd chatbot_backend
   source venv/bin/activate
   python src/main.py
   ```

2. **Access the chatbot**
   - Open your browser and go to `http://localhost:5000`
   - Start asking questions in the chat interface

## API Endpoints

### POST /api/chatbot/ask
Send a question to the chatbot and receive an answer.

**Request:**
```json
{
    "question": "What are your operating hours?"
}
```

**Response:**
```json
{
    "question": "What are your operating hours?",
    "answer": "Our operating hours are Monday to Friday, 9 AM to 5 PM."
}
```

## Customizing FAQs

Edit the `src/faqs.json` file to add, modify, or remove FAQ entries:

```json
[
    {
        "question": "Your question here",
        "answer": "Your answer here"
    }
]
```

After modifying the FAQ file, restart the Flask server to load the changes.

## How It Works

1. **Text Preprocessing**: User questions are processed using SpaCy to:
   - Convert to lowercase
   - Remove stop words and punctuation
   - Lemmatize tokens

2. **Similarity Matching**: The system uses:
   - TF-IDF vectorization to convert text to numerical vectors
   - Cosine similarity to find the most similar FAQ question
   - Returns the answer from the best matching FAQ

3. **Web Interface**: The frontend provides:
   - Real-time chat interface
   - Typing indicators
   - Responsive design for mobile and desktop
   - Error handling for network issues

## Technical Stack

- **Backend**: Flask (Python web framework)
- **NLP**: SpaCy (natural language processing)
- **ML**: Scikit-learn (TF-IDF vectorization and cosine similarity)
- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Database**: SQLite (for user management, optional)

## Deployment

For production deployment, consider:
- Using a production WSGI server like Gunicorn
- Setting up a reverse proxy with Nginx
- Using environment variables for configuration
- Implementing proper logging and monitoring



