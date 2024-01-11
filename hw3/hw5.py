import math
import random

#sqrt 2 , 1 , 1 is right isosceles triangle
#all equal is equaliteral
#two sides even and random third is isoseles

length_first_side = float(input("Length of the first side: "))
length_second_side = float(input("Length of the second side: "))
length_third_side = float(input("Length of the third side: "))

if (length_first_side == length_second_side == length_third_side):
    print(str(length_first_side)+ ", " + str(length_second_side) + ", " + str(length_third_side) + " form an equlateral triangle")

elif length_first_side == length_second_side or length_first_side == length_third_side or length_second_side == length_third_side:
    if (length_first_side == length_third_side * math.sqrt(2)) or (length_second_side == length_third_side * math.sqrt(2)) or (length_third_side == length_first_side * math.sqrt(2)):
        print(str(length_first_side) + ", " + str(length_second_side) + ", " + str(length_third_side) + " form an isosceles right triangle")

    else:
        print(str(length_first_side) + ", " + str(length_second_side) + ", " + str(length_third_side) + " form an a isosceles triangle")

else:
     print(str(length_first_side) + ", " + str(length_second_side) + ", " + str(length_third_side) + " form an a scalene triangle")
