# Weekly task 08
# Author Cian Gallagher
# matlotlib used to create 1. A random standard distribution and d 2. plot the function h(x)=x^3 in the range 0 to 10. 

import numpy as np
import matplotlib.pyplot as plt

# 1000 random numbers in a normal distribution with mean 5,stddev of 2, and 1000 data points.
normData = np.random.normal(5, 2, 1000)

# Plotting the normData histogram
plt.hist(normData, bins = 50, density = True, color = 'whitesmoke', edgecolor = 'midnightblue')

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Normal Distribution (mean = 5, stddev = 2)')

plt.show()