
import arpeggiator
ARPEGGIATOR = arpeggiator.Arpeggiator()
UP = arpeggiator.Direction.UP
DOWN = arpeggiator.Direction.DOWN

user_input = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")

while user_input != 'DONE':
    ARPEGGIATOR.add_note(user_input)
    user_input = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")
print(ARPEGGIATOR)

ask = True
direction = ''

user_direction = input("Enter an arpeggiator direction [U/D] ")

while ask:
    if user_direction == "U":
        direction = "UP"
        ask = False
    elif user_direction == "D":
        direction = "DOWN"
        ask = False
    else:
        user_direction = input("Enter an arpeggiator direction [U/D] ")

ask_2 = True

times_to_play = int(input("How many times do you want your arpeggiator to play? "))

while ask_2:
    if times_to_play > 0:
        ask_2 = False
    else:
        times_to_play = int(input("How many times do you want your arpeggiator to play? (Must be a positive number) "))

for i in range(times_to_play):
    ARPEGGIATOR.play(direction)

