import random
x=random.randint(0,100)

for i in range(0,100):
    difficulty=input("Welcome, youngling, to guess the number from 0-100. Would you like easy (15 guesses), medium (10 guesses), or hard (5 guesses)? ").lower()
    if difficulty=="easy":
            tries=15
            break
    elif difficulty=="medium":
            tries=10
            break
    elif difficulty=="hard":
            tries=5
            break
    else:
        print("Whatt....................................... That is not a valid input please try again.")

while True:
    guess=int(input("guess a number. "))
    if guess<x:
        print("too low. ")
        tries-=1
        if tries==0:
            print("Womp womp. You ran out of tries! The number was",x)
            break
        print("You still have",tries,"tries.")
    if guess>x:
        print("too high. ")
        tries-=1
        if tries==0:
            print("Womp womp. You ran out of tries! The number was",x)
            break
        print("You still have",tries,"tries.")
    if guess==x:
        print("Congrats! You guessed it!")
        break