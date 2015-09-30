import split
#This script is the general CSP solving algorithm.
        
def Solve(variables):
    #Preprocess() (rewrite problem in the format you want)
    #Constraint propagation() (k-consistency)
    #Happy() (Check if problem is solved)
    solved = False
    if solved:
        return True, solution
    else:
        #Create sub-problems
        CSP_1, CSP_2 = split.Split(variables)
        #Solve the sub-problems
        success, result = Solve(CSP_1)
        if success:
            return result
        success, result = Solve(CSP_2)
        if success:
            return result
    return False, variables