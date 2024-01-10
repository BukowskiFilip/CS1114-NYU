import math
import random

days_semi = int(input("Please enter the number of days Semi has worked: "))
hours_semi = int(input("Please enter the number of hours Semi has worked: "))
minutes_semi = int(input("Please enter the number of minutes Semi has worked: "))
days_daniel = int(input("Please enter the number of days Semi has worked: "))
hours_daniel = int(input("Please enter the number of hours Semi has worked: "))
minutes_daniel = int(input("Please enter the number of minutes Semi has worked: "))


semi_total = (((days_semi) * ((24)*(60)*(60)))+((hours_semi) * ((60)*(60))) + ((minutes_semi) * (60)))

daniel_total = (((days_daniel) * ((24)*(60)*(60)))+((hours_daniel) * ((60)*(60))) + ((minutes_daniel) * (60)))

seconds_total = semi_total + daniel_total

total_days = seconds_total // ((24)*(60)*(60))
seconds_total_hour = seconds_total % ((24)*(60)*(60))
total_hours = seconds_total_hour // ((60)*(60))
seconds_total_minute = seconds_total_hour % ((60)*(60))
total_minutes = seconds_total_minute // 60

print("The total time both of them worked together is: " + str(total_days) + " days, " + str(total_hours) + " hours and " + str(total_minutes) + " minutes.")

