#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
a = ["Palm","Beach","Pete","Palantir","Israel"]
#2. Append a new name onto the Name List.
a.append("Benjamin Netenyaho")
#3. Print out the 4th name on the list.
print(a[3])
#4. Create a list with 4 different integers in it.
b = [69,420,67,21]
#5. Insert a new integer into the 2nd spot and print the new list.
b.insert(1,19)
#6. Sort the list from lowest to highest and print the sorted list.
b.sort()
print(b)
#7. Add the 1st three numbers on the sorted list together and print the sum.
c = b[0]+b[1]+b[2]
print(c)
#8. Create a list with two strings, two integers, and two boolean values.
d = ["Flock","Cameraz",9,11,False,True]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(d[int(input("Index Value For the Second List"))])