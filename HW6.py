#Name:Owen Gunselman
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
a = [9,69,4,420,67,8006,76,9009,43]
#2. Sort the list from highest to lowest.
a.sort(reverse=True)
#3. Create an empty list.
b=[]
#4. Remove the median number from the first list and add it to the second list.
b.append(a.pop(3))
#5. Remove the first number from the first list and add it to the second list.
b.append(a.pop(0))
#6. Print both lists.
print(a)
print(b)
#7. Add the two numbers in the second list together and print the result.
c = b[0] + b[1]
print(c)

#8. Add the sum from #7 to the first list.
a.append(c)
#9. Sort the first list from lowest to highest and print it.
a.sort(reverse=False)
print(a)