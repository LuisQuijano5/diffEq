import numpy as np

alfa = 0.35
gamma = 1

def rik_dyn(t, y):
    y_scaled = [i / 100 for i in y]
    dy = [y_scaled[1] * (y_scaled[2] - 1 + y_scaled[0] ** 2) + gamma * y_scaled[0],
          y_scaled[0] * (3 * y_scaled[2] + 1 - y_scaled[0] ** 2) + gamma * y_scaled[1],
          -2 * y_scaled[2] * (alfa + y_scaled[0] * y_scaled[1])]
    return np.array(dy)