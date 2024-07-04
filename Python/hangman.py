print("Welcome......to HANGMAN!!!!!!!")
hangman=[
    ["       _____________"],
    ["       |           |"],
    ["                   |"],
    ["                   |"],
    ["                   |"],
    ["                   |"],
    ["                   |"],
    ["                   |"],
    ["                   |"],
    ["                   |"],
    ["                   |"],
    ["                   |"],
    ["        ____________"],
    ["                    "]
]
for i in hangman:
    print(i)

secretwords=[
    'abandon', 'ability', 'account', 'advance', 'balance', 'capital', 'deliver', 'economy', 'freedom', 'general',
    'history', 'improve', 'justice', 'keyword', 'library', 'mission', 'network', 'opinion', 'primary', 'quality',
    'routine', 'service', 'support', 'trouble', 'victory', 'weather', 'welcome', 'account', 'balance', 'catalog',
    'conduct', 'deliver', 'fiction', 'general', 'highway', 'install', 'journey', 'keyword', 'library',
    'measure', 'network', 'operate', 'primary', 'station', 'trouble', 'victory', 'weather',
    'analyze', 'balance', 'journey', 'analyze', 'balance'
]
import random
secretword=random.choice(secretwords)
secretList=["_ _ _ _ _ _ _"]
playerguess=input("Guess a letter! ").lower()
for playerguess in secretword: