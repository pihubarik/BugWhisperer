# BugWhisperer Backend Main Entry Point

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "BugWhisperer backend running"}

