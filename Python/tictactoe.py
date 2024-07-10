gameboard=[
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

print("Welome to Tic-Tac-Toe")

def checkwin(m,j):

    if m[0][0]==j and m[0][1]==j and m[0][2]==j:
        return True
    elif m[1][0]==j and m[1][1]==j and m[1][2]==j:
        return True
    elif m[2][0]==j and m[2][1]==j and m[2][2]==j:
       return True
    elif m[0][0]==j and m[1][0]==j and m[2][0]==j:
       return True
    elif m[0][1]==j and m[1][1]==j and m[2][1]==j:
       return True
    elif m[0][2]==j and m[1][2]==j and m[2][2]==j:
       return True
    elif m[0][2]==j and m[1][1]==j and m[2][0]==j:
       return True
    elif m[0][0]==j and m[1][1]==j and m[2][2]==j:
       return True
    else:
        return False

for i in range(0,5):
    for k in gameboard:
            print(k)

    while True:
        player1Row = int(input("Player 1, you are X. What is the row that you would like to go? "))
        player1Column = int(input("What is the column that you would like to go? "))

        if gameboard[player1Row-1][player1Column-1]=="-":
            gameboard[player1Row-1][player1Column-1]="X"
            break
        else:
            print("Someone's already here, try another position!!")

    if checkwin(gameboard,"X")==True:
        print("X won!")
        for k in gameboard:
            print
        break

    if checkwin(gameboard,"X")==False and checkwin(gameboard,"O")==False and i==4:
        print("TIEEEEEEEEE")
        break

    
    for k in gameboard:
            print(k)    

    while True:
        player2Row=int(input("Player 2, you are O. What is the row that you would like to go? "))
        player2Column=int(input("What is the column that you would like to go? "))

        if gameboard[player2Row-1][player2Column-1]=="-":
            gameboard[player2Row-1][player2Column-1]="O"
            break
        else:
            print("Someone's already here, try another position!!")

    if checkwin(gameboard,"O")==True:
        print("O won!")
        break

 