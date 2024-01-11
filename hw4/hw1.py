user_input = int(input("Please enter a positive integer: "))
counter = 0
value = 1

print("Executing while-loop...")

while counter < user_input:
    print(value)
    value += 2
    counter += 1
    
print(" ")

print("Executing for-loop...")

value_2 = 1

for number_2 in range(user_input):
    print (value_2)
    value_2 += 2
