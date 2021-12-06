
import math
from math import sqrt
x = int(input("Enter length for pentagon "))
print("")
print("With the given length, the perimeter of the pentagon will be")
total = str(x+x+x+x+x)
print("{} cm".format(total))
print("")
area = (sqrt(5 * (5 + 2 *
                  (sqrt(5)))) * x * x) / 4
print("The area of the pentagon will be ")
print("{} cm^2 ".format(area))
