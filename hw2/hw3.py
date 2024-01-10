
import math
import random


maximum_health = float(input("Enter the amount of health points does the Pokémon has! "))

pokéball_value = random.randint(1,255)
pokémon_current = random.randint(1,maximum_health)
random_number = random.randint(0,255)


formula_for_catch = ((maximum_health * 255 * 4)//(pokémon_current * pokéball_value))

print(formula_for_catch >= random_number)
