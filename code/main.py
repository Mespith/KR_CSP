import sudokuParser as sp
import CSPsolver as so
import random
#This is the main structure of the sudoku solver.
#Input:
#- A file containing sudokus. Example: sudoku-1000.txt

#Parse the sudoku input

sudokus = sp.ParseFile("D:/Jaimy/Documents/UVA/Knowledge Representation/Assignment2/KR_CSP/1000 sudokus.txt")

#Solve the CSP's
results = []
sample_size = [602, 419, 840, 740, 806, 757, 532, 568, 406, 492]
#random_sample = random.sample(xrange(len(sudokus)), sample_size)
for i in sample_size:
    print('Solving sudoku ' + str(i + 1))
    result = so.Solve(sudokus[i][0], sudokus[i][1], sudokus[i][2], 0, [])
    print('Found a solution in ' + str(result[2]) + ' recursions.')
    results.append(result)

#Generate output file
def ParseResults(filePath, results):
    fileName = filePath[:filePath.index('.')] + ' solutions.txt'
    f1 = open(fileName, 'w')
    f2 = open('D:/Jaimy/Documents/UVA/Knowledge Representation/Assignment2/KR_CSP/solution-recursions.txt', 'w')
    
    for i in range(len(results)):
        result = results[i]
        for var in result[1]:
            value = str(var.domain[0])
            f1.write(value)
        f1.write('\n')

        recursions = str(i) + ' ' + str(result[2]) + '\n'
        f2.write(recursions)
    f1.close()
    f2.close()

print('Generating output file.')
ParseResults("D:/Jaimy/Documents/UVA/Knowledge Representation/Assignment2/KR_CSP/1000 sudokus.txt", results)
print('Finished.')