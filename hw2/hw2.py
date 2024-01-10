import math
import random

frequency = float(input("Enter a value for the frequency, w: "))
duration = float(input("Enter a value for the duration of the sound wave, T: "))

fourier_transform = (2 * math.sin(frequency*duration))/(frequency)

fourier_transform = round(fourier_transform,3)

print("The amplitude spectrum of this Fourier transform is: " + str(fourier_transform))

