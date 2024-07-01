playerinput=int(input("what number do you want here?"))
f = 1
for i in range(playerinput,0,-1):
    #the 1 is what it ends at
    #the -1 is what it decreases by
    f *= i
print(f)