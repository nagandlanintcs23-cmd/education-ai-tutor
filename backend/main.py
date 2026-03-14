from fastapi import FastAPI
from pydantic import BaseModel
from qa_engine import answer_question

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Education AI Tutor API Running"}

# Ask AI Tutor
@app.post("/ask")
def ask_ai(question: Question):
    answer = answer_question(question.question)
    return {"question": question.question, "answer": answer}