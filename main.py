import numpy as np

sudokutest = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

print('The inputted grid is \n')
print(np.matrix(sudokutest))
#openpos = list(zip(*np.where(sudokutest == 0)))
def possnum(row, col, num):
    global sudokutest
  #start and end points for square
    sectrow = (row // 3) * 3
    sectcol = (col // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
          #checking to see if the number is in the square
            if sudokutest[sectrow+i][sectcol+j] == num:
              #if that number is in the square, returning false
                return False
    #checking to see if the number is in its row
    for i in range(0,9):
      #if it is, returning false
        if sudokutest[row][i] == num:
            return False
    #checking to see if the number is in its column
    for j in range(0,9):
      #if it is, returning false
        if sudokutest[j][col] == num:
            return False
    
    return True

def finalgrid():
  global sudokutest
  for row in range(0,9):
    for col in range(0,9):
      #going through the open spaces
      if sudokutest[row][col] == 0:
        for num in range(1,10):
          if possnum(row, col, num):
            sudokutest[row][col] = num
            finalgrid()
            sudokutest[row][col] = 0
        return
  print(np.matrix(sudokutest))

print('\n The final solution of this grid could be:\n')
finalgrid()
        
#This Sudoku solver uses a backtracking algorithm to find the solution. The finalgrid() function is a recursive function that iterates over the grid, attempting to place a valid number in each empty cell. If it encounters a cell for which no valid number can be placed, it backtracks to the previous cell and continues exploring other possibilities. The algorithm continues until it reaches a solution or exhausts all possibilities.

#inspiration: https://www.youtube.com/watch?v=PZJ5mjQyxR8

