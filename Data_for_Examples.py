import random
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#Insert variables in parenthesis in place of x.
variables_1=sp.symbols('x1 x2 t')
x1,x2=variables_1[:-1]
F=x1**4-4,x2*x1-2 #Polynomial system we want to solve
Homotopy_1=(F,variables_1)