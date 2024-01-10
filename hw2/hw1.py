import math
import random


GRAVITATIONAL_CONSTANT = (6 * (10 ** -11))

mass_of_first = float(input("Enter the mass of the first object: "))
radius_of_first = float(input("Enter the radius of the first object: "))
mass_of_second = float(input("Enter the mass of the second object: "))
radius_of_second = float(input("Enter the radius of the second object: "))
distance = float(input("Enter the distance between the surfaces of both objects: "))

gravitational_force = ((mass_of_first)*(mass_of_second)*(GRAVITATIONAL_CONSTANT)/((radius_of_second)+(radius_of_first)+(distance)) ** 2)

print("The force of gravitation between these two objects is " + str(gravitational_force) + " N.")

