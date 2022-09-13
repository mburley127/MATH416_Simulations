### Load in Necessary Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import random
import math
from scipy.integrate import quad, dblquad




### CHAPTER 3, EXERCISE 2
### If x_0 = 3, and x_n = (5x_(n-1)+7)mod200, calculate x_1,...,x_10

# Set up variables and create array of zeros length n+1
n = 10
index = range(n+1)
x = np.zeros(len(range(n+1)))
x[0] = 3

# Loop to compute difference equation
for n in index[1:]:
    x[n] = (5*x[n-1]+7)%200
    print(("x_" + str(n)) + " =", x[n]) 
    
    
 

### CHAPTER 3, EXERCISE 5
### Use simulation to compute int(-2, 2) e^(x + x^2)dx and find the actual answer

# Set limits of integration, and the number of trials
a = -2
b = 2
N = 100000

## Calculate MC Integration Answer
# Create an array of zeros of length N
ar = np.zeros(N)
  
# Filling each value of the array with generated random numbers
for i in range (len(ar)):
    ar[i] = random.uniform(a,b)
  
# Variable to store sum of the functions of different values of x
integral = 0.0
  
# Input and return the desired function inside the integral
def f(x):
    return math.exp(x + x**2)
  
# Iterate and sum up values of different functions of x
for i in ar:
    integral += f(i)
  
# Generate calculated Monte Carlo Integration Answer
ans_mc = (b-a)/float(N)*integral
print ("The value calculated by monte carlo integration is {}".format(ans_mc))

## Calculate actual answer
def integrand(x):
    return math.exp(x + x**2)

ans, err = quad(integrand, a, b)
print(ans)




### CHAPTER 3, EXERCISE 8
### Compute the double integral int(0, 1)int(0, 1) e^(x + y)dydx 

# Set limits of integration, and the number of trials
a = 0
b = 1
c = 0
d = 1

## Calculate answer

# In this case, y is the first argument, and x is the second
def integrand(y, x):
    return math.exp((x + y)**2)

ans, err = dblquad(integrand, a, b, c, d)
print(ans)
