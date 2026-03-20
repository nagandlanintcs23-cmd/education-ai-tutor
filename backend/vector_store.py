import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_DIR = os.path.join(os.path.dirname(__file__), "db")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def load_vectorstore():
    if not os.path.exists(DB_DIR):
        return None

    return Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding_model
    )