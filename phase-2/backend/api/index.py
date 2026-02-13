"""
Vercel serverless handler for FastAPI application.
Uses Mangum to adapt FastAPI ASGI app for serverless environment.
"""
from mangum import Mangum
from app.main import app

# Wrap FastAPI app with Mangum for AWS Lambda/Vercel compatibility
handler = Mangum(app, lifespan="off")
