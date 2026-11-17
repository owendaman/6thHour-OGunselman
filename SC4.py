#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
player_count = int(input("How many players?"))
a = 0
ratings = []
for player_count in range(1,player_count+1):
    print("player",player_count,"is up")
    a = int(input("Rate the model out of 5"))
    ratings.append(a)
    if a > 5 or a < 0:
        print("1 to 5 idiot")
        break
added =sum(ratings)
average = added/player_count
print(average)
