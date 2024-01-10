import math
import random

pokemon_level = float(input("What is this PokÃ©mon's level? "))
pokemon_speed = float(input("What is this PokÃ©mon's speed? "))


random_value = random.randint(0,255)
threshold_value = (pokemon_speed/2)

if threshold_value > random_value:
    damage_multiplier = (((2)*pokemon_level)+6) / (pokemon_level + 6)
    print("The PokÃ©mon's move will be " + str(round(damage_multiplier, 2)) + "x stronger!")
else:
     print("The PokÃ©mon's move will have no critical hit!")

