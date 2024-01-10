import math
import random

day_of_call = input("Enter the day the call started at: ")
call_start_time = float(input("Enter the time the call started at (hhmm): "))
duration_of_call = float(input("Enter the duration of the call (in minutes): "))

if (day_of_call == "Fri" or day_of_call == "Sat" or day_of_call == "Sun"):
    payment_weekend = duration_of_call * 0.10
    print("This call will cost $" + str(round(payment_weekend,1)))
elif (call_start_time >= 0.0500 and call_start_time <= 2100):
        payment_weekday_normal_time = duration_of_call * 0.55
        print("This call will cost $" + str(round(payment_weekday_normal_time,1)))
else:
        payment_weekday_not_normal_time = duration_of_call * 0.35
        print("This call will cost $" + str(round(payment_weekday_not_normal_time,1)))


