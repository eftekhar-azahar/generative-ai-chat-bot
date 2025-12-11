PDF Chatbot using Groq, HuggingFace, FAISS & Streamlit

This project is a lightweight, efficient PDF Question-Answering Chatbot built with Groq LLMs, HuggingFace sentence-transformer embeddings, FAISS vector search, and Streamlit for a simple web interface.
Users can upload a PDF, and the chatbot retrieves relevant text chunks and generates accurate, context-aware responses.

Features

Upload any PDF file and extract its text.

Automatic chunking of text using LangChain's RecursiveCharacterTextSplitter.

High-quality vector embeddings via HuggingFace MiniLM.

Fast semantic search using FAISS.

Natural language question answering using Groq LLM APIs.

Simple, clean user interface built with Streamlit.

Maintains chat history for multi-turn conversations.

Tech Stack

Python 3.10+

Streamlit

Groq API (LLM inference)

LangChain

HuggingFace Sentence Transformers

FAISS

PyPDF

Installation
1. Clone the repository
git clone https://github.com/your-username/pdf-chatbot-groq
cd pdf-chatbot-groq

2. Create & activate virtual environment
python -m venv venv
venv/Scripts/activate    # Windows
source venv/bin/activate # macOS/Linux

3. Install dependencies
pip install -r requirements.txt

Environment Setup

Create a .env file:

GROQ_API_KEY=your_api_key_here

Run the Application
streamlit run chat_bot.py


The app will open in your browser.

Project Structure
├── chat_bot.py
├── requirements.txt
├── README.md
└── assets/

How It Works

PDF Parsing
The user uploads a PDF, and the text is extracted using PyPDF.

Chunking
Text is split into manageable chunks for embedding.

Embedding & Vector Store
HuggingFace embeddings encode the chunks, stored in a FAISS index.

Semantic Search
User queries are matched against the vector store to retrieve relevant context.

Groq LLM Response
The retrieved context + question are submitted to a Groq LLM to produce an answer.

Conversation Memory
Chat history persists within the session.

Screenshot (Optional)

Add a screenshot of your UI for better presentation:

![App Screenshot](assets/screenshot.png)

Future Improvements

Support for multiple PDFs.

Chat memory stored in FAISS or Chroma DB.

Option to download chat history.

Better UI/UX components.

Model selection from UI.

License

This project is open-source under the MIT License.
