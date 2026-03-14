from vector_store import load_db
from context_pruning import prune_context
import openai

db = load_db()

def answer_question(question):

    docs = db.similarity_search(question, k=5)

    context = prune_context(docs)

    prompt = f"""
    Answer the question using the textbook context.

    Context:
    {context}

    Question:
    {question}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )

    return response["choices"][0]["message"]["content"]