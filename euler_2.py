import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

x0 = 0
y0 = 1
h = 0.05
N = 6
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

# fig = Figure(x_label=r"t (s)", y_label="$x$ (arb. units)", x_min=0, x_max=N, y_min=-3, y_max=3)

# fig.plot(x, y, ls='--', m='', lw=0.7, c='k', label="x = √t")

# for i in (1, 0.5, 0, -0.5, -0.75, -1):
#     x, y = euler(x0, i, h, N)
#     fig.plot(x, y, m='', ls='-', lw=0.7, label=f"x\u2080 = {i}")

# fig.legend()
# fig.save("e2_comparison to sqrt(t).svg")

##################################################################

################# Breakdown at Large Values of N ################

N = 533
x = np.linspace(0, N, 1000)
y = np.sqrt(x)

fig = Figure(x_label=r"t (s)", y_label="$x$ (arb. units)", x_min=531, x_max=N, y_min=5, y_max=40)
# fig.plot(x, y, ls='--', m='', lw=1, c='k', label="x = √t", zorder=4)
for i in [0.050, 0.045, 0.040]:
    x, y = euler(x0, y0, i, N)
    fig.plot(x, y, m='', ls='-', lw=0.7, label=f"Approximation (h = {i})", c=None)

fig.legend()
fig.save("e2_breakdown.svg")

###############################################################
