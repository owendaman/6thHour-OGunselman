#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW12


#1. Print Hello World!
print("Hello World")
#2. Create three different boolean variables named wifi, login, and admin.
Wifi =  True
Login = False
Admin = False
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
admin_logins = 67
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if Wifi == True:
    if Login == True:
        if Admin == True:
            print("Welcome you chud")
            admin_logins += 1
        else:
            print("Error Admin missing")
    else:
        print("Error Login missing")
else :
    print("Error Wifi missing")


