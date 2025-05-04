# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:16:21 2025

@author: kutadgu
"""

from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

# function to optimize
def f(xy):
    x = xy[0]
    y = xy[1]
    profit = 50*x + 60*y
    return -profit

# Initial guesses
xy_start = [15, 15]

# bounds
bounds = [[1, None], [1, None]]

# constraints
cons = ({'type': 'ineq', 'fun': lambda xy: 120 - (2*xy[0] + 3*xy[1])},    # LHS <= 0
        {'type': 'ineq', 'fun': lambda xy: 85 - (2*xy[0] + 4*xy[1])},
        {'type': 'eq', 'fun': lambda xy: xy[0] + xy[1] - 30 })


# Optimizing the results
op_pro = minimize(f, xy_start, bounds = bounds, constraints = cons)


# Print Results
# if op_pro.success:
#     x, y = op_pro.x
#     production = op_pro.x
#     print(f"Optimal Production: X = {x:.3f}, Y = {y:.3f}")
#     print(f"Total Profit: ${-op_pro.fun:.2f}")
#     print(f"Machine Hours Used: {2*x + 3*y:.2f} (≤120)")
#     print(f"Labor Hours Used: {2*x + 4*y:.2f} (≤85)")
# else:
#     print("Optimization failed")


if op_pro.success:
    production = op_pro.x
    total_profit = -op_pro.fun
    print(f"Production is, {round(production[0])} of product X, and {round(production[1])} product Y.")
    print(f"Total profit is {round(total_profit)} dollars.")
    print(f"Total machine time is {round(2*production[0] + 3*production[1])} hours.")
    print(f"Total labor time is {round(2*production[0] + 4*production[1])} hours.")
else:
    print("Optimization failed")

# Plotting the data
labels = ('Product X', 'Product Y')
plt.bar(labels, production, color = 'black')
plt.xlabel("Product Type")
plt.ylabel("Product Quantity")
plt.title("Optimal Montly Production")
plt.grid(axis ='y', linestyle='--')



def utility_function(vars):
    c, m= vars
    return -(c**0.7 * m**0.3)

# Define the constraint function
def constraint(vars):
    return 2 - np.sum(vars)

initial_guess = [12, 12]  

# Set up the constraint
constraint_definition = {'type': 'eq', 'fun': constraint}

# Perform optimization
result = minimize(utility_function, initial_guess, constraints=constraint_definition)
c, m = result.x

print("Optimal study hours for classical music:", round(c, 2))
print("Optimal study hours for modern music:", round(m, 2))
