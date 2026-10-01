#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game

enemy_database = {
    "Mara from Persona" : {
        "Hp" : 350,
        "Damage" : 145,
        "Endurance" : 75
    },

    "Jack Frost" : {
        "Hp" : 85,
        "Damage" : 40,
        "Endurance" : 17
    },

    "Grim Reaper" : {
        "Hp" : 850,
        "Damage" : 300,
        "Endurance" : 115
    },

    "Fruit Fly" : {
        "Hp" : 1,
        "Damage" : 999,
        "Endurance" : 1
    },

    "Pixie" : {
        "Hp" : 40,
        "Damage" : 15,
    "Endurance" : 5}

}
print(enemy_database)

enemy_database["Mara from Persona"].update({"Damage" : int(input("Mara from Persona Damage"))})
enemy_database["Jack Frost"].update({"Damage" : int(input("Jack Frost Damage"))})
enemy_database["Grim Reaper"].update({"Damage" : int(input("Grim Reaper Damage"))})
enemy_database["Fruit Fly"].update({"Damage" : int(input("Fruit Fly Damage"))})
enemy_database["Pixie"].update({"Damage" : int(input("Pixie Damage"))})
print(enemy_database)