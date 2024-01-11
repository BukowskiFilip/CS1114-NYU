number_of_players = int(input("Enter a valid number of players: "))

while (number_of_players < 2) or (number_of_players > 8):
    number_of_players = int(input("ERROR. Enter a valid number of players: "))

max_cost = 0
max_player = 0
total_cost = 0

for player in range(1, number_of_players + 1):
    cost = (input("Enter the value of a property/asset, or DONE to finish: "))
    
    while cost != "DONE":
        total_cost += float(cost)
        cost = (input("Enter the value of a property/asset, or DONE to finish: "))
        
    print("Player " + str(player) + " has", str(total_cost) + " dollars.")

    if (total_cost > max_cost):
        max_cost = total_cost
        max_player = player
print(str(max_player) + " wins with " + str(max_cost) + " dollars!")
