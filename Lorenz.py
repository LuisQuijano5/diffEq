"""
Reference: Steve Brunton
https://www.youtube.com/watch?v=vNoFdtcPFdk&list=PLMrJAkhIeNNTYaOnVI3QpH7jgULnAmvPA&index=45
"""
import numpy as np

sigma = 10
beta = 8 / 3
rho = 28

def lorenz(t, y):
    dy = [sigma * (y[1] - y[0]),
          y[0] * (rho - y[2]) - y[1],
          y[0] * y[1] - beta * y[2]]
    return np.array(dy)
