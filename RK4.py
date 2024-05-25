"""
Reference: Steve Brunton
https://www.youtube.com/watch?v=vNoFdtcPFdk&list=PLMrJAkhIeNNTYaOnVI3QpH7jgULnAmvPA&index=45
"""


import numpy as np


def r4singlestep(function, dt, t0, y0):
    f1 = function(t0, y0)
    f2 = function(t0 + dt / 2, y0 + (dt / 2) * f1)
    f3 = function(t0 + dt / 2, y0 + (dt / 2) * f2)
    f4 = function(t0 + dt, y0 + dt * f3)
    y_out = y0 + (dt / 6) * (f1 + 2 * f2 + 2 * f3 + f4)
    return y_out


def run(y0, dt, T, function):
    num_time_pts = int(T / dt)
    t = np.linspace(0, T, num_time_pts)
    Y = np.zeros((3, num_time_pts))
    Y[:, 0] = y0
    y_in = y0

    # Min and max for normalizing
    min_values = np.array(y0)
    max_values = np.array(y0)

    for i in range(num_time_pts - 1):
        y_out = r4singlestep(function, dt, t[i], y_in)
        # y_out = r4singlestep(our_function, dt, t[i], y_in)

        # Update min/max values
        min_values = np.minimum(min_values, y_out)
        max_values = np.maximum(max_values, y_out)

        Y[:, i + 1] = y_out
        y_in = y_out

    """
    DANGER: THIS CODE SHOULDNT BE UNCOMMENTED, ONLY COPIED AND PASTED ON NON REITERATING CODE
    """
    #ax = plt.figure().add_subplot(projection='3d')
    #ax.plot(Y[0, :], Y[1, :], Y[2, :], 'b')
    #plt.show()

    return Y[0, :], Y[1, :], Y[2, :], min_values, max_values



"""Library solution"""
# lorenz_solution = solve_ivp(lorenz, (0, T), y0, t_eval=t)
# t = lorenz_solution.t
# y = lorenz_solution.y.T
# ax.plot(y[:, 0], y[:, 1], y[:, 2], 'r')
# print(y[:, 0])
# plt.show()
