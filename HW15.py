#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW15


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5,0,-1):
    print(i)
print("Hello World")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for b in range(1,31):
    if b%2==0:
        continue
    print(b)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for c in range(1,31):
    if c%3==0:
        continue
    print(c)
#4. Create a for loop that prints 5 different animals from a list.
animals = ["cat", "dog", "rabbit", "elephant", "Nautilus"]
for animal in animals:
    print(animal)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

for e in input("Give Me A Word")[::-1]:
    print(e)
#6. Create a list containing 10 integers of your choice and print the list.
martin = [67,69,420,911,711,42,777,8005,11,10]
print(martin)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for inti in martin:
    if inti%2==0:
       evenNumbers = evenNumbers + 1
    else:
        oddNumbers = oddNumbers + 1
print(evenNumbers)
print(oddNumbers)
#9. Create a variable that asks the user for an integer and an empty integer variable.
user_value = int(input("Give me a integer"))
empty_int = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for q in range(1,user_value+1):
        empty_int *= q

print(empty_int)
