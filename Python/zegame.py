print("Welcome to zegame, youngling! In this game, you will navigate yourself through a maze, trying to get to E. You are &. If you touch a wall, you will go back to the starting point. Good luck!")

x=2
y=1

zegame=[
    ["#","#","#","#","#","#","#","#"],
    ["#","#","#","-","-","-","#","#"],
    ["#","&","-","-","#","-","#","#"],
    ["#","#","#","#","-","-","#","#"],
    ["#","#","#","#","-","#","#","#"],
    ["#","#","#","#","-","#","#","#"],
    ["#","-","-","-","-","#","#","#"],
    ["#","E","#","-","-","#","#","#"],
    ["#","W","#","#","#","#","#","#",]
]


reachedDestination=False

while reachedDestination==False:

    for k in zegame:
        print(k)



    direction=input("Which direction would you like to go? Please input w, a, s, or d.").lower()


    if direction=="w" and zegame[x-1][y]=="-":
        x-=1
        zegame[x][y]="&"
        zegame[x+1][y]="-"
    elif direction=="w" and zegame[x-1][y]=="#":
        print("You bumped into the wall! Choose a different one.")
    elif direction=="a" and zegame[x][y-1]=="-":
        y-=1
        zegame[x][y]="&"
        zegame[x][y+1]="-"
    elif direction=="a" and zegame[x][y-1]=="#":
        print("You bumped into the wall! Choose a different one.")
    elif direction=="d" and zegame[x][y+1]=="-":
        y+=1
        zegame[x][y]="&"
        zegame[x][y-1]="-"
    elif direction=="d" and zegame[x][y+1]=="#":
        print("You bumped into the wall! Choose a different one.")
    elif direction=="s" and zegame[x+1][y]=="-":
        x+=1
        zegame[x][y]="&"
        zegame[x-1][y]="-"
    elif direction=="s" and zegame[x+1][y]=="#":
        print("You bumped into the wall! Choose a different one.")

    elif zegame[6][1]=="&":
        if direction=="s" and zegame[7][1]=="E":
            zegame[6][1]="-"
            zegame[7][1]="&"
            print("You reached E! Congratulations!")
            reachedDestination==True
            break
   
for k in zegame:
    print(k)