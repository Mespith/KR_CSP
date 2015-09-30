#This script checks if a given CSP is a solution.

def Happy(CSP):
    for variable in CSP:
        if len(variable.domain) > 1:
            return False