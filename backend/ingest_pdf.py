import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from vector_store import store_embeddings


def ingest_all_pdfs():

    folder_path = "../data/textbooks"
    all_documents = []

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(folder_path, file)
            print("Reading:", pdf_path)

            loader = PyMuPDFLoader(pdf_path)
            documents = loader.load()

            all_documents.extend(documents)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(all_documents)

    store_embeddings(chunks)

    print("✅ All PDFs ingested successfully")


if __name__ == "__main__":
    ingest_all_pdfs()