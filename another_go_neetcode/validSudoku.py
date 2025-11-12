def function(board):
    #go through each row and entry, add to a dictionary for each type
    rowDict = {}
    columnDict = {}
    squareDict = {}
    for rowNumber in range(len(board)):
        for columnNumber in range(len(board)):
            entry = board[rowNumber][columnNumber]
            if(entry != "."):
                if(rowNumber not in rowDict):
                    rowDict[rowNumber] = {}
                rowDict[rowNumber][entry] = rowDict[rowNumber].get(entry, 0) + 1
                if(rowDict[rowNumber][entry] > 1):
                    return False
                
                if(columnNumber not in columnDict):
                    columnDict[columnNumber] = {}
                columnDict[columnNumber][entry] = columnDict[columnNumber].get(entry, 0) + 1
                if(columnDict[columnNumber][entry] > 1):
                    return False

                #number 1 = row, number2 = column
                squareDictIndex = str(rowNumber//3) + str(columnNumber//3)
                if(squareDictIndex not in squareDict):
                    squareDict[squareDictIndex] = {}
                squareDict[squareDictIndex][entry] = squareDict[squareDictIndex].get(entry, 0) + 1
                if(squareDict[squareDictIndex][entry] > 1):
                    return False
    return True

s = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


print(function(s))

"""
def function(board):
    # go vertically, horizontally, then in 3x3
    for line in board:
        dictLine = {}
        for entry in line: 
            dictLine[entry] = dictLine.get(entry, 0) + 1
            if(entry != "." and dictLine[entry] > 1):
                return False    
    for column in range(len(board)):
        dictLine = {}
        board[column][0]
        for entry in range(len(board)):
            dictLine[board[entry][column]] = dictLine.get(board[entry][column], 0) + 1
            if(board[entry][column] != "." and dictLine[board[entry][column]] > 1):
                return False
    return True
"""