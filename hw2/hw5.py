import math
import random

dean = input("Do you have permission from the dean? [y/n] ")
advisor = input("Do you have permission from your advisor? [y/n] ")
senior = input("Do you hold senior status? [y/n] ")
credits_amount = int(input("How many credits do you have? "))

dean_permission = dean == 'y'
advisor_permission = advisor == 'y'
senior_status = senior == 'y'


graduation = ( credits_amount >= 64 and senior_status) or (credits_amount >= 40 and advisor_permission) or (dean_permission)

print("This student can graduate: " + str(graduation))
