# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:01:41 2025

@author: kutadgu
"""

from sympy import symbols, diff, solve
import numpy as np
from scipy.optimize import minimize_scalar

K, L = symbols('K L')

# Function
F = (K**0.34) * (L**0.66)

# Parital differentiation
dF_dK = diff(F, K)
dF_dL = diff(F, L) 

critical_points = solve([dF_dK, dF_dL], (K, L))

print(critical_points)

def f(x):
    return x**2 -12*x +4

optimal = minimize_scalar(f)
print(optimal)