from vector_store import load_db

def answer_question(question):
    db = load_db()

    docs = db.similarity_search(question, k=3)

    context = " ".join([doc.page_content for doc in docs])

    return context