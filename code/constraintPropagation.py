import itertools
#This script describes the constraint propagation.
#This can be done in different ways:
#- Reduce a Domain
#- Reduce Constraints (Usually by introducing new constraints)

def consistency(k, CSP, constraints):
    #Initialization
    someList = []
    R = list(constraints)
    M = 0
    
    for i in range(1, k+1):
        #create i-tuples of N
        Ni = itertools.combinations(CSP, i)
        print('Ni: ', Ni)
        for ni in Ni:
            print('ni: ', ni)
            Li = i_tupleL(ni, i)
            print('Li: ', Li)
            for li in Li:
                print('li: ', li)
                if not CheckRelations(ni, li, constraints):
                    print('False')
                    someList.append((ni, li, i))
                    M[ni, li] = 1

def i_tupleL(variables, i):
    domains = []
    for var in variables:
        domains.append(var.domain)
    return itertools.product(domains, repeat=i)
    
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
                    return False
    return True