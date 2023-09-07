import matplotlib
import numpy as np
import matplotlib.pyplot as plt


import math

def f(x):
    return x * math.log(x) - 16.0

xvals = np.arange(0.01, 10, 0.01)
yvals = np.array([f(x) for x in xvals])
plt.plot(xvals, yvals)
plt.plot(xvals, 0*xvals)
plt.show()