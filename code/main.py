import sudokuParser
import CSPsolver
#This is the main structure of the sudoku solver.
#Input:
#- A file containing sudokus. Example: sudoku-1000.txt

#Parse the sudoku input
sudokus = sudokuParser.ParseFile("C:/Users/Jaimy/Documents/UVA/Knowledge Representation/Assignment2/KR_CSP/1000 sudokus.txt")
print('parsed')

#Solve the CSP
#for i in range(len(sudokus)):
result = CSPsolver.Solve(sudokus[0][0], sudokus[0][1])
print(result[0], result[1])

#Generate output file