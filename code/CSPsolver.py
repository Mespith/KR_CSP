#This script is the general CSP solving algorithm.
        
def Solve(variables):
    #Preprocess() (rewrite problem in the format you want)
    #Constraint propagation() (k-consistency)
    #Happy() (Check if problem is solved)
    solved = False
    if solved:
        return true, solution
    else:
        #Split() (Create sub-problems)
        for CSP in splits:
            success, result = Solve(CSP)
            if success:
                return result
    return false, variables