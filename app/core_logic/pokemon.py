import requests
import json

def getPokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon')
    print(response)
    pokemonOutput = json.loads(response.text)
    return pokemonOutput