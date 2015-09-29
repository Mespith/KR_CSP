#This script parses sudokus from an input file into variables with domains.
#Input:
#- Each Sudoku is represented on a single line with 81 numbers and dots
#- Cells are enumerated from top-left to bottom-right

oneLine = ".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8............942.8.16.....29........89.6.....14..25......4.......2...8.9..5....7.."

def ParseLine(line):
    for unit in line:
        if unit == '.':
            #Create a variable without value and a domain.
        else:
            #Create a variable with an assigned value and an emtpy domain.
    return sudoku
    
def ParseFile(filePath):
    #Open the file.
    for line in file:
        sudoku = ParseLine(line)
    return sudokus