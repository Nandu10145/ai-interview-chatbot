from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

questions = {
    "java": [
        "what is OOP?",
        "what is JVM?",
        "explain inheritance in java?"
    ],
    "python": [
        "what is a list?",
        "what is dictionary?"
    ]
}

class UserInput(BaseModel):
    topic: Optional[str] = None
    answer: Optional[str] = None


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/get-question")
def get_question(data: UserInput):
    if not data.topic:
        return {"message": "please provide a topic"}

    topic = data.topic.lower()

    if topic in questions:
        return {"questions": questions[topic]}

    return {"message": "topic not found"}


@app.post("/evaluate")
def evaluate(data: UserInput):
    if not data.answer:
        return {"feedback": "please provide an answer"}

    answer = data.answer.strip()

    if len(answer) < 20:
        return {"feedback": "try explaining in more detail"}

    return {"feedback": "good answer, try adding examples for improvement"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)