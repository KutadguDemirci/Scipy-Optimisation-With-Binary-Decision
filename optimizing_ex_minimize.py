# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:47:12 2025

@author: kutadgu
"""

from scipy.optimize import minimize

#  Function to optimize (1 variable)
def f(x):
    y = (x**4) - (12534*x) + 349483
    return y

# Initial guess
x_start = 4

# Optimizing
result = minimize(f, x_start)

# Get results
if result.success:
    print(f"x = {result.x} y = {result.fun}")
else:
    print("No Result")
    
# Function to optimize (2 variable) 
def g(hk):
    h = hk[0]
    k = hk[1]
    area = (h * k)
    return -area

# Starting Guess
hk_start = [50, 50]

# Constraints
cons = ({'type': 'eq', 'fun' : lambda hk: (2*hk[0]) + hk[1] - 100})

# Bounds

bounds = ((1, 100), (1, 100))

# Optimizing
optimal = minimize(g, hk_start, bounds = bounds, constraints = cons)

if optimal.success:
    hk = optimal.x
    h = hk[0]
    k = hk[1]
    print(f"h = {h}, k = {k}")
    print(-optimal.fun)
    
else:
    print("No success")