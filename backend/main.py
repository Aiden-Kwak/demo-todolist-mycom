# My Dev Company Backend
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello from My Dev Company!'}
