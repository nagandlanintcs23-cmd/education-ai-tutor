import os
from fastapi import FastAPI
from qa_engine import answer_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Tutor API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ask")
def ask(q: str):
    if not q:
        return {"error": "Query parameter 'q' is required"}

    try:
        answer = answer_question(q)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)