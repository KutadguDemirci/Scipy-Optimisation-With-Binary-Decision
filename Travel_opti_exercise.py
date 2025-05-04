import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Staying Costs
hotel_cost = np.array([0, 50, 80, 60, 100])
food_cost = np.array([0, 20, 25, 22, 30])

#Travleiing Costs
fuel_cost = np.array([0, 0.1, 0.12, 0.15, 0.08])
distance_from_previous = np.array([0, 200, 300, 250, 400])

#Combined Costs
travel_cost = fuel_cost * distance_from_previous
cost_per_day = hotel_cost + food_cost

# cost = hotel_cost + food_cost

n = len(cost_per_day)

c = cost_per_day

A_eq= np.array([[1, 1, 1, 1, 1]])   
result = linprog(c, A_ub=None, b_ub=None, A_eq= A_eq, b_eq =[7], bounds=[(1, 4) for _ in range(n)], method='highs')

if result.success:
    nights_spent = result.x
    total_cost = result.fun
    total_hotel_cost = nights_spent.dot(hotel_cost)
    total_food_cost = nights_spent.dot(food_cost)
    
else:
    print("no success found")

cities = ['A', 'B', 'C', 'D', 'E']
plt.bar(cities, nights_spent, color='black')
plt.xlabel = 'Cities'
plt.ylabel = 'Nights Spent'


print("Night spent at each city", nights_spent)
print("Total money spent", total_cost)
print("Total hotel cost is", total_hotel_cost)
print("Total food cost is", total_food_cost)