#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: HW13
import random
#1. Import the random function

#2. Create a variable called 'temp' that randomly generates a number between 1 and 30
temp = random.randint(1,30)
#3. Go to the link below and convert the flowchart into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

#create temp
#If temp > 20 print ("It is hot")
#elif temp > 10 print ("It is mild")
#else print ("It is cold")
#   print ("Thank You")

print(temp)
if temp > 20:
    print("It is hot")

elif temp > 10:
    print("It is mild")

else:
    print("It is cold")
print("Thank You")




