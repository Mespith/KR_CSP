from collections import deque

def AC_3(variables, constraints):
    for x in variables:
        # Make consistent with unary constraints.
        unary_reduce(x, constraints)
    
    #Create the queue for checking constraints
    queue = deque(constraints)
    
    while len(queue) != 0:
        r = queue.popleft()
        if not r.unary_constraint:
              if arc_reduce(r.variable1, r.variable2):
                  if len(r.variable1.domain) == 0:
                      return False
                  else:
                      # Add all the constraints to the queue where x is the second variable.
                      for con in constraints:
                          if con.variable2 == r.variable1:
                              queue.append(con)  
    return True                              
        
def unary_reduce(x, constraints):
    for r in constraints:
        if r.variable1 == x and r.unary_constraint:
            x.domain.remove(r.unary_constraint)
            
def arc_reduce(x, y):
    change = False
    
    if len(y.domain) == 1:
        print(y.domain)
        #Try to remove the value of y from the domain of x
        try:
            print(x.domain)
            x.domain.remove(y.domain[0])
            print(x.domain)
            change = True
        except:
            change = False
    return change