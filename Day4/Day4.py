import copy
file = open("Data.txt",'r')
data = file.readlines()
file.close()

#manually copied bcs pffffft
chosenNumbers = [37,60,87,13,34,72,45,49,61,27,97,88,50,30,76,40,63,9,38,67,82,6,59,90,99,54,11,66,98,23,64,14,18,4,10,89,46,32,19,5,1,53,25,96,2,12,86,58,41,68,95,8,7,3,85,70,35,55,77,44,36,51,15,52,56,57,91,16,71,92,84,17,33,29,47,75,80,39,83,74,73,65,78,69,21,42,31,93,22,62,24,48,81,0,26,43,20,28,94,79]

def findFirstWinnerNumber():
    for num in chosenNumbers:
        print(num)
        updateBoards(num)
        win, c = checkWin()
        
        if win:
            bb = allBoardsBools[c]
            wb = allBoards[c]
            winNumber = getWinningNumber(bb, wb)
            solution = num * winNumber
            print(solution)
            break

def findLastWinnerNumber():
    winners = []
    for num in chosenNumbers:
        updateBoards(num)
        win, c = checkWin()
        while (win):
            bb = allBoardsBools.pop(c)
            print(len(allBoards))
            wb = allBoards.pop(c)
            
            winners.append({"board" : copy.deepcopy(wb), "bools" : copy.deepcopy(bb), "number" : num})
            win, c = checkWin()
            
            
    lastWinner = winners.pop()
    print(lastWinner["bools"])
    winNumber = getWinningNumber(lastWinner["bools"], lastWinner["board"])
    print(lastWinner["number"])
    print(winNumber)
    solution = lastWinner["number"] * winNumber
    print(solution)



def updateBoards(num):
    for b, board in enumerate(allBoards):
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                if int(column) == int(num):
                    allBoardsBools[b][i][j] = True

def checkWin():
    for count, board in enumerate(allBoardsBools):
        for i in board:
            #rows
            if all(i):
                return True, count
        # columns
        for k in range(5):
            if board[0][k] and board[1][k] and board[2][k] and board[3][k] and board[4][k]:
                return True, count
        #diagonals:
        if board[0][0] and board[1][1] and board[2][2] and board[3][3] and board[4][4]:
            return True, count
        if board[0][4] and board[1][3] and board[2][2] and board[3][1] and board[4][0]:
            return True, count
    return False, -1


def getWinningNumber(boolboard, winBoard):
    winSum = 0
    for i in range(5):
        for j in range(5):
            if (not boolboard[i][j]):
                winSum += int(winBoard[i][j])
    return winSum
    


def initializeBoards():
    

    currentboard = []
    for b in data:
        if b == '\n':
            allBoards.append(currentboard)
            allBoardsBools.append([[False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False]])
            currentboard = []
            continue
        currentboard.append(b.split()) # every row is now an array, every board an array of arrays and all boards an array of arrays of arrays :)

#manually copied bcs pffffft
chosenNumbers = [37,60,87,13,34,72,45,49,61,27,97,88,50,30,76,40,63,9,38,67,82,6,59,90,99,54,11,66,98,23,64,14,18,4,10,89,46,32,19,5,1,53,25,96,2,12,86,58,41,68,95,8,7,3,85,70,35,55,77,44,36,51,15,52,56,57,91,16,71,92,84,17,33,29,47,75,80,39,83,74,73,65,78,69,21,42,31,93,22,62,24,48,81,0,26,43,20,28,94,79]

allBoards = []
allBoardsBools = []
#part 1
initializeBoards()
findFirstWinnerNumber()

#part 2
allBoards = []
allBoardsBools = []
initializeBoards()
findLastWinnerNumber()