gameboard=[
    [0,1,2],
    [3,4,5],
    [6,7,8]
]


print("Welome to Tic-Tac-Toe")
for i in gameboard:
    print(i)

#TopLeft=gameboard([0][0])

player1Input = input("Player 1, you are X. Where do you wanna go? 0, 1, 2, 3, 4, 5, 6 ,7, or 8?")

if player1Input==0:
    gameboard[0][0]="X"

if player1Input==1:
    gameboard[0][1]="X"
if player1Input==2:
    gameboard[0][2]="X"

if player1Input==3:
    gameboard[1][0]="X"

if player1Input==4:
    gameboard[1][1]="X"

if player1Input==5:
    gameboard[1][2]="X"

if player1Input==6:
    gameboard[2][0]="X"

if player1Input==7:
    gameboard[2][1]="X"

if player1Input==8:
    gameboard[2][2]="X"
