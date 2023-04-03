# SudokuSolver
The goal of this code is to solve any Sudoku grid in the fastest time possible.

The Sudoku solver program uses a backtracking algorithm in which the computer iterates through each open space, placing the first possible number 1 through 9. A possible number is defined as a number that isn't in the same column, same row, or in the square of the said open spot. As soon as the code interacts with an error, when no number fits the requirements, the code moves back one space and chooses a different available number. The algorithm continues until it reaches a solution or exhausts all possibilities.

