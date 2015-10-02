class constraint:
	#so it initializes as a object with only variable one, and then a unary and normal contraint can be added
	def __init__(self, variable1):
		self.variable1 = variable1
		self.variable2 = None
		self.unary_constraint = None

    

	#my first attempt at a constraint class
    #def __init__(self, variables):
    	#variable 1 should always be a variable indicated as a number referring to the index of the list of variables that represent the sudoku
    	#if one only wants to express unary constraints than input a single variable
     #   self.variables = variables
        #unary contraints can also be added
      #  self.domain_constraint = []'''