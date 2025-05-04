import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# ----------------------------
# 1. Problem Setup (REVISED)
# ----------------------------
profit = [-20, -30, -25]  # Negative for maximization

# Machine hours PER UNIT of product (A, B, C)
A_ub = [
    [2, 1, 4],  # Machine 1 hours per product
    [1, 3, 2]   # Machine 2 hours per product
]
b_ub = [100, 80]  # Max hours available per machine

# Minimum 10 units of Product C
bounds = [(0, None), (0, None), (10, None)]

# ----------------------------
# 2. Solve
# ----------------------------
result = linprog(
    c=profit,
    A_ub=A_ub,
    b_ub=b_ub,
    bounds=bounds,
    method='highs'
)

if result.success:
    production = result.x
    print(f"Optimal Production: {np.round(production, 2)}")

    # ----------------------------
    # 3. Machine Hours Calculation
    # ----------------------------
    # Convert A_ub to numpy array for vector math
    A_ub_array = np.array(A_ub)
    
    # Calculate machine hours used
    machine_hours = A_ub_array @ production  # Matrix multiplication
    
    print(f"\nMachine 1 Hours Used: {machine_hours[0]:.2f} (Max 100)")
    print(f"Machine 2 Hours Used: {machine_hours[1]:.2f} (Max 80)")

    # ----------------------------
    # 4. Plotting
    # ----------------------------
    # Plot 1: Production
    plt.figure()
    plt.bar(['A', 'B', 'C'], production, color='blue')
    plt.title("Production Units")
    plt.ylabel("Quantity")
    plt.show()

    # Plot 2: Machine Hours
    plt.figure()
    plt.bar(['Machine 1', 'Machine 2'], machine_hours, color='orange')
    plt.axhline(100, color='red', linestyle='--', label='Machine 1 Limit')
    plt.axhline(80, color='purple', linestyle='--', label='Machine 2 Limit')
    plt.title("Machine Utilization")
    plt.ylabel("Hours Used")
    plt.legend()
    plt.show()

    print(f"\nTotal Profit: ${-result.fun:.2f}")

else:
    print("No solution found.")