#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library
import random
from random import shuffle

#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(a,b,c)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
sum_a=(a+2)
sum_b=(b-4)
sum_c=(c*1.5)
#6. Print each result from #5 on the same line.
print(sum_a,sum_b,sum_c)
#7. Create a list containing four values that each randomly generate an integer between 1 and 6
list_d=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
list_d.sort()
print(list_d)
#9. Add together the highest three numbers in the list from #7 and print the result.
list_d_sum=list_d[1]+list_d[2]+list_d[3]
print(list_d_sum)
#10. Create a list with 5 names of other students in this class and print the list.
list_name=["matthew","tucker","owyn","misa","malachai"]
#11. Shuffle the list in #10 and print the list again.
shuffle(list_name)
print(list_name)
#12. Print a random choice from the list of names from #10.
list_name_random= random.choice(list_name)
print(list_name_random)