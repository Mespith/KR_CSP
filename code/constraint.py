class constraint:
	#a list of variables that cannot be the same
    def __init__(self, variables):
    	#variable 1 should always be a variable indicated as a number referring to the index of the list of variables that represent the sudoku
    	#if one only wants to express unary constraints than input a single variable
        self.variables = variables
        #unary contraints can also be added
        self.domain_constraint = []

