import numpy as np

alfa = 35
beta = 3
gamma = 28

def chen(t, y):
    dy = [alfa * (y[1] - y[0]),
          (gamma - alfa) * y[0] - y[0] * y[2] + gamma * y[1],
          y[0] * y[1] - beta * y[2]]
    return np.array(dy)