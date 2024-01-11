
letters = input("Please enter a string of lowercase letters: ")

current_value = ord(letters[0])
is_decreasing = True

for i in range(1, len(letters)):
    letter_value = ord(letters[i])
    if (letter_value > current_value):
        is_decreasing = False
    current_value = letter_value

if is_decreasing == True:
    print(letters + " is decreasing")
else:
    print(letters + " is not decreasing")
