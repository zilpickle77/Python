for i in range(0,3492878424782348972342934284387423874234872497234875):
    print("Welcome to ze game of rock, paper, scissors.")
    words = [
    "SCISSORS",
    "PAPER",
    "ROCK"
    ]
    import random
    secretThing=random.choice(words)

    playerchoice=input(("What would you like to do? Rock, paper, or scissors?")).upper()
    if playerchoice==secretThing:
        print("It was a tie!")
    if playerchoice=="ROCK" and secretThing=="SCISSORS":
        print("The bot chose SCISSORS! Rock smashes scissors, and you win!")
    if playerchoice=="SCISSORS" and secretThing=="PAPER":
        print("The bot chose PAPER! Scissors cut paper, and you win!")
    if playerchoice=="PAPER" and secretThing=="ROCK":
        print("The bot chose ROCK! Paper covers rock, and you win!")
    if secretThing=="ROCK" and playerchoice=="SCISSORS":
        print("The bot chose ROCK! Rock smashes scissors, and you lost!")
    if secretThing=="SCISSORS" and playerchoice=="PAPER":
        print("The bot chose SCISSORS! Scissors cut paper, and you lost!")
    if secretThing=="PAPER" and playerchoice=="ROCK":
        print("The bot chose PAPER! Paper covers rock, and you lost!")
    input("Press enter to play again.")