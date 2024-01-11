
from TouchType import TouchType, SwipeDirection
SINGLE_TOUCH = TouchType.SINGLE_TOUCH
DOUBLE_TAP = TouchType.DOUBLE_TAP
SWIPE = TouchType.SWIPE
HOLD = TouchType.HOLD
UP = SwipeDirection.UP
DOWN = SwipeDirection.DOWN
LEFT = SwipeDirection.LEFT
RIGHT = SwipeDirection.RIGHT
NO_DIRECTION = SwipeDirection.NO_DIR


def get_touch():
    user_direction = NO_DIRECTION
    user_hold = 0.1
    type_of_touch = None

    user_touch = input("What type of touch did the user perform? [single/double/swipe/hold] ")
    if user_touch == "single":
        type_of_touch = SINGLE_TOUCH
    elif user_touch == "double":
        type_of_touch = DOUBLE_TAP
    if user_touch == "hold":
        type_of_touch = HOLD
        user_hold = float(input("For how long did the user hold the touch? "))
    elif user_touch == "swipe":
        type_of_touch = SWIPE
        user_direction = input("In what direction did the user swipe? ")
        if user_direction == "left":
            user_direction = LEFT
        elif user_direction == "right":
            user_direction = RIGHT
        elif user_direction == "up":
            user_direction = UP
        elif user_direction == "down":
            user_direction = DOWN
    user_strong = float(input("How strong was the user's touch? [0.0 to 1.0] "))
    if type_of_touch == HOLD:
        register_touch(type_of_touch, user_hold, user_direction, user_strong)
    else:
        register_touch(type_of_touch, user_hold, user_direction, user_strong = 0.1)


def register_touch(type_of_touch, user_hold, user_direction, user_strong):
    if type_of_touch == (SINGLE_TOUCH):
        print("Registering single touch...")
    elif type_of_touch == DOUBLE_TAP:
        print("Registering double tap...")
    elif type_of_touch == SWIPE:
        print("Registering swipe...")
    elif type_of_touch == HOLD:
        print("Registering hold...")

        touch_ratio = (user_strong)/(user_hold)

        give_haptic_feedback(touch_ratio)

    if user_direction != NO_DIRECTION:
        if user_direction == UP:
            print("Exiting app...")
        elif user_direction == LEFT or user_direction == RIGHT:
            print("Changing page...")
        elif user_direction == DOWN:
            print("Scrolling up...")


def give_haptic_feedback(user_ratio):
    if 0.0 < user_ratio < 0.5:
        print("Vibrating once...")
    elif 0.5 <= user_ratio <= 2.0:
        print("Vibrating twice...")
    elif user_ratio > 2.0:
        print("Vibrating thrice...")

def main():
 get_touch()

main()
