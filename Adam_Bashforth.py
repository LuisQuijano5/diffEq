from RK4 import r4singlestep as rk4

import numpy as np

def adams_bashforth_4(function, y0, t_span, dt):
    t0, tf = t_span
    num_steps = int(np.round((tf - t0)/dt)) + 1
    t_values = np.linspace(t0, tf, num_steps)
    y_values = np.zeros((num_steps, len(y0)))
    y_values[0] = y0

    #RK4 to get the first 3 steps
    for i in range(3):
        y_values[i + 1] = rk4(function, dt, t_values[i], y_values[i])

    # Adams-Bashforth iterations
    for i in range(3, num_steps - 1):
        f0 = function(t_values[i], y_values[i])
        f1 = function(t_values[i - 1], y_values[i - 1])
        f2 = function(t_values[i - 2], y_values[i - 2])
        f3 = function(t_values[i - 3], y_values[i - 3])
        y_values[i + 1] = y_values[i] + (dt / 24) * (55 * f0 - 59 * f1 + 37 * f2 - 9 * f3)

    return y_values[:, 0], y_values[:, 1], y_values[:, 2]
