# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:56:54 2025

@author: kutadgu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog 

cost = np.array([0.5, 0.3]) #cost of items
sugar = np.array([10, 12]) #sugar per item
fiber = np.array([3, 2]) #fiber per item

m_sugar = 80 #minimum sugar intake per day
m_fiber = 20 #minimum fiber intake per day

c = cost

A_ub = ([ -sugar, 
         -fiber]) #left hand side of inequality

b_ub = ([ -m_sugar,
         -m_fiber]) #right hand side of inequality

bounds = ([2, None], [0, None])

optimal = linprog(c, A_ub = A_ub , b_ub = b_ub , bounds = bounds, method = 'highs')

if optimal.success:
    optimal_results = optimal.fun
    optimal_servings = optimal.x
    total_sugar = optimal_servings.dot(sugar)
    total_fiber = optimal_servings.dot(fiber)
    print ("Total cost is", optimal_results, "dollars.")
    print ("Total fiber intake is", total_fiber)
    print ("Total sugar intake is", total_sugar)
else:
    print("no result found")
    
foods = ["Apple", "Banana"]
plt.bar(foods, optimal_servings, color = 'black')
plt.xlabel = ("Foods")
plt.ylabel = ("Servings")
plt.show()

