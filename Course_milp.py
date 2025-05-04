# regular minimize doesnt give correct answers

from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

def profit(gt):
    g = gt[0]
    t = gt[1]
    return -(545*g + 330*t)

bounds = ((0,20), (0,12))
gt0 = (10, 10)
cons = ({'type': 'ineq', 'fun': lambda gt: 40 - 6*gt[0] - 4*gt[1]},
        {'type': 'ineq', 'fun': lambda gt: 20 - 3*gt[0] - gt[1]})

production = minimize(profit, gt0, bounds=bounds, constraints=cons)

if production.success:
    opt_ratio = production.x
    opt_profit = production.fun
    print(f"{round(opt_ratio[0])}, {round(opt_ratio[1])}")
    print(f"{round(-opt_profit)}")



# AI SOLUTION

from scipy.optimize import milp, Bounds, LinearConstraint

result = milp([-545, -330],
              integrality=[1, 1],
              bounds = Bounds([0, 0], (20, 12)),
              constraints = LinearConstraint([[6, 4], [3, 1]], ub=[40,20]))

print(result.x)







# EXAMPLE 1

from scipy.optimize import milp, Bounds, LinearConstraint

result = milp([-50, -80], 
              integrality=[1, 1],
              bounds = Bounds([5, 0], [20, 15]),
              constraints = LinearConstraint([[3, 5], [2, 4]], ub=[100, 60]))

print(result.x)
print(result.fun)






# EXAMPLE 2 BINARY VARIABLES

from scipy.optimize import milp, Bounds, LinearConstraint

result = milp([-100, -150, -120],
              integrality=(1, 1, 1),
              bounds = Bounds([0, 0, 0], [1, 1, 1]),
              constraints = LinearConstraint([[30, 50, 40]], ub=70))

print(result.x)
print(-result.fun)







# EXAMPLE 3 EQUALITY CONSTRAINT

from scipy.optimize import milp, Bounds, LinearConstraint

result = milp([-8, -6, -5, -7],
              integrality = [1, 1, 1, 1],
              bounds = Bounds([0, 0, 0, 0], [1, 1, 1, 1]),
              constraints = LinearConstraint([[3, 2, 4, 1], [2, 4, 1, 3], [-1, 0, 1, 0]], ub=[8, 7, 0]))
print(result.x)
print(result.fun)














