import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from vector_store import store_embeddings


def ingest_folder(folder_path):
    all_chunks = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            print(f"📄 Loading {file}...")

            try:
                # ✅ FIX: use PyMuPDFLoader (no decompression error)
                loader = PyMuPDFLoader(file_path)
                documents = loader.load()

                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=500,
                    chunk_overlap=50
                )

                chunks = splitter.split_documents(documents)
                print(f"   ➜ {len(chunks)} chunks created")

                all_chunks.extend(chunks)

            except Exception as e:
                print(f"❌ Skipping {file} due to error: {e}")

    if not all_chunks:
        print("❌ No documents processed")
        return

    store_embeddings(all_chunks)
    print(f"✅ All PDFs ingested successfully ({len(all_chunks)} chunks)")


if __name__ == "__main__":
    # ✅ FIX: pass FOLDER, not single PDF
    ingest_folder("../data/textbooks/science/")