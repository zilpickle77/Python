anotherlist=[1,2,3,4,5,6,7,8]
anotherlist.reverse()
print(anotherlist)

emptyHat=[]
hat=["hello","hi","goodbye"]
for i in range(0,3):
    #includes 0 but doesn't include 3, hence inclusive 0-2
    x=hat[i]
    emptyHat.insert(0,x)
    #puts every x from front to back of hat into the back of emptyHat
print(emptyHat)