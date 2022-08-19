from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    ...


@app.post("/another")
def another():
    ...


@app.get("/health", include_in_schema=False)
def health():
    ...
