import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import basinhopping

# Define the Ackley function (2D)
def ackley(x):
    term1 = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x[0]**2 + x[1]**2)))
    term2 = -np.exp(0.5 * (np.cos(2 * np.pi * x[0]) + np.cos(2 * np.pi * x[1])))
    return term1 + term2 + np.e + 20

# Bounds for x and y
bounds = [(-5, 5), (-5, 5)]

# Callback to track optimization steps
path = []
def callback(x, f, accepted):
    path.append(x.copy())

# Set up basinhopping
minimizer_kwargs = {
    "method": "L-BFGS-B",  # Local minimization method
    "bounds": bounds
}

result = basinhopping(
    ackley,
    x0=[4, 4],         # Initial guess (far from the global minimum)
    niter=100,         # Number of basin-hopping iterations
    T=1.0,             # Temperature for accept/reject criterion
    stepsize=1.0,      # Initial step size for random displacement
    minimizer_kwargs=minimizer_kwargs,
    callback=callback
)

# Results
print("Global minimum found at:", result.x)
print("Function value at minimum:", result.fun)

# Plot the optimization path
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = ackley([X, Y])

plt.figure(figsize=(10, 6))
plt.contourf(X, Y, Z, 50, cmap='viridis', alpha=0.8)
plt.colorbar()
path = np.array(path)
plt.plot(path[:, 0], path[:, 1], 'r.-', markersize=2, label='Optimization Path')
plt.scatter(result.x[0], result.x[1], c='red', s=100, label='Global Minimum')
plt.legend()
plt.title("Basinhopping Optimization Path on Ackley Function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()