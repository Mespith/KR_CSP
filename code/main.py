import sudokuParser as sp
import CSPsolver as so
#This is the main structure of the sudoku solver.
#Input:
#- A file containing sudokus. Example: sudoku-1000.txt

#Parse the sudoku input
#sudokus = sp.ParseFile("C:/Users/Jaimy/Documents/UVA/Knowledge Representation/Assignment2/KR_CSP/1000 sudokus.txt")
print('parsed')

#Solve the CSP
results = []
#for i in range(len(sudokus)):
 #   result = so.Solve(sudokus[i][0], sudokus[i][1])
  #  results.append(result)

#Generate output file
def ParseResults(filePath, results):
    fileName = filePath[:filePath.index('.')] + ' solutions.txt'
    f = open(fileName, 'w')
    
    for result in results:
        for var in result[0]:
            value = str(var.domain[0])
            f.write(value)
        f.write('\n')
    f.close()
    
ParseResults("C:/Users/Jaimy/Documents/UVA/Knowledge Representation/Assignment2/KR_CSP/1000 sudokus.txt")