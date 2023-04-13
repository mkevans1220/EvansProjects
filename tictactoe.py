import random
#prnting the game board 
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

currentPlayer = "X"
winner = None
gameRunning = True

def printboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8]) 
    print("------")

#checks player1 input
def playerInput():
    while True:
        inp = int(input("Enter a number 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-": 
            board[inp-1] = currentPlayer
            break
        else:
            print("choose again , player already there!")
    

#checks if player input results in win or tie
def checkHorizontal():
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkRow(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-": 
        winner = board[2]
        return True
    
def checkdiag():
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return winner 
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
        print(f"the winner is: {winner}")

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printboard(board)
        print("Tie! go again")
        gameRunning = False

def checkWin():
    if checkHorizontal() or checkdiag() or checkRow(board): 
        print(f"the winner is {winner}")

#switch player
def switchplayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


#check for win or tie again 

while winner == None:
    printboard(board)
    playerInput()
    checkWin()
    checkTie(board)
    switchplayer()
    checkWin()
    checkTie(board)
print(f"winner is {winner}")
printboard(board) 