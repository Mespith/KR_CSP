import split
import validation
import arc_consistency
#This script is the general CSP solving algorithm.
        
def Solve(variables, unary_constraints, constraints, count):
    if count == 0:
        arc_consistency.unary_reduce(variables, unary_constraints)
    #Propagate the constraints. If false, then it is unsatifiable
    satisfiable = arc_consistency.AC_3(variables, constraints)
    if not satisfiable:
        return (False, variables, count)
    #Check if problem is solved
    solved = validation.Happy(variables)
    if solved:
        return (True, variables, count)
    else:
        #Create sub-problems
        CSP_1, CSP_2 = split.most_constraining_split2(variables, constraints)
        #Solve the sub-problems
        result = Solve(CSP_1, unary_constraints, constraints, count+1)
        if result[0]:
            return result
        result = Solve(CSP_2, unary_constraints, constraints, result[2]+1)
        if result[0]:
            return result
        else:
            count = result[2]
    return (False, variables, count)