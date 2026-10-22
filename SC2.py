#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
usr_height = float(input("Height(In)"))
usr_weight = float(input("Weight(Ibs)"))


BMI = (usr_weight / (usr_height ** 2)) * 703
print(BMI)

if BMI > 30:
    print("YOU ARE OBESE BIG BOY")
if BMI > 25 and BMI < 29.9:
    print("You Are Over Weight")
if BMI > 18.5 and BMI < 24.9:
    print("You Normal Weight. Mr.Perfect")
if BMI < 18.5:
    print("You Are Underweight. You need a snickers or something lil buddy.")