import random

common_enemy_database = {
    "Slime":  {
        "HP" : 14 ,
        "Physical" : random.randint(2,5),
        "Magic" : 0,
        "Speed" : 2
    },
    "Lowly Spirit": {
        "HP" : 20 ,
        "Physical" : random.randint(1,3),
        "Magic" : random.randint(5,9),
        "Speed" : 4
    },
    "Explosive Bulb": {
        "HP" : 1 ,
        "Physical" : random.randint(13,19),
        "Magic" : 0,
        "Speed" : 1
    }
}
player = {
    "HP" : 20 ,
    "Physical" : random.randint(6,10),
    "Magic" : random.randint(2,7),
    "Speed" : 3
}
spawn = 0

encounter = random.randint(1,2)
if encounter == 1: fight=True
else: fight=False
if fight==True: print("Enemy Approaches")
if fight==True: spawn = random.randint(1,3)
if spawn==1: print("Slime Approaches")
elif spawn==2: print("Lowly Spirit Approaches")
elif spawn ==3: print("Explosive Bulb Approaches")
Turn=False
Act=0
if fight==True:
    if spawn==1:
        if player["Speed"] > common_enemy_database["Slime"]["Speed"]:Turn=True and print("Your Turn")
        else: print("Enemy Turn")

if fight==True:
    if spawn==2:
        if player["Speed"] > common_enemy_database["Lowly Spirit"]["Speed"]:Turn=True and print("Your Turn")
        else: print("Enemy Turn")

if fight==True:
    if spawn==3:
        if player["Speed"] > common_enemy_database["Explosive Bulb"]["Speed"]:Turn=True and print("Your Turn")
        else: print("Enemy Turn")

if Turn==True:
 Act = int(input("Attack 1 - Run 2"))
