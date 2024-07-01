a=[1,'h',1]
b=[0,'y',0]
c=[0,'j',1]
print(a)
print(b)
print(c)

if a[0]==1 and a[2]==1:
    print("you won!")
elif a[0]==1 and a[2]==0 or a[0]==0 and a[2]==1:
    print("you're close to winning!")
else:
    print("you lost")

if b[0]==0 and b[2]==0:
    print("you won!")
elif b[0]==1 and b[2]==0 or b[0]==0 and b[2]==1:
    print("you're close to winning!")
else:
    print("you lost")

if c[0]==0 and c[2]==1:
    print("you won!")
elif c[0]==0 and c[2]==0 or c[0]==1 and c[2]==1:
    print("you're close to winning!")
else:
    print("you lost")