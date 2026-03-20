import os
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from vector_store import load_vectorstore

def answer_question(query: str):
    db = load_vectorstore()

    if db is None:
        return "Database not found. Please ingest data first."

    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa.run(query)