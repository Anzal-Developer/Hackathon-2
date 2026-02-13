"""
Vercel serverless handler for FastAPI application.
This file is required for Vercel to properly serve the FastAPI app as a serverless function.
"""
from app.main import app

# Vercel expects a handler or the app itself
handler = app
