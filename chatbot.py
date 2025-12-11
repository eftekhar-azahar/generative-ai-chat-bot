import streamlit as st
from groq import Groq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from pypdf import PdfReader
from langchain.schema import Document

# ------------------ Groq Setup ------------------
GROQ_API_KEY = [api key]
client = Groq(api_key=GROQ_API_KEY)

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="Free PDF Chatbot", layout="wide")
st.header("Free PDF Chatbot (Groq + HuggingFace + FAISS)")

with st.sidebar:
    st.title("Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Session state for chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------ Process PDF ------------------
if uploaded_file is not None:
    # Read PDF
    pdf_reader = PdfReader(uploaded_file)
    full_text = "".join([page.extract_text() for page in pdf_reader.pages])

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    chunks = text_splitter.split_text(full_text)

    # Initialize embeddings
    hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create FAISS vector store
    vector_store = FAISS.from_texts(chunks, hf_embeddings)

    # ------------------ User Question ------------------
    user_question = st.text_input("Ask something about the PDF")

    if user_question:
        # Search relevant chunks
        relevant_docs = vector_store.similarity_search(user_question, k=3)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])

        # Generate answer using Groq Llama-3
        completion = client.chat.completions.create(
            model="llama3-13b-8k",  # use a currently supported model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {user_question}"}
            ]
        )

        answer = completion.choices[0].message["content"]

        # Save to chat history
        st.session_state.chat_history.append(("User", user_question))
        st.session_state.chat_history.append(("Bot", answer))

# ------------------ Display chat history ------------------
for sender, message in st.session_state.chat_history:
    if sender == "User":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
