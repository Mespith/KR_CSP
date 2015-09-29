import variable
import math
#This script parses sudokus from an input file into variables with domains.
#Input:
#- Each Sudoku is represented on a single line with 81 numbers and dots
#- Cells are enumerated from top-left to bottom-right

oneLine = ".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8............942.8.16.....29........89.6.....14..25......4.......2...8.9..5....7.."
size = 0

def ParseLine(line):
    sudoku = []
    for unit in line:
        if unit == '.':
            #Create a variable with a full domain.
            sudoku.append(variable.Variable(range(1, size+1)))
        else:
            #Create a variable with its number as the only value in the domain.
            sudoku.append(variable.Variable([int(unit)]))
    return sudoku
    
def ParseFile(filePath):
    sudokus = []
    #Open the file.
    sudokuFile = open(filePath, 'r')
    for line in sudokuFile:
        #Save the dimension of the sudoku (it is the size of the domain)
        if size == 0:
            size = math.sqrt(len(line))
        sudokus.append(ParseLine(line))
    return sudokus
    
results = ParseFile("100 sudokus.txt")
print(results)