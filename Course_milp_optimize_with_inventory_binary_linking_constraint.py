import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


c = [10, 10, 10, # production cost per item
     500, 500, 500, # setup cost per month
     2, 2, 2] # inventory cost

integ = [1, 1, 1,
         1, 1, 1,
         1, 1, 1] #define everything as a whole number output

bounds = Bounds([0, 0, 0,
                 0, 0, 0,
                 0, 0, 0], # Demand per month and binary decision and inventory limit
                [250, 250, 250,# Max production per mont
                 1, 1, 1, # Binary decision to produce or not
                 1000, 1000, 1000]) # Inventory limit

cons = LinearConstraint([[1, 0, 0, 0, 0, 0, -1, 0, 0], # max demand month 1 and inventory
                         [0, 1, 0, 0, 0, 0, 1, -1, 0], # max demand month 2 and inventory
                         [0, 0, 1, 0, 0, 0, 0, 1, -1], # max demand month 3 and inventory
                         [1, 0, 0, -250, 0, 0, 0, 0, 0], # decision to produce or not for month 1
                         [0, 1, 0, 0, -250, 0, 0, 0, 0], # decision to produce or not for month 1
                         [0, 0, 1, 0, 0, -250, 0, 0, 0]], # decision to produce or not for month 1
                         [50, 150, 200, -np.inf, -np.inf, -np.inf], #lower bounds
                         [50, 150, 200, 0, 0, 0] #upper bounds
                         )

result = milp(c,
              integrality = integ,
              bounds = bounds,
              constraints = cons)


if result.success:
    x1, x2, x3, y1, y2, y3, i1, i2, i3 = result.x
    print(f"Month 1: Produce {x1:.1f} units (Setup: {y1:.0f}), Inventory: {i1:.1f}")
    print(f"Month 2: Produce {x2:.1f} units (Setup: {y2:.0f}), Inventory: {i2:.1f}")
    print(f"Month 3: Produce {x3:.1f} units (Setup: {y3:.0f}), Inventory: {i3:.1f}")
    print(f"\nTotal Cost: ${result.fun:.2f}")
else:
    print("No solution found")
