print("Welcome to Wordle!")
gameboard=[
    ['*','*','*','*','*'],
    ['*','*','*','*','*'],
    ['*','*','*','*','*'],
    ['*','*','*','*','*'],
    ['*','*','*','*','*'],
    ['*','*','*','*','*']
 ]

for k in gameboard:
    print(k)
print("In this game, you will get 6 chances to guess a five-letter word. If you get the correct letter in the correct place, it will be capital. If you get the correct letter in the wrong place, it will be lowercase. If you get the wrong letter in the wrong place, it will have an asterisk next to it. Good luck!")

words = [
    "apple", "batch", "cloak", "drape", "equip",
    "flute", "giant", "hurry", "ivory", "joint",
    "knife", "large", "match", "noble", "opera",
    "piano", "quake", "route", "shake", "table",
    "umbra", "vault", "whale", "yield",
    "zebra", "abide", "blend", "chime", "decoy",
    "elbow", "ferry", "globe", "hover", "ideal",
    "jolly", "knell", "lemon", "mango", "never",
    "oasis", "pouch", "query", "raise", "swoop",
    "tulip", "union", "vocal", "wound", "xenon",
    "young", "zesty", "adapt", "blink", "crisp",
    "dough", "error", "flock", "gravy", "hoist",
    "image", "jumbo", "knots", "laser", "mocha",
    "nymph", "olive", "paste", "quick", "radar",
    "shark", "theme", "unity", "video", "whisk",
    "xylon", "yearn", "hello", "abuzz", "blade",
    "charm", "daisy", "elate", "flask", "gleam",
    "havoc", "index", "dolly", "kudos", "leash",
    "mirth", "novel", "ocean", "puppy", "quilt",
    "rover", "stark", "trump", "vivid", "witty",
    "xylog", "youth", "zappy"
]

import random
secretword=random.choice(words)

for i in range(0,6):
    playerguess=input("Guess a word! ").lower()
    if playerguess==secretword:
        print("Congratulations! You guessed the word!")
        break
    else:
        for j in range(0,5):
            gameboard[i][j]=playerguess[j]
            if secretword[j]==playerguess[j]:
                gameboard[i][j]=gameboard[i][j].upper()
            elif playerguess[j] in secretword:
                 gameboard[i][j]=gameboard[i][j]+"*"

    for k in gameboard:
                print(k)
print("You ran out of tries!")
print("The secret word was",secretword.upper(),".")