import math
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Databáze Pokémonů
ALL_POKEMONS = [
    {'id': 1, 'name': 'Bulbasaur', 'type': 'Grass / Poison', 'type_class': 'type-grass', 'hp': 45, 'attack': 49,
     'defense': 49, 'speed': 45, 'height': '0.7 m', 'weight': '6.9 kg',
     'desc': 'Pokémon travního a jedovatého typu. Na zádech nosí cibulku, ze které čerpá sluneční energii.',
     'img': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png'},
    {'id': 4, 'name': 'Charmander', 'type': 'Fire', 'type_class': 'type-fire', 'hp': 39, 'attack': 52, 'defense': 43,
     'speed': 65, 'height': '0.6 m', 'weight': '8.5 kg',
     'desc': 'Malý ještěří Pokémon. Plamen na konci jeho ocasu ukazuje jeho životní sílu a náladu.',
     'img': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png'},
    {'id': 7, 'name': 'Squirtle', 'type': 'Water', 'type_class': 'type-water', 'hp': 44, 'attack': 48, 'defense': 65,
     'speed': 43, 'height': '0.5 m', 'weight': '9.0 kg',
     'desc': 'Vodní želví Pokémon. Jeho krunýř ho nejen chrání, ale snižuje odpor vody při plavání.',
     'img': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png'},
    {'id': 25, 'name': 'Pikachu', 'type': 'Electric', 'type_class': 'type-electric', 'hp': 35, 'attack': 55,
     'defense': 40, 'speed': 90, 'height': '0.4 m', 'weight': '6.0 kg',
     'desc': 'Elektrický myší Pokémon. Ve svých tvářích shromažďuje elektřinu, kterou vypouští v bojích.',
     'img': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png'},
    {'id': 6, 'name': 'Charizard', 'type': 'Fire / Flying', 'type_class': 'type-fire', 'hp': 78, 'attack': 84,
     'defense': 78, 'speed': 100, 'height': '1.7 m', 'weight': '90.5 kg',
     'desc': 'Létající ohnivý drak. Jeho dech dokáže roztavit i nejtvrdší balvany.',
     'img': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png'},
    {'id': 94, 'name': 'Gengar', 'type': 'Ghost / Poison', 'type_class': 'type-ghost', 'hp': 60, 'attack': 65,
     'defense': 60, 'speed': 110, 'height': '1.5 m', 'weight': '40.5 kg',
     'desc': 'Stínový Pokémon, který předstírá, že je něčí stín, a v noci straší kolemjdoucí.',
     'img': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png'},
    {'id': 133, 'name': 'Eevee', 'type': 'Normal', 'type_class': 'type-normal', 'hp': 55, 'attack': 55, 'defense': 50,
     'speed': 55, 'height': '0.3 m', 'weight': '6.5 kg',
     'desc': 'Pokémon s nepravidelným genovým kódem, který se dokáže vyvinout do mnoha různých forem.',
     'img': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png'},
    {'id': 150, 'name': 'Mewtwo', 'type': 'Psychic', 'type_class': 'type-psychic', 'hp': 106, 'attack': 110,
     'defense': 90, 'speed': 130, 'height': '2.0 m', 'weight': '122.0 kg',
     'desc': 'Geneticky stvořený legendární Pokémon s obrovskou psychickou energií.',
     'img': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png'},
    {'id': 143, 'name': 'Snorlax', 'type': 'Normal', 'type_class': 'type-normal', 'hp': 160, 'attack': 110,
     'defense': 65, 'speed': 30, 'height': '2.1 m', 'weight': '460.0 kg',
     'desc': 'Velmi líný Pokémon, který celý den jen jí a spí. Jeho břicho je neuvěřitelně odolné.',
     'img': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png'}
]

PER_PAGE = 6


@app.route('/')
def index():
    # 1. Kontrola zobrazení detailu (přesměrování při chybném ID)
    pokemon_id = request.args.get('id', type=int)
    selected_pokemon = None

    if pokemon_id:
        selected_pokemon = next((p for p in ALL_POKEMONS if p['id'] == pokemon_id), None)
        if not selected_pokemon:
            return redirect(url_for('index'))

    # 2. Logika stránkování
    page = request.args.get('page', 1, type=int)
    total_pokemons = len(ALL_POKEMONS)
    total_pages = max(1, math.ceil(total_pokemons / PER_PAGE))

    if page < 1:
        page = 1
    elif page > total_pages:
        page = total_pages

    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    pokemons_on_page = ALL_POKEMONS[start:end]

    return render_template(
        'index.html',
        pokemons=pokemons_on_page,
        selected_pokemon=selected_pokemon,
        current_page=page,
        total_pages=total_pages,
        total_pokemons=total_pokemons
    )


if __name__ == '__main__':
    app.run(debug=True)