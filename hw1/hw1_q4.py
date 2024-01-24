#question correct 3/3


print("Please enter your amount of dollars and cents, in two seperate lines.")

user_dollars = int(input(" "))
user_cents = int(input(" "))


user_total = ((user_dollars * 100) + (user_cents))

user_quarters = (user_total//25)
user_total2 = (user_total % 25)
user_dimes = (user_total2 // 10)
user_total3 = (user_total2 % 10)
user_nickels = (user_total3 // 5)
user_total4 = (user_total3 % 5)
user_pennies = (user_total4)

print(str(user_dollars) + " dollars and " + str(user_cents) + " cents are: " + str(user_quarters) +  " quarters, " + str(user_dimes) + " dimes, " + str(user_nickels) + " nickels and " + str(user_pennies) + " pennies")





