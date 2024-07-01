correctCount=0
firstAnswer=int(input("What is 20/5?"))
if firstAnswer == 4:
    print("Correct! Yippee!")
    correctCount += 1
else:
    print("Wrong. Womp womp.")
secondAnswer=input("Who is the face on the US dollar bill?")
if secondAnswer == "Benjamin Franklin" or "benjamin franklin" or "Benjamin franklin" or "benjamin Franklin":
    print("Achieved success.")
    correctCount += 1
else:
    print("Unsuccessful. Whoops.")
thirdAnswer=input("True or False: Hola means hello in Hawaiian.")
if thirdAnswer == "False" or "false":
    print("Yesssss!")
    correctCount += 1
else:
    print("Nah. Wrooong.")
fourthAnswer=input("Which of these following animals live in the sea? a.Human b.Whale c.Jaguar d.Panda")
if fourthAnswer=="b." or "B." or "b" or "B" or "whale" or "Whale":
    print("Good job!")
    correctCount += 1
else:
    print("Awww. Nope.")
print("Good job! You got", correctCount, "out of 4 questions correct.")