import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
import matplotlib.pyplot as plt

# FUNCTION TO MINIMIZE
c = [2, 3, 4, # WAREHOUSE A TO ALL THE DESTINATION COST
     1, 2, 3, # WAREHOUSE B TO ALL THE DESTINATION COST
     50, 30, 40, # FIXED COST WAREHOUSE A BINARY DECISION
     60, 20, 10, #FIXED COST WAREHOUSE B BINARY DECISION
     ]


# BOUNDS OF THE VARIABLES
bounds = Bounds([0, 0, 0,
                 0, 0, 0,
                 0, 0, 0,
                 0, 0, 0],
                [60, 70, 90, #WAREHOUSE A DESTIONATIONS CAPACITY
                 50, 80, 100,#WAREHOUSE B DESTIONATIONS CAPACITY
                 1, 1, 1,
                 1, 1, 1])

# CONSTRAINTS OF THE VARIABLES
cons = LinearConstraint([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #WAREHOUSE A TOTAL SUPPLY
                         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], #WAREHOUSE B TOTAL SUPPLY
                         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], #DESTIONATION 1 DEMAND
                         [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], #DESTIONATION 2 DEMAND
                         [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], #DESTIONATION 3 DEMAND
                         [1, 0, 0, 0, 0, 0, -1000, 0, 0, 0, 0, 0], #BINARY DECISION OF A TO 1
                         [0, 1, 0, 0, 0, 0, 0, -1000, 0, 0, 0, 0], #BINARY DECISION OF A TO 2
                         [0, 0, 1, 0, 0, 0, 0, 0, -1000, 0, 0, 0], #BINARY DECISION OF A TO 3
                         [0, 0, 0, 1, 0, 0, 0, 0, 0, -1000, 0, 0], #BINARY DECISION OF B TO 1
                         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1000, 0], #BINARY DECISION OF B TO 2
                         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1000]], #BINARY DECISION OF B TO 3
                        [0, 0, 80, 70, 90, -np.inf, -np.inf, -np.inf, -np.inf, -np.inf, -np.inf], #LOWE BOUNDS OF CONSTRAINT
                        [100, 150, 80, 70, 90, 0, 0, 0, 0, 0, 0])

#OPTIMIZATION
result = milp(c, integrality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              bounds = bounds,
              constraints=cons)

# PRINT AND PLOT RESULTS
if result.success:
    print(f"From Warehouse A {result.x[0]+result.x[1]+result.x[2]} products are shipped to all destinations.")
    print(f"From Warehouse A {result.x[3]+result.x[4]+result.x[5]} products are shipped to all destinations.")
    print(f"Warehouse A ships {result.x[0]}, {result.x[1]}, and {result.x[2]} products to all destinations respectively.")
    print(f"Warehouse B ships {result.x[3]}, {result.x[4]}, and {result.x[5]} products to all destinations respectively.")
    print(f"Total cost of shipment is {result.fun} dollars.")
    
    
    
# PLOTTING
    fig, ax = plt.subplots(figsize=(10, 6))  # Added figure size for better spacing

    labels = ["A TO 1", "A TO 2", "A TO 3", "B TO 1", "B TO 2", "B TO 3"]
    values = [result.x[0], result.x[1], result.x[2], 
          result.x[3], result.x[4], result.x[5]]

# Create bar chart
    bars = ax.bar(labels, values, color='gray')

# Labels and title
    ax.set_xlabel('Warehouse and Destination', fontsize=16, family='Arial')
    ax.set_ylabel("Product Quantity", fontsize=16, family='Arial')
    ax.set_title("Shipment Quantities", fontsize=16)

# Fixed y-axis ticks (3 main changes)
    ax.set_yticks(np.arange(0, 91, 30))  # 1. Use parentheses () instead of brackets []
                                      # 2. End at 91 to include 90
                                      # 3. Match tick positions with labels
    ax.set_yticklabels([0, 30, 60, 90], fontsize=12)  # Added fontsize for readability

# Format x-axis
    plt.xticks(rotation=45, ha='right')  # Rotate labels to prevent overlap
    ax.tick_params(axis='x', which='both', labelsize=12)
    ax.tick_params(axis='y', which='both', labelsize=12)

# Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom')

    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()  # Automatically adjust subplot params
    plt.show()

else:
    print("No results.")


