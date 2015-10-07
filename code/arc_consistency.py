from collections import deque

def AC_3(variables, constraints, satisfied_constraints):
    new_satisfied_constraints = []
    #Create the queue for checking constraints
    #queue = [item for item in constraints if item not in satisfied_constraints]
    queue = deque(queue)
    
    while len(queue) > 0:
        r = queue.popleft()
        if r not in satisfied_constraints:
            x = variables[r.variable1]
            y = variables[r.variable2]
            # Check if the reduction causes a change
            if arc_reduce(x, y):
                if len(x.domain) == 0:
                    return False, satisfied_constraints
                elif len(x.domain) == 1:
                    # This means dat the constraint between x and y is satisfied.
                    new_satisfied_constraints.append(r)

                    # Add all the constraints to the queue where x is the second variable.
                    # This is only useful if x is reduced to 1 value.
                    for con in constraints:
                        if con.variable2 == r.variable1 and con not in queue:
                            queue.append(con)
    return True, satisfied_constraints + new_satisfied_constraints
        
def unary_reduce(variables, constraints):
    for i in range(len(variables)):
        # Make consistent with unary constraints.
        for r in constraints:
            if r.variable1 == i and r.unary_constraint:
                x = variables[i]
                if r.unary_constraint in x.domain:
                    x.domain.remove(r.unary_constraint)
            
def arc_reduce(x, y):
    change = False    
    if len(y.domain) == 1 and y.domain[0] in x.domain:
        #Try to remove the value of y from the domain of x
        try:
            x.domain.remove(y.domain[0])
            change = True
        except:
            change = False
    return change