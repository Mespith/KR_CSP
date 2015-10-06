import sudokuParser
import CSPsolver
#This is the main structure of the sudoku solver.
#Input:
#- A file containing sudokus. Example: sudoku-1000.txt

#Parse the sudoku input
sudokus = sudokuParser.ParseFile("../1000 sudokus.txt")

#Solve the CSP
for i in range(len(sudokus)):
    success, result = CSPsolver.Solve(sudokus[i], constraints[i])

#Generate output file