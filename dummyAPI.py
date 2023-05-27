from fastapi import FastAPI

app=FastAPI()

@app.post('/')
def create():
    consumption = 500/20
    return consumption