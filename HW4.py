#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW4
import math
from math import sqrt, ceil, floor

#1. Print "Hello World!"
print("Hello World")
#2. import the 'math' library

#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
x= float(input("Enter a decimal"))
y= int(input("Enter a integer"))
#4. Create a variable with the value that is x and y added together.
z=(x+y)
#5. Print the variable from #4.
print(z)
#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
a=(z/3)
#7. Print the variable from #6.
print(a)
#8. Create a variable with the value of the square root of y, then print the result.
b=sqrt(y)
print(b)
#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
c=round(x,1)
print(c)
#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
d=ceil(x)
print(d)
#11. Use the floor function to round x down to the nearest whole number. Print the result.
e=floor(x)
print(e)