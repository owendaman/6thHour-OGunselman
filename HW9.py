#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
primary_dict = {
    "poop" : "wonder",
    "numbers" : [69,420,67],
    "skin cancer" : "melanoma"
}
#3. Print the keys of the dictionary from #2.
print(primary_dict.keys())
#4. Print the values of the dictionary from #2
print(primary_dict.values())
#5. Print one of the three numbers from the list by itself
print(primary_dict["numbers"][2])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
primary_dict.update({"Family" : "Guy"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(primary_dict)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
class_n_stuff = {
    "Tucker" : {
        "grade" : 12,
        "funny" : True
    },

    "Matthew" : {
        "grade" : 12,
        "funny" : False},

    "Owyn" : {
        "grade" : 9,
    "chud" : True}
}
#9. Print the names of all three classmates on the same line.
print(class_n_stuff.keys())
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
class_n_stuff.pop("Owyn")
print(class_n_stuff)