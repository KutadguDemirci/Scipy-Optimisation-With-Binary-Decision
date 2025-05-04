import numpy as np
import matplotlib.pyplot as plt



# LINPROG SOLUTION
from scipy.optimize import linprog

labour = np.array([2, 4]) # HOURS NEEDED TO MAKE 1 CHAIR
material = np.array([3, 5]) # MATERIAL NEEDED TO MAKE 1 CHAIR


max_labour = 100 # TOTAL LABOUR AVAILABLE
max_material = 120 # TOTAL MATERIAL AVAILABLE


c = [-50, -80] # NEGATIVE FOR MINIMIZATION

# DEFINE BOTH SIDES OF THE INEQUALITIES
A_ub = np.array([labour, 
        material])

b_ub = np.array([max_labour,
        max_material])

# SET THE BOUNDS
bounds = [(0, None), (5, None)]

# OPTIMIZING PRODUCTION
result = linprog(c, A_ub = A_ub, b_ub = b_ub, bounds = bounds, method='highs') 


# GETTING RESULTS
if result.success:
    optimal_ratio = result.x
    optimal_profit = result.fun
    print(f"Maximum profit is {-optimal_profit} dollars.")
    print(f"Optimal production ratios are {optimal_ratio[0]} for regular chair, and {optimal_ratio[1]} for deluxe chair.")
else:
    print("No results.")


# MILP SOLUTION

from scipy.optimize import milp, LinearConstraint, Bounds

result = milp([-50, -80],
              integrality = [1, 1], 
              bounds = Bounds([0, 5], [np.inf, np.inf]),
              constraints = LinearConstraint([[2, 4], [3, 5]], ub = [100, 120]))

if result.success:
    optimal_ratio = result.x
    optimal_profit = result.fun
    print(f"Maximum profit is {-optimal_profit} dollars.")
    print(f"Optimal production ratios are {optimal_ratio[0]} for regular chair, and {optimal_ratio[1]} for deluxe chair.")
else:
    print("No results.")




# plotting the results
fig, ax = plt.subplots()

ax.bar(['Regular Chair', "Deluxe Chair"], optimal_ratio)
ax.set_xlabel("Product Type")
ax.set_ylabel("Production Quantity")
ax.set_title("Chair Production")