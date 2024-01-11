
POKEMON_DATA = """#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False
2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False
3,Venusaur,Grass,Poison,525,80,82,83,100,100,80,1,False
3,VenusaurMega Venusaur,Grass,Poison,625,80,100,123,122,120,80,1,False
4,Charmander,Fire,,309,39,52,43,60,50,65,1,False"""

def create_entry(number, name, type1, type2, hp, attack, defense, speed, legendary):
    if type2 == '':
        type2 = None
    types = type1, type2
    battle_stats = {"HP": hp, "Attack": attack, "Defense": defense, "Speed": speed}
    entry = {"Number": number, "Name": name, "Types": types, "Battle Stats": battle_stats, "Legendary": legendary}

    return entry

def create_pokedex(pokemon_data):
    pokedex_dict = {}
    pokemon_data = POKEMON_DATA.split('\n')
    for line in pokemon_data[1:]:
        pokemon_list = line.split(',')
        legendary = False
        if pokemon_list[12] == "True":
            legendary = True
        pokemon = create_entry(int(pokemon_list[0]),pokemon_list[1], pokemon_list[2],pokemon_list[3], int(pokemon_list[5]), int(pokemon_list[6]),int(pokemon_list[7]),int(pokemon_list[10]), legendary)
        pokedex_dict[pokemon_list[1]] = pokemon
    return pokedex_dict


def main():
    pokedex = create_pokedex(POKEMON_DATA)
    pokemon_key = "Ivysaur"

    if pokemon_key not in pokedex:
        print(f"ERROR: Pokemon {pokemon_key} does not exist!")
    else:
        print(f"PRINTING {pokemon_key}'S INFORMATION...")

        my_favorite_pokemon = pokedex[pokemon_key]

        for key in my_favorite_pokemon.keys():
            print(f"{key}: {my_favorite_pokemon[key]}")

main()

