from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Recruitment Intelligence API",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Recruitment API is running! - main.py"}