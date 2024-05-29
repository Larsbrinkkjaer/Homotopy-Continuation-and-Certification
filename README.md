README file:

The repository consists of the following four files:

The file "Data_for_Examples.py" contains data for specific examples that are used in the thesis, or which enables use of an algorithm described in the project. This file is made in **Python v.3.8.8**.

The file "Results_of_Examples.ipynb" contains the results of applying functions for homotopy continuation and for certification on the examples defined in "Data_for_Examples.py". This file is a *Jupyter Notebook* using **Python v.3.8.8**.

The file "Julia Homotopy Continuation 6R-Serial Link Robot.ipynb" contains solutions of the 6R-serial link robot with the same parameters as defined in "Example 10" in "Data_for_Examples.py". This file is a *Jupyter Notebook* using **Julia v.1.8.2**.

The file "Homotopy_Contiuation_and_Certification" contains callable function for all version of homotopy continuation and ceritification used thoughout the thesis. This file is a *Jupyter Notebook* using **Python v.3.8.8**.
Only few of the version of functions are designed to work in general, which are the following:
 - Homotopy_Continuation_4
 - Homotopy_Continuation_5
 - Homotopy_Continuation_A
 - Homotopy_Continuation_B
 - Homotopy_Continuation_CP
 - Certify

  The following contains information about how to use these functions:

  Before applying any of these functions, we need to define the variables and polynomial systems in the following way:
  - Variables:
      x1,x2,x3=sp.symbols('x1 x2 x3') #Set any number of variables
  - Polynomial Systems:
      F=x1\*\*2-1,x2\*\*2-2*x1,x3\*\*2-x2\*x1 #Seperate each polynomial in the defined variables by a comma.

  - Homotopy_Continuation_4(F,M=1000):
    - Input: F: polynomial system in defined variables, M:  Number of iterations (Optional)
    - Output: Display of solutions to F, Array of solutions to F

  - Homotopy_Continuation_5(F,M=1000):
    - Input: F: polynomial system in defined variables, M:  Number of iterations (Optional)
    - Output: Display of solutions to F, Array of solutions to F
  
  - Homotopy_Continuation_A(F,M=1000):
    - Input: F: polynomial system in defined variables, M:  Number of iterations (Optional)
    - Output: Array of solutions to F
  
  - Homotopy_Continuation_B(F,M=1000):
    - Input: F: polynomial system in defined variables M: Number of iterations (Optional)
    - Output: Array of solutions to F
  
  - Homotopy_Continuation_CP(F0,F0_roots,F1,U_complement=1,M=1000):
    - Input: F0: polynomial system in defined variables for known solutions, F0_roots: solutions to F0, F1: polynomial system of same structure as F0 with different parameters, U_complement: Equation of defined variables, which the desired solutions do not fulfill (Optional), M: Number of iterations (Optional)
    - Output: Array of solutions to F1
  
  - Certify(F, sol):
    - Input: polynomial system in defined variables for known solutions, sol: solutions to F
    - Output: Certified solutions, Interval of number of real solutions, Lower bound of number of distinct solutions, Maximal numerical inaccuracy of solutions.
