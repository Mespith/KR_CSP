import random
import variable
import sudokuParser
import copy
import sys
#This script creates sub-CSP's given a CSP.

#this takes the variable with the smallest domain and splits it on this domain
def most_constraining_split(CSP):
    variables = CSP

    CSP_1 = copy.deepcopy( CSP ) 
    CSP_2 = copy.deepcopy( CSP )
    #this picks a most contraining variable by choosing the first variable with the lowst
    #numbers of domains
    index_variable = 0
    variables_domain = []

    for i in variables:
        #this so that split doesn't take empty domains or domains of 1
        if (len(i.domain) <= 1 ):
            variables_domain.append( sys.maxint )
        else:
            variables_domain.append( len(i.domain) )

    m = min(variables_domain)

    smallest_domains = [i for i, j in enumerate(variables_domain) if j == m]

    smallest_domain = smallest_domains[0]

    varIndex = smallest_domain

    splitVar = CSP[varIndex]

    valueIndex = random.randint(0, len(splitVar.domain)-1)

    value = copy.deepcopy(splitVar.domain[valueIndex])
    CSP_1[varIndex].domain = []
    CSP_1[varIndex].domain.append(value)
    CSP_2[varIndex].domain.remove(value)

    return CSP_1, CSP_2


#this splits the CSP for the variable that occurs in most constraints
def most_constraining_split2( CSP , constraints, satisfied_constraints):

    CSP_1 = copy.deepcopy( CSP ) 
    CSP_2 = copy.deepcopy( CSP )
    new_constraints = []

    for i in constraints:
        if ( i not in satisfied_constraints ):
            new_constraints.append( i )
    

    variables_in_constraints = []
    # makes the list variables_in_constraints that loops over all constraints
    # to append every variable instance
    for  x in constraints:
        variables_in_constraints.append( x.variable1 )
        variables_in_constraints.append( x.variable2 )

    # the most occuring variable in variables_in_constrains
    most_constraining = max(set( variables_in_constraints ), key=variables_in_constraints.count)

    varIndex = most_constraining

    splitVar = CSP[varIndex]
    while len(splitVar.domain) <= 1:
        varIndex = random.randint(0, len(CSP)-1)
        splitVar = CSP[varIndex]

    valueIndex = random.randint(0, len(splitVar.domain)-1)
    
    value = copy.deepcopy(splitVar.domain[valueIndex])
    CSP_1[varIndex].domain = []
    CSP_1[varIndex].domain.append(value)
    CSP_2[varIndex].domain.remove(value)

    return CSP_1, CSP_2




def Split(CSP):
    CSP_1 = copy.deepcopy( CSP ) 
    CSP_2 = copy.deepcopy( CSP )

    varIndex = random.randint(0, len(CSP)-1)
    splitVar = CSP[varIndex]
    while len(splitVar.domain) <= 1:
        varIndex = random.randint(0, len(CSP)-1)
        splitVar = CSP[varIndex]
        
    valueIndex = random.randint(0, len(splitVar.domain)-1)
    
    value = copy.deepcopy(splitVar.domain[valueIndex])
    CSP_1[varIndex].domain = []
    CSP_1[varIndex].domain.append(value)
    CSP_2[varIndex].domain.remove(value)
    
    return CSP_1, CSP_2