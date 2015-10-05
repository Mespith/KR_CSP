import split
import validation
import arc_consistency
#This script is the general CSP solving algorithm.
        
def Solve(variables, constraints, depth):
    #print('Solving CSP on level: ' + str(depth))
    #Propagate the constraints. If false, then it is unsatifiable
    #print('Propagating constraints')
    satisfiable = arc_consistency.AC_3(variables, constraints)
    if not satisfiable:
        #print('This CSP is insatifiable.')
        return (False, variables)
    #Check if problem is solved
    #print('Checking if we found a solution.')
    solved = validation.Happy(variables)
    if solved:
        #print('We did!')
        return (True, variables)
    else:
        #print('We did not. Creating sub-problems now.')
        #Create sub-problems
        CSP_1, CSP_2 = split.Split(variables)
        #Solve the sub-problems
        result = Solve(CSP_1, constraints, depth+1)
        if result[0]:
            return result
        result = Solve(CSP_2, constraints, depth+1)
        if result[0]:
            return result
    return (False, variables) 