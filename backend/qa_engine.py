from vector_store import load_or_create_vector_store
from ingest_pdf import load_pdf_texts
from context_pruning import prune_context
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

pdf_texts = load_pdf_texts("data/textbooks")

db = load_or_create_vector_store(pdf_texts)

def answer_question(question: str) -> str:
    docs = db.similarity_search(question, k=5)
    context = prune_context(docs)
    prompt = f"""
Answer the question using the textbook context below.

Context:
{context}

Question:
{question}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response["choices"][0]["message"]["content"].strip()