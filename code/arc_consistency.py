from collections import deque

def AC_3(variables, constraints):
    #Create the queue for checking constraints
    queue = deque(constraints)
    
    while len(queue) > 0:
        r = queue.popleft()
        if not r.unary_constraint:
            x = variables[r.variable1]
            y = variables[r.variable2]
            if arc_reduce(x, y):
                if len(x.domain) == 0:
                    return False
                elif len(x.domain) == 1:
                    # Add all the constraints to the queue where x is the second variable.
                    # This is only useful if x is reduced to 1 value.
                    for con in constraints:
                        if con.variable2 == r.variable1:
                            queue.append(con)
    return True                              
        
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