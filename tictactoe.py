board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
def displayBoard():
    print("| "+board[0]+" | "+board[1]+" | "+board[2]+" |");
    print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |");
    print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |");
   

#displayBoard()
   
   
def checkRow():
    if(board[0] == board[1] == board[2] and board[0] != "-"):
        if(board[0]=="X"):
            return "X"
        else:
            return "O"
       
    elif(board[3]==board[4] and board[4] == board[5] and board[3] !="-"):
        if(board[3]=="X"):
            return "X"
        else:
            return "O"
   
    elif ((board[6] == board[7]) and board[6] == board[8] and board[6] != "-"):
        if(board[6]=="X"):
            return "X"
        else:
            return "O"
    else:
        return 0
   
   
   
def checkColumn():
    if(board[0] == board[3] and board[0] == board[6] and board[0] != "-"):
        if(board[0]=="X"):
            return "X"
        else:
            return "O"
       
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != "-"):
        if(board[1]=="X"):
            return "X"
        else:
            return "O"
       
       
    elif(board[2] == board[5] and board[2] == board[8] and board[2] != "-"):
        if(board[2]=="X"):
            return "X"
        else:
            return "O"
       
    else:
        return 0
   
def checkDiagonal():
    if(board[0] == board[4] and board[0]==board[8] and board[0] != "-"):
        if(board[0]=="X"):
            return "X"
        else:
            return "O"
    elif(board[2] == board[4] and board[2] == board[6] and board[2] != "-"):
        if(board[2]=="X"):
            return "X"
        else:
            return "O"
    else:
        return 0;
   
def checkWin():
    '''print(checkRow());
    print(checkColumn());
    print(checkDiagonal());'''
    if(checkRow() == 0 and checkColumn() == 0 and checkDiagonal() == 0):
        return ["play","null"]
    else:
        if(checkRow() == "X" or checkColumn() == "X" or checkDiagonal() == "X"):
            winner="X"
        else:
            winner="O"
        return ["dont", winner]
   
#print(checkWin())

def checkTie():
    count=0;
    check=checkWin()
    for i in range(len(board)):
        if(board[i] == "O" or board[i] == "X"):
            count +=1;
    if(count == 9 and check[0]=="play"):
        return "dont";
    else :
        return "play";

#print(checkTie())

def handleTurn(player,symbol):
    while True:
        position = int(input("Enter your position "+player+": "))
        if(board[position-1]=="-"):
            board[position-1]=symbol
            break
        else:
            print("Don't Cheat")
            continue
   


def playGame():
    c=0;
    result1 = "play"
    result2="play"
    player1 = raw_input("Enter player 1's name: ");
    player2 = raw_input("Enter player 2's name: ");
    displayBoard()
    while True:
        if(c%2 == 0):
            handleTurn(player1,"X")
        else:
            handleTurn(player2,"O")
        displayBoard();
        #print(checkWin())
        result1 = checkWin();
        result2=checkTie();
        if(result1[0]=="dont"):
            if(result1[1]=="X"):
                name=player1
            else:
                name=player2
            print(name+" Won!!!!!!!!!!!")
            break
        if(result2=="dont"):
            print("Tied :)")
            break
        c += 1;
   
#playGame()
