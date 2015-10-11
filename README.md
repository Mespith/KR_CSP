Authors: Jaimy van Dijk & David Zomerdijk

-----How to run the program----
To use the program run "main.py", it takes two arguments, an input and an outputfile. for example:
>python main.py inputfile.txt outputfile.txt

Since the input is one folder higher one should use:
>python main.py ../1000\ sudokus.txt solutions.txt


----where to find what-----

>Main.py
in this file all necessary code is called.
to find the constraints, go to sudokuparser

>CSPSolver.py
here one finds the general CSP solving algorithm.

>split.py
Here one finds all the split algorithms we used, if you want to use the program with a different solver one can change this is CSPSolver.py (this is the only place in the code where the split function is called).

>SudokuParser
    This code parses the input and creates the variables and the constraints (both the binary and the unary constraints). To add constraints append constraints to the list "contraints" in the definition
    general sudoku constraints


>validation
    Here one finds our happy function. Which basically only checks whether the CSP is a solution
>constraintpropagation

>constraint
this is where we define the object constraint

>Variable
this is where we define the object variable



