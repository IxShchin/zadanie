from fastapi import FastAPI, Query
from pydantic import validator


app = FastAPI()


nomera = [{1: 'a713aa', 2: 'e888aн', 3: 'e777aa', 4: 'u789pp', }]


@app.get('/PLATE/GENERATE')
async def zadanieone(token: int, amount: int):
    if token != 12345:
        raise ValueError('Error TOKEN')
    return nomera([amount])
