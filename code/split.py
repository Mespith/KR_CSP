import random
import variable
import sudokuParser
import copy
import sys
#This script creates sub-CSP's given a CSP.

# This takes the variable with the smallest domain and splits it on this domain
def SmallestDomainSplit(CSP):
    CSP_1 = copy.deepcopy( CSP ) 
    CSP_2 = copy.deepcopy( CSP )

    index_variable = 0
    variables_domain = []

    for i in CSP:
        # This so that split doesn't take empty domains or domains of 1
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
def MostConstrainingSplit( CSP , constraints, satisfied_constraints):
    CSP_1 = copy.deepcopy( CSP ) 
    CSP_2 = copy.deepcopy( CSP )

    constraint_count = [0] * len(CSP)
    # Loop through the constraints and count the number of times a variable occurs in this list
    for r in constraints:
        if r not in satisfied_constraints and len(CSP[r.variable1].domain) > 1:
            constraint_count[r.variable1] += 1

    #variables_in_constraints = []
    # makes the list variables_in_constraints that loops over all constraints
    # to append every variable instance
    #for  x in constraints:
     #   variables_in_constraints.append( x.variable1 )
      #  variables_in_constraints.append( x.variable2 )

    # The most occuring variable in variables_in_constrains
    most_constraining = max(constraint_count)
    varIndex = constraint_count.index(most_constraining)
    splitVar = CSP[varIndex]
    valueIndex = random.randint(0, len(splitVar.domain)-1)
    
    value = copy.deepcopy(splitVar.domain[valueIndex])
    CSP_1[varIndex].domain = []
    CSP_1[varIndex].domain.append(value)
    CSP_2[varIndex].domain.remove(value)

    return CSP_1, CSP_2

def combined_split( CSP , constraints, satisfied_constraints):
    CSP_1 = copy.deepcopy( CSP ) 
    CSP_2 = copy.deepcopy( CSP )
    #this picks a most contraining variable by choosing the first variable with the lowst
    #numbers of domains
    index_variable = 0
    variables_domain = []

    for i in CSP:
        # This so that split doesn't take empty domains or domains of 1
        if (len(i.domain) <= 1 ):
            variables_domain.append( sys.maxint )
        else:
            variables_domain.append( len(i.domain) )

    m = min(variables_domain)

    smallest_domains = [i for i, j in enumerate(variables_domain) if j == m]
    #if there are more smallest domains instead of choosing random, choose the most constrained variable
    if ( len(smallest_domains) > 1 ):
            constraint_count = [0] * len(CSP)
            # Loop through the constraints and count the number of times a variable occurs in this list
            for r in constraints:
                if r not in satisfied_constraints and len(CSP[r.variable1].domain) > 1:
                    constraint_count[r.variable1] += 1
                    most_constraining = max(constraint_count)
            if most_constraining in smallest_domains:
                smallest_domain = most_constraining
            else: smallest_domain = smallest_domains[0]

    else: smallest_domain = smallest_domains[0]

    varIndex = smallest_domain

    splitVar = CSP[varIndex]

    valueIndex = random.randint(0, len(splitVar.domain)-1)

    value = copy.deepcopy(splitVar.domain[valueIndex])
    CSP_1[varIndex].domain = []
    CSP_1[varIndex].domain.append(value)
    CSP_2[varIndex].domain.remove(value)

    return CSP_1, CSP_2

# This method picks a random variable and selects a random value to split on.
def RandomSplit(CSP):
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