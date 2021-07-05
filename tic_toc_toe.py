import random

def drawBoard(board):
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print('- + - + -')
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print('- + - + -')
    print(f"{board[1]} | {board[2]} | {board[3]}")

def inputPlayerLetter():
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    return int(move) == 'letter'

def isWinner(bo, le):
        return ((bo[8] == bo[7] == bo[9] == le) or
               (bo[4] == bo[5] == bo[6] == le) or
               (bo[1] == bo[2] == bo[3] == le) or
               (bo[7] == bo[4] == bo[1] == le) or
               (bo[8] == bo[5] == bo[2] == le) or
               (bo[9] == bo[6] == bo[3] == le) or
               (bo[7] == bo[5] == bo[3] == le) or
               (bo[9] == bo[5] == bo[1] == le))

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return int(move) == ' '

def getPlayerMove(board, move):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, move):
        print('What is your next move? (1-9)')
        move = input(board)
    
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter, move):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy,i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5
    
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to Tic-Tac-Toe!")

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The {turn} will go first")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard, playerLetter)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
               if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break

        else:
            move = getComputerMove(theBoard, computerLetter, playerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    
    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith('y'):
        break

