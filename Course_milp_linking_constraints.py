from scipy.optimize import minimize, milp, LinearConstraint, NonlinearConstraint, Bounds
import numpy as np
import matplotlib.pyplot as plt

# MILP SOLUTION

c = [-50, -80, -60, 200, 300, 250] #profit per product and the one time setup cost per product
bounds = Bounds([0, 0, 0, 0, 0, 0], # Minimum number of product made, and binary decision if the product gets made or not
                [40, 30, 50, 1, 1, 1]) # Maximum demand per product, and binary decision if the product gets made or not

cons = LinearConstraint([[2, 3, 4, 0, 0, 0], # Machining time per product
                         [3, 2, 4, 0, 0, 0], # Labour hour per product
                         [4, 5, 3, 0, 0, 0], # Material used per prod
                        [1, 0, 0, -40, 0, 0], # Linking the constraints with binary decision
                        [0, 1, 0, 0, -30, 0], # Linking the constraints with binary decision
                        [0, 0, 1, 0, 0, -50]], # Linking the constraints with binary decision
                        lb = [0, 0, 0, -np.inf, -np.inf, -np.inf], # Min values of constraints
                        ub =[200, 150, 180, 0, 0, 0]) #Max values of constraints
# Optimizing

result = milp(c,
              integrality = [1, 1, 1, 1, 1, 1],
              bounds = bounds,
              constraints = cons)

# Print Results

if result.success:
    prod_a, prod_b, prod_c, setup_a, setup_b, setup_c = result.x
    total_profit = -(result.fun)  # Convert back to positive profit
    print(f"Produce Product A: {setup_a:.0f} (Quantity: {prod_a:.1f})")
    print(f"Produce Product B: {setup_b:.0f} (Quantity: {prod_b:.1f})")
    print(f"Produce Product C: {setup_c:.0f} (Quantity: {prod_c:.1f})")
    print(f"\nTotal Profit: ${total_profit:.2f}")
    print(f"Machine Time A: {2*prod_a}")
    print(f"Machine Time B: {3*prod_b}")
    print(f"Machine Time C: {4*prod_c}")
    print(f"Labour Time A: {3*prod_a}")
    print(f"Labour Time B: {2*prod_b}")
    print(f"Labour Time C: {4*prod_c}")
    print(f"Material used for A: {4*prod_a}")
    print(f"Material used for B: {5*prod_b}")
    print(f"Material used for C: {4*prod_c}")
else:
    print("No solution found")
    
# Plot the figure

fig, ax = plt.subplots()

ax.bar(['Product A', "Product B", "Product C"], [result.x[0], result.x[1], result.x[2]], color = 'red')
ax.set_xlabel('Product Types', color = 'blue')
ax.set_ylabel('Product Quantity', color = 'red')
ax.tick_params(axis = 'x', color = 'blue')
ax.tick_params(axis = 'y', color = 'red')

plt.show