from typing import Optional
from fastapi import FastAPI
from core_logic import pokemon

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pokemon")
def getPokemon():
    response = pokemon.getPokemon()
    return response