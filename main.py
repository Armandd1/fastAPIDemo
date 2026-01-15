#First FastAPI project
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello World'}

@app.get('/hello2')
def read_root():
    return {'message': 'World, again!'}