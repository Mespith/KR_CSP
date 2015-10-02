import intertools
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
        
def i_tuples(variables, i):
    