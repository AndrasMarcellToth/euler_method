import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

x0 = 0
y0 = 10
h = 0.1
N = 10
n = int(N / h)

tau = 1


def f(x, y):
    return -y / tau

def ori(x):
    return y0 * np.e ** (-x / tau)

def euler(x0, y0, h, N):
    n = int(N/h)
    x = np.zeros(n+1, 'float64')
    y = np.zeros(n+1, 'float64')
    
    x[0] = x0
    y[0] = y0
    
    for i in range(1, n+1):
        xi = x[i-1] + h
        yi = y[i-1] + h * f(x[i-1], y[i-1])
        x[i] = xi
        y[i] = yi

    return x, y



################# Plot Euler Approximation #################

# fig = Figure(x_label="Time (s)", y_label="Count")

# x, y = euler(x0, y0, h, N)
# yori = ori(x)
# fig.plot(x, yori, m='', ls='--', lw=0.7, c='k', label="Exact Solution")

# for i in [0.1]:
#     x, y = euler(x0, y0, i, N)
#     yori = ori(x)
#     fig.plot(x, y, m='', ls='-', lw=0.7, c='k', label="Euler Approximation")


# fig.legend()
# fig.save("e1_approximation.svg")

###########################################################


################## Plot Error #############################

# fig = Figure(x_label="Time (s)", y_label="Error in Count")

# for i in (0.1, 0.05, 0.01, 0.001):
#     x, y = euler(x0, y0, i, N)
#     yori = ori(x)
#     yerr = yori - y
#     fig.plot(x, yerr, m='', ls='-', lw=0.7, label=f"h = {i} s")

# fig.legend()
# fig.save("e1_error.svg")

###########################################################

