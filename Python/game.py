print("Welcome to the Skibbler Game! You will fight monsters and maintain your strength! You will win when your strength reaches 200. Copyright Ariel Wang for making the names")
strength=80
hello=False
print("You have", strength, "strength.")
print("You have the abiilty to fly.")
while not hello:
    print("")
    print("A. Status check.")
    print("B. Fight Rizzio. He has the ability to jump very high.")
    print("C. Fight Rizzman. He has the ability to summon vampires.")
    print("D. Fight Spiderizz. He has the ability to make spider webs and trap people.")
    print("Q. Quit")
    print("")
    user_choice=input("Please type the letter that you would like to choose. ").upper()
    if user_choice=="Q":
        hello=True
        print("You quit the game.")

    elif user_choice=="A":
        print("You have", strength, "strength")
        print("You have the abiilty to fly.")

    elif user_choice=="B":
        secondOne=input("You chose to fight Rizzio. If you defeat him, you will upgrade your strength by 40. Are you sure you would like to fight him? Yes or no? ").upper()
        if secondOne=="YES":
            lkjadf=input("Rizzio starts off by jumping up and landing on a cloud. Do you A. Fly and follow him or B. Stay on the ground? ").upper()
            if lkjadf=="A":
                strength+=40
                print("You pushed Rizzio off the cloud successfully defeated him. You have upgraded your strength by 40.")
            if lkjadf=="B":
                strength-=20
                print("Rizzio's teammate sneaked up on you and attacked you from the back. You have lost 10 strength.")
        if secondOne=="NO":
            print("You chickened out against Rizzio. Your status has not changed.")
    
    elif user_choice=="C":
        dfs=input("You chose to fight Rizzman. If you defeat him, you will upgrade your strength by 40. Are you sure you would like to fight him? Yes or no? ").upper()
        if dfs=="YES":
            lkjadf=input("Rizzman summons a circle of vampires that circle you. Do you A. Shoot each of them through the heart or B. Show them garlic? ").upper()
            if lkjadf=="A":
                strength-=30
                print("Oh no! You killed 3 vampires but the missed the other 5! They circled you and you were defeated. You lost 15 strength.")
            if lkjadf=="B":
                strength+=40
                print("All the vampires ran away! Rizzman is powerless. You won and upgraded your strength by 40!")
        if dfs=="NO":
            print("You chickened out against Rizzman. Your status has not changed.")
    
    elif user_choice=="D":
        sdf=input("You chose to fight Spiderizz. If you defeat him, you will upgrade your strength by 40. Are you sure you would like to fight him? Yes or no? ").upper()
        if sdf=="YES":
            ateh=input("Spiderizz traps you in a spiderweb. Do you A. Threaten him with Mary Jane or B. Break through the web? ").upper()
            if ateh=="A":
                strength+=40
                print("He surrenders. You won and upgraded your strength by 40.")
            if ateh=="B":
                print("You break through and he trapped you again. You break through and he trapped you again. You break through and he trapped you again. You break through and he trapped you again. You break through and he trapped you again. You break through and he trapped you again. It's an endless cycle and you run out of strength.")
                print("You lost the game.")
                hello=True
        if sdf=="NO":
            print("You chickened out against Rizzman. Your status has not changed.")
    
    if strength>=200:
        print("You won the game!")
        hello=True

    if strength<=0:
        hello=True
        print("You lost the game.")


