import sudokuParser as sp
import CSPsolver as so
import random
import time

#This is the main structure of the sudoku solver.
#Input:
#- A file containing sudokus. Example: sudoku-1000.txt

#Parse the sudoku input
sudokus = sp.ParseFile("../1000 sudokus.txt")

#Solve the CSP's
results = []
sample_size = [ 419, 840, 740, 740, 806, 757, 532, 568, 406, 492, 602]  
sample_size2 = [x for x in range(50, 150)]
#random_sample = random.sample(xrange(len(sudokus)), sample_size)
for i in sample_size2:
    print('Solving sudoku ' + str(i + 1))
    start_time = time.time()
    result = so.Solve(sudokus[i][0], sudokus[i][1], sudokus[i][2], 0, [])
    runtime = time.time() - start_time
    print('Found a solution in ' + str(result[2]) + ' recursions.' )
    print('runtime: ' + str( runtime ) )

    result2 = result + [runtime]

    results.append( result2 )

print results
#Generate output file
def ParseResults(filePath, results):
    fileName = filePath[:filePath.index('.')] + ' solutions.txt'
    f1 = open(fileName, 'w')
    f2 = open('solution-recursions.txt', 'w')

    for i in range(0, len(results)):
        result = results[i]
        for var in result[1]:
            value = str(var.domain[0])
            f1.write(value)
        f1.write('\n')

        recursions = str(i) + ' ' + str(result[2]) +  ' ' + str( result[3] ) + '\n'
        f2.write(recursions)
    f1.close()
    f2.close()

print('Generating output file.')
ParseResults("../1000 sudokus.txt", results)
print('Finished.')