import variable
import constraint
import math
#This script parses sudokus from an input file into variables with domains.
#Input:
#- Each Sudoku is represented on a single line with 81 numbers and dots
#- Cells are enumerated from top-left to bottom-right

oneLine = ".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8............942.8.16.....29........89.6.....14..25......4.......2...8.9..5....7.."
size = 0

#this def is right from: http://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def ParseLine(line,size):
    #the variables of the sudoku
    variables = []
    constraints = []
    count = 0
    for unit in line:
        if unit == '.':
            #Create a variable with a full domain.
            variables.append(variable.Variable(range(1, size+1)))
        elif( RepresentsInt( unit ) ):
            #Create a variable with a full domain
            variables.append(variable.Variable(range(1, size+1)))
            #create a constraint
            new_constraint =  constraint.constraint( count )
            new_constraint.domain_constraint = [1 , 2, 3, 4, 5, 6, 7, 8, 9].remove(int(unit))
            constraints.append (new_constraint)
        count = count + 1
    
    return [variables, constraints]
   

def ParseFile(filePath):
    sudokus = []
    #Open the file.
    sudokuFile = open(filePath, 'r')
    for line in sudokuFile:
        size = int (math.sqrt(len(line) -1) )
        sudokus.append(ParseLine(line,size))
    return sudokus
    
results = ParseFile("../1000 sudokus.txt")

print results[0][0][0].domain