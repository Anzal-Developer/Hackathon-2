from fastapi import FastAPI

app = FastAPI(title="Todo API", version="1.0.0")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "todo-backend"}

@app.get("/")
async def root():
    return {"message": "Todo Backend API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
