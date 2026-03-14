from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def store_embeddings(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="../vector_db"
    )

    print("✅ Embeddings stored successfully")