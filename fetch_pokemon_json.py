import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        return name, abilities
    else:
        return None, None

name, abilities = fetch_pokemon_data('pikachu')
print(f"Name: {name}")
print("Abilities:", ", ".join(abilities))

import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        weight = data['weight']
        return name, abilities, weight
    else:
        return None, None, None

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemons = []

for name in pokemon_names:
    pokemon_data = fetch_pokemon_data(name)
    if pokemon_data:
        pokemons.append({
            'name': pokemon_data[0],
            'abilities': pokemon_data[1],
            'weight': pokemon_data[2]
        })

average_weight = calculate_average_weight(pokemons)

for pokemon in pokemons:
    print(f"Name: {pokemon['name']}, Abilities: {', '.join(pokemon['abilities'])}, Weight: {pokemon['weight']}")

print(f"Average Weight: {average_weight}")

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    if response.status_code == 200:
        planets = response.json()['bodies']
        for planet in planets:
            if planet['isPlanet']:
                name = planet.get('englishName', 'Unknown')
                mass = planet.get('mass', {}).get('massValue', 'Unknown')
                orbit_period = planet.get('sideralOrbit', 'Unknown')
                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = []
    if response.status_code == 200:
        data = response.json()['bodies']
        for body in data:
            if body['isPlanet']:
                name = body.get('englishName', 'Unknown')
                mass = body.get('mass', {}).get('massValue', 0)
                orbit_period = body.get('sideralOrbit', 0)
                planets.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})
    return planets

def find_heaviest_planet(planets):
    heaviest = max(planets, key=lambda planet: planet['mass'])
    return heaviest['name'], heaviest['mass']

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} x10^24 kg.")

