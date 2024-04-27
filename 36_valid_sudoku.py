def validSudoku(board):
    # check across -> horziontal -> 3x3s
    for x in range(0, 9):
        #blanks = board[x].count(".") # bad runtime
        if(len(set(board[x]) != 9 - board[x].count("."))):
            return False
    for x in range(0, 9):
        l1 = []
        for y in range(0, 9):
            l1.append(board[y][x]) 
        if(len(set(l1)) != 9 - l1.count(".")):  
            return False
    for x in range(0, 9, 3):
        l1 = []
        for y in range(0,3):
            l1 = board[x][y]

    return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(validSudoku(board))