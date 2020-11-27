# Calculation of Pi
# Using Monte Carlo method
# Given a unit square and a circle inscribed inside of it.
# The pi would be the ratio * 4 where ratio is number of times a random point (x, y) with 0<= x, y <=1
# falls inside of the circle between that falls inside the unit square.
import random
import matplotlib.pyplot as plt
import math
import numpy as np

def compute_pi(N_trials):
    inside_circle_count = 0
    inside_square_count = N_trials

    for i in range(N_trials):
        x = random.random()
        y = random.random()
        if (x - 0.5)**2 + (y - 0.5)**2 <= 0.5**2:
            inside_circle_count += 1

    pi = 4.0 * inside_circle_count / inside_square_count
    return pi


x = np.array([10**i for i in range(8)])
y = np.array([compute_pi(i) for i in x])
x_log = np.log10(x)
plt.plot(x_log, y, 'bo-', markersize = 12)
plt.xlabel('Number of trials, log10', fontsize = 12)
plt.ylabel('Computed Pi', fontsize = 12)
plt.title('Compute Pi with Monte Carlo')
plt.hlines(math.pi, min(x_log), max(x_log), 'r', 'dotted', lw=2)
plt.show()

