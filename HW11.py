#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW11
import random


#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
Ripvanwinkle = [
     random.randint(1,100),
     random.randint(1,100),
     random.randint(1,100)
]
#3. Print the list.
print(Ripvanwinkle)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if Ripvanwinkle[0] > Ripvanwinkle[1] and Ripvanwinkle[0] > Ripvanwinkle[2]:
    print("First is the highest")
    num=Ripvanwinkle[0]
elif Ripvanwinkle[1] > Ripvanwinkle[0] and Ripvanwinkle[1] > Ripvanwinkle[2]:
    print("Second is the highest")
    num=Ripvanwinkle[1]
else:
    print("Third is the highest")
    num=Ripvanwinkle[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".
print(num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    if num % 2 == 0:
        print("Divisible by 2")
    elif num % 3 == 0:
        print("Divisible by 3")
    else:
        print("Divisible by neither")

