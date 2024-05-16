# Define the variables and polynomial system:
x1,x2,t=sp.symbols('x1 x2 t') #Insert variables in parenthesis in place of x.
variables=(x1,x2,t)
d1,d2=3,2 #degrees with respect to each variable
degrees=[d1,d2] #Definition for syntax
F=np.array([5-x[0]**d1, 3*x[1]**d2-2]) #Polynomial system we want to solve
G=np.array([x[0]**d1-1,x[1]**d2-1])