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
def RepresentsInt( s ):
    try: 
        int(s)
        return True
    except ValueError:
        return False

#takes number of variables which decides on the size of the list how big the sudoku must be
def general_sudoku_constraints( variables ):
    size = int (math.sqrt(len(variables) )) 
    constraints = []
    
    #constraint for every number in every column the number cannot be equal
    for a in range (0, size):
        row = variables[ size * a : size * a + size]
        for i in row:
            for j in row:
                if(i != j):
                    new_constraint =  constraint.constraint( i )
                    new_constraint.variable2 = j
                    constraints.append( new_constraint )


    #constraints for every 
    for i in range(0,size):
        #makes 9 rows
        column = []

        for j in range( 0, size ):
            #makes a row 
            column.append( variables[ size * j + i] )
        for k in column:
            for z in column:
                if( k != z ):
                    new_constraint = constraint.constraint( k )
                    new_constraint.variable2 = z
                    constraints.append( new_constraint )

    #constraints for every box
    #first column of boxes
    boxsize = int (math.sqrt( size) )

    for i in range( 0, boxsize ):
        #makes 9 boxes (a box has the same number of variables as the size of the sudoku)
        box = []
        for j in range(0, boxsize ) :
            for k in range(0, boxsize ):
                box.append( variables [ k + j* size + (i * boxsize * size) ] )

        for k in box:
            for z in box:
                if( k != z ):
                    new_constraint = constraint.constraint( k )
                    new_constraint.variable2 = z
                    constraints.append( new_constraint )

    #second column of boxes
    for i in range( 0, boxsize ):
        #makes 9 boxes (a box has the same number of variables as the size of the sudoku)
        box = []
        for j in range(0, boxsize ) :
            for k in range(0, boxsize ):
                box.append( variables [ k + j* size + (i * boxsize * size) + 3 ] )
                
                #print (k + j* size + (i * boxsize * size) + 3)
                
        for k in box:
            for z in box:
                if( k != z ):
                    new_constraint = constraint.constraint( k )
                    new_constraint.variable2 = z
                    constraints.append( new_constraint )

    #third column of boxes
    for i in range( 0, boxsize ):
        #makes 9 boxes (a box has the same number of variables as the size of the sudoku)
        box = []
        for j in range(0, boxsize ) :
            for k in range(0, boxsize ):
                box.append( variables [ k + j* size + (i * boxsize * size) + 6 ] )
        for k in box:
            for z in box:
                if( k != z ):
                    new_constraint = constraint.constraint( k )
                    new_constraint.variable2 = z
                    constraints.append( new_constraint )

    return constraints

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
            constraint_list = [1 , 2, 3, 4, 5, 6, 7, 8, 9] 
            constraint_list.remove (int(unit) )
            for x in constraint_list:
                new_constraint =  constraint.constraint( variables[ len(variables) - 1 ] )
                new_constraint.unary_constraint = x
                constraints.append (new_constraint)
        count = count + 1

    sudoku_constraints = general_sudoku_constraints( variables )
    constraints = constraints + sudoku_constraints
    
    return [variables, constraints]
   
#it returns a list of sukoku's
#a sudoku is a tuple of a list ofvariables and a list of constraints
#both the variables and the constrains are objects

def ParseFile(filePath):
    sudokus = []
    #Open the file.
    sudokuFile = open(filePath, 'r')
    for line in sudokuFile:
        size = int (math.sqrt(len(line) -1) )
        sudokus.append(ParseLine(line,size))
    return sudokus
    
results = ParseFile("../1000 sudokus.txt")
#print results[0]

#ParseLine( results[0], 9)


#print results[0][0][0].domain