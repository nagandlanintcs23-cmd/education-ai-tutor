from fastapi import FastAPI
from qa_engine import answer_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Tutor Running"}

@app.get("/ask")
def ask(question: str):
    answer = answer_question(question)
    return {"answer": answer}