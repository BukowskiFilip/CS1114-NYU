from dance_dance_revolution import DanceDanceRevolution
GAME = DanceDanceRevolution()

def get_game_parameters():
    user_steps = int(input("How many steps would you like to memorize? (positive non-zero integers only: "))

    while (user_steps <= 0):
        print("WARNING: Please enter a positive non-zero integer value.")
        user_steps = int(input("How many steps would you like to memorize? (positive non-zero integers only: "))

    user_speed = float(input("How fast would you like the game to run? (positive non-zero numerical values only: "))

    while (user_speed <= 0):
        print("WARNING: Please enter a positive non-zero numerical value.")
        user_speed = float(input("How fast would you like the game to run? (positive non-zero numerical values only: "))

    return(user_steps, user_speed)

def get_user_answers():

    answer = []

    check = False

    while (check == False):
        user_input = input("Enter a direction (U/D/L/R) or 'DONE' to finish: ")

        if user_input == 'DONE' and len(answer) == 0:
            print("Please enter at least one answer before selecting 'DONE'.")

        elif (user_input == 'DONE'):
            return(answer)
        else:
            answer.append(user_input)

def run_game():
    game_parameters = get_game_parameters()
    GAME.set_speed(game_parameters[1])
    GAME.set_amount(game_parameters[0])
    GAME.play_sequence()
    user_answers = get_user_answers()
    if GAME.check_answers(user_answers) == True:
        print("Congratulations! You've guessed correctly!")
    else:
        print("Oh No! You didn't guess correctly! Play again to try again!")

run_game()
