print("")
print("Welcome to the ALIEN GAME!")
print("You have stolen a UFO to make your way across outer space.")
print("The aliens want their UFO back and are chasing you down!")
print("Survive and outrun the aliens!")
done=False
milesTraveled=0
thirst=0
tiredness=0
alienDistanceBehind=20
drinksInBottle=3
while not done:
    print("")
    print("A. Drink from your water bottle.")
    print("B. Speed up at moderate speed.")
    print("C. Speed up at full speed.")
    print("D. Rest.")
    print("E. Status check.")
    print("Q. Quit")
    print("")
    user_choice=input("Please type the letter that you would like to choose. ").upper()
    if user_choice=="Q":
        done=True
        print("You quit the game.")
    elif user_choice=="E":
        print("Miles traveled:", milesTraveled)
        print("Drinks in water bottle:", drinksInBottle)
        print("The aliens are",alienDistanceBehind,"miles behind you.")
    elif user_choice=="D":
        tiredness=0
        print("You are well rested and ready to continue flying the UFO.")
        import random
        x=random.randint(7,15)
        alienDistanceBehind += x
    elif user_choice=="C":
        import random
        x=random.randint(10,21)
        milesTraveled += x
        print("You traveled",milesTraveled,"miles")
        thirst += 1
        import random
        x=random.randint(1,3)
        tiredness += x
        import random
        x=random.randint(8,15)
        alienDistanceBehind += x
    elif user_choice=="B":
        import random
        x=random.randint(5,13)
        milesTraveled += x
        print("You traveled",milesTraveled,"miles")
        thirst += 0.5
        tiredness += 1
        import random
        x=random.randint(6,13)
        alienDistanceBehind += x
    elif user_choice=="A":
        if drinksInBottle>0:
            drinksInBottle -= 1
            thirst=0
            print("You have been hydrated and are ready to keep going.")
        else:
            print("Error. You have ran out of water bottles.")
    if 6>thirst>=4:
        print("You are thirsty.")
    elif thirst>6:
        done=True
        print("You fainted of thirst and the aliens caught up! The aliens caught you and you lost the game.")
    if 8>tiredness>=5:
        print("You are tired.")
    if tiredness>8:
        done=True
        print("You fell asleep while flying the UFO and the aliens caught up! The aliens caught you and you lost the game.")
    elif alienDistanceBehind<15:
        print("The aliens are getting close!")
    if milesTraveled>=200:
        done=True
        print ("You won!")