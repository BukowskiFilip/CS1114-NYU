
user_input = int(input("Input a positive integer: "))
spacing = 0

for steps in range((1),(user_input + 1)):
    answer = ("")
    user_input -= 1
    spacing = ((user_input) * (" "))
    
    for counting in range(steps,0,-1):
        answer += str(counting)
        
    print(spacing + answer)
    
