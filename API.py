import requests
poke_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{poke_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data

    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_info = get_pokemon('ditto')

if pokemon_info:
    print(f'{pokemon_info["name"].capitalize()}')
    print(f'{pokemon_info["id"]}')
    print(f'{pokemon_info["height"]}')
    print(f'{pokemon_info["weight"]}')