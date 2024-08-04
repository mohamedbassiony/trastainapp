from fastapi import FastAPI
app = FastAPI()


@app.get("/w")
def welcome():
    return {
        "message": "Hello World!"
    }