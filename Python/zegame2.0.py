print("Welcome to zegame, youngling! In this game, you will navigate yourself through a maze, trying to get to E. You are &. If you touch a wall, you will have to choose a different option. Ther B's are movable blocks. Good luck!")

x=2
y=1
zegame=[
    ["#","#","#","#","#","#","#","#"],
    ["#","#","#","-","-","-","#","#"],
    ["#","&","#","-","#","-","#","#"],
    ["#","-","B","-","-","-","#","#"],
    ["#","#","#","#","-","#","#","#"],
    ["#","-","-","B","-","#","#","#"],
    ["#","-","-","#","#","#","#","#"],
    ["#","E","#","#","#","#","#","#"],
    ["#","#","#","#","#","#","#","#",]
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
    elif direction=="w" and zegame[x-1][y]=="B" and zegame[x-2][y]=="-":
        x-=1
        zegame[x][y]="&"
        zegame[x+1][y]="-"
        zegame[x-1][y]="B"
    elif direction=="w" and zegame[x-1][y]=="#" or direction=="w" and zegame[x-1][y]=="B" and zegame[x-2][y]=="-":
        print("You bumped into the wall! Choose a different one.")
    
    
    elif direction=="a" and zegame[x][y-1]=="-":
        y-=1
        zegame[x][y]="&"
        zegame[x][y+1]="-"
    elif direction=="a" and zegame[x][y-1]=="B" and zegame[x][y-2]=="-":
        y-=1
        zegame[x][y]="&"
        zegame[x][y+1]="-"
        zegame[x][y-1]="B"
    elif direction=="a" and zegame[x][y-1]=="#" or direction=="a" and zegame[x][y-1]=="B" and zegame[x][y-2]=="#":
        print("You bumped into the wall! Choose a different one.")
    
    
    elif direction=="d" and zegame[x][y+1]=="-":
        y+=1
        zegame[x][y]="&"
        zegame[x][y-1]="-"
    elif direction=="d" and zegame[x][y+1]=="B" and zegame[x][y+2]=="-":
        y+=1
        zegame[x][y]="&"
        zegame[x][y-1]="-"
        zegame[x][y+1]="B"
    elif direction=="d" and zegame[x][y+1]=="#" or direction=="d" and zegame[x][y+1]=="B" and zegame[x][y+2]=="#":
        print("You bumped into the wall! Choose a different one.")
    
    
    elif direction=="s" and zegame[x+1][y]=="-":
        x+=1
        zegame[x][y]="&"
        zegame[x-1][y]="-"
    elif direction=="s" and zegame[x+1][y]=="B" and zegame[x+2][y]=="-":
        x+=1
        zegame[x][y]="&"
        zegame[x-1][y]="-"
        zegame[x+1][y]="B"
    elif direction=="s" and zegame[x+1][y]=="#" or direction=="s" and zegame[x+1][y]=="B" and zegame[x+2][y]=="#":
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