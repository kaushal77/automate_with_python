theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printboard(board):
    print(board['top-L'] + ' |' + board['top-M'] + ' |' + board['top-R'])
    print('--+--+--')
    print(board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])
    print('--+--+--')
    print(board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])
    
printboard(theBoard)
turn = 'X'
for i in range(9):
    print('turn of '+ turn + '. Enter the cell name :')
    cell = input()
    theBoard[cell] = turn
    if turn == 'X':
        turn = 'O'
    else :
        turn  = 'X'
    printboard(theBoard)   