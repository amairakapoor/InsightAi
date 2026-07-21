"""
InsightAI backend FastAPI app.

This file is imported by /api/index.py, which is what Vercel actually
invokes as the serverless function. Kept separate from api/index.py so the
backend can also be run locally with:
    uvicorn app:app --reload --port 8000
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routes import router
from .config import settings
from . import models  # noqa: F401  (ensures models are registered with Base)

# NOTE: on a hosted Postgres DB, this runs once per cold start and is a
# cheap no-op if tables already exist (CREATE TABLE IF NOT EXISTS semantics).
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="InsightAI API",
    description="Conversational Business Intelligence backend: NL -> SQL -> Charts -> Insights",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.get("/")
def root():
    return {"message": "InsightAI API is running. See /api/docs for the interactive API explorer."}
