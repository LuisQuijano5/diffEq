import numpy as np
from matplotlib import pyplot as plt
from RK4 import run

# Our parameters, you can modify them to see different results
P = 2 / 100
Q = 2 / 100
U = 5.7


def our_function(t, y):
    dy = [U * y[1] - y[2],
          y[0] + (y[1] * P) - 0.05 * y[1],
          y[0] * y[1]]
    return np.array(dy)


y0 = [-1, 28, 6]  # these are the initial values
dt = 0.01  # dt and T will ultimately set the number of iterations
T = 15
Y = [[], [], []]

Y[0], Y[1], Y[2], min_values, max_values = run(y0, dt, T, our_function)
#values
print("X values: " + str(Y[0]))
print("Y values: " + str(Y[1]))
print("Z values: " + str(Y[2]))
#draw
ax = plt.figure().add_subplot(projection='3d')
ax.plot(Y[0], Y[1], Y[2], 'b')
plt.show()