import numpy as np

# Our parameters
P = 2 / 100
Q = 2 / 100
U = 5.7


def our_function(t, y):
    dy = [U * y[1] - y[2] - 0.1 * y[0],
          y[0] + (y[1] * P * (1 - y[0])) - 0.05 * y[1],
          (Q + y[2]) + y[1] * - 0.2 * y[2]]
    return np.array(dy)