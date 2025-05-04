# GLOBAL OPTIMIZATION USING BASINSHOPPING

from scipy.optimize import basinhopping, NonlinearConstraint


# FUNCTION TO OPTIMIZE WITH MULTIPLE MAXIMAS
def profit(q):
    return -q**4 / 4 + 11 * q**3 - 160 * q**2 + 900 * q



# INITAL VALUE
x0 = 0

# CONSTRAINTS
#kwargs = {"constraints": NonlinearConstraint(lambda x: x, lb=0, ub=30)}   # can put bounds and constraints 
kwargs = {'bounds': [(0, 30)]}


# EMPTY LIST TO RECORD CALLBACKS
maxima=[]

def callback(x, f, accept):
    if accept:
        maxima.append(*x)
        

# FINDING THE OPTIMAL VALUES
result = basinhopping(lambda q: -profit(q), x0, callback = callback, niter=10, minimizer_kwargs=kwargs)



print(result.message)
print(-result.fun)
print(f"The maximum according to basinhopping(x0={x0}) is at {result.x[0]:.2f}\n")
print(f"(Local) maxima found by basinhopping are: {[round(x, 2) for x in maxima]}")