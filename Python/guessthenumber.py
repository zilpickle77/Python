import random
x=random.randint(0,100)
guess=int((input("guess a number.")))
while guess!=x:
    if guess<x:
        print("Not it.")
        print("too low.")
        guess=int((input("guess a number")))
    if guess>x:
        print("Not it.")
        print("too high.")
        guess=int((input("guess a number")))
print("Congrats! You guessed it!")