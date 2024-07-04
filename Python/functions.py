def roastMarshmallow ():
    print("1. Start a bonfire.")
    print("2. Put marshmallow on stick.")
    print("3. Roast marshmallow on top on fire until golden.")
    print("4. Take marshmallow off the stick and eat it.")

for i in range(0,5):
    roastMarshmallow()

def product(x,y):
    this = x*y
    return this
a=product(5,6)
print(a)

def aTestFunction(ParamA,ParamB):
    hello=ParamA*ParamB
    return hello
hi=aTestFunction(4,8)
print(hi)

def anotherFunction(ParamA):
    if (ParamA == True):
        return 23498
print(anotherFunction(True))

#assignment
def anotherFunction(thislist):
    for i in thislist:
        print(i)
thislist=[1,2,3]
anotherFunction(thislist)

def factorFunction(x):
    f=1
    for i in range(x,0,-1):
        f*=i
    print(f)
factorFunction(5)

def lengthFunction(e):
    print(len(e))
lengthFunction("Hello")

#activity
prices=[10,20,30,40,50]
def priceFunction(k):
    for k in prices:
        print(float(0.2*k))
priceFunction(prices)