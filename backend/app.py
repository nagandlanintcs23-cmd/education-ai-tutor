from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.qa_engine import answer_question

app = FastAPI()

# CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is LIVE 🚀"}

@app.get("/ask")
def ask(question: str):
    try:
        answer = answer_question(question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}