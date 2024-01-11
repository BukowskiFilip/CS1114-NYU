
user_input = int(input("Input a positive integer: "))



for upper_half in range(user_input, 0, -1):
    answer = " "
    for spacing in range(user_input - upper_half):
        answer = ((answer) + " ")
    for printing in range(1, 2 * upper_half):
        answer = (answer + "*")
    print(answer)

    
for lower_half in range(2, user_input + 1):
    answer = ' '
    for spacing_2 in range(user_input - lower_half):
        answer = ((answer) + " ")
    for spacing_2 in range(1, 2 * lower_half):
        answer = (answer + "*") 
    print(answer)
