changed_letters = 0
unchanged_letters = 0
non_alpabetical_characters = 0

user_input = input("Say something: ")

answer = ""

for i in range(len(user_input)):
    ord_value = ord(user_input[i])
    if ord_value >= 97 and ord_value <= 122:
        
        answer += user_input[i]
        
        unchanged_letters += 1
        
    elif ord_value >= 65 and ord_value <= 90:
        
        new_value = chr(ord_value + 32)
       
        changed_letters += 1
        
        answer += new_value
        
    else:
        answer += user_input[i]
        
        non_alpabetical_characters += 1

print(answer)
print("Number of changed letters: " + str(changed_letters))
print("Number of unchanged letters: " + str(unchanged_letters))
print("Number of non-alphabetic characters: " + str(non_alpabetical_characters))
