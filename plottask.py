# Weekly task 08
# Author Cian Gallagher
# matplotlib used to create 1. A random standard distribution and d 2. Plot the function h(x)=x^3 in the range 0 to 10. 

import numpy as np
import matplotlib.pyplot as plt

# 1000 random numbers in a normal distribution with mean 5,stddev of 2, and 1000 data points.
normData = np.random.normal(5, 2, 1000)

# Plotting the normData histogram
plt.hist(normData, bins = 50, color = 'whitesmoke', edgecolor = 'midnightblue', label='Normal Distribution')

# Plotting h(x) = x^3 function
xpoints = np.linspace(0, 10, 10)
ypoints = xpoints ** 3 # y equals x cubed
plt.plot(xpoints, ypoints, color = 'green', label = 'h(x) = x^3' )

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of a Normal Distribution and a h(x) = x^3 function')
plt.legend()

plt.show()