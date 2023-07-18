#question correct 2/2





print("Please enter number of coins")
user_quarters = int(input("Number of quarters: "))
user_dimes = int(input("Number of dimes: "))
user_nickels = int(input("Number of nickels: "))
user_pennies = int(input("Number of pennies: "))

total_money = ((user_quarters * 25)+(user_dimes * 10) + (user_nickels * 5) + (user_pennies))

total_dollars = (total_money // 100)
total_cents = (total_money % 100)

print("The total is " + str(total_dollars) + " dollar(s) and " + str(total_cents) + " cent(s)")
