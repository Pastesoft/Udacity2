
# correct = [[1,2,3],
#           [2,3,1],
#           [3,1,2]]

# incorrect = [[1,2,3,4],
#             [2,3,1,3],
#             [3,1,2,3],
#             [4,4,4,4]]

def findPos(array, toFind, start):
    res = -1
    i = start
    ln = len(array)
    while(i < ln):
        if(array[i] == toFind):
            res = i
            break;
        i = i + 1
    return res

def checkArray(array):
    res = True
    ln = len(array)
    i = 0
    while i < ln:
        src = array[i]
        firstPos = findPos(row, src, 0) + 1
        if((firstPos > 0) and (firstPos < ln)):
            if(findPos(row, src, firstPos) > -1):
                res = False
                print i
                break
        else:
            res = False
            print "else", i
            break
        i = i+1
    return res


def checkCols(sudoku):
    res = False
    col = []
    i = 0
    ln = len(sudoku)
    
    

    return res


def checkRows(sudoku):
    res = True
    i = 0
    ln = len(sudoku)
    while((i < ln) and (res)):
        row = sudoku[i]
        res = checkArray(row)
        i = i + 1

    return res
    

def check_sudoku(sudoku):
    res = False
    if(len(sudoku) > 0):
        res = checkRows(sudoku)
        # res = res and checkCols(sudoku)

    return res

incorrect = [[1,2,3,4],
            [2,3,3,1],
            [1,4,2,3],
            [1,2,3,4]]

correct = [[1,2,3],
          [2,3,1],
          [3,1,2]]

print check_sudoku(incorrect)
print check_sudoku(correct)
