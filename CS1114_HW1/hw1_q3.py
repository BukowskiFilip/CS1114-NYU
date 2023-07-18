"""
Author: [Filip Bukowski]
Assignment / Part: HW1 - Q1 (etc.)
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter number of coins")
user_quarters = int(input("Number of quarters: "))
user_dimes = int(input("Number of dimes: "))
user_nickels = int(input("Number of nickels: "))
user_pennies = int(input("Number of pennies: "))

total_money = ((user_quarters * 25)+(user_dimes * 10) + (user_nickels * 5) + (user_pennies))

total_dollars = (total_money // 100)
total_cents = (total_money % 100)

print("The total is " + str(total_dollars) + " dollar(s) and " + str(total_cents) + " cent(s)")
