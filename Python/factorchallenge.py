playerinput=int(input("What number do you want to be factored?"))
f = 1
for i in range(playerinput,0,-1):
    #the 1 is what it ends at
    #the -1 is what it decreases by
    f *= i
print(f)