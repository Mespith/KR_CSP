import random
#This script creates sub-CSP's given a CSP.

def Split(CSP):
    CSP_1 = list(CSP)
    CSP_2 = list(CSP)
    #TODO: Choose the most constraining variable to split the domain.
    varIndex = random.randint(0, len(CSP)-1)
    splitVar = CSP[varIndex]
    while len(splitVar.domain) <= 1:
        varIndex = random.randint(0, len(CSP)-1)
        splitVar = CSP[varIndex]
    valueIndex = random.randint(0, len(splitVar.domain)-1)
    
    CSP_1[varIndex].domain = [splitVar[valueIndex]]
    CSP_2[varIndex].domain.remove(splitVar[valueIndex])
    
    return CSP_1, CSP_2