# backend/app/main.py

from fastapi import FastAPI
from app.api.routes import router

from app.config.logging_config import configure_logging, get_logger
from app.config.settings import settings

# app = FastAPI(
#     title="AI Recruitment Intelligence API",
#     version="0.1.0"
# )


configure_logging()

logger = get_logger(__name__)

logger.info("Starting AI Recruitment Intelligence API")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

logger.info("Application initialized successfully")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Recruitment API is running! - main.py"}