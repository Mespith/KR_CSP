import random
import variable
import sudokuParser
import copy
import sys
#This script creates sub-CSP's given a CSP.

#this takes the variable with the smallest domain and splits it on this domain
def most_constraining_split(CSP):
    variables = CSP[0]

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

    Smallest_domains = [i for i, j in enumerate(a) if j == m]

    Smallest_domain = smallest_domains[0]

    varIndex = smallest_domain

    splitVar = CSP[0][varIndex]

    valueIndex = random.randint(0, len(splitVar.domain)-1)
    
    CSP_1[varIndex].domain = [splitVar[valueIndex]]
    CSP_2[varIndex].domain.remove(splitVar[valueIndex])
    
    return CSP_1, CSP_2



    return smallest_domains[0]

#this splits the CSP for the variable that occurs in most constraints
def most_constraining_split2( CSP ):
    constraints = CSP[1]

    variables_in_constraints = []
    # makes the list variables_in_constraints that loops over all constraints
    # to append every variable instance
    for  x in constraints:
        variables_in_constraints.append( x.variable1 )
        variables_in_constraints.append( x.variable2 )

    # the most occuring variable in variables_in_constrains
    most_constraining = max(set( variables_in_constraints ), key=lst.coun)

    varIndex = CSP[0].index( most_constraining )
    splitVar = CSP[varIndex]
    while len(splitVar.domain) <= 1:
        varIndex = random.randint(0, len(CSP)-1)
        splitVar = CSP[varIndex]
    valueIndex = random.randint(0, len(splitVar.domain)-1)
    
    CSP_1[varIndex].domain = [splitVar[valueIndex]]
    CSP_2[varIndex].domain.remove(splitVar[valueIndex])

    return CSP_1, CPS_2




def Split(CSP):
    CSP_1 = list(CSP)
    CSP_2 = list(CSP)


    varIndex = random.randint(0, len(CSP)-1)
    splitVar = CSP[varIndex]
    while len(splitVar.domain) <= 1:
        varIndex = random.randint(0, len(CSP)-1)
        splitVar = CSP[varIndex]
    valueIndex = random.randint(0, len(splitVar.domain)-1)
    
    CSP_1[varIndex].domain = [splitVar[valueIndex]]
    CSP_2[varIndex].domain.remove(splitVar[valueIndex])
    
    return CSP_1, CSP_2