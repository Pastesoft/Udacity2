
def expectedValue(num):
    res = 0
    ln = num
    while ln > 0:
        res = res + ln
        ln = ln - 1
    return res

def getCols(matrix, ind):
    res = []
    i = 0
    while i < len(matrix) :
        res.append(matrix[i][ind])
        i = i + 1
    return res
    

def check_sudoku(sudoku):
    row = []
    col = []
    res = False
    ln = len(sudoku)
    print col
    if(ln > 0):
        expected = expectedValue(ln)
        i = 0
        while i < ln:
            row = sudoku[i]
            col = getCols(sudoku, i)
            if(sum(row) == expected) and (sum(col) == expected):
                res = True
            else :
                res = False
                break
            i = i + 1

    return res

incorrect = [[1,2,3,4],
            [2,3,3,1],
            [3,4,2,3],
            [4,2,3,4]]

bug = [[3,3,3,3,3],
       [3,3,3,3,3],
       [3,3,3,3,3],
       [3,3,3,3,3],
       [3,3,3,3,3]]

correct = [[1,2,3],
          [2,3,1],
          [3,1,2]]

print check_sudoku(incorrect)
print check_sudoku(bug)
print check_sudoku(correct)
