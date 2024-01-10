import math
import random

user_xp = float(input("Enter this user's current XP: "))
user_xp = round(user_xp,1)

if (user_xp < 0 or user_xp >= 50):
    print("ERROR: Please enter a valid XP value.")
if (50.0 >= user_xp >= 40.0):
    print("Level 5 Player (XP: " + str(user_xp) + ")")
if (40.0 > user_xp >= 30.0):
    print("Level 4 Player (XP: " + str(user_xp) + ")")
if (30.0 > user_xp >= 25.0):
    print("Level 3 Player (XP: " + str(user_xp) + ")")
if (25.0 > user_xp >= 18.0):
    print("Level 2 Player (XP: " + str(user_xp) + ")")
if (18.0 > user_xp >= 0):
    print("Level 1 Player (XP: " + str(user_xp) + ")")
