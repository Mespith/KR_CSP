import variable
import constraint
import math
#This script parses sudokus from an input file into variables with domains.
#Input:
#- Each Sudoku is represented on a single line with 81 numbers and dots
#- Cells are enumerated from top-left to bottom-right

#This def is right from: http://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
def RepresentsInt( s ):
    try: 
        int(s)
        return True
    except ValueError:
        return False

#Takes number of variables which decides on the size of the list how big the sudoku must be
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
    #The variables of the sudoku
    variables = []
    #The constraints of the sudoku
    constraints = []
    count = 0
    for unit in line:
        if unit == '.':
            #Create a variable with a full domain.
            variables.append(variable.Variable(range(1, size+1)))
        elif( RepresentsInt( unit ) ):
            #Create a variable with a full domain
            variables.append(variable.Variable(range(1, size+1)))
            #Create all the unary constraints for this given number
            constraint_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
            constraint_list.remove (int(unit))
            for x in constraint_list:
                new_constraint =  constraint.constraint( variables[ len(variables) - 1 ] )
                new_constraint.unary_constraint = x
                constraints.append (new_constraint)
        count = count + 1

    sudoku_constraints = general_sudoku_constraints( variables )
    constraints = constraints + sudoku_constraints
    
    return (variables, constraints)
   
#It returns a list of sukoku's
#A sudoku is a tuple of a list of variables and a list of constraints.
def ParseFile(filePath):
    sudokus = []
    size = 0
    #Open the file.
    print('Opening the file...')
    sudokuFile = open(filePath, 'r')
    #Parse every line into a sudoku with respecting constraints
    for line in sudokuFile:
        if size == 0:
            print('Apparently we are working with a sudoku of size ' + str(size))
            size = int (math.sqrt(len(line) -1) )
        print('Parsing line: ', line)
        sudoku = ParseLine(line,size)
        print('Success! We have ' + str(len(sudoku[0])) + ' variables and ' + str(len(sudoku[1])) + 'constraints.')
        sudokus.append(sudoku)
    return sudokus