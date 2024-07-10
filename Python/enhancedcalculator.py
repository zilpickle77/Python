print("Hello youngling. Welcome to the enhanced, I repeat, ENHANCED, calculator.")
print("A. Add numbers")
print("B. Subtract numbers")
print("C. Multiply numbers")
print("D. Divide numbers")
print("E. Exponentiation")
print("F. Quadratic Formula")
playerwish=input(("What would you like to do?")).upper()
lsdlist=[]
zlist=[]
if playerwish=="A":
    asdf=int(input("How many numbers would you like to add?"))
    for i in range(0,asdf):
        fsd=float(input("What is a number you would like to add?"))
        lsdlist.append(fsd)
    print(sum(lsdlist))
if playerwish=="B":
    asdf=float(input("What would you like your starting number to be?"))
    tree=int(input("How many numbers would you like to subtract from that number?"))
    for i in range(0,tree):
        fsd=float(input("What is a number you would like to subtract?"))
        zlist.append(fsd)
    print(asdf-sum(zlist))
if playerwish=="C":
    playerinput=int(input("How many numbers would you like to multiply?"))
    f = 1
    for i in range(0,playerinput):
        hj=float(input("What number would you like to multiply?"))
        f *= hj
    print(f)
if playerwish=="D":
    sdfkj=float(input("What would you like your starting number to be?"))
    playerinput=int(input("How many numbers would you like to divide that by?"))
    f = 1
    for i in range(0,playerinput):
        hj=float(input("What number would you like to divide that by?"))
        f *= hj
    print(sdfkj/f)
if playerwish=="E":
    playerinput=int(input("What would you like the base to be?"))
    road=int(input("How many numbers would you like to raise that to?"))
    for i in range(0,road):
        hj=float(input("What number would you like to raise the base by?"))
        playerinput **= hj
    print(playerinput)
if playerwish=="F":
    print("Right now, your quadratic equation is at ax^2+bx+c=0.")
    a=float(input("What would you like a to be?"))
    b=float(input("What would you like b to be?"))
    c=float(input("What would you like c to be?"))
    import math
    if b**2-4*a*c>0.0:
        x=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        print("X is equal to",x,"and",x2,".")
    if b**2-4*a*c==0.0:
        x=(-b/(2*a))
        
        print("X is equal to",x)
    if b**2-4*a*c<0.0:
        """x=+"i"
        (-b+math.sqrt(abs(b**2-4*a*c)))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)"""
        x=(-b/(2*a))
        y=math.sqrt(abs(b**2-4*a*c))/(2*a)
        print(str(x)+"+i"+str(y))