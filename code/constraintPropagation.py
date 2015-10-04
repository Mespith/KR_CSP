import itertools
import variable
import constraint
import math
#This script describes the constraint propagation.
#This can be done in different ways:
#- Reduce a Domain
#- Reduce Constraints (Usually by introducing new constraints)

oneLine = ".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8............942.8.16.....29........89.6.....14..25......4.......2...8.9..5....7.."

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
    
    return [variables, constraints]
    
def RepresentsInt( s ):
    try: 
        int(s)
        return True
    except ValueError:
        return False
        
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
    
result = ParseLine(oneLine, 9)
CSP = result[0]
constraints = result[1]

def consistency(k, CSP, constraints):
    #Initialization
    someList = []
    R = list(constraints)
    M = dict()
    
    for i in range(1, k+1):
        #create i-tuples of N
        Ni = itertools.combinations(CSP, i)
        for ni in Ni:
            Li = i_tupleL(ni, i)
            for li in Li:
                print(li)
                if not CheckRelations(ni, li, constraints):
                    someList.append((ni, li, i))
                    M[(ni, li)] = 1
    #Step 2
    for element in someList:
        ni = element[0]
        li = element[1]
        i = element[2]
        if i < k:
            #Propagate the lvl i + 1
            for n in CSP:
                if n not in ni:
                    for l in n.domain:
                        N = ni + n
                        L = li + l
                        if M[(N, L)] == 0:
                            someList.append((N, L, i+1))
                            M[(N, L)] = 1
                            R

def i_tupleL(variables, i):
    domains = []
    for var in variables:
        domains.append(var.domain)
    if i == 1:
        return itertools.combinations(domains[0], i)
    else:
        return itertools.product(*domains)
    
def CheckRelations(variables, values, constraints):
    for constraint in constraints:
        #Check if this constraint applies to one of our variables.
        if constraint.variable1 in variables:
            value1 = values[variables.index(constraint.variable1)]
            #If this is a unary constraint, it is not met if the value equals the unary constraint value.
            if constraint.unary_constraint and constraint.unary_constraint == value1:
                return False
            #Check if the second variable of the constraint is contained in the tuple.
            elif constraint.variable2 in variables:
                value2 = values[variables.index(constraint.variable2)]
                #Because all the constraints are inequlity constraints, it is not met if the values are the same.
                if value1 == value2:
                    print('Variable with value: ', value1, 'Second variable: ', value2)
                    return False
    return True
    
consistency(2, CSP, constraints)