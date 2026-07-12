"""
Vercel serverless function entry point.

Vercel's Python runtime auto-detects an ASGI app exported as `app` in a
file under /api and serves it as a serverless function. This file just
adds ../backend to the import path and re-exports the FastAPI instance
defined in backend/app.py.

Do not rename the exported variable `app` -- Vercel looks for that name.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from app import app  # noqa: E402  (FastAPI instance, re-exported for Vercel)
