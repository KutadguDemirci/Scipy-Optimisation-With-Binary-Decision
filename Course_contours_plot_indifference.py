import numpy as np
import matplotlib.pyplot as plt

c = np.linspace(1, 2, 10)  
# Define the constraint and generate combinations
m = 2-c
C, M = np.meshgrid(c, m)
# Define the utility function
F = C**0.7 * M**0.3
    
plt.figure(figsize=(8, 6))
# Plot the controls and constraints
contours = plt.contour(C, M, F, levels=[0.9, 1.00, 1.085, 1.2])
plt.clabel(contours)
plt.plot(c, m, color='red')
plt.title('Indifference Curve with Constraint Line')
plt.xlabel('c')
plt.ylabel('m')
plt.grid(True)
plt.show()



from scipy.optimize import minimize

def utility(vars):
    w, l =vars
    return -(w**0.4 * l**0.6)

def constraint(vars):
    return 24- np.sum(vars)


initial_guess=[12, 12]
constraint_definition = {'type': 'eq', 'fun': constraint}

result = minimize(utility, initial_guess, constraints = constraint_definition)

print(result.x)