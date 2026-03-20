from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store embeddings
def store_embeddings(chunks):
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="../embeddings_db"
    )
    db.persist()
    print("Embeddings stored successfully")

# Load database
def load_db():
    db = Chroma(
        persist_directory="../embeddings_db",
        embedding_function=embedding
    )
    return db