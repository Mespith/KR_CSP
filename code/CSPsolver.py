import split
import validation
import arc_consistency
#This script is the general CSP solving algorithm.
        
def Solve(variables, constraints):
    #Preprocess() (rewrite problem in the format you want)
    #Propagate the constraints. If false, then it is unsatifiable
    if not arc_consistency.AC_3(variables, constraints):
        return False, variables
    #Check if problem is solved
    solved = validation.Happy(variables)
    if solved:
        return True, variables
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