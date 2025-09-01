from fastapi import FastAPI

app = FastAPI(title="CaliforniaProPerSavior API")

@app.get("/")
def root():
    return {"status": "ok", "app": "CaliforniaProPerSavior"}

@app.get("/health")
def health():
    return {"health": "ok"}
