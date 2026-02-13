"""
Hugging Face Space Entry Point for NestTask Backend API
This file is required for Hugging Face Spaces to run the FastAPI application.
"""
from app.main import app

# Hugging Face Spaces will run this using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
