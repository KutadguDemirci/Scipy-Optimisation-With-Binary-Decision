# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:59:07 2025

@author: kutadgu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


################            EXERCISE NO1        ###############################


#DEFINE THE FUNCTION PARAMETERS TO FIT
def f(a, x, b):
    return a*x + b


#THE DATA TO CURVE FIT
x_plot = [1, 2, 3, 4, 5]
y_plot = [5.1, 7.0, 8.8, 10.9, 13.1]


#CURVE FITTING
popt, pcov = curve_fit(f, x_plot, y_plot)

#POPT HAS THE OPTIMAL VALUES FOR ALL THE VARIABLES
a_fit, b_fit = popt

x_fit = np.linspace(0, 5, 100)
y_fit = f(a_fit, x_fit, b_fit)

fig, ax = plt.subplots()
ax.scatter(x_plot, y_plot, color = 'blue', marker = 'o', label = 'Acquiered Data')
ax.plot(x_fit, y_fit, '--', color = 'red', label = 'Curve Fit')
ax.set_xlabel('Extention (cm)')
ax.set_ylabel('Force (N)')

plt.legend()
plt.show()


################            EXERCISE NO2        ###############################

# DATA TO CURVE FIT
x_data = np.array([400, 450, 500, 550, 600, 650])  # Wavelength (nm)
y_data = np.array([12, 28, 75, 95, 40, 18])        # Intensity

# DEFINE THE FUNCTION

def f(x, a, b, c):
    return a * np.exp(-(x-b)**2 / (2*c**2))

#CURVE FIT AND GET RESULT
p0 = [50, 500, 20]
bounds = ([0 , 400, 10], [200, 700, 100])

popt, pcov = curve_fit(f, x_data, y_data, p0 = p0, bounds = bounds)
a_fit, b_fit, c_fit = popt

x_fit = np.linspace(350, 700, 1000)
y_fit = f(x_fit, a_fit, b_fit, c_fit)


# PLOT THE FIGURE
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(x_data, y_data, color = 'red', marker = 'o', label = 'Experimental Data')
ax.plot(x_fit, y_fit, color = 'blue', linestyle = '--', label = 'Curve Fit')
ax.set_xlabel('Wavelenght (cm)')
ax.set_ylabel('Intensity')
ax.set_title('Guassian Fit')


ax.grid(True)
plt.legend()
plt.show()

print(f"{a_fit:.1f}")
print(f"{b_fit:.1f}")
print(f"{c_fit:.1f}")