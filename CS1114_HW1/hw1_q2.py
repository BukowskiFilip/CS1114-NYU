"""
Author: [Filip Bukowski]
Assignment / Part: HW1 - Q1 (etc.)
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

user_year = int(input("Please enter a year greater than 2022: "))

current_population = 330109174
#birth every 9 seconds
#death every 18 seconds
#immigration every 40 seconds
#emigration every 60 seconds

#every 18 seconds = 1 person
#every 120 seconds = another person
#3600 seconds in an hour

population_18 = 3600//18

population_120 = 3600//120


population_increase_hour = ((population_18) + (population_120))

population_increase_day = ((population_increase_hour) * (24))

population_increase_year = ((population_increase_day) * (365))


year_gap = (user_year - 2022)
population_increase = ((year_gap) * (population_increase_year))


print("The population in year", str(user_year), "will be", str(population_increase + current_population))



