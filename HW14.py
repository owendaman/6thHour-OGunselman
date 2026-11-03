#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW14
import random

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i=5
while i>=0:
    print(i)
    i-=1
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
b=0
print("Even Numbers")
while b<= 30:
    print(b)
    if b%2==0:
        b+=2

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
c=0
while c<30:
    c+=1
    if c%3==0:
        continue
    print(c)
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
d=0
while d!=1:
    d=random.randint(1,6)
    print(d)

d = random.randint(1,6)
#5. Create a while loop that asks for a number input until the user inputs the number 0.
user_input = 999
while user_input!=0:
   user_input = int(input("Enter a number"))