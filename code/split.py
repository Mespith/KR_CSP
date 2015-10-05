import random
import variable
import sudokuParser
import copy
import sys
#This script creates sub-CSP's given a CSP.

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
    
    CSP_1[varIndex].domain = [splitVar.domain[valueIndex]]
    CSP_2[varIndex].domain.remove(splitVar.domain[valueIndex])
    
    return CSP_1, CSP_2



    return smallest_domains[0]

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