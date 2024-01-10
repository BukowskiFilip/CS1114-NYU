#check discriminant to figure out solutions
#if a is zero no solutions cause divided by 0
#if all zero, infinite

import math
import random

value_of_a = float(input("Please enter value of a: "))
value_of_b = float(input("Please enter value of b: "))
value_of_c = float(input("Please enter value of c: "))

discriminant = math.pow(value_of_b,2) - (4 * value_of_a * value_of_c)

if value_of_a == 0 and value_of_b == 0 and value_of_c == 0:
    print("This equation has an infinite number of solutions.")
    
elif value_of_a == 0:
    print("This equation has no solution.")
    
else:
    if discriminant < 0:
        print("This equation has no real solution.")
        
    elif discriminant == 0:
        solution_of_first = (((-value_of_b) + math.sqrt(discriminant)) / (2 * value_of_a))
        print("This equation has 1 solution, x =", solution_of_first)
        
    elif discriminant > 0:
        solution_of_first = (((-value_of_b) + math.sqrt(discriminant)) / (2 * value_of_a))
        solution_of_second = (((-value_of_b) - math.sqrt(discriminant)) / (2 * value_of_a))
        print("This equation has 2 solutions, x =", solution_of_first, "x =", solution_of_second)
