import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

x0 = 0
y0 = 1
h = 0.01
N = 10
n = int(N / h)


def f(x, y):
    return x - y**2


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


############### Plot Comparison to sqrt(t) ########################
 
# x = np.linspace(0, N, 1000)
# y = np.sqrt(x)

# fig = Figure(x_label="t", y_label="x", x_min=0, x_max=N)

# fig.plot(x, y, ls='--', m='', lw=0.7, c='k', label="x = √t")

# for i in (3, 1, 0, -0.5, -0.7):
#     x, y = euler(x0, i, h, N)
#     fig.plot(x, y, m='', ls='-', lw=0.7, label=f"x\u2080 = {i}")

# fig.legend()
# fig.save("e2_comparison to sqrt(t).svg")

##################################################################

################# Breakdown at Large Values of N ################

# N = 440
# x = np.linspace(0, N, 1000)
# y = np.sqrt(x)

# fig = Figure(x_label="t", y_label="x", x_min=435, x_max=N, y_min=10, y_max=30)

# fig.plot(x, y, ls='-', m='', lw=1, c='r', label="x = √t")

# x, y = euler(x0, y0, h, N)
# fig.plot(x, y, m='', ls='-', lw=0.5, label=f"Approximation (h = {h})", c='k')

# fig.legend()
# fig.save("e2_breakdown_h=0.01.svg")

###############################################################
