from fastapi import FastAPI

app = FastAPI(title="Lab 02 - FastAPI")

@app.get("/")
def read_root():
    return {"message": "Hello from a Dockerized FastAPI app!"}

@app.get("/health")
def health():
    return {"status": "ok"}
