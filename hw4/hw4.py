answer = " "

user_input = int(input("Input a positive integer: "))

for number in range(1, user_input + 1):
    even = 0
    odd = 0
    for digit in str(number):
        number_2 = int(digit)
        if number_2 % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        answer = answer + str(number) + " "
        
print(answer)
