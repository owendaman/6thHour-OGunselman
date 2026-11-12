#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW16
import random
import time
#1. import the "random" library

#2. print "Hello World!"
print("Hello World")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a= int(input("Enter a number"))
b= int(input("Enter another number"))
c= int(input("Come on we are doing this again"))
#4. Add a and b together, then divide the sum by c. Print the result.
d = (a + b) / c
print(d)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
e = round(d)
print(e)
if e % 2 == 0:
    print("D is even")
else:
    print("D is odd")
#6. Create a list of five different random integers between 1 and 10.
z = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
print(z)
#7. Print the 4th number in the list.
print(z[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
z.append(random.randint(1,10))
print(z)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
z.sort(reverse=True)
print(z)
print(z[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
x=0
while x<=100:
    print(x)
    x=x+1
#11. Create a list containing the names of five other students in the classroom.
y= ["Tucker","Matthew","Owyn","Misa","Brayle"]
#12. Create a for loop that individually prints out the names of each student in the list.
for y[0] in y:
    print(y[0])
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
poop = 1
for poop in range(1,101):
    print(poop)
    poop+=1
    if poop % 10 ==0:break
#14. Free space. Do something creative. :)
print("I want to stick my head in a particle accelerator now")
o = 0
while o < 999999999999999999:
    print(o)
    time.sleep(5)
    o+=1