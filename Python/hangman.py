print("Welcome......to HANGMAN!!!!!!!")

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
secretword=[
    'abandon', 'ability', 'account', 'advance', 'balance', 'capital', 'deliver', 'economy', 'freedom', 'general',
    'history', 'improve', 'justice', 'keyword', 'library', 'mission', 'network', 'opinion', 'primary', 'quality',
    'routine', 'service', 'support', 'trouble', 'victory', 'weather', 'welcome', 'account', 'balance', 'catalog',
    'conduct', 'deliver', 'fiction', 'general', 'highway', 'install', 'journey', 'keyword', 'library',
    'measure', 'network', 'operate', 'primary', 'station', 'trouble', 'victory', 'weather',
    'analyze', 'balance', 'journey', 'analyze', 'balance'
]
notdead=True
import random
secretword=random.choice(secretword)
secretList=[
    "_","_","_","_","_","_","_"
]
# playerletter=input("Guess a letter! ").lower()
# Check Guess #
print(hangman[0])
x=0
allTriedLetters=""
while notdead == True:
    secretGuess=""
    playerletter=input("Guess a letter! ").lower()
    if playerletter in secretword and playerletter not in allTriedLetters:
        allTriedLetters+=playerletter
        for i in range(0,7):
            if playerletter==secretword[i]:
                secretList[i]=playerletter
        print(secretList)
    elif playerletter in allTriedLetters:
        print("You have already tried this letter.")
    else:
        allTriedLetters+=playerletter
        x+=1
        print(hangman[x])
        if x==6:
          print("You ran out of tries!")
          print("The secret word was",secretword.upper(),".")
          break
    for k in secretList:
        secretGuess+=k
    if secretGuess==secretword:
        print("You guessed the secret word and saved hangman!")
        break
        # SHow where the letter appears in the secret word (Similar to wordle)
        # does NOT increment the hangman progress
            
"""  else:
        for i in hangman:
            print(i)
        # do something to hangman"""