'''
# Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''
from math import *
n=int(input("Enter a number: "))
print("Square root of",n,"is",sqrt(n))
print("Natural logarithm of",n,"is",log(n))
print("Sine of ",n,"is",sin(n))
